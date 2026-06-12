# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Project Overview

**ibmdiagrams** is a Python package (v3.1.10) that generates architecture diagrams following the [IBM Diagram Standard](https://www.ibm.com/design/language/infographics/technical-diagrams/design). It enables infrastructure visualization through multiple input methods:

1. **Diagram as Code**: Write Python code using the ibmdiagrams API to programmatically create diagrams
2. **Terraform State Files**: Automatically generate diagrams from `.tfstate` files
3. **JSON Input**: Generate diagrams from internal JSON format (not externally available)

All diagrams are output as `.drawio` files that can be opened in draw.io desktop application.

### Core Technologies

- **Language**: Python 3.11+
- **Key Dependencies**: pandas, PyYAML, requests, tabulate, urllib3
- **Output Format**: DrawIO XML format
- **Design Standard**: IBM Design Language (IBM Color Palette, IBM Plex Sans fonts)

### Architecture

The codebase is organized into four main modules:

1. **`ibmbase/`**: Core functionality for diagram generation
   - `build.py`: Diagram construction logic
   - `compose.py`: Composition and layout engine
   - `load.py`: Input file parsing (Terraform, JSON)
   - `elements.py`, `shapes.py`: Shape and element definitions
   - `colors.py`, `properties.py`: IBM design standard implementation
   - `icons.py`, `resources.py`: Icon and resource management

2. **`ibmcloud/`**: IBM Cloud-specific diagram components
   - `diagram.py`: Main Diagram class (entry point for Python API)
   - `groups.py`: Container elements (IBMCloud, Region, VPC, Zone, Subnet, SecurityGroup, etc.)
   - `compute.py`, `network.py`, `storage.py`, `security.py`, `observability.py`: Service-specific components
   - `actors.py`, `connectors.py`: Supporting elements

3. **`ibmshapes/`**: Alternative shape library
   - `diagram.py`: Shape-based diagram API
   - `collapsed.py`, `expanded.py`, `grouping.py`: Shape variants
   - `connectors.py`: Connection elements

4. **`ibmscripts/`**: Command-line interface
   - `ibmdiagrams.py`: CLI entry point (installed as `ibmdiagrams` command)

## Building and Running

### Installation

```bash
# Install from wheel (download from Releases)
pip install ibmdiagrams-x.y.z-py3-none-any.whl

# Install IBM Plex Sans fonts from https://fonts.google.com/?query=Plex
# Required for proper rendering in draw.io desktop
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

### Development Setup

```bash
# Clone repository
git clone <repository-url>
cd ibmdiagrams

# Install dependencies
pip install -r requirements.txt

# The package uses setuptools build backend
# Build configuration in pyproject.toml
```

### Testing

The project emphasizes maintaining code coverage. Run tests before submitting pull requests (specific test commands not documented in reviewed files).

## Development Conventions

### Code Organization

- **Module Structure**: Follow the existing four-module pattern (ibmbase, ibmcloud, ibmshapes, ibmscripts)
- **Naming**: Use descriptive names following Python conventions (snake_case for functions/variables, PascalCase for classes)
- **Imports**: Relative imports within modules, absolute imports from other modules

### Diagram API Patterns

**Context Manager Pattern**: All diagram components use Python's `with` statement for hierarchical structure:

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet

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
- **Fonts**: Default to IBM Plex Sans (configurable for global variants)
- **Labels**: Support two-line labels with SemiBold primary and regular sublabel using HTML: `<b style='font-weight:600'>label</b><br>sublabel`
- **Shapes**: 
  - Groups (container=1): Represent "deployedOn" relationships
  - Zones (container=0): Represent "deployedTo" relationships
  - Nodes (square): Standalone components
  - Actors (round): User roles and external entities

### Contributing Guidelines

1. **Branch Strategy**: Always branch from `main`, never merge directly to `main`
2. **Pull Requests**: 
   - Require at least 2 reviews
   - Must reference corresponding issue
   - Maintain code coverage
   - Explain unexpected changes in PR description
3. **Issue Format**:
   - Bugs: `[VERSION][BUG] <title>` with `bug` label
   - Features: `[VERSION] <feature name>` with `enhancement` label
   - Vulnerabilities: Use `vulnerability` label for urgent security issues
4. **Code Quality**: Maintain existing code coverage levels before merging

### File Conventions

- **License Headers**: All source files include Apache 2.0 license header
- **Documentation**: Keep docs/ folder updated with examples and guides
- **Examples**: Place example diagrams in `docs/examples/` with .py, .md, and .png files

### Known Limitations

1. **Group Spanning**: Diagram-as-code cannot represent groups spanning other groups (e.g., same security group across multiple subnets must be coded as separate groups)
2. **Connectors**: Currently direct point-to-point; layout improvements planned
3. **Early Release**: External APIs subject to change (v3.x is alpha stage)

## Key Design Decisions

- **DrawIO Output**: Generates XML format compatible with draw.io desktop for manual editing
- **IBM Standards**: Strict adherence to IBM Design Language for enterprise consistency
- **Terraform Integration**: Parses `.tfstate` files to auto-generate infrastructure diagrams
- **Font Flexibility**: Supports IBM Plex Sans global variants (Arabic, Devanagari, Hebrew, JP, KR, Thai)
- **Label Flexibility**: HTML-based labels support multi-line text with formatting

## Quick Reference

- **Main Entry Point (Python API)**: `ibmdiagrams.ibmcloud.diagram.Diagram`
- **CLI Command**: `ibmdiagrams` (installed via setuptools entry point)
- **Configuration**: `pyproject.toml` (setuptools-based build)
- **Dependencies**: Listed in `requirements.txt` and `pyproject.toml`
- **Examples**: See `docs/examples/slzvsi.py` for comprehensive usage
- **Documentation**: `docs/setup.md`, `docs/diagram-as-code.md`, `docs/terraform.md`
