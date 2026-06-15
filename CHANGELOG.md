# 📝 Change Log

All notable changes to ibmdiagrams are documented here.

---

## 🎉 [3.3.1] - 2026-06-12

### 🐛 Fixes

#### 🚨 Critical Runtime Errors Eliminated

- **Fixed NameError in connector validation** (`build.py`): Corrected undefined `style` variable to properly reference `linetype` parameter, preventing crashes during diagram generation with invalid connector styles
- **Fixed NameError in color validation** (`colors.py`): Corrected `validFamilyColor` to `checkFamilyColor()` method call, eliminating validation failures when checking fill colors
- **Fixed silent failure in direction handling** (`common.py`): Added missing return statement in `getDirection()` method, ensuring proper layout direction behavior
- **Fixed incorrect method call** (`common.py`): Corrected `setAnyProviderAny()` to `setProviderAny()` for proper provider configuration
- **Fixed incorrect method reference** (`options.py`): Corrected `getInputFolder()` to return `inputFolder` instead of `outputFile`
- **Removed duplicate dictionary key** (`icons.py`): Eliminated conflicting "fill" key in Enterprise Icon definition that caused unpredictable rendering

#### 🔧 Code Quality Improvements

- **Refactored color validation logic**: Added `_getColorName()` helper method for safer color lookups with proper error handling
- **Removed dead code**: Cleaned up unused label type methods and invalid provider warnings from `common.py`
- **Fixed dictionary construction** (`types.py`): Removed undefined "header" reference, now properly uses `CombinedStyle` constant
- **Improved code documentation**: Fixed comment formatting (changed `##` to `#`) and enhanced inline documentation

### 🔧 Infrastructure

#### ⚙️ CI/CD Pipeline

- **GitHub Actions workflow**: Added automated CI pipeline (`.github/workflows/ci.yml`) with linting, formatting, testing, and build verification steps
- **Modernized tox configuration**: Updated `tox.ini` to use ruff for linting/formatting and pytest for testing

#### 🧪 Testing

- **Regression test suite**: Added comprehensive `test_release_stabilization.py` covering all 6 bug fixes
- **Unit tests**: Added `test_options_common.py` for Options and Common wrapper behavior validation
- **MCP validation**: Tests verify diagram generation from both Python code and JSON inputs
- **Quality metrics**: All tests passing with zero linting errors and zero formatting issues

### 📚 Documentation

- **Issue templates**: Updated bug report and good first issue templates with Python/ibmdiagrams-specific environment fields
- **PR template**: Updated pull request template with relevant test configuration fields

### 📦 Breaking Changes

None - v3.3.1 maintains full backward compatibility with v3.3.0


---

## 🎉 [3.3.0] - 2026-05-19

### ✨ Features

#### 🤖 Model Context Protocol (MCP) Integration

- **MCP Server Implementation**: Added FastMCP-based server (`src/ibmdiagrams/ibmscripts/mcp.py`) enabling AI assistants to generate IBM Cloud architecture diagrams programmatically
- **AI Assistant Skill**: New `ibmdiagrams-builder` skill in `skills/` directory for seamless integration with AI coding assistants
- **Tool Exposure**: MCP server exposes diagram generation capabilities as tools that AI assistants can invoke directly

#### 🧪 Visual Regression Testing Framework

- **Automated Visual Testing**: Comprehensive PNG-based visual regression testing system (`tests/test_visual_regression.py`, `tests/test_complete_diagrams.py`)
- **Baseline Management**: 100+ PNG baselines in `tests/baselines/png/` covering all diagram elements
- **Cross-Platform Support**: Configurable threshold (1.25%) for handling rendering differences across operating systems
- **Image Comparison Utilities**: Custom comparison tools in `tests/utils/` for pixel-perfect diagram validation

#### 🔐 Code Quality Infrastructure

- **Pre-commit Hooks**: Automated code quality checks using ruff linting/formatting and detect-secrets security scanning
- **Security Scanning**: Integrated detect-secrets with baseline file (`.secrets.baseline`) to prevent credential leaks
- **Linting Configuration**: Ruff configuration in `pyproject.toml` enforcing 100-character line length and Python best practices
- **Development Workflow**: Standardized development process with automated checks before commits

#### 📐 Layout Enhancements

- **LayoutGroup Component**: New invisible container (`src/ibmdiagrams/ibmbase/elements.py`) for advanced diagram organization without visual boundaries
- **Height Equalization**: Automatic height balancing for sibling top-level groups ensuring consistent visual hierarchy
- **Multi-line Label Support**: Improved label rendering with proper height calculations for HTML-formatted two-line labels

#### 🤖 New AI/ML Components

