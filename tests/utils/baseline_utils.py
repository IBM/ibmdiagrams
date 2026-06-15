"""
Utility helpers for baseline diagram generation tests.
"""

import logging
import os
import platform
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

from defusedxml import ElementTree as DET

from ibmdiagrams.ibmcloud.diagram import Diagram

logger = logging.getLogger(__name__)

ALLOWED_FORMATS = {"png", "svg", "pdf", "jpg"}
CONVERSION_TIMEOUT = 60  # seconds
SVG_NAMESPACE = "http://www.w3.org/2000/svg"
XLINK_NAMESPACE = "http://www.w3.org/1999/xlink"

# PNG export quality settings
PNG_SCALE = 2.0  # 2x resolution for higher quality
PNG_QUALITY = 100  # Maximum quality (affects compression)


@dataclass
class DiagramElement:
    """Represents a diagram element to be generated."""

    obj: type
    slug: str
    label: str
    wrapper_obj: type | None = None
    wrapper_label: str = "Baseline<br>Container"


def find_drawio_executable() -> Path | None:
    """
    Find the draw.io executable across different operating systems.

    Returns:
        Path to the draw.io executable if found, None otherwise.
    """
    system = platform.system()

    # Check if drawio is in PATH first (works for all platforms)
    drawio_in_path = shutil.which("drawio")
    if drawio_in_path:
        return Path(drawio_in_path)

    # Platform-specific paths
    if system == "Darwin":  # macOS
        possible_paths = [
            Path("/Applications/draw.io.app/Contents/MacOS/draw.io"),
            Path.home() / "Applications/draw.io.app/Contents/MacOS/draw.io",
        ]
    elif system == "Windows":
        possible_paths = [
            Path(os.environ.get("PROGRAMFILES", "C:/Program Files")) / "draw.io/draw.io.exe",
            Path(os.environ.get("PROGRAMFILES(X86)", "C:/Program Files (x86)"))
            / "draw.io/draw.io.exe",
            Path.home() / "AppData/Local/Programs/draw.io/draw.io.exe",
        ]
    elif system == "Linux":
        possible_paths = [
            Path("/usr/bin/drawio"),
            Path("/usr/local/bin/drawio"),
            Path.home() / ".local/bin/drawio",
        ]
    else:
        logger.warning(f"Unsupported operating system: {system}")
        return None

    # Check each possible path
    for path in possible_paths:
        if path.is_file() and os.access(path, os.X_OK):
            logger.info(f"Found draw.io executable at: {path}")
            return path

    return None


def validate_format(fmt: str) -> None:
    """
    Validate the output format.

    Args:
        fmt: The format to validate.

    Raises:
        ValueError: If the format is not allowed.
    """
    if fmt not in ALLOWED_FORMATS:
        raise ValueError(f"Invalid format: {fmt}. Allowed formats: {ALLOWED_FORMATS}")


def should_use_xvfb() -> bool:
    """
    Determine if xvfb-run should be used for headless execution.

    Returns:
        True if xvfb-run should be used, False otherwise.
    """
    # Only use xvfb on Linux systems where it's available
    if platform.system() != "Linux":
        return False

    # Check if xvfb-run is available
    if not shutil.which("xvfb-run"):
        logger.debug("xvfb-run not found, running draw.io directly")
        return False

    # Check if we're in a headless environment (no DISPLAY variable)
    if not os.environ.get("DISPLAY"):
        logger.debug("No DISPLAY detected, will use xvfb-run")
        return True

    return False


