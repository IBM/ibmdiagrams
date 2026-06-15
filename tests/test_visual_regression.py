"""
Visual regression tests for IBM Cloud diagram elements.

This module tests that all diagram elements render identically to their
baseline images, detecting unintended visual changes.
"""

import logging
from pathlib import Path

import pytest
from utils.baseline_utils import generate_baseline_diagram
from utils.image_comparison import (
    ImageComparisonError,
    ImageLoadError,
    ImageSizeMismatchError,
    compare_images,
    compare_images_with_tolerance,
    generate_size_mismatch_diff,
    save_diff_image,
)

logger = logging.getLogger(__name__)


def generate_test_diagram(
    element,
    output_dir: Path,
    drawio_path: Path | None,
) -> Path:
    """
    Generate a diagram for testing.

    Args:
        element: DiagramElement to generate.
        output_dir: Directory for output files.
        drawio_path: Path to draw.io executable.

    Returns:
        Path to generated PNG file.

    Raises:
        RuntimeError: If diagram generation fails.
    """
    # Create subdirectories for drawio and png
    drawio_dir = output_dir / "drawio"
    png_dir = output_dir / "png"
    drawio_dir.mkdir(parents=True, exist_ok=True)
    png_dir.mkdir(parents=True, exist_ok=True)

    # Generate diagram
    success = generate_baseline_diagram(element, drawio_dir, png_dir, drawio_path)

    if not success:
        raise RuntimeError(f"Failed to generate diagram for {element.slug}")

    # Return path to generated PNG
    png_file = png_dir / f"{element.slug}.png"
    if not png_file.exists():
        raise RuntimeError(f"Generated PNG not found: {png_file}")

    return png_file


def format_failure_message(
    element,
    diff_percentage: float,
    threshold: float,
    diff_path: Path | None = None,
) -> str:
    """
    Format detailed error message for test failure.

    Args:
        element: DiagramElement that failed.
        diff_percentage: Percentage of different pixels.
        threshold: Threshold that was used.
        diff_path: Path to saved diff image (if any).

    Returns:
        Formatted error message.
    """
    message = (
        f"\nVisual regression test failed for element: {element.slug}\n"
        f"  Label: {element.label}\n"
        f"  Difference: {diff_percentage:.2f}%\n"
        f"  Threshold: {threshold:.2f}%\n"
    )

    if diff_path:
        message += f"  Diff image: {diff_path}\n"

    message += (
        f"\nThe generated diagram differs from the baseline by {diff_percentage:.2f}%.\n"
        f"This exceeds the allowed threshold of {threshold:.2f}%.\n"
    )

    if diff_path:
        message += f"\nReview the diff image at: {diff_path}\n"

    message += (
        "\nIf this change is intentional:\n"
        "  1. Review the visual changes carefully\n"
        "  2. Run: pytest tests/test_visual_regression.py --update-baselines\n"
        "  3. Commit the updated baseline images\n"
    )

    return message


def update_baseline(
    element,
    generated_png: Path,
    baseline_dir: Path,
) -> None:
    """
    Update baseline image with newly generated image.

    Args:
        element: DiagramElement being updated.
        generated_png: Path to newly generated PNG.
        baseline_dir: Directory containing baseline images.
    """
    import shutil

    baseline_png = baseline_dir / f"{element.slug}.png"

    # Ensure baseline directory exists
    baseline_dir.mkdir(parents=True, exist_ok=True)

    # Copy generated image to baseline
    shutil.copy2(generated_png, baseline_png)

    logger.info(f"Updated baseline for {element.slug}: {baseline_png}")


def pytest_generate_tests(metafunc):
    """
    Dynamically parametrize tests with baseline elements.

    This hook is called for each test function and allows us to
    parametrize the test with all baseline elements.
    """
    if "element" in metafunc.fixturenames:
        # Get baseline elements from the session
        from utils.baseline_elements import get_baseline_elements

        elements = get_baseline_elements()
        metafunc.parametrize("element", elements, ids=lambda e: e.slug)