- **watsonx Suite**: Complete watsonx family support (AI, Assistant, Code Assistant, Data, Governance, Orchestrate, Runtime, Studio, z Code Assistant)
- **Watson Services**: Watson Studio, Watson Discovery, Watson Machine Learning components
- **Custom Icons**: Support for custom icon URLs enabling organization-specific diagram elements

### 📚 Documentation

#### 📖 Comprehensive Documentation Overhaul

- **MCP Server Guide**: New `docs/mcp.md` and `docs/mcp-onboarding.md` with step-by-step AI assistant integration
- **Testing Documentation**: Detailed `docs/testing.md` covering visual regression testing, baseline management, and test execution
- **Example Reorganization**: Restructured `docs/examples/` with separate directories for Python, Terraform, and JSON examples
- **AGENTS.md Enhancement**: Updated with MCP server architecture, FastMCP implementation details, and AI integration patterns
- **GPG Signing Guide**: Comprehensive GPG commit signing setup in `CONTRIBUTING.md` for secure contributions

#### 🔑 Development Guidelines

- **Contribution Standards**: Enhanced `CONTRIBUTING.md` with GPG signing requirements, pre-commit hook setup, and code quality expectations
- **Testing Standards**: Clear guidelines for maintaining code coverage and updating visual regression baselines
- **Security Practices**: Documentation of detect-secrets usage and secret scanning workflow

### 🐛 Fixes

- **InstanceGroup Typo**: Corrected class name typo in super call preventing proper inheritance
- **Label Overlap**: Fixed overlapping labels in dense diagram layouts
- **Multi-line Layout**: Improved vertical positioning of two-line labels on group and zone shapes

### 🔧 Maintenance

- **Team Updates**: Updated CODEOWNERS and team contacts reflecting current maintainers
- **Dependency Management**: Consolidated dependencies in `requirements.txt`, `requirements-dev.txt`, and `pyproject.toml`
- **Build Configuration**: Standardized setuptools configuration with dependency groups

### 📦 Breaking Changes

None - v3.3.0 maintains backward compatibility with v3.2.x


---

## 🎉 [3.2.1]

### ✨ Features

- 🪝 Added pre-commit hooks and development tooling for code quality
- 🎨 Improved development workflow with ruff linting and formatting
- 🔐 Added detect-secrets for security scanning

### 🧪 Testing

- 📸 Added visual regression testing framework
- 🖼️ Added PNG baselines for visual regression testing
- ⚙️ Adjusted visual regression defaults for cross-platform compatibility
- 📊 Increased visual regression threshold to 1.25%

---

## 🎉 [3.2.0]

### ✨ Features

- 📦 Added LayoutGroup component for invisible layout containers
- 📏 Equalized heights of sibling top-level groups in diagram layout
- 🤖 Added new diagram components including watsonx and watson AI components
- 🎨 Added custom icon support
- 👥 Updated team contacts and maintainers

### 🐛 Fixes

- 📐 Improved multi-line label layout and height calculations
- ✏️ Corrected InstanceGroup class name typo in super call

### 🧪 Testing

- ✅ Added comprehensive test coverage for new components

---

## 🎉 [3.1.10]

### 🐛 Fixes

- 🔧 Fixed output parameter is null issue

---

## 🎉 [3.1.9]

### 🐛 Fixes

- 📁 Ensure directories are created for output parameter

---

## 🎉 [3.1.8]

### 🐛 Fixes

- 🔧 Fixed output parameter

---

## 🎉 [3.1.7]

### ✨ Features

- 🚀 Added support for OpenShift

---

## 🎉 [3.1.6]

### ✨ Features

- 🗑️ Removed icon for deprecated EnterpriseDB offering

---

## 🎉 [3.1.5]

### ✨ Features

- 🔌 Completed endpoint gateway implementation

---

## 🎉 [3.1.4]

### ✨ Features

- 🗑️ Removed icon for deprecated etcd offering

---

## 🎉 [3.1.3]

### ✨ Features

- 🔑 Added Key Protect and Cloud Logs services

---

## 🎉 [3.1.2]

### ✨ Features

- 🔗 Completed combining services

---

## 🎉 [3.1.1]

### ✨ Features

- 📦 Combined services to reduce space

### 🐛 Fixes

- 🏷️ Fixed overlapping labels, print error if input not found

---

## 🎉 [3.1.0]

### ✨ Features

- 🏗️ Initial move of internal JSON use case to new base design with VPC, Subnet, Virtual Server initially

---

## 🎉 [3.0.4]

### ✨ Features

- 🧹 Eliminated unnecessary start and done statements to prevent confusion

---

## 🎉 [3.0.3]

### ✨ Features

- 🌐 Enabled fontFamily for global IBM Plex languages

