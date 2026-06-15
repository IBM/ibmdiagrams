# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Project Overview

**ibmdiagrams** is a Python package (v3.3.0+) that generates architecture diagrams following the [IBM Diagram Standard](https://www.ibm.com/design/language/infographics/technical-diagrams/design). It enables infrastructure visualization through multiple input methods:

1. **Diagram as Code**: Write Python code using the ibmdiagrams API to programmatically create diagrams
2. **Terraform State Files**: Automatically generate diagrams from `.tfstate` files
3. **JSON Input**: Generate diagrams from internal JSON format (not externally available)

All diagrams are output as `.drawio` files that can be opened in draw.io desktop application.

### Core Technologies

- **Language**: Python 3.11+
- **Key Dependencies**: pandas, PyYAML, requests, tabulate, urllib3
- **Dev Dependencies**: pytest, pytest-cov, pytest-xdist, ruff, pre-commit, detect-secrets, Pillow, defusedxml
- **Output Format**: DrawIO XML format
- **Design Standard**: IBM Design Language (IBM Color Palette, IBM Plex Sans fonts)

### Architecture

The codebase is organized into four main modules under `src/ibmdiagrams/`:

1. **`ibmbase/`**: Core functionality for diagram generation
   - `build.py`: Diagram construction logic
   - `compose.py`: Composition and layout engine
   - `load.py`: Input file parsing (Terraform, JSON)
   - `elements.py`, `shapes.py`: Shape and element definitions
   - `colors.py`, `properties.py`: IBM design standard implementation
   - `icons.py`, `resources.py`: Icon and resource management
   - `common.py`, `constants.py`, `messages.py`, `options.py`, `types.py`: Utilities and shared code

2. **`ibmcloud/`**: IBM Cloud-specific diagram components
   - `diagram.py`: Main Diagram class (entry point for Python API)
   - `groups.py`: Container elements (IBMCloud, Region, VPC, Zone, Subnet, SecurityGroup, etc.)
   - `compute.py`: Compute services (VirtualServer, BareMetalServer, DedicatedHost, etc.)
   - `network.py`: Network services (LoadBalancer, PublicGateway, FloatingIP, TransitGateway, etc.)
   - `storage.py`: Storage services (BlockStorage, ObjectStorage, FileStorage, etc.)
   - `security.py`: Security services (VPNGateway, BastionHost, AppID, etc.)
   - `observability.py`: Monitoring and logging services
   - `ai.py`: AI/ML services (watsonx, Watson Studio, Watson Discovery, etc.)
   - `data.py`: Database services (Db2, Cloudant, PostgreSQL, MySQL, Redis, etc.)
   - `devops.py`: DevOps services (CI/CD, Toolchain, GitLab, Ansible, etc.)
   - `containers.py`: Container services (OpenShift, CodeEngine, Kubernetes, etc.)
   - `applications.py`: Application-level components
   - `actors.py`: User roles and external entities
   - `connectors.py`: Connection elements
   - `colors.py`: IBM Cloud-specific color definitions

3. **`ibmshapes/`**: Alternative shape library
   - `diagram.py`: Shape-based diagram API
   - `collapsed.py`, `expanded.py`, `grouping.py`: Shape variants
   - `connectors.py`: Connection elements
   - `colors.py`: Shape-specific color definitions

4. **`ibmscripts/`**: Command-line interface and MCP server
   - `ibmdiagrams.py`: CLI entry point (installed as `ibmdiagrams` command)
   - `mcp.py`: Model Context Protocol (MCP) server implementation using FastMCP

## Building and Running

### Installation

```bash
# Using uv (recommended - 10-100x faster)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

# Or install from wheel (download from Releases)
pip install ibmdiagrams-x.y.z-py3-none-any.whl

# Install IBM Plex Sans fonts from https://fonts.google.com/?query=Plex
# Required for proper rendering in draw.io desktop
```

### Development Setup

```bash
# Clone repository
git clone <repository-url>
cd ibmdiagrams

# Install dependencies with uv (recommended)
uv sync

# Or with pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .

# Install pre-commit hooks
pre-commit install

# The package uses setuptools build backend
# Build configuration in pyproject.toml
```

### Usage Patterns

**1. Diagram as Code (Python)**
```bash
# Create a Python file using ibmdiagrams API
python your_diagram.py
# Output: your_diagram.drawio
```

**2. Terraform State File**
```bash
# Generate with custom labels (default)
ibmdiagrams cloud.tfstate

# Generate with general labels
ibmdiagrams --general cloud.tfstate

# Generate Python code instead of drawio
ibmdiagrams --python cloud.tfstate

# Specify output folder
ibmdiagrams -output ./diagrams cloud.tfstate

# Specify custom font
ibmdiagrams -font "IBM Plex Sans JP" cloud.tfstate
```

**3. JSON Input**
```bash
ibmdiagrams cloud.json
```

### Testing

The project emphasizes maintaining code coverage and visual regression testing.

```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=src/ibmdiagrams --cov-report=html

# Run visual regression tests
pytest tests/test_visual_regression.py -v
pytest tests/test_complete_diagrams.py -v

# Update visual regression baselines (after intentional changes)
pytest tests/test_visual_regression.py --update-baselines
pytest tests/test_complete_diagrams.py --update-baselines

# Run tests in parallel (faster)
pytest tests/ -n auto

# Run pre-commit hooks
pre-commit run --all-files
```

See [`docs/testing.md`](docs/testing.md) for comprehensive testing documentation.

## Development Conventions

### Code Organization

- **Module Structure**: Follow the existing four-module pattern (ibmbase, ibmcloud, ibmshapes, ibmscripts)
- **Source Location**: All source code is in `src/ibmdiagrams/` (not root level)
- **Naming**: Use descriptive names following Python conventions (snake_case for functions/variables, PascalCase for classes)
- **Imports**: Relative imports within modules, absolute imports from other modules
- **Type Hints**: Encouraged for public APIs

### Diagram API Patterns

**Context Manager Pattern**: All diagram components use Python's `with` statement for hierarchical structure:

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet
from ibmdiagrams.ibmcloud.compute import VirtualServer

with Diagram("my-diagram"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas", direction="TB"):
            with VPC("Management VPC"):
                with Zone("Zone 1", "10.24.0.0/18"):
                    with Subnet("VSI Subnet", "10.10.40.0/24"):
                        vsi = VirtualServer("Management VSI", "10.10.40.4")
```

### IBM Design Standards

- **Colors**: Use colors defined in `colors.py` following IBM Color Palette
- **Fonts**: Default to IBM Plex Sans (configurable for global variants: Arabic, Devanagari, Hebrew, JP, KR, Thai)
- **Labels**: Support two-line labels with SemiBold primary and regular sublabel using HTML: `<b style='font-weight:600'>label</b><br>sublabel`
- **Shapes**: 
  - Groups (container=1): Represent "deployedOn" relationships
  - Zones (container=0): Represent "deployedTo" relationships
  - Nodes (square): Standalone components
  - Actors (round): User roles and external entities

### Code Style

- **Linter**: Ruff (configured in `pyproject.toml`)
- **Line Length**: 100 characters
- **Indentation**: 4 spaces
- **Quotes**: Double quotes for strings
- **Pre-commit Hooks**: Ruff formatting/linting + detect-secrets
- **Security**: Secrets detection via detect-secrets with baseline file

### Contributing Guidelines

1. **Branch Strategy**: Always branch from `main`, never merge directly to `main`
2. **Pull Requests**: 
   - Require at least 2 reviews
   - Must reference corresponding issue
   - Maintain code coverage
   - Explain unexpected changes in PR description
   - Pre-commit hooks must pass
3. **Issue Format**:
   - Bugs: `[VERSION][BUG] <title>` with `bug` label
   - Features: `[VERSION] <feature name>` with `enhancement` label
   - Vulnerabilities: Use `vulnerability` label for urgent security issues
4. **Code Quality**: 
   - Maintain existing code coverage levels before merging
   - Run visual regression tests for UI changes
   - Update baselines with clear explanations

### File Conventions

- **License Headers**: All source files include Apache 2.0 license header
- **Documentation**: Keep `docs/` folder updated with examples and guides
- **Examples**: Place example diagrams in `docs/examples/` with `.py`, `.md`, and `.svg` files
- **Tests**: Place tests in `tests/` directory
- **Baselines**: Visual regression baselines in `tests/baselines/png/`

### Known Limitations

1. **Group Spanning**: Diagram-as-code cannot represent groups spanning other groups (e.g., same security group across multiple subnets must be coded as separate groups)
2. **Connectors**: Currently direct point-to-point; layout improvements planned
3. **Alpha Stage**: External APIs subject to change (v3.x is alpha/early release)

## Key Design Decisions

- **DrawIO Output**: Generates XML format compatible with draw.io desktop for manual editing
- **IBM Standards**: Strict adherence to IBM Design Language for enterprise consistency
- **Terraform Integration**: Parses `.tfstate` files to auto-generate infrastructure diagrams
- **Font Flexibility**: Supports IBM Plex Sans global variants (Arabic, Devanagari, Hebrew, JP, KR, Thai)
- **Label Flexibility**: HTML-based labels support multi-line text with formatting
- **Modular Architecture**: Separate modules for base functionality, cloud services, shapes, and CLI
- **Visual Regression Testing**: PNG-based comparison to ensure rendering consistency

## Service Categories

The `ibmcloud` module organizes services into logical categories:

- **Compute**: Virtual servers, bare metal, dedicated hosts,  image services
- **Network**: Load balancers, gateways, VPNs, DNS, floating IPs, transit gateways
- **Storage**: Block storage, object storage, file storage, cloud backup
- **Security**: VPN gateways, bastion hosts, App ID, security groups, SSH keys
- **Observability**: Monitoring, flow logs, logging services
- **AI/ML**: watsonx suite, Watson Studio, Watson Discovery, Watson Machine Learning
- **Data**: Databases (Db2, Cloudant, PostgreSQL, MySQL, Redis, Elasticsearch, etc.)
- **DevOps**: CI/CD pipelines, toolchains, source repositories, GitLab, Ansible, MQ
- **Containers**: OpenShift, Code Engine, Kubernetes services, z/OS containers
- **Applications**: User directories, application components
- **Groups**: Organizational containers (VPC, regions, zones, subnets, resource groups, etc.)
- **Actors**: Users, enterprises, microservices, web applications
- **Connectors**: Relationships and connections between components

## Quick Reference

- **Main Entry Point (Python API)**: `ibmdiagrams.ibmcloud.diagram.Diagram`
- **CLI Command**: `ibmdiagrams` (installed via setuptools entry point)
- **Configuration**: `pyproject.toml` (setuptools-based build with dependency groups)
- **Dependencies**: Listed in `requirements.txt`, `requirements-dev.txt`, and `pyproject.toml`
- **Examples**: See `docs/examples/slzvsi.py` for comprehensive usage
- **Documentation**: `docs/setup.md`, `docs/diagram-as-code.md`, `docs/terraform.md`, `docs/testing.md`
- **Testing**: Visual regression tests in `tests/test_visual_regression.py` and `tests/test_complete_diagrams.py`
- **Build System**: Uses setuptools with `pyproject.toml` configuration
- **Code Quality**: Ruff linting, pre-commit hooks, pytest with coverage, detect-secrets

## Development Tools

- **Package Manager**: uv (recommended) or pip
- **Linting/Formatting**: Ruff (replaces black, isort, flake8)
- **Testing**: pytest with pytest-cov, pytest-xdist for parallel execution
- **Security**: detect-secrets for credential scanning
- **Pre-commit**: Automated code quality checks
- **Visual Testing**: Custom PNG comparison for diagram rendering
- **Build**: setuptools with pyproject.toml configuration
- **Dependencies**: Managed via dependency groups in pyproject.toml
