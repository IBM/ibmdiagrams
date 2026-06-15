# Getting Started with IBM Diagrams

Welcome to IBM Diagrams! This guide will help you get up and running in minutes, whether you're creating diagrams from scratch or visualizing existing infrastructure.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Your First Diagram](#your-first-diagram)
4. [Common Workflows](#common-workflows)
5. [Next Steps](#next-steps)
6. [Getting Help](#getting-help)

---

## Prerequisites

### Required

- **Python 3.11+**: [Download Python](https://www.python.org/downloads/)
- **draw.io Desktop**: [Download draw.io](https://github.com/jgraph/drawio-desktop/releases) (to view/edit diagrams)

### Recommended

- **uv Package Manager**: 10-100x faster than pip ([Install uv](https://github.com/astral-sh/uv))
- **IBM Plex Sans Fonts**: For proper rendering ([Install fonts](https://fonts.google.com/?query=Plex))

---

## Installation

### Option 1: Using uv (Recommended)

**Why uv?** It's blazingly fast and handles virtual environments automatically.

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone or download the repository
git clone git@github.com:IBM/ibmdiagrams.git
cd ibmdiagrams

# Install dependencies (creates venv automatically)
uv sync

# Verify installation
uv run ibmdiagrams --help
```

### Option 2: Using pip

```bash
# Download the wheel from Releases
# https://github.com/IBM/ibmdiagrams/releases

# Install the package
pip install ibmdiagrams-X.Y.Z-py3-none-any.whl

# Verify installation
ibmdiagrams --help
```

### Install IBM Plex Sans Fonts

For proper diagram rendering in draw.io:

1. Visit [Google Fonts - IBM Plex](https://fonts.google.com/?query=Plex)
2. Select **IBM Plex Sans** → **Get font** → **Download all**
3. Unpack `IBM_Plex_Sans.zip`
4. **macOS**: Open Font Book → File → Add Fonts to Current User
5. **Windows**: Right-click fonts → Install
6. **Linux**: Copy to `~/.local/share/fonts/` and run `fc-cache -f -v`

---

## Your First Diagram

Let's create a simple VPC architecture in 3 steps:

### Step 1: Create a Python File

Create `my-first-diagram.py`:

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet
from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.network import PublicGateway

with Diagram("my-first-diagram"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC("Production VPC"):
                pgw = PublicGateway("Public Gateway")
                
                with Zone("Zone 1", "10.10.0.0/18"):
                    with Subnet("Web Subnet", "10.10.10.0/24"):
                        web = VirtualServer("Web Server", "10.10.10.4")
```

### Step 2: Run the Script

```bash
# Using uv
uv run python my-first-diagram.py

# Using pip
python my-first-diagram.py
```

### Step 3: Open in draw.io

```bash
# Output file: my-first-diagram.drawio
open my-first-diagram.drawio  # macOS
start my-first-diagram.drawio  # Windows
xdg-open my-first-diagram.drawio  # Linux
```

**🎉 Congratulations!** You've created your first IBM-standard architecture diagram!

---

## Common Workflows

### Workflow 1: Diagram as Code

**Use Case**: Planning new architectures, creating documentation

```python
# Create diagram.py
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC
from ibmdiagrams.ibmcloud.compute import VirtualServer

with Diagram("my-architecture"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC("My VPC"):
                vsi = VirtualServer("App Server")

# Run it
python diagram.py
# Output: my-architecture.drawio
```

**Benefits**:
- ✅ Version control your diagrams
- ✅ Quick iterations without manual positioning
- ✅ Reusable templates
- ✅ Consistent styling

[📚 Full Guide](docs/diagram-as-code.md)

---

### Workflow 2: Terraform to Diagram

**Use Case**: Documenting existing infrastructure

```bash
# Generate diagram from Terraform state
ibmdiagrams cloud.tfstate
# Output: cloud.drawio (with custom labels)

# Generate with general labels only
ibmdiagrams --general cloud.tfstate
# Output: cloud.drawio (with resource types)

# Specify output folder
ibmdiagrams -output ./diagrams cloud.tfstate

# Use custom font
ibmdiagrams -font "IBM Plex Sans JP" cloud.tfstate
```

**Benefits**:
- ✅ Instant infrastructure visualization
- ✅ Always up-to-date documentation
- ✅ Onboard new team members faster
- ✅ Compliance and audit reporting

[📚 Full Guide](docs/terraform.md)

---

### Workflow 3: Terraform to Python

**Use Case**: Converting infrastructure to editable code

```bash
# Generate Python code from Terraform state
ibmdiagrams --python docs/examples/terraform/cloud.tfstate
# Output: cloud.py (editable Python code)

# Edit the generated Python file
vim cloud.py

# Run it to create diagram
python cloud.py
# Output: cloud.drawio
```

**Benefits**:
- ✅ Start with existing infrastructure
- ✅ Customize and extend diagrams
- ✅ Create templates from real deployments
- ✅ Bridge Terraform and diagram-as-code

---

## Next Steps

### 1. Use with AI Assistants (Recommended)

For the easiest experience, install the **ibmdiagrams-builder AI skill** for your AI assistant:

**For IBM Bob:**
```bash
# Project-scoped (recommended for teams)
mkdir -p .bob/skills
cp -r skills/ibmdiagrams-builder .bob/skills/

# Or global (available in all projects)
mkdir -p ~/.bob/skills
cp -r skills/ibmdiagrams-builder ~/.bob/skills/
```

**For Claude Code:**
```bash
mkdir -p .claude/skills
cp -r skills/ibmdiagrams-builder .claude/skills/
```

**Benefits:**
- 🎯 Automatic activation when you ask about architecture diagrams
- 📚 Expert knowledge of all IBM Cloud components
- 🔧 Correct MCP tool usage built-in
- ✅ IBM Design Language compliance checks

**Example prompts:**
```
Generate a diagram from my Terraform state file at ./infrastructure.tfstate

Help me create a diagram for a 3-zone VPC with web and database tiers

Create a clean architecture diagram without IP addresses for a presentation
```

See the [AI Skill README](skills/ibmdiagrams-builder/README.md) for installation on other AI assistants (Cursor, Windsurf, Copilot, Cline, Continue.dev, Aider).

---

### 2. Explore Examples

Check out comprehensive examples in [`docs/examples/`](docs/examples/):

- **[simple-vpc.py](docs/examples/python/simple-vpc.md)**: Basic VPC with virtual servers
- **[slzvsi.py](docs/examples/python/slzvsi.md)**: Enterprise landing zone with multi-zone deployment
- **[Terraform examples](docs/examples/terraform/slzvsi.md)**: Terraform state file examples

### 3. Learn the API

Explore available components:

```python
# Groups (containers)
from ibmdiagrams.ibmcloud.groups import (
    IBMCloud, Region, VPC, Zone, Subnet,
    SecurityGroup, ResourceGroup, CloudServices
)

# Compute resources
from ibmdiagrams.ibmcloud.compute import (
    VirtualServer, PowerVirtualServer, BareMetalServer
)

# Network components
from ibmdiagrams.ibmcloud.network import (
    LoadBalancer, PublicGateway, VPNGateway,
    EndpointGateway, TransitGateway
)

# Security services
from ibmdiagrams.ibmcloud.security import (
    KeyProtect, SecretsManager, SecurityGroup
)

# Storage services
from ibmdiagrams.ibmcloud.storage import (
    ObjectStorage, BlockStorage
)

# Observability
from ibmdiagrams.ibmcloud.observability import (
    CloudLogs, FlowLogs, Monitoring
)
```

[📚 Full API Reference](docs/diagram-as-code.md)

### 3. Customize Your Diagrams

```python
# Use direction parameter for layout
with VPC("My VPC", direction="TB"):  # Top to Bottom
    pass

with VPC("My VPC", direction="LR"):  # Left to Right (default)
    pass

# Add sublabels for additional info
vsi = VirtualServer(
    label="Web Server",
    sublabel="10.10.10.4<br>Ubuntu 22.04"
)

# Use custom fonts (for global variants)
with Diagram("my-diagram", font="IBM Plex Sans JP"):
    pass
```

### 4. Integrate with CI/CD

```yaml
# .github/workflows/diagrams.yml
name: Generate Diagrams

on:
  push:
    paths:
      - '**.tf'
      - '**.tfstate'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install ibmdiagrams-*.whl
      - run: ibmdiagrams terraform.tfstate
      - uses: actions/upload-artifact@v3
        with:
          name: diagrams
          path: '*.drawio'
```

---

## Getting Help

### Documentation

- 📖 [Setup Guide](docs/setup.md) - Detailed installation instructions
- 📝 [Diagram as Code](docs/diagram-as-code.md) - Python API reference
- 🔄 [Terraform Guide](docs/terraform.md) - Terraform integration
- 🧪 [Testing Guide](docs/testing.md) - Visual regression testing

### Community

- 💬 **Slack**: Join our IBM internal Slack channel (link in repo)
- 🐛 **Issues**: [Report bugs or request features](https://github.com/IBM/ibmdiagrams/issues)
- 🤝 **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

### Common Issues

<details>
<summary><b>Fonts not rendering correctly</b></summary>

**Solution**: Install IBM Plex Sans fonts from [Google Fonts](https://fonts.google.com/?query=Plex) and restart draw.io desktop.

</details>

<details>
<summary><b>Command not found: ibmdiagrams</b></summary>

**Solution**: 
- Using uv: Run `uv run ibmdiagrams` instead
- Using pip: Ensure Python's bin directory is in your PATH

</details>

<details>
<summary><b>Import errors when running Python scripts</b></summary>

**Solution**:
- Using uv: Run `uv run python script.py`
- Using pip: Activate your virtual environment first

</details>

---

## Quick Reference

### Command Cheat Sheet

```bash
# Diagram as Code
python my-diagram.py                    # Create diagram from Python

# Terraform
ibmdiagrams cloud.tfstate              # Custom labels
ibmdiagrams --general cloud.tfstate    # General labels
ibmdiagrams --python cloud.tfstate     # Generate Python code
ibmdiagrams -output ./out cloud.tfstate # Custom output folder

# Help
ibmdiagrams --help                     # Show all options
```

### Python Template

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet
from ibmdiagrams.ibmcloud.compute import VirtualServer

with Diagram("diagram-name"):
    with IBMCloud("IBM Cloud"):
        with Region("Region Name"):
            with VPC("VPC Name"):
                with Zone("Zone Name", "CIDR"):
                    with Subnet("Subnet Name", "CIDR"):
                        resource = VirtualServer("Name", "IP")
```

---

## What's Next?

Now that you're set up, explore these resources:

1. 📚 **[Examples](docs/examples/)** - Learn from real-world diagrams
2. 🎨 **[Design Standards](https://www.ibm.com/design/language/infographics/technical-diagrams/design)** - Understand IBM diagram guidelines
3. 🤝 **[Contributing](CONTRIBUTING.md)** - Help improve IBM Diagrams
4. 🔧 **[Development Setup](CONTRIBUTING.md#development-setup)** - Set up for development

---

**Happy Diagramming! 🎉**

If you find IBM Diagrams useful, please ⭐ star the repository!