---

## 🎉 [3.0.2]

### ✨ Features

- 🌉 Added Transit Gateway, Endpoint Gateway, and Flow Log to Cloud/VPC Services

---

## 🎉 [3.0.1]

### ✨ Features

- ☁️ Added support for Cloud Services with Object Storage initially

---

## 🚀 [3.0.0]

### ✨ Features

- 🤖 Initial automation of Terraform resources

---

## 🚀 [2.0.0]

### ✨ Features

- 🎨 Completed move to drawio implementation

---

## 🎉 [1.0.30]

### ✨ Features

- ⚙️ Added general option in ibmdiagrams script for generalized Terraform output

---

## 🎉 [1.0.29]

### ✨ Features

- 🎨 Added initial changes for drawio implementation (not currently enabled)

### 🐛 Fixes

- 🔧 Fixed incorrect check resulting in missing VPC error for Terraform

---

## 🎉 [1.0.28]

### ✨ Features

- ✅ Added and verified all Terraform resources as of 10/19/24, subject to placement

---

## 🎉 [1.0.27]

### ✨ Features

- 🔗 Completed connectors implementation for solid, dashed, dotted, double, and tunnel

---

## 🎉 [1.0.26]

### ✨ Features

- 🔧 Base connectors parameter simplification

---

## 🎉 [1.0.25]

### ✨ Features

- 🔗 Base connectors implementation for solid, dashed, dotted, double, and tunnel

### 🐛 Fixes

- ✏️ (John Pape) Typos fixed in PublicNetwork and AccessGroup
- 🔧 Fixes in conjunction with base connectors implementation

---

## 🎉 [1.0.24]

### 🐛 Fixes

- 🎨 Fixed Power icon
- 📊 Updated diagram examples and collage with corrected label positions

---

## 🎉 [1.0.23]

### 🐛 Fixes

- 🔧 Fixed and redesigned static support
- 📐 (Internal issue #4) Fixed vertical label position on group shapes, zone shapes, and expanded shapes

---

## 🎉 [1.0.22]

### ✨ Features

- 📦 External preparation

---

## 🎉 [1.0.21]

### ✨ Features

- 📦 External preparation
- 🎨 Added hideicon externals

---

## 🎉 [1.0.20]

### ✨ Features

- 📦 External preparation

---

## 🎉 [1.0.19]

### ✨ Features

- 📦 External preparation

---

## 🎉 [1.0.18]

### ✨ Features

- 🎨 Added additional icons
- 🤖 Added additional Terraform resources

---

## 🎉 [1.0.17]

### ✨ Features

- 📦 External preparation

---

## 🎉 [1.0.16]

### ✨ Features

- ⚙️ Make input filename a required argument (no need to specify -input)

---

## 🎉 [1.0.15]

### ✨ Features

- 📄 Changed filetype to drawio

---

## 🎉 [1.0.14]

### ✨ Features

- 📚 Added benefits to README

---

## 🎉 [1.0.13]

### ✨ Features

- 🎨 Added catalog icons

---

## 🎉 [1.0.12]

### ✨ Features

- 🔄 Changed script from ibmdiagramscli to ibmdiagrams

---

## 🎉 [1.0.11]

### ✨ Features

- 🎨 Added additional icons

---

## 🎉 [1.0.10]

### ✨ Features

- 🤖 Added automation of Terraform resources

---

## 🎉 [1.0.9]

### ✨ Features

- ©️ Updated copyrights

---

## 🎉 [1.0.8]

### 🐛 Fixes

- 🔧 Fixed options for cli

---

## 🎉 [1.0.7]

### ✨ Features

- 📦 Changed import to ibmdiagrams

---

## 🎉 [1.0.6]

### ✨ Features

- 🤖 Added watsonx icons

---

## 🎉 [1.0.5]

### ✨ Features

- 🎨 Added additional icons

---

## 🎉 [1.0.4]

### 🐛 Fixes

- 🎨 Fixed fillcolor

---

## 🎉 [1.0.3]

### ✨ Features

- 🏗️ Created process for building wheel

---

## 🎉 [1.0.2]

### ✨ Features

- 🔄 Changed AZ from container group shape to non-container Zone shape

---

## 🎉 [1.0.1]

### ✨ Features

- 🎨 Added additional icons

---

## 🚀 [1.0.0]

### ✨ Features

- 🎊 Initial release

---

## 📖 Legend

- 🎉 Minor/Patch Release
- 🚀 Major Release
- ✨ New Features
- 🐛 Bug Fixes
- 🧪 Testing
- 📚 Documentation
- 🔧 Maintenance
- ⚙️ Configuration
- 🎨 UI/Design
- 🔐 Security