@pytest.mark.visual_regression
def test_element_visual_regression(
    element,
    temp_output_dir: Path,
    baseline_dirs: tuple[Path, Path],
    test_threshold: float,
    pixel_tolerance: int,
    update_baselines: bool,
    save_diffs: bool,
    diff_output_dir: Path,
    drawio_executable: Path | None,
) -> None:
    """
    Test that diagram element renders identically to baseline.

    This test generates a diagram for the element and compares it with the
    baseline image. If differences exceed the threshold, the test fails.

    Args:
        element: DiagramElement to test.
        temp_output_dir: Temporary directory for test outputs.
        baseline_dirs: Tuple of (drawio_dir, png_dir) for baselines.
        test_threshold: Maximum allowed difference percentage.
        pixel_tolerance: Per-pixel color tolerance.
        update_baselines: If True, update baselines instead of comparing.
        save_diffs: If True, save diff images on failure.
        diff_output_dir: Directory for saving diff images.
        drawio_executable: Path to draw.io executable.
    """
    # Skip if draw.io not available
    if drawio_executable is None:
        pytest.skip(
            "draw.io executable not found. "
            "Install from: https://github.com/jgraph/drawio-desktop/releases"
        )

    # Get baseline paths
    _, baseline_png_dir = baseline_dirs
    baseline_png = baseline_png_dir / f"{element.slug}.png"

    # Check baseline exists
    if not baseline_png.exists() and not update_baselines:
        pytest.fail(
            f"Baseline image not found: {baseline_png}\n"
            f"Run 'pytest tests/test_visual_regression.py --update-baselines' to generate baselines."
        )

    # Generate test diagram
    try:
        generated_png = generate_test_diagram(element, temp_output_dir, drawio_executable)
    except Exception as e:
        pytest.fail(f"Failed to generate diagram for {element.slug}: {e}")

    # Update baseline mode
    if update_baselines:
        update_baseline(element, generated_png, baseline_png_dir)
        return  # Skip comparison in update mode

    # Compare images
    try:
        if pixel_tolerance > 0:
            # Use tolerance-based comparison
            is_match, diff_percentage, diff_image = compare_images_with_tolerance(
                generated_png,
                baseline_png,
                pixel_tolerance=pixel_tolerance,
                threshold=test_threshold,
            )
        else:
            # Use exact comparison
            is_match, diff_percentage, diff_image = compare_images(
                generated_png,
                baseline_png,
                threshold=test_threshold,
            )

    except ImageSizeMismatchError as e:
        # Generate size mismatch diff if save_diffs is enabled
        diff_path = None
        if save_diffs:
            try:
                diff_image = generate_size_mismatch_diff(baseline_png, generated_png)
                diff_path = diff_output_dir / f"{element.slug}_diff.png"
                save_diff_image(diff_image, diff_path)
                logger.info(f"Saved size mismatch diff to {diff_path}")
            except Exception as diff_error:
                logger.warning(f"Failed to generate size mismatch diff: {diff_error}")

        failure_msg = (
            f"Image size mismatch for {element.slug}: {e}\n"
            f"This usually indicates a significant change in diagram generation.\n"
        )
        if diff_path:
            failure_msg += f"Diff image saved to: {diff_path}\n"
        failure_msg += "Review the changes and update baselines if intentional."

        pytest.fail(failure_msg)
    except ImageLoadError as e:
        pytest.fail(f"Failed to load images for {element.slug}: {e}")
    except ImageComparisonError as e:
        pytest.fail(f"Image comparison failed for {element.slug}: {e}")

    # Save diff image if requested and test failed
    diff_path = None
    if not is_match and (save_diffs or diff_image is not None) and diff_image is not None:
        diff_path = diff_output_dir / f"{element.slug}_diff.png"
        try:
            save_diff_image(diff_image, diff_path)
        except ImageComparisonError as e:
            logger.warning(f"Failed to save diff image: {e}")

    # Assert match
    if not is_match:
        failure_message = format_failure_message(
            element,
            diff_percentage,
            test_threshold,
            diff_path,
        )
        pytest.fail(failure_message)

    # Log success
    logger.debug(
        f"Visual regression test passed for {element.slug} "
        f"(difference: {diff_percentage:.2f}%, threshold: {test_threshold:.2f}%)"
    )


@pytest.mark.visual_regression
def test_all_baselines_exist(baseline_elements, baseline_dirs: tuple[Path, Path]) -> None:
    """
    Test that baseline images exist for all elements.

    This is a sanity check to ensure baselines have been generated.

    Args:
        baseline_elements: List of all diagram elements.
        baseline_dirs: Tuple of (drawio_dir, png_dir) for baselines.
    """
    _, baseline_png_dir = baseline_dirs
    missing_baselines = []

    for element in baseline_elements:
        baseline_png = baseline_png_dir / f"{element.slug}.png"
        if not baseline_png.exists():
            missing_baselines.append(element.slug)

    if missing_baselines:
        pytest.fail(
            f"Missing baseline images for {len(missing_baselines)} elements:\n"
            + "\n".join(f"  - {slug}" for slug in missing_baselines)
            + "\n\nRun 'pytest tests/test_visual_regression.py --update-baselines' to generate baselines."
        )


@pytest.mark.visual_regression
def test_drawio_available(drawio_executable: Path | None) -> None:
    """
    Test that draw.io executable is available.

    This test helps identify environment setup issues early.

    Args:
        drawio_executable: Path to draw.io executable.
    """
    if drawio_executable is None:
        pytest.skip(
            "draw.io executable not found. "
            "This is expected in CI environments without draw.io installed. "
            "Install from: https://github.com/jgraph/drawio-desktop/releases"
        )

    assert drawio_executable.exists(), f"draw.io executable not found: {drawio_executable}"
    logger.info(f"draw.io executable found: {drawio_executable}")
