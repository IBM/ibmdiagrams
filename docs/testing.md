# Testing Guide

## Overview

This guide covers both visual regression testing and code coverage testing for the ibmdiagrams project. Visual regression testing ensures that IBM Cloud diagram elements render consistently, while code coverage testing helps maintain code quality by tracking which parts of the codebase are exercised by tests.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Code Coverage Testing](#code-coverage-testing)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Understanding Test Results](#understanding-test-results)
- [Updating Baselines](#updating-baselines)
- [Threshold Selection](#threshold-selection)
- [Troubleshooting](#troubleshooting)
- [CI Integration](#ci-integration)

## Prerequisites

### Required Software

1. **draw.io Desktop Application**
   - Download from: https://github.com/jgraph/drawio-desktop/releases
   - Required for converting `.drawio` files to PNG images
   - Tests will skip gracefully if not installed

2. **Python Dependencies**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Install development/testing dependencies
   pip install -r requirements-dev.txt
   
   # Or using uv (recommended)
   uv sync --group dev
   ```

### IBM Plex Sans Fonts

For accurate rendering, install IBM Plex Sans fonts:
- Download from: https://fonts.google.com/?query=Plex
- Install all IBM Plex Sans variants

## Quick Start

```bash
# Run all element visual regression tests
pytest tests/test_visual_regression.py

# Run complete diagram tests
pytest tests/test_complete_diagrams.py

# Run with verbose output
pytest tests/test_visual_regression.py -v

# Run in parallel (faster)
pytest tests/test_visual_regression.py -n auto

# Generate baseline for complete diagrams (first time)
pytest tests/test_complete_diagrams.py::test_slzpowervs_diagram --update-baselines -v

# Run tests with coverage report
pytest --cov=src/ibmdiagrams --cov-report=html

# Run tests with coverage and show missing lines
pytest --cov=src/ibmdiagrams --cov-report=term-missing
```

## Code Coverage Testing

### Overview

Code coverage testing measures which parts of the codebase are executed during test runs. This helps identify untested code and maintain high code quality standards.

### Running Coverage Tests

```bash
# Basic coverage report
pytest --cov=src/ibmdiagrams

# Coverage with HTML report (opens in browser)
pytest --cov=src/ibmdiagrams --cov-report=html
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux

# Coverage with terminal report showing missing lines
pytest --cov=src/ibmdiagrams --cov-report=term-missing

# Coverage for specific module
pytest --cov=src/ibmdiagrams/ibmcloud --cov-report=term-missing

# Coverage with branch coverage
pytest --cov=src/ibmdiagrams --cov-branch --cov-report=term-missing
```

### Coverage Configuration

Coverage settings are configured in [`pyproject.toml`](../pyproject.toml):

```toml
[tool.coverage.run]
source = ["src/ibmdiagrams"]
omit = [
    "*/tests/*",
    "*/test_*.py",
    "*/__pycache__/*",
    "*/site-packages/*",
]
branch = true

[tool.coverage.report]
precision = 2
show_missing = true
skip_covered = false
```

### Understanding Coverage Reports

**Terminal Report:**
```
Name                                    Stmts   Miss  Cover   Missing
---------------------------------------------------------------------
src/ibmdiagrams/__init__.py                 5      0   100%
src/ibmdiagrams/ibmbase/build.py          234     12    95%   45-48, 123-125
src/ibmdiagrams/ibmcloud/diagram.py       156      8    95%   89-92
---------------------------------------------------------------------
TOTAL                                    2456    145    94%
```

- **Stmts**: Total statements in the file
- **Miss**: Statements not executed during tests
- **Cover**: Percentage of statements covered
- **Missing**: Line numbers not covered

**HTML Report:**
- Open `htmlcov/index.html` in a browser
- Interactive view showing covered/uncovered lines
- Color-coded: green (covered), red (not covered)
- Click files to see line-by-line coverage

### Coverage Best Practices

1. **Aim for high coverage** (>90%) but focus on meaningful tests
2. **Review uncovered lines** to identify gaps in test coverage
3. **Use branch coverage** to ensure all code paths are tested
4. **Exclude generated code** and third-party code from coverage
5. **Run coverage regularly** during development
6. **Include coverage in CI** to prevent regressions

## Configuration

### Command-Line Options

#### `--threshold`
Maximum allowed difference percentage (0.0-100.0).

```bash
# Allow 1% difference
pytest tests/test_visual_regression.py --threshold=0.01

# Allow 5% difference
pytest tests/test_visual_regression.py --threshold=0.05
```

**Default:** 1.25

#### `--pixel-tolerance`
Per-pixel color tolerance (0-255) for handling anti-aliasing differences.

```bash
# Allow 5 units difference per color channel
pytest tests/test_visual_regression.py --pixel-tolerance=5
```

**Default:** 10

#### `--update-baselines`
Regenerate baseline images instead of comparing.

```bash
# Update all baselines
pytest tests/test_visual_regression.py --update-baselines

# Update specific element
pytest tests/test_visual_regression.py -k "vpc" --update-baselines
```

#### `--save-diffs`
Save diff images for failed comparisons.

```bash
pytest tests/test_visual_regression.py --save-diffs
```

Diff images are saved to `tests/visual_regression_diffs/`

### Environment Variables

#### `VISUAL_REGRESSION_THRESHOLD`
Set default threshold without command-line option.

```bash
export VISUAL_REGRESSION_THRESHOLD=0.01
pytest tests/test_visual_regression.py
```

#### `VISUAL_REGRESSION_PIXEL_TOLERANCE`
Set default pixel tolerance without command-line option.

```bash
export VISUAL_REGRESSION_PIXEL_TOLERANCE=5
pytest tests/test_visual_regression.py
```

### Per-Test Threshold Override

Use the `@pytest.mark.threshold()` marker for test-specific thresholds:

```python
@pytest.mark.threshold(0.05)
def test_complex_element_visual_regression(...):
    pass
```

## Running Tests

### Run All Tests

```bash
# Run all element tests
pytest tests/test_visual_regression.py

# Run all complete diagram tests
pytest tests/test_complete_diagrams.py

# Run all visual regression tests
pytest tests/test_visual_regression.py tests/test_complete_diagrams.py
```

### Run Specific Elements

```bash
# Single element
pytest tests/test_visual_regression.py -k "vpc"

# Multiple elements (pattern matching)
pytest tests/test_visual_regression.py -k "virtual-server or bare-metal"

# All expanded elements
pytest tests/test_visual_regression.py -k "expanded"

# Specific complete diagram
pytest tests/test_complete_diagrams.py::test_slzpowervs_diagram
```

### Parallel Execution

```bash
# Auto-detect CPU count
pytest tests/test_visual_regression.py -n auto

# Specific number of workers
pytest tests/test_visual_regression.py -n 4
```

### Verbose Output

```bash
# Show test names
pytest tests/test_visual_regression.py -v

# Show detailed output
pytest tests/test_visual_regression.py -vv

# Show print statements
pytest tests/test_visual_regression.py -s
```

## Understanding Test Results

### Successful Test

```
tests/test_visual_regression.py::test_element_visual_regression[vpc] PASSED
```

The generated diagram matches the baseline within the threshold.

### Failed Test

```
tests/test_visual_regression.py::test_element_visual_regression[vpc] FAILED

Visual regression test failed for element: vpc
  Label: VPC
  Difference: 2.34%
  Threshold: 0.00%
  Diff image: tests/visual_regression_diffs/vpc_diff.png

The generated diagram differs from the baseline by 2.34%.
This exceeds the allowed threshold of 0.00%.

Review the diff image at: tests/visual_regression_diffs/vpc_diff.png

If this change is intentional:
  1. Review the visual changes carefully
  2. Run: pytest tests/test_visual_regression.py --update-baselines
  3. Commit the updated baseline images
```

### Diff Images

Diff images show side-by-side comparison:
- **Left side:** Baseline image
- **Right side:** Generated image with differences highlighted in red

## Updating Baselines

### When to Update

Update baselines when:
- Intentional visual changes are made to diagram elements
- IBM Design Standards are updated
- Icon or shape definitions change
- Font rendering improvements are implemented

### How to Update

1. **Review Changes First**
   ```bash
   # Run tests with diff saving
   pytest tests/test_visual_regression.py --save-diffs
   
   # Review diff images in tests/visual_regression_diffs/
   ```

2. **Update Baselines**
   ```bash
   # Update all element baselines
   pytest tests/test_visual_regression.py --update-baselines
   
   # Update specific elements
   pytest tests/test_visual_regression.py -k "vpc or subnet" --update-baselines
   
   # Update complete diagram baselines
   pytest tests/test_complete_diagrams.py --update-baselines
   
   # Update specific complete diagram
   pytest tests/test_complete_diagrams.py::test_slzpowervs_diagram --update-baselines
   pytest tests/test_complete_diagrams.py::test_cloud_diagram --update-baselines
   ```

3. **Verify Updates**
   ```bash
   # Run tests again to confirm
   pytest tests/test_visual_regression.py
   ```

4. **Commit Changes**
   ```bash
   git add tests/baselines/png/
   git commit -m "Update visual regression baselines for [reason]"
   ```

## Threshold Selection

### Threshold Levels

| Threshold | Use Case | Description |
|-----------|----------|-------------|
| 0.0% | Exact match | No pixel differences allowed (default) |
| 0.01-1% | Very strict | Minor anti-aliasing differences |
| 1-5% | Moderate | Font rendering variations across platforms |
| 5-10% | Lenient | Significant platform differences |

### Guidelines

**Use 0.0% (exact match) when:**
- Running on the same platform consistently
- Baselines were generated on the same system
- Maximum precision is required

**Use 0.01-1% when:**
- Minor anti-aliasing differences are expected
- Font rendering may vary slightly
- Cross-platform testing with similar environments

**Use 1-5% when:**
- Testing across different operating systems
- Font rendering varies significantly
- Draw.io version differences exist

**Use 5-10% when:**
- Major platform differences (macOS vs Linux vs Windows)
- Different draw.io versions
- Temporary tolerance during development

### Platform-Specific Considerations

**macOS:**
- Font rendering is generally consistent
- Use threshold 0.0-0.01%

**Linux:**
- Font rendering may vary by distribution
- Use threshold 0.01-1%
- Consider using xvfb for headless environments

**Windows:**
- Font rendering may differ from macOS/Linux
- Use threshold 1-5%

**CI Environments:**
- Use higher threshold (1-5%) for flexibility
- Consider platform-specific baselines if needed

## Troubleshooting

### draw.io Not Found

**Error:**
```
draw.io executable not found. Please install draw.io desktop application.
Download from: https://github.com/jgraph/drawio-desktop/releases
```

**Solution:**
1. Install draw.io desktop application
2. Ensure it's in your PATH or at a standard location
3. Tests will skip gracefully if not found

### Baseline Images Missing

**Error:**
```
Baseline image not found: tests/baselines/png/vpc.png
Run 'pytest tests/test_visual_regression.py --update-baselines' to generate baselines.
```

**Solution:**
```bash
pytest tests/test_visual_regression.py --update-baselines
```

### Image Size Mismatch

**Error:**
```
Image dimensions don't match: (800, 600) vs (1024, 768)
```

**Cause:** Diagram generation changed significantly

**Solution:**
1. Review the changes
2. If intentional, update baselines:
   ```bash
   pytest tests/test_visual_regression.py --update-baselines
   ```

### High Difference Percentage

**Error:**
```
Difference: 15.34%
Threshold: 0.00%
```

**Solutions:**

1. **Review diff image:**
   ```bash
   pytest tests/test_visual_regression.py --save-diffs
   # Check tests/visual_regression_diffs/
   ```

2. **Adjust threshold if appropriate:**
   ```bash
   pytest tests/test_visual_regression.py --threshold=1.0
   ```

3. **Update baseline if intentional:**
   ```bash
   pytest tests/test_visual_regression.py --update-baselines
   ```

### Font Rendering Differences

**Issue:** Tests fail due to font rendering variations

**Solutions:**

1. **Install IBM Plex Sans fonts** on all systems
2. **Use pixel tolerance:**
   ```bash
   pytest tests/test_visual_regression.py --pixel-tolerance=5
   ```
3. **Use appropriate threshold:**
   ```bash
   pytest tests/test_visual_regression.py --threshold=1.0
   ```

### Slow Test Execution

**Issue:** Tests take too long to run

**Solutions:**

1. **Run in parallel:**
   ```bash
   pytest tests/test_visual_regression.py -n auto
   ```

2. **Run specific tests:**
   ```bash
   pytest tests/test_visual_regression.py -k "vpc or subnet"
   ```

3. **Skip draw.io conversion** (if already generated):
   - Tests cache generated diagrams in temp directories

## CI Integration

The repository includes a base GitHub Actions workflow at `.github/workflows/ci.yml` that runs Ruff, pytest, and package build checks on Python 3.11. The visual regression workflow below is optional for environments that install draw.io desktop and IBM Plex Sans fonts.

**Note:** If GitHub Actions workflows are available in your repository, you can use them to automate testing. The examples below show how to configure visual regression testing in CI environments.

### Visual Regression GitHub Actions Example

```yaml
name: Visual Regression Tests

on: [push, pull_request]

jobs:
  visual-regression:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Install draw.io
      run: |
        wget https://github.com/jgraph/drawio-desktop/releases/download/v22.1.2/drawio-amd64-22.1.2.deb
        sudo apt-get install -y ./drawio-amd64-22.1.2.deb
    
    - name: Install IBM Plex Sans fonts
      run: |
        sudo apt-get install -y fonts-ibm-plex
    
    - name: Run visual regression tests
      run: |
        pytest tests/test_visual_regression.py \
          --threshold=1.0 \
          --save-diffs \
          -n auto
    
    - name: Upload diff images
      if: failure()
      uses: actions/upload-artifact@v3
      with:
        name: visual-regression-diffs
        path: tests/visual_regression_diffs/
```

### CI Best Practices

1. **Use appropriate threshold** (1-5% for CI)
2. **Save diff images** as artifacts on failure
3. **Run in parallel** for faster execution
4. **Install draw.io** in CI environment
5. **Install fonts** for consistent rendering
6. **Cache dependencies** to speed up builds

## Advanced Usage

### Custom Comparison Logic

For advanced use cases, you can use the image comparison utilities directly:

```python
from pathlib import Path
from tests.utils.image_comparison import compare_images, save_diff_image

# Compare two images
is_match, diff_percentage, diff_image = compare_images(
    Path("image1.png"),
    Path("image2.png"),
    threshold=1.0
)

# Save diff if needed
if not is_match and diff_image:
    save_diff_image(diff_image, Path("diff.png"))
```

### Generating Baselines Programmatically

```python
from pathlib import Path
from tests.utils.baseline_elements import get_baseline_elements
from tests.utils.baseline_utils import (
    generate_baseline_diagram,
    setup_baseline_directories,
    find_drawio_executable
)

# Setup
elements = get_baseline_elements()
drawio_dir, png_dir = setup_baseline_directories()
drawio_path = find_drawio_executable()

# Generate specific element
element = elements[0]  # First element
generate_baseline_diagram(element, drawio_dir, png_dir, drawio_path)
```

## Best Practices

1. **Run tests before committing** visual changes
2. **Review diff images** before updating baselines
3. **Use appropriate thresholds** for your environment
4. **Document intentional changes** in commit messages
5. **Keep baselines up to date** with code changes
6. **Run tests in CI** to catch regressions early
7. **Use parallel execution** for faster feedback
8. **Save diff images** when debugging failures

## Support

For issues or questions:
1. Check this documentation
2. Review existing test code in `tests/test_visual_regression.py`
3. Check image comparison utilities in `tests/utils/image_comparison.py`
4. Open an issue on the project repository