def convert_drawio(
    input_path: Path,
    output_path: Path,
    fmt: str = "png",
    drawio_path: Path | None = None,
    scale: float | None = None,
    quality: int | None = None,
) -> bool:
    """
    Convert a draw.io file to another format.

    Args:
        input_path: Path to the input .drawio file.
        output_path: Path to the output file.
        fmt: Output format (png, svg, pdf, jpg).
        drawio_path: Optional path to draw.io executable. If None, will auto-detect.
        scale: Optional scale factor for output (e.g., 2.0 for 2x resolution).
        quality: Optional quality setting (1-100, affects PNG compression and JPEG quality).

    Returns:
        True if conversion succeeded, False otherwise.

    Raises:
        FileNotFoundError: If draw.io executable or input file not found.
        ValueError: If format is invalid.
    """
    # Find draw.io executable if not provided
    if drawio_path is None:
        drawio_path = find_drawio_executable()
        if drawio_path is None:
            raise FileNotFoundError(
                "draw.io executable not found. Please install draw.io desktop application.\n"
                "Download from: https://github.com/jgraph/drawio-desktop/releases"
            )

    # Validate format
    validate_format(fmt)

    # Validate input file exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Ensure executable path is a local executable file before invocation
    if not drawio_path.is_file():
        raise FileNotFoundError(f"draw.io executable is not a file: {drawio_path}")
    if not os.access(drawio_path, os.X_OK):
        raise PermissionError(f"draw.io executable is not executable: {drawio_path}")

    # Build command with quality options
    cmd = [
        str(drawio_path.resolve(strict=True)),
        "--export",
        "--format",
        fmt,
        "--crop",
        "--output",
        str(output_path.resolve()),
    ]

    # Add scale option for higher resolution (especially useful for PNG)
    if scale is not None:
        cmd.extend(["--scale", str(scale)])

    # Add quality option (affects PNG compression and JPEG quality)
    if quality is not None:
        cmd.extend(["--quality", str(quality)])

    # Add input file last
    cmd.append(str(input_path.resolve(strict=True)))

    # Wrap with xvfb-run if needed (Linux headless environments)
    if should_use_xvfb():
        cmd = ["xvfb-run", "-a", "--server-args=-screen 0 1920x1080x24"] + cmd
        logger.info("Using xvfb-run for headless execution")

    try:
        # Execute conversion with validated executable and resolved file paths
        # Security: Safe subprocess call - executable path validated,
        # all paths resolved to absolute, shell=False prevents injection
        subprocess.run(  # noqa: S603
            cmd,
            check=True,
            shell=False,
            timeout=CONVERSION_TIMEOUT,
            capture_output=True,
            text=True,
        )
        logger.info(f"Successfully converted {input_path.name} to {fmt}")
        return True

    except subprocess.CalledProcessError as e:
        logger.error(f"Error during conversion: {e}")
        if e.stderr:
            logger.error(f"Error output: {e.stderr}")
        return False

    except subprocess.TimeoutExpired:
        logger.error(f"Conversion timed out after {CONVERSION_TIMEOUT} seconds")
        return False


def clean_svg_for_compatibility(input_file: Path, output_file: Path) -> None:
    """
    Clean SVG file to remove browser-specific CSS features.

    Removes color-scheme properties and flattens light-dark() functions
    to ensure compatibility across different viewers.

    Args:
        input_file: Path to the input SVG file.
        output_file: Path to the output SVG file.

    Raises:
        ValueError: If the SVG file is invalid or empty.
    """
    # Register namespaces
    ET.register_namespace("", SVG_NAMESPACE)
    ET.register_namespace("xlink", XLINK_NAMESPACE)

    # Parse SVG file securely
    tree = DET.parse(str(input_file))
    root = tree.getroot()

    if root is None:
        raise ValueError(f"Invalid or empty XML file: {input_file}")

    # Compile regex patterns
    color_scheme_pattern = re.compile(r"color-scheme\s*:\s*[^;]+;?")
    light_dark_pattern = re.compile(r"light-dark\s*\(([^,]+),.*?\)")

    # Process all elements
    for elem in root.iter():
        style = elem.get("style")
        if style:
            # Remove color-scheme property
            style = color_scheme_pattern.sub("", style)
            # Flatten light-dark() functions to first value
            style = light_dark_pattern.sub(r"\1", style)
            # Update attribute with cleaned style
            cleaned_style = style.strip()
            if cleaned_style:
                elem.set("style", cleaned_style)
            else:
                elem.attrib.pop("style", None)

    # Write cleaned SVG
    tree.write(str(output_file), encoding="utf-8", xml_declaration=True)
    logger.info(f"Cleaned SVG file: {output_file.name}")


def build_output_paths(name: str, drawio_dir: Path, png_dir: Path) -> tuple[Path, Path]:
    """
    Build output file paths for all formats.

    Args:
        name: Base name for the files.
        drawio_dir: Directory for .drawio files.
        png_dir: Directory for PNG files.

    Returns:
        Tuple of (drawio_file, png_file) paths.
    """
    return (
        drawio_dir / f"{name}.drawio",
        png_dir / f"{name}.png",
    )


