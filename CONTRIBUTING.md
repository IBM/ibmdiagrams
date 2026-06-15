# Contributing to IBM Diagrams

Thank you for your interest in contributing to IBM Diagrams! 🎉 We're excited to have you here. Whether you're fixing a bug, adding a feature, improving documentation, or just asking questions, your contributions make this project better for everyone.

This guide will help you get started with contributing to IBM Diagrams. We've designed it to be welcoming for both first-time contributors and experienced developers.

---

## 📋 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Ways to Contribute](#ways-to-contribute)
3. [Getting Started](#getting-started)
4. [Development Workflow](#development-workflow)
5. [Reporting Issues](#reporting-issues)
6. [Submitting Pull Requests](#submitting-pull-requests)
7. [Development Setup](#development-setup)
8. [Testing Guidelines](#testing-guidelines)
9. [Code Style and Standards](#code-style-and-standards)
10. [Documentation](#documentation)
11. [Community and Support](#community-and-support)

---

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

**In short**: Be respectful, be kind, and help us maintain a welcoming community for everyone.

---

## Ways to Contribute

There are many ways to contribute to IBM Diagrams, and all contributions are valued:

### 🐛 Report Bugs
Found something that doesn't work? Let us know! Clear bug reports help us fix issues quickly.

### ✨ Suggest Features
Have an idea for a new feature or improvement? We'd love to hear it!

### 📝 Improve Documentation
Help others by improving guides, fixing typos, or adding examples.

### 💻 Write Code
Fix bugs, implement features, or improve performance.

### 🧪 Add Tests
Increase code coverage and prevent regressions.

### 🎨 Design Examples
Create example diagrams that showcase IBM Diagrams capabilities.

### 💬 Help Others
Answer questions, review pull requests, or help newcomers get started.

### 🌍 Translate
Help make IBM Diagrams accessible to more people by improving documentation for global audiences.

---

## Getting Started

### Prerequisites

Before you begin, ensure you have:

- **Python 3.11+** installed ([Download](https://www.python.org/downloads/))
- **Git** for version control
- **draw.io Desktop** for testing diagrams ([Download](https://github.com/jgraph/drawio-desktop/releases))
- **IBM Plex Sans fonts** for proper rendering ([Install](https://fonts.google.com/?query=Plex))
- **GPG key** for signing commits (required for main branch contributions)

### Setup GPG Signing

This repository requires signed commits for contributions to the main branch. Follow these steps to set up GPG signing:

**1. Generate a GPG key (if you don't have one):**

```bash
# Generate a new GPG key
gpg --full-generate-key

# When prompted:
# - Select RSA and RSA (default)
# - Key size: 4096 bits
# - Expiration: 0 (key does not expire) or set an expiration date
# - Enter your name and email (use the same email as your GitHub account)
```

**2. List your GPG keys and copy the key ID:**

```bash
# List your GPG keys
gpg --list-secret-keys --keyid-format=long

# Output will look like:
# sec   rsa4096/YOUR_KEY_ID 2024-01-01 [SC]
# Copy the YOUR_KEY_ID part (the part after rsa4096/)
```

**3. Add your GPG key to GitHub:**

```bash
# Export your public key
gpg --armor --export YOUR_KEY_ID

# Copy the output (including -----BEGIN PGP PUBLIC KEY BLOCK----- and -----END PGP PUBLIC KEY BLOCK-----)
# Go to GitHub Settings > SSH and GPG keys > New GPG key
# Paste your key and save
```

**4. Configure Git to sign commits:**

```bash
# Tell Git to use your GPG key
git config --global user.signingkey YOUR_KEY_ID

# Enable commit signing by default
git config --global commit.gpgsign true

# Optional: Enable tag signing
git config --global tag.gpgsign true
```

**5. Test your setup:**

```bash
# Make a test commit
git commit --allow-empty -m "Test signed commit"

# Verify the signature
git log --show-signature -1
```

**Troubleshooting:**

If you encounter issues with GPG signing:

```bash
# On macOS, you may need to configure GPG to use the correct TTY
echo 'export GPG_TTY=$(tty)' >> ~/.bashrc  # or ~/.zshrc
source ~/.bashrc  # or ~/.zshrc

# If using GPG 2.x, you may need to add this to ~/.gnupg/gpg.conf
echo 'use-agent' >> ~/.gnupg/gpg.conf

# Restart the GPG agent
gpgconf --kill gpg-agent
```

For more detailed instructions, see [GitHub's GPG documentation](https://docs.github.com/en/authentication/managing-commit-signature-verification).

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone git@github.com:YOUR-USERNAME/ibmdiagrams.git
   cd ibmdiagrams
   ```
3. **Add upstream remote** to stay in sync:
   ```bash
   git remote add upstream git@github.com:IBM/ibmdiagrams.git
   ```

### Install Dependencies

We recommend using **uv** for faster dependency management:

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Verify installation
uv run ibmdiagrams --help
```

**Alternative (using pip):**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install in editable mode
pip install -e .
```

---

## Development Workflow

### 1. Create a Branch

Always create a new branch for your work. **Never commit directly to `main`**.

```bash
# Update your main branch
git checkout main
git pull upstream main

# Create a feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/issue-123-description
```

**Branch naming conventions:**
- `feature/` - New features or enhancements
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `test/` - Test additions or improvements
- `refactor/` - Code refactoring

### 2. Make Your Changes

- Write clear, readable code
- Follow existing code style and conventions
- Add tests for new functionality
- Update documentation as needed
- Keep commits focused and atomic

### 3. Test Your Changes

Before submitting, ensure all tests pass:

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_visual_regression.py -v

# Run with coverage
pytest tests/ --cov=src/ibmdiagrams --cov-report=html
```

See [Testing Guidelines](#testing-guidelines) for more details.

### 4. Commit Your Changes

Write clear, descriptive commit messages. **All commits must be signed** for contributions to the main branch:

```bash
git add .
git commit -m "Add support for new IBM Cloud service

- Implement VirtualPrivateEndpoint class
- Add corresponding icon and shape definitions
- Include tests and documentation
- Fixes #123"

# Verify your commit is signed
git log --show-signature -1
```

**Note:** If you've configured `commit.gpgsign true` globally (as shown in [Setup GPG Signing](#setup-gpg-signing)), all commits will be automatically signed. Otherwise, use `git commit -S` to sign individual commits.

**Good commit message format:**
```
Short summary (50 chars or less)

More detailed explanation if needed. Wrap at 72 characters.
Explain what and why, not how.

- Bullet points are okay
- Use present tense ("Add feature" not "Added feature")
- Reference issues and PRs

Fixes #123
```

### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create pull request on GitHub
```

---

## Reporting Issues

### Before Creating an Issue

1. **Search existing issues** to avoid duplicates
2. **Check the documentation** - your question might be answered there
3. **Try the latest version** - the issue might already be fixed

### Bug Reports

When reporting a bug, please include:

**Title Format:** `[VERSION][BUG] Brief description`
- Example: `[3.1.10][BUG] Terraform parser fails with nested modules`

**Required Information:**
- **IBM Diagrams version** (run `ibmdiagrams --version`)
- **Python version** (run `python --version`)
- **Operating system** (macOS, Windows, Linux)
- **Steps to reproduce** the issue
- **Expected behavior** vs **actual behavior**
- **Error messages** or logs (as text or code blocks, not screenshots)
- **Minimal reproducible example** if possible

**Optional but Helpful:**
- Screenshots of diagram output
- Sample input files (Terraform state, Python code)
- Relevant configuration files

**Labels:** Add the `bug` label. For urgent security issues, use `vulnerability`.

**Example:**
```markdown
## Bug Description
Terraform parser crashes when processing nested module resources.

## Steps to Reproduce
1. Run `ibmdiagrams nested-modules.tfstate`
2. Parser fails with KeyError

## Expected Behavior
Should generate diagram with all resources from nested modules.

## Actual Behavior
Crashes with error: `KeyError: 'module.vpc.resource'`

## Environment
- IBM Diagrams: 3.1.10
- Python: 3.11.5
- OS: macOS 14.0

## Error Log
```
[paste error log here]
```

## Sample File
[Attach or link to minimal tfstate file that reproduces the issue]
```

### Feature Requests

When suggesting a feature, please include:

**Title Format:** `[VERSION] Feature name`
- Example: `[3.2.0] Add support for IBM Cloud Code Engine`

**Required Information:**
- **User story**: "As a [user type], I want [goal] so that [benefit]"
- **Detailed description** of the proposed feature
- **Use cases** - when and why would this be useful?
- **Proposed implementation** (if you have ideas)
- **Alternatives considered**

**Labels:** Add the `enhancement` label.

**Example:**
```markdown
## Feature Request

### User Story
As an IBM Cloud developer, I want to include Code Engine applications in my diagrams so that I can document serverless architectures.

### Description
Add support for IBM Cloud Code Engine resources including applications, jobs, and functions.

### Use Cases
1. Documenting serverless microservices architectures
2. Showing event-driven workflows
3. Visualizing container-based applications

### Proposed Implementation
- Add `CodeEngineApp`, `CodeEngineJob`, `CodeEngineFunction` classes
- Include Code Engine icons from IBM Design Library
- Support Terraform state parsing for Code Engine resources

### Alternatives
Currently, users must manually add these as generic containers, which doesn't follow IBM design standards.
```

---

## Submitting Pull Requests

### Pull Request Checklist

Before submitting your PR, ensure:

- [ ] **Branch is up to date** with `main`
- [ ] **All tests pass** locally
- [ ] **Code follows style guidelines** (pre-commit hooks pass)
- [ ] **New code has tests** (maintain or improve coverage)
- [ ] **Documentation is updated** (if applicable)
- [ ] **Commit messages are clear** and descriptive
- [ ] **All commits are signed** with GPG (required for main branch)
- [ ] **PR references related issue(s)**
- [ ] **No merge conflicts** with main branch

### Pull Request Guidelines

1. **Link to Issue**: Reference the issue your PR addresses
   - Use keywords: `Fixes #123`, `Closes #123`, `Resolves #123`

2. **Clear Description**: Explain what changes you made and why
   ```markdown
   ## Changes
   - Added support for VirtualPrivateEndpoint
   - Updated Terraform parser to handle new resource type
   - Added visual regression tests
   
   ## Why
   Addresses feature request in #123 for VPE support
   
   ## Testing
   - Added unit tests for VPE class
   - Added visual regression baseline
   - Tested with sample Terraform state
   
   ## Screenshots
   [Include before/after diagrams if applicable]
   ```

3. **Keep PRs Focused**: One feature or fix per PR
   - Easier to review
   - Faster to merge
   - Simpler to revert if needed

4. **Update Documentation**: If your PR changes behavior or adds features
   - Update relevant `.md` files in `docs/`
   - Add examples if appropriate
   - Update `CHANGELOG.md`

5. **Respond to Feedback**: Be open to suggestions and iterate on your PR

### Review Process

- **At least 2 reviews required** before merging
- **Maintainers will review** within a few business days
- **Be patient and respectful** during the review process
- **Address feedback promptly** to keep the PR moving

### After Your PR is Merged

1. **Delete your branch** (GitHub will prompt you)
2. **Update your local repository**:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
3. **Celebrate!** 🎉 You've contributed to IBM Diagrams!

---

## Development Setup

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality and security. The hooks run automatically before each commit.

**Installation:**

```bash
# Install pre-commit (if not already installed)
pip install pre-commit

# Or with uv
uv pip install pre-commit

# Install the git hooks
pre-commit install
```

**Configured Hooks:**

1. **Ruff** - Fast Python linter and formatter
   - Automatically fixes issues when possible
   - Enforces code style consistency
   - Checks for common errors

2. **Detect Secrets** - Prevents committing sensitive information
   - Scans for API keys, passwords, tokens, etc.
   - Uses baseline file (`.secrets.baseline`) for known false positives

**Manual Execution:**

```bash
# Run all hooks on all files
pre-commit run --all-files

# Run specific hook
pre-commit run ruff --all-files
pre-commit run detect-secrets --all-files

# Skip hooks for a commit (use sparingly!)
git commit --no-verify
```

**Updating Secrets Baseline:**

If detect-secrets flags a false positive:

```bash
# Regenerate the baseline
detect-secrets scan > .secrets.baseline

# Or update with new findings
detect-secrets scan --baseline .secrets.baseline
```

### Development Tools

**Recommended VS Code Extensions:**
- Python (Microsoft)
- Ruff (Astral Software)
- GitLens
- Better Comments

**Useful Commands:**

```bash
# Format code with ruff
ruff format src/ tests/

# Lint code
ruff check src/ tests/

# Type checking (if using mypy)
mypy src/

# Build package
python -m build

# Install local development version
pip install -e .
```

---

## Testing Guidelines

Testing is crucial for maintaining code quality and preventing regressions. We use **pytest** for testing and have visual regression tests for diagram output.

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_visual_regression.py -v

# Run specific test
pytest tests/test_visual_regression.py::test_vpc_diagram -v

# Run with coverage report
pytest tests/ --cov=src/ibmdiagrams --cov-report=html

# Run tests in parallel (faster)
pytest tests/ -n auto
```

### Visual Regression Tests

Visual regression tests ensure diagram rendering remains consistent:

```bash
# Run visual regression tests
pytest tests/test_visual_regression.py -v
pytest tests/test_complete_diagrams.py -v

# Update baselines (after intentional changes)
pytest tests/test_visual_regression.py --update-baselines
pytest tests/test_complete_diagrams.py --update-baselines

# Update specific baseline
pytest tests/test_complete_diagrams.py::test_slzpowervs_diagram --update-baselines -v
```

**When to Update Baselines:**
- You've intentionally changed diagram rendering
- You've updated icons or shapes
- You've modified layout algorithms
- You've changed IBM design standard implementation

**Important:** Always commit baseline changes with a clear explanation:
```bash
git add tests/baselines/
git commit -m "Update visual regression baselines: improved VPC layout spacing"
```

### Writing Tests

When adding new features, include tests:

**Unit Tests:**
```python
# tests/test_new_feature.py
import pytest
from ibmdiagrams.ibmcloud.compute import NewService

def test_new_service_creation():
    """Test that NewService can be instantiated."""
    service = NewService("Test Service", "10.0.0.1")
    assert service.label == "Test Service"
    assert service.sublabel == "10.0.0.1"

def test_new_service_properties():
    """Test NewService properties."""
    service = NewService("Test")
    assert service.shape == "square"
    assert service.icon is not None
```

**Visual Regression Tests:**
```python
# tests/test_visual_regression.py
def test_new_service_rendering(diagram_tester):
    """Test NewService renders correctly."""
    from ibmdiagrams.ibmcloud.compute import NewService
    
    with diagram_tester("new-service"):
        service = NewService("Test Service")
    
    # Baseline will be created/compared automatically
```

See [docs/testing.md](docs/testing.md) for comprehensive testing documentation.

---

## Code Style and Standards

### Python Style Guide

We follow **PEP 8** with some project-specific conventions:

- **Line length**: 100 characters (not 79)
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Double quotes for strings
- **Imports**: Organized and sorted
- **Type hints**: Encouraged for public APIs

**Ruff** enforces these automatically via pre-commit hooks.

### Code Organization

```
src/ibmdiagrams/
├── ibmbase/          # Core diagram generation logic
├── ibmcloud/         # IBM Cloud-specific components
├── ibmshapes/        # Alternative shape library
└── ibmscripts/       # CLI entry points
```

**Module Guidelines:**
- Keep modules focused and cohesive
- Use relative imports within modules
- Use absolute imports between modules
- Follow existing patterns for consistency

### Naming Conventions

```python
# Classes: PascalCase
class VirtualServer:
    pass

# Functions and variables: snake_case
def generate_diagram():
    resource_name = "my-resource"

# Constants: UPPER_SNAKE_CASE
MAX_DIAGRAM_SIZE = 10000

# Private: prefix with underscore
def _internal_helper():
    pass
```

### Documentation Strings

Use clear docstrings for public APIs:

```python
def create_vpc(name: str, cidr: str) -> VPC:
    """Create a VPC resource.
    
    Args:
        name: The VPC name
        cidr: The CIDR block (e.g., "10.0.0.0/16")
    
    Returns:
        VPC: The created VPC instance
    
    Example:
        >>> vpc = create_vpc("my-vpc", "10.0.0.0/16")
    """
    return VPC(name, cidr)
```

### IBM Design Standards

When adding new components, follow IBM Design Language:

- **Colors**: Use colors from `ibmbase/colors.py` (IBM Color Palette)
- **Fonts**: Default to IBM Plex Sans
- **Labels**: Support two-line format with SemiBold primary and regular sublabel
- **Shapes**: Follow existing patterns (groups, zones, nodes, actors)
- **Icons**: Use official IBM Design icons

**Example:**
```python
from ibmdiagrams.ibmbase.colors import IBM_BLUE_60
from ibmdiagrams.ibmbase.shapes import create_square_node

class NewService:
    """New IBM Cloud service."""
    
    def __init__(self, label: str, sublabel: str = ""):
        self.label = label
        self.sublabel = sublabel
        self.color = IBM_BLUE_60  # Use IBM color
        self.shape = "square"     # Follow shape conventions
        self.icon = "new-service-icon.svg"  # IBM Design icon
```

---

## Documentation

Good documentation helps everyone use and contribute to IBM Diagrams.

### What to Document

- **New features**: Add usage examples and API documentation
- **Breaking changes**: Clearly document migration paths
- **Configuration options**: Explain all parameters and defaults
- **Common patterns**: Show best practices and examples

### Documentation Structure

```
docs/
├── setup.md              # Installation and setup
├── diagram-as-code.md    # Python API reference
├── terraform.md          # Terraform integration
├── testing.md            # Testing guide
└── examples/             # Example diagrams
    ├── python/           # Python examples
    ├── terraform/        # Terraform examples
    └── json/             # JSON examples
```

### Writing Documentation

**Be Clear and Concise:**
```markdown
# Good
Create a VPC with `VPC("name", "cidr")`.

# Less Good
You can create a VPC by instantiating the VPC class with a name parameter and a CIDR parameter.
```

**Include Examples:**
```markdown
## Creating a Virtual Server

```python
from ibmdiagrams.ibmcloud.compute import VirtualServer

# Basic usage
vsi = VirtualServer("Web Server")

# With IP address
vsi = VirtualServer("Web Server", "10.0.0.4")

# With additional details
vsi = VirtualServer(
    label="Web Server",
    sublabel="10.0.0.4<br>Ubuntu 22.04"
)
```
```

**Update CHANGELOG.md:**

When your PR is merged, ensure `CHANGELOG.md` is updated:

```markdown
## [Unreleased]

### Added
- Support for VirtualPrivateEndpoint resources (#123)
- New example diagram for VPE configuration

### Fixed
- Terraform parser handling of nested modules (#124)

### Changed
- Improved layout algorithm for complex VPCs
```

---

## Community and Support

### Getting Help

- **Documentation**: Check [docs/](docs/) first
- **Issues**: Search existing issues or create a new one
- **Discussions**: Use GitHub Discussions for questions
- **Slack**: Join our IBM internal Slack channel (link in repo)

### Asking Questions

When asking for help:

1. **Search first** - your question might already be answered
2. **Be specific** - provide context and details
3. **Include examples** - show what you've tried
4. **Be patient** - maintainers are volunteers

**Good Question:**
```markdown
I'm trying to create a diagram with multiple VPCs connected via Transit Gateway,
but the connectors aren't rendering correctly. Here's my code:

[code example]

Expected: Connectors between VPCs
Actual: No connectors visible

IBM Diagrams version: 3.1.10
Python version: 3.11.5
```

### Helping Others

Contributing isn't just about code! You can help by:

- Answering questions in issues and discussions
- Reviewing pull requests
- Improving documentation
- Creating tutorials and examples
- Sharing your diagrams and use cases

### Recognition

We value all contributions! Contributors are recognized in:

- `CHANGELOG.md` for significant contributions
- GitHub's contributor graph
- Release notes for major features

---

## Additional Resources

### Project Links

- **Repository**: [github.com/IBM/ibmdiagrams](https://github.com/IBM/ibmdiagrams)
- **Issues**: [Report bugs or request features](https://github.com/IBM/ibmdiagrams/issues)
- **Releases**: [Download latest version](https://github.com/IBM/ibmdiagrams/releases)

### External Resources

- **IBM Design Language**: [Technical Diagrams Guideline](https://www.ibm.com/design/language/infographics/technical-diagrams/design)
- **IBM Plex Fonts**: [Google Fonts](https://fonts.google.com/?query=Plex)
- **draw.io Desktop**: [Download](https://github.com/jgraph/drawio-desktop/releases)
- **Python Style Guide**: [PEP 8](https://pep8.org/)

### Learning Resources

- **Getting Started**: [GETTING_STARTED.md](GETTING_STARTED.md)
- **Examples**: [docs/examples/](docs/examples/)
- **Testing Guide**: [docs/testing.md](docs/testing.md)
- **API Reference**: [docs/diagram-as-code.md](docs/diagram-as-code.md)

---

## Thank You! 🙏

Thank you for taking the time to contribute to IBM Diagrams! Every contribution, no matter how small, makes a difference. We're grateful for your support and look forward to working with you.

**Questions?** Don't hesitate to ask! We're here to help.

**Ready to contribute?** Pick an issue labeled `good first issue` or `help wanted` and get started!

---

**Happy Contributing! 🚀**

*Last updated: 2026-05-07*
