"""
Image comparison utilities for visual regression testing.

This module provides functions to compare images with configurable thresholds,
generate visual diffs, and calculate image hashes for quick exact matching.
"""

import hashlib
import logging
from pathlib import Path
from typing import Optional

import numpy as np
from PIL import Image, ImageDraw

logger = logging.getLogger(__name__)


class ImageComparisonError(Exception):
    """Base exception for image comparison errors."""

    pass


class ImageSizeMismatchError(ImageComparisonError):
    """Raised when images have different dimensions."""

    pass


class ImageLoadError(ImageComparisonError):
    """Raised when an image cannot be loaded."""

    pass


def calculate_image_hash(image_path: Path) -> str:
    """
    Calculate SHA-256 hash of an image file for quick exact matching.

    Args:
        image_path: Path to the image file.

    Returns:
        Hexadecimal hash string.

    Raises:
        ImageLoadError: If the image cannot be read.
    """
    try:
        with open(image_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception as e:
        raise ImageLoadError(f"Failed to read image {image_path}: {e}") from e


def compare_images(
    image1_path: Path,
    image2_path: Path,
    threshold: float = 0.0,
) -> tuple[bool, float, Optional[Image.Image]]:
    """
    Compare two images with configurable threshold.

    Performs pixel-by-pixel comparison and calculates the percentage of
    different pixels. Optionally generates a visual diff image highlighting
    differences in red.

    Args:
        image1_path: Path to the first image.
        image2_path: Path to the second image.
        threshold: Maximum allowed difference percentage (0.0-100.0).
                  0.0 means exact match required.
                  Values represent percentage of different pixels allowed.

    Returns:
        Tuple of (is_match, difference_percentage, diff_image):
        - is_match: True if images match within threshold
        - difference_percentage: Percentage of different pixels (0.0-100.0)
        - diff_image: PIL Image showing differences (None if exact match)

    Raises:
        ImageLoadError: If either image cannot be loaded.
        ImageSizeMismatchError: If images have different dimensions.
        ValueError: If threshold is invalid.
    """
    # Validate threshold
    if not 0.0 <= threshold <= 100.0:
        raise ValueError(f"Threshold must be between 0.0 and 100.0, got {threshold}")

    # Load images
    try:
        img1 = Image.open(image1_path).convert("RGB")
    except Exception as e:
        raise ImageLoadError(f"Failed to load image {image1_path}: {e}") from e

    try:
        img2 = Image.open(image2_path).convert("RGB")
    except Exception as e:
        raise ImageLoadError(f"Failed to load image {image2_path}: {e}") from e

    # Check dimensions match
    if img1.size != img2.size:
        raise ImageSizeMismatchError(
            f"Image dimensions don't match: {img1.size} vs {img2.size}"
        )

    # Quick exact match check using hash
    if threshold == 0.0:
        hash1 = calculate_image_hash(image1_path)
        hash2 = calculate_image_hash(image2_path)
        if hash1 == hash2:
            logger.debug("Images match exactly (hash comparison)")
            return True, 0.0, None

    # Convert to numpy arrays for efficient comparison
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Calculate pixel-wise differences
    # For RGB images, consider a pixel different if any channel differs
    pixel_diff = np.any(arr1 != arr2, axis=2)
    different_pixels = np.sum(pixel_diff)
    total_pixels = arr1.shape[0] * arr1.shape[1]

    # Calculate difference percentage
    diff_percentage = (different_pixels / total_pixels) * 100.0

    # Determine if images match within threshold
    is_match = diff_percentage <= threshold

    # Generate diff image if there are differences
    diff_image = None
    if different_pixels > 0:
        diff_image = _generate_diff_image(img1, img2, pixel_diff)

    logger.debug(
        f"Image comparison: {diff_percentage:.2f}% different "
        f"(threshold: {threshold}%, match: {is_match})"
    )

    return is_match, diff_percentage, diff_image


def _generate_diff_image(
    img1: Image.Image, img2: Image.Image, pixel_diff: np.ndarray
) -> Image.Image:
    """
    Generate a visual diff image highlighting differences.

    Creates a side-by-side comparison with differences highlighted in red.

    Args:
        img1: First image.
        img2: Second image.
        pixel_diff: Boolean array indicating different pixels.

    Returns:
        PIL Image showing the diff visualization.
    """
    width, height = img1.size

    # Create side-by-side comparison image
    diff_img = Image.new("RGB", (width * 2, height))
    diff_img.paste(img1, (0, 0))
    diff_img.paste(img2, (width, 0))

    # Highlight differences in red on the second image
    draw = ImageDraw.Draw(diff_img)
    for y in range(height):
        for x in range(width):
            if pixel_diff[y, x]:
                # Draw red pixel on the right side
                draw.point((width + x, y), fill=(255, 0, 0))

    return diff_img


def save_diff_image(diff_image: Image.Image, output_path: Path) -> None:
    """
    Save a diff image to disk.

    Args:
        diff_image: PIL Image to save.
        output_path: Path where the image will be saved.

    Raises:
        ImageComparisonError: If the image cannot be saved.
    """
    try:
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Save as PNG with high quality
        diff_image.save(output_path, "PNG", optimize=False)
        logger.info(f"Saved diff image to {output_path}")

    except Exception as e:
        raise ImageComparisonError(f"Failed to save diff image to {output_path}: {e}") from e


def compare_images_with_tolerance(
    image1_path: Path,
    image2_path: Path,
    pixel_tolerance: int = 0,
    threshold: float = 0.0,
) -> tuple[bool, float, Optional[Image.Image]]:
    """
    Compare images with per-pixel tolerance for color differences.

    This is useful for handling minor anti-aliasing or compression artifacts.

    Args:
        image1_path: Path to the first image.
        image2_path: Path to the second image.
        pixel_tolerance: Maximum allowed difference per color channel (0-255).
                        0 means exact match required per pixel.
        threshold: Maximum allowed percentage of different pixels (0.0-100.0).

    Returns:
        Tuple of (is_match, difference_percentage, diff_image).

    Raises:
        ImageLoadError: If either image cannot be loaded.
        ImageSizeMismatchError: If images have different dimensions.
        ValueError: If parameters are invalid.
    """
    # Validate parameters
    if not 0 <= pixel_tolerance <= 255:
        raise ValueError(f"Pixel tolerance must be between 0 and 255, got {pixel_tolerance}")
    if not 0.0 <= threshold <= 100.0:
        raise ValueError(f"Threshold must be between 0.0 and 100.0, got {threshold}")

    # Load images
    try:
        img1 = Image.open(image1_path).convert("RGB")
    except Exception as e:
        raise ImageLoadError(f"Failed to load image {image1_path}: {e}") from e

    try:
        img2 = Image.open(image2_path).convert("RGB")
    except Exception as e:
        raise ImageLoadError(f"Failed to load image {image2_path}: {e}") from e

    # Check dimensions match
    if img1.size != img2.size:
        raise ImageSizeMismatchError(
            f"Image dimensions don't match: {img1.size} vs {img2.size}"
        )

    # Convert to numpy arrays
    arr1 = np.array(img1, dtype=np.int16)
    arr2 = np.array(img2, dtype=np.int16)

    # Calculate absolute difference per channel
    channel_diff = np.abs(arr1 - arr2)

    # A pixel is different if any channel exceeds tolerance
    pixel_diff = np.any(channel_diff > pixel_tolerance, axis=2)
    different_pixels = np.sum(pixel_diff)
    total_pixels = arr1.shape[0] * arr1.shape[1]

    # Calculate difference percentage
    diff_percentage = (different_pixels / total_pixels) * 100.0

    # Determine if images match within threshold
    is_match = diff_percentage <= threshold

    # Generate diff image if there are differences
    diff_image = None
    if different_pixels > 0:
        diff_image = _generate_diff_image(img1, img2, pixel_diff)

    logger.debug(
        f"Image comparison (tolerance={pixel_tolerance}): {diff_percentage:.2f}% different "
        f"(threshold: {threshold}%, match: {is_match})"
    )

    return is_match, diff_percentage, diff_image