def convert_to_formats(
    drawio_file: Path,
    output_files: dict[str, Path],
    drawio_path: Path | None = None,
) -> bool:
    """
    Convert drawio file to multiple formats with optimized quality settings.

    Args:
        drawio_file: Path to the source .drawio file.
        output_files: Dictionary mapping format names to output paths.
        drawio_path: Optional path to draw.io executable.

    Returns:
        True if all conversions succeeded, False if any failed.
    """
    for fmt, output_path in output_files.items():
        # Apply high-quality settings for PNG exports
        scale = PNG_SCALE if fmt == "png" else None
        quality = PNG_QUALITY if fmt == "png" else None

        if not convert_drawio(
            drawio_file, output_path, fmt=fmt, drawio_path=drawio_path, scale=scale, quality=quality
        ):
            logger.error(f"Failed to convert {drawio_file.name} to {fmt}")
            return False
    return True


def setup_baseline_directories() -> tuple[Path, Path]:
    """
    Create and return baseline directory paths.

    Returns:
        Tuple of (drawio_dir, png_dir).
    """
    base_dir = Path(__file__).parent.parent / "baselines"
    drawio_dir = base_dir / "drawio"
    png_dir = base_dir / "png"

    # Create directories
    for directory in (drawio_dir, png_dir):
        directory.mkdir(parents=True, exist_ok=True)

    return drawio_dir, png_dir


def create_drawio_diagram(element: DiagramElement, drawio_file: Path) -> bool:
    """
    Create a .drawio diagram file.

    Group elements can be rendered standalone. Item elements require a
    containing group and may optionally specify a wrapper group.

    Args:
        element: The diagram element to generate.
        drawio_file: Path where the .drawio file will be created.

    Returns:
        True if creation succeeded, False otherwise.
    """
    import inspect

    from ibmdiagrams import Group, Item
    from ibmdiagrams.ibmcloud import groups

    is_group = issubclass(element.obj, Group)
    is_item = issubclass(element.obj, Item)
    sig = inspect.signature(element.obj.__init__)
    has_direction = "direction" in sig.parameters

    logger.info(
        f"Element {element.slug}: is_group={is_group}, is_item={is_item}, has_direction={has_direction}"
    )
    logger.info(f"Element {element.slug} parameters: {list(sig.parameters.keys())}")

    if not is_group and not is_item:
        logger.warning(
            f"Skipping {element.slug}: unsupported baseline element type {element.obj!r}"
        )
        return False

    try:
        with Diagram(name=element.slug, filename=element.slug, output=str(drawio_file.parent)):
            if is_group:
                with element.obj(element.label, direction="TB"):
                    pass
            else:
                wrapper_obj = element.wrapper_obj or groups.IBMCloud
                wrapper_sig = inspect.signature(wrapper_obj.__init__)
                wrapper_kwargs = (
                    {"direction": "TB"} if "direction" in wrapper_sig.parameters else {}
                )
                with wrapper_obj(element.wrapper_label, **wrapper_kwargs):
                    element.obj(element.label)
        logger.debug(f"Created .drawio file: {drawio_file}")
        return True
    except Exception as e:
        logger.error(f"Failed to generate diagram {element.slug}: {type(e).__name__}: {e}")
        return False


def generate_baseline_diagram(
    element: DiagramElement,
    drawio_dir: Path,
    png_dir: Path,
    drawio_path: Path | None = None,
) -> bool:
    """
    Generate a baseline diagram in drawio and PNG formats.

    Args:
        element: The diagram element to generate.
        drawio_dir: Directory for .drawio files.
        png_dir: Directory for PNG files.
        drawio_path: Optional path to draw.io executable.

    Returns:
        True if all conversions succeeded, False otherwise.
    """
    name = element.slug
    logger.info(f"Generating baseline diagram: {name}")

    drawio_file, png_file = build_output_paths(name, drawio_dir, png_dir)

    if not create_drawio_diagram(element, drawio_file):
        return False

    conversions = {"png": png_file}
    if not convert_to_formats(drawio_file, conversions, drawio_path):
        return False

    logger.info(f"Successfully generated all formats for: {name}")
    return True
