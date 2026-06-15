![IBM Diagrams](docs/images/ibmdiagrams.drawio.svg)

# IBM Diagrams

**Transform your infrastructure into beautiful, standards-compliant architecture diagrams.**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

---

## 🎯 What is IBM Diagrams?

IBM Diagrams is a powerful Python package that generates professional architecture diagrams following the [IBM Design Language - Technical Diagrams Guideline](https://www.ibm.com/design/language/infographics/technical-diagrams/design). Whether you're documenting existing infrastructure, planning new deployments, or maintaining architecture documentation, IBM Diagrams makes it effortless.

### ✨ Key Features

- **📝 Diagram as Code**: Write Python code to create diagrams programmatically
- **🔄 Terraform Integration**: Auto-generate diagrams from `.tfstate` files
- **🎨 IBM Design Standards**: Automatic compliance with IBM Color Palette and IBM Plex fonts
- **📤 DrawIO Output**: Edit and customize diagrams in draw.io desktop
- **⚡ Fast & Flexible**: Multiple input methods for different workflows

---

## 🚀 Quick Start

### Installation

```bash
# Using uv (recommended - 10-100x faster)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

# Or using pip
pip install ibmdiagrams-x.y.z-py3-none-any.whl
# If already installed, upgrade it with:
pip install --force-reinstall ibmdiagrams-x.y.z-py3-none-any.whl

# To install the latest CLI globally on your machine, use uv tool install or pip install against the rebuilt wheel.
uv tool install ibmdiagrams-x.y.z-py3-none-any.whl
# If already installed, upgrade it with:
uv tool install --upgrade ibmdiagrams-x.y.z-py3-none-any.whl
```

### Your First Diagram (30 seconds)

```python
from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import VPC, IBMCloud, Region, Subnet, Zone

with Diagram("my-first-diagram"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC("Production VPC"):
                with Zone("Zone 1", "10.10.0.0/18"):
                    with Subnet("App Subnet", "10.10.10.0/24"):
                        vsi = VirtualServer("Web Server", "10.10.10.4")
```

**Run it:**
```bash
python my-first-diagram.py
# Output: my-first-diagram.drawio
```

**Open in draw.io desktop** and see your architecture come to life! 🎉

---

## 💡 Use Cases

IBM Diagrams supports four powerful workflows:

### 1️⃣ Python (Diagram as Code) → DrawIO

**Perfect for:** Planning new architectures, documentation, presentations

```bash
python docs/examples/python/cloud.py
# Output: cloud.drawio
```

**Benefits:**
- Version control your diagrams
- Quickly iterate on designs
- Reusable templates
- No manual positioning

[📖 See Examples](#-examples) | [📚 Full Guide](docs/diagram-as-code.md)

---

### 2️⃣ Terraform State → DrawIO

**Perfect for:** Documenting existing infrastructure, compliance audits

```bash
# With custom labels (resource names, IPs, etc.)
ibmdiagrams docs/examples/terraform/cloud.tfstate
# Output: cloud.drawio

# With general labels (resource types only)
ibmdiagrams --general docs/examples/terraform/cloud.tfstate
# Output: cloud.drawio
```

**Benefits:**
- Instant infrastructure visualization
- Always up-to-date documentation
- Onboard new team members faster
- Audit and compliance reporting

[📖 See Examples](#-examples) | [📚 Full Guide](docs/terraform.md)

---

### 3️⃣ Terraform State → Python Code

**Perfect for:** Converting existing infrastructure to diagram-as-code

```bash
ibmdiagrams --python docs/examples/terraform/cloud.tfstate
# Output: cloud.py (editable Python code)
```

**Benefits:**
- Start with existing infrastructure
- Customize and extend diagrams
- Create templates from real deployments
- Bridge Terraform and diagram-as-code workflows

[📖 See Examples](#-examples)

---

### 4️⃣ JSON → DrawIO (Internal Format)

**Perfect for:** Advanced integrations, custom tooling

```bash
ibmdiagrams docs/examples/json/cloud.json
# Output: cloud.drawio
```

> **Note:** JSON format is for internal use and not externally documented.

---

## 📚 Examples

### Simple VPC with Virtual Server

<details>
<summary><b>Click to expand code</b></summary>

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet
from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.network import PublicGateway
from ibmdiagrams.ibmcloud.security import SecurityGroup

with Diagram("simple-vpc"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas", direction="TB"):
            with VPC("My VPC"):
                pgw = PublicGateway("Public Gateway")
                
                with Zone("Zone 1", "10.10.0.0/18"):
                    with Subnet("Web Subnet", "10.10.10.0/24"):
                        web = VirtualServer("Web Server", "10.10.10.4")
                    
                    with Subnet("App Subnet", "10.10.20.0/24"):
                        app = VirtualServer("App Server", "10.10.20.4")
```

</details>

[🔗 More Examples](docs/examples/)

---

### Enterprise Landing Zone

See our comprehensive [VSI on VPC Landing Zone](docs/examples/python/slzvsi.md) example featuring:
- Multi-zone deployment
- VPN and VPE configuration
- Cloud services integration
- Security and observability

![SLZ VSI Example](docs/examples/python/slzvsi.drawio.svg)

---

## 🎨 Design Standards

IBM Diagrams automatically applies IBM Design Language standards:

| Feature | Implementation |
|---------|---------------|
| **Colors** | IBM Color Palette (Cyan, Teal, Purple, Magenta) |
| **Fonts** | IBM Plex Sans (with global variants support) |
| **Labels** | Two-line labels with SemiBold primary + regular sublabel |
| **Shapes** | Groups (containers), Zones, Nodes (square), Actors (round) |
| **Layout** | Automatic Z-order and positioning |

### Shape Types

- **Groups** (container=1): Represent "deployedOn" relationships (e.g., VSI on subnet)
- **Zones** (container=0): Represent "deployedTo" relationships (e.g., VSI to security group)
- **Nodes** (square): Standalone components or devices
- **Actors** (round): Users, roles, and external entities

---

## 📖 Documentation

| Guide | Description |
|-------|-------------|
| [🚀 Getting Started](GETTING_STARTED.md) | Complete setup and first steps |
| [⚙️ Setup](docs/setup.md) | Installation with uv or pip |
| [📝 Diagram as Code](docs/diagram-as-code.md) | Python API reference and examples |
| [🔄 Terraform](docs/terraform.md) | Terraform state file integration |
| [🤖 MCP Integration](docs/mcp.md) | Model Context Protocol server for AI assistants |
| [🎯 MCP Onboarding](docs/mcp-onboarding.md) | Step-by-step setup for IBM Bob and Claude Desktop |
| [🤖 AI Skill](skills/ibmdiagrams-builder/README.md) | Portable AI skill for IBM Bob, Claude Code, and other AI assistants |
| [🧪 Testing](docs/testing.md) | Visual regression testing guide |

---

## 🛠️ Development

### Pre-commit Hooks

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### Visual Regression Testing

```bash
# Install draw.io desktop first
pip install -r requirements-dev.txt

# Run tests
pytest tests/test_visual_regression.py

# Update baselines after intentional changes
pytest tests/test_visual_regression.py --update-baselines
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed development guidelines.

---

## 🎯 Why IBM Diagrams?

### For DevOps Teams
- **Automate documentation** from Terraform state
- **Version control** your architecture diagrams
- **Reduce manual work** with auto-generated layouts

### For Architects
- **Validate designs** before implementation
- **Communicate clearly** with IBM-standard visuals
- **Iterate quickly** without repositioning elements

### For Compliance Teams
- **Audit infrastructure** with up-to-date diagrams
- **Document changes** automatically
- **Meet standards** with IBM Design Language compliance

---

## ⚠️ Known Limitations

1. **Group Spanning**: Diagram-as-code cannot represent groups spanning other groups (e.g., same security group across multiple subnets must be coded separately)
2. **Connectors**: Currently direct point-to-point; layout improvements planned

---

## 🤝 Contributing

We welcome contributions! Please see:
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Community standards
- [SECURITY.md](SECURITY.md) - Security policy

---

## 📄 License

This project is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

---

## 🌟 Star Us!

If IBM Diagrams helps you, please ⭐ star this repository to show your support!
