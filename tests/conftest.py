"""
Pytest configuration and fixtures for visual regression testing.

This module provides fixtures and configuration for running visual regression
tests on IBM Cloud diagram elements.
"""

import os
import tempfile
from collections.abc import Generator
from pathlib import Path

import pytest
from utils.baseline_elements import get_baseline_elements
from utils.baseline_utils import find_drawio_executable, setup_baseline_directories


def pytest_addoption(parser: pytest.Parser) -> None:
    """
    Add custom command-line options for visual regression testing.

    Args:
        parser: Pytest command-line parser.
    """
    parser.addoption(
        "--threshold",
        action="store",
        default="0.5",
        type=float,
        help="Maximum allowed difference percentage for image comparison (0.0-100.0). Default: 0.5",
    )
    parser.addoption(
        "--update-baselines",
        action="store_true",
        default=False,
        help="Regenerate baseline images instead of comparing. Use when intentional visual changes are made.",
    )
    parser.addoption(
        "--save-diffs",
        action="store_true",
        default=False,
        help="Save diff images for failed comparisons to help debug visual differences.",
    )
    parser.addoption(
        "--pixel-tolerance",
        action="store",
        default="10",
        type=int,
        help="Per-pixel color tolerance (0-255) for handling anti-aliasing differences. Default: 10",
    )


def pytest_configure(config: pytest.Config) -> None:
    """
    Register custom markers for visual regression testing.

    Args:
        config: Pytest configuration object.
    """
    config.addinivalue_line(
        "markers",
        "visual_regression: mark test as a visual regression test",
    )
    config.addinivalue_line(
        "markers",
        "threshold(value): override default threshold for a specific test",
    )


@pytest.fixture(scope="session")
def baseline_elements() -> list:
    """
    Provide list of all baseline diagram elements for testing.

    Returns:
        List of DiagramElement instances from baseline_elements.py.
    """
    return get_baseline_elements()


@pytest.fixture(scope="session")
def baseline_dirs() -> tuple[Path, Path]:
    """
    Provide paths to baseline directories.

    Returns:
        Tuple of (drawio_dir, png_dir) paths.
    """
    return setup_baseline_directories()


@pytest.fixture(scope="session")
def default_threshold(request: pytest.FixtureRequest) -> float:
    """
    Provide default comparison threshold from command-line or environment.

    Priority:
    1. Command-line option (--threshold)
    2. Environment variable (VISUAL_REGRESSION_THRESHOLD)
    3. Default value (0.0)

    Args:
        request: Pytest fixture request object.

    Returns:
        Threshold value as float (0.0-100.0).
    """
    # Check command-line option first
    threshold = request.config.getoption("--threshold")

    # Fall back to environment variable if not set via CLI
    if threshold == 0.5:  # Default value
        env_threshold = os.environ.get("VISUAL_REGRESSION_THRESHOLD")
        if env_threshold is not None:
            try:
                threshold = float(env_threshold)
            except ValueError:
                pytest.fail(
                    f"Invalid VISUAL_REGRESSION_THRESHOLD value: {env_threshold}. "
                    "Must be a number between 0.0 and 100.0"
                )

    # Validate threshold range
    if not 0.0 <= threshold <= 100.0:
        pytest.fail(f"Threshold must be between 0.0 and 100.0, got {threshold}")

    return threshold


@pytest.fixture(scope="session")
def pixel_tolerance(request: pytest.FixtureRequest) -> int:
    """
    Provide per-pixel color tolerance from command-line or environment.

    Priority:
    1. Command-line option (--pixel-tolerance)
    2. Environment variable (VISUAL_REGRESSION_PIXEL_TOLERANCE)
    3. Default value (0)

    Args:
        request: Pytest fixture request object.

    Returns:
        Pixel tolerance value as int (0-255).
    """
    # Check command-line option first
    tolerance = request.config.getoption("--pixel-tolerance")

    # Fall back to environment variable if not set via CLI
    if tolerance == 10:  # Default value
        env_tolerance = os.environ.get("VISUAL_REGRESSION_PIXEL_TOLERANCE")
        if env_tolerance is not None:
            try:
                tolerance = int(env_tolerance)
            except ValueError:
                pytest.fail(
                    f"Invalid VISUAL_REGRESSION_PIXEL_TOLERANCE value: {env_tolerance}. "
                    "Must be an integer between 0 and 255"
                )

    # Validate tolerance range
    if not 0 <= tolerance <= 255:
        pytest.fail(f"Pixel tolerance must be between 0 and 255, got {tolerance}")

    return tolerance


@pytest.fixture(scope="session")
def update_baselines(request: pytest.FixtureRequest) -> bool:
    """
    Check if baseline update mode is enabled.

    Args:
        request: Pytest fixture request object.

    Returns:
        True if baselines should be updated, False otherwise.
    """
    return request.config.getoption("--update-baselines")


@pytest.fixture(scope="session")
def save_diffs(request: pytest.FixtureRequest) -> bool:
    """
    Check if diff images should be saved on failure.

    Args:
        request: Pytest fixture request object.

    Returns:
        True if diff images should be saved, False otherwise.
    """
    return request.config.getoption("--save-diffs")


@pytest.fixture(scope="function")
def temp_output_dir() -> Generator[Path, None, None]:
    """
    Provide temporary directory for test-generated diagrams.

    The directory is automatically cleaned up after the test completes.

    Yields:
        Path to temporary directory.
    """
    with tempfile.TemporaryDirectory(prefix="visual_regression_") as tmpdir:
        yield Path(tmpdir)


@pytest.fixture(scope="session")
def drawio_executable() -> Path | None:
    """
    Find and provide path to draw.io executable.

    Returns:
        Path to draw.io executable, or None if not found.
    """
    return find_drawio_executable()


@pytest.fixture(scope="function")
def test_threshold(request: pytest.FixtureRequest, default_threshold: float) -> float:
    """
    Provide threshold for current test, respecting test-specific overrides.

    Checks for @pytest.mark.threshold(value) marker on the test function.

    Args:
        request: Pytest fixture request object.
        default_threshold: Default threshold from session fixture.

    Returns:
        Threshold value for the current test.
    """
    # Check for test-specific threshold marker
    marker = request.node.get_closest_marker("threshold")
    if marker is not None and len(marker.args) > 0:
        threshold = marker.args[0]
        if not isinstance(threshold, int | float):
            pytest.fail(f"Threshold marker must have a numeric value, got {type(threshold)}")
        if not 0.0 <= threshold <= 100.0:
            pytest.fail(f"Threshold must be between 0.0 and 100.0, got {threshold}")
        return float(threshold)

    return default_threshold


@pytest.fixture(scope="session")
def diff_output_dir() -> Path:
    """
    Provide directory for saving diff images.

    Creates the directory if it doesn't exist.

    Returns:
        Path to diff output directory.
    """
    diff_dir = Path(__file__).parent / "visual_regression_diffs"
    diff_dir.mkdir(parents=True, exist_ok=True)
    return diff_dir
