# IBM Diagrams Examples

Comprehensive examples demonstrating all IBM Diagrams use cases and workflows.

---

## 📚 Quick Navigation

### By Use Case

| Use Case | Example | Description |
|----------|---------|-------------|
| **Python to DrawIO** | [Simple VPC](python/simple-vpc.md) | Create diagrams with Python code |
| **Terraform to DrawIO (Detailed)** | [Custom Labels](terraform/terraform-custom-labels.md) | Auto-generate with resource details |
| **Terraform to DrawIO (Simple)** | [General Labels](terraform/terraform-general-labels.md) | Auto-generate simplified diagrams |
| **Terraform to Python** | [Terraform to Python](terraform/terraform-to-python.md) | Convert for customization |
| **JSON to DrawIO** | [JSON Format](json/README.md) | Internal format (advanced) |

### By Complexity

| Level | Examples |
|-------|----------|
| **Beginner** | [Simple VPC](python/simple-vpc.md) |
| **Intermediate** | [Terraform Custom Labels](terraform/terraform-custom-labels.md), [Terraform General Labels](terraform/terraform-general-labels.md) |
| **Advanced** | [Terraform to Python](terraform/terraform-to-python.md), [SLZ VSI](python/slzvsi.md), [SLZ Power VS](python/slzpowervs.md) |
| **Expert** | [JSON Format](json/README.md) |

---

## 🎯 Use Case 1: Python (Diagram as Code) → DrawIO

**Perfect for:** Planning new architectures, creating documentation, presentations

### Examples

#### [XML String Output](python/xml-string-output.md)
Get Draw.io XML as a string without writing to files.

**What you'll learn:**
- Using `filename="*"` to prevent file writing
- Accessing diagram data with `_savediagrams`
- Converting diagrams to XML strings
- Use cases for API responses, databases, and streaming

**Run it:**
```bash
python docs/examples/python/xml-string-output.py
# Output: XML string (no file created)
```

#### [Simple VPC](python/simple-vpc.md)
Basic VPC with web and app tiers.

**What you'll learn:**
- Creating diagrams with Python
- Using context managers for hierarchy
- Adding subnets and virtual servers
- Configuring security groups

**Run it:**
```bash
python docs/examples/python/simple-vpc.py
# Output: simple-vpc.drawio
```

#### [SLZ VSI](python/slzvsi.md)
Enterprise landing zone with multi-zone deployment.

**What you'll learn:**
- Multi-zone architectures
- Resource groups and VPCs
- VPN and VPE configuration
- Cloud services integration

**Run it:**
```bash
python docs/examples/python/slzvsi.py
# Output: slzvsi.drawio
```

#### [SLZ Power VS](python/slzpowervs.md)
Power Virtual Server with VPC landing zone.

**What you'll learn:**
- Power Virtual Server integration
- Hybrid cloud architectures
- Direct Link connectivity
- Transit Gateway configuration

**Run it:**
```bash
python docs/examples/python/slzpowervs.py
# Output: slzpowervs.drawio
```

---

## 🔄 Use Case 2: Terraform → DrawIO (Custom Labels)

**Perfect for:** Documenting existing infrastructure, compliance audits, troubleshooting

### [Terraform Custom Labels Example](terraform/terraform-custom-labels.md)

Generate detailed diagrams showing:
- Resource names (e.g., "web-server-1")
- IP addresses (e.g., "10.10.10.4")
- CIDR blocks (e.g., "10.10.10.0/24")
- Resource metadata

**Run it:**
```bash
# Apply Terraform
terraform apply

# Export state
terraform show -json > production.tfstate

# Generate diagram
ibmdiagrams production.tfstate
# Output: production.drawio
```

**Best for:**
- ✅ Internal documentation
- ✅ Troubleshooting
- ✅ Compliance audits
- ✅ Team onboarding

---

## 📊 Use Case 3: Terraform → DrawIO (General Labels)

**Perfect for:** Presentations, public documentation, architecture proposals

### [Terraform General Labels Example](terraform/terraform-general-labels.md)

Generate simplified diagrams showing:
- Resource types only (e.g., "Virtual Server")
- No specific names or IPs
- Clean architecture overview

**Run it:**
```bash
# Export state
terraform show -json > production.tfstate

# Generate with general labels
ibmdiagrams --general production.tfstate
# Output: production.drawio
```

**Best for:**
- ✅ Executive presentations
- ✅ Public documentation
- ✅ Architecture proposals
- ✅ Training materials

---

## 🔀 Use Case 4: Terraform → Python

**Perfect for:** Creating templates, customizing diagrams, learning diagram-as-code

### [Terraform to Python Example](terraform/terraform-to-python.md)

Convert Terraform infrastructure to editable Python code.

**Run it:**
```bash
# Export state
terraform show -json > production.tfstate

# Generate Python code
ibmdiagrams --python production.tfstate
# Output: production.py

# Customize the code
vim production.py

# Generate diagram
python production.py
# Output: production.drawio
```

**Best for:**
- ✅ Creating reusable templates
- ✅ Customizing auto-generated diagrams
- ✅ Learning diagram-as-code
- ✅ Building on existing infrastructure

---

## 🔧 Use Case 5: JSON → DrawIO (Internal Format)

**Perfect for:** Advanced integrations, custom tooling (internal use only)

### [JSON Format Example](json/README.md)

⚠️ **Warning:** Internal format, not officially supported for external use.

**Run it:**
```bash
ibmdiagrams docs/examples/json/cloud.json
# Output: cloud.drawio
```

**Note:** Use Python API or Terraform integration instead for production use.

---

## 🎓 Learning Path

### 1. Start Here: Simple VPC

Begin with the [Simple VPC](python/simple-vpc.md) example to learn the basics:

```bash
# Copy the example
cp docs/examples/python/simple-vpc.py my-first-diagram.py

# Run it
python my-first-diagram.py

# Open in draw.io
open my-first-diagram.drawio
```

### 2. Explore Terraform Integration

Try generating diagrams from Terraform:

```bash
# If you have Terraform infrastructure
terraform show -json > infrastructure.tfstate
ibmdiagrams infrastructure.tfstate
```

### 3. Customize with Python

Convert Terraform to Python for customization:

```bash
# Generate Python code
ibmdiagrams --python infrastructure.tfstate

# Edit and run
vim infrastructure.py
python infrastructure.py
```

### 4. Study Complex Examples

Examine enterprise examples:
- [SLZ VSI](python/slzvsi.md) - Multi-zone VPC deployment
- [SLZ Power VS](python/slzpowervs.md) - Hybrid cloud architecture

---

## 💡 Tips & Tricks

### Quick Reference

```bash
# Python to DrawIO
python diagram.py

# Terraform to DrawIO (detailed)
ibmdiagrams infrastructure.tfstate

# Terraform to DrawIO (simplified)
ibmdiagrams --general infrastructure.tfstate

# Terraform to Python
ibmdiagrams --python infrastructure.tfstate

# Custom output directory
ibmdiagrams -output ./diagrams infrastructure.tfstate

# Custom font
ibmdiagrams -font "IBM Plex Sans JP" infrastructure.tfstate
```

### Common Patterns

#### Multi-Zone Deployment

```python
for zone_num in range(1, 4):
    with Zone(f"Zone {zone_num}", f"10.{zone_num}0.0.0/18"):
        with Subnet(f"Subnet {zone_num}", f"10.{zone_num}0.10.0/24"):
            VirtualServer(f"Server-{zone_num}")
```

#### Reusable Components

```python
def create_tier(name, cidr, server_count):
    with Subnet(f"{name} Subnet", cidr):
        for i in range(1, server_count + 1):
            VirtualServer(f"{name} Server {i}")

create_tier("Web", "10.10.10.0/24", 3)
create_tier("App", "10.10.20.0/24", 2)
```

#### Conditional Diagrams

```python
ENVIRONMENT = "production"

if ENVIRONMENT == "production":
    # Production: 3 zones
    zones = 3
else:
    # Development: 1 zone
    zones = 1

for z in range(1, zones + 1):
    with Zone(f"Zone {z}"):
        # ... resources
```

---

## 🔍 Finding the Right Example

### By Goal

| Goal | Example |
|------|---------|
| Learn the basics | [Simple VPC](python/simple-vpc.md) |
| Document Terraform infrastructure | [Terraform Custom Labels](terraform/terraform-custom-labels.md) |
| Create presentation diagrams | [Terraform General Labels](terraform/terraform-general-labels.md) |
| Customize auto-generated diagrams | [Terraform to Python](terraform/terraform-to-python.md) |
| Build enterprise architecture | [SLZ VSI](python/slzvsi.md) |
| Integrate Power VS | [SLZ Power VS](python/slzpowervs.md) |

### By Technology

| Technology | Examples |
|------------|----------|
| **VPC** | [Simple VPC](python/simple-vpc.md), [SLZ VSI](python/slzvsi.md) |
| **Power Virtual Server** | [SLZ Power VS](python/slzpowervs.md) |
| **Terraform** | [Custom Labels](terraform/terraform-custom-labels.md), [General Labels](terraform/terraform-general-labels.md), [To Python](terraform/terraform-to-python.md) |
| **Multi-Zone** | [SLZ VSI](python/slzvsi.md), [SLZ Power VS](python/slzpowervs.md) |
| **Security** | All examples include security groups |
| **Observability** | [SLZ VSI](python/slzvsi.md), [SLZ Power VS](python/slzpowervs.md) |

---

## 📖 Additional Resources

### Documentation

- [Getting Started Guide](../../GETTING_STARTED.md) - Complete setup and first steps
- [Setup Guide](../setup.md) - Installation instructions
- [Diagram as Code](../diagram-as-code.md) - Python API reference
- [Terraform Integration](../terraform.md) - Terraform guide

### External Resources

- [IBM Design Language](https://www.ibm.com/design/language/infographics/technical-diagrams/design) - Design standards
- [draw.io Documentation](https://www.drawio.com/doc/) - draw.io help
- [Terraform Documentation](https://www.terraform.io/docs) - Terraform reference

---

## 🤝 Contributing Examples

Have a great example to share? We'd love to include it!

### Example Template

```markdown
# Example Title

Brief description of what this example demonstrates.

## Overview

Detailed description of the architecture and use case.

## Code

[View Source](example.py)

```python
# Your example code here
```

## How to Run

Step-by-step instructions.

## What You'll Learn

- Key concept 1
- Key concept 2
- Key concept 3

## Related Examples

Links to related examples.
```

### Submission Process

1. Create your example following the template
2. Test it thoroughly
3. Add documentation
4. Submit a pull request
5. See [CONTRIBUTING.md](../../CONTRIBUTING.md) for details

---

## 🆘 Getting Help

### Common Issues

- **Fonts not rendering**: Install [IBM Plex Sans fonts](https://fonts.google.com/?query=Plex)
- **Command not found**: Use `uv run ibmdiagrams` or check PATH
- **Import errors**: Activate virtual environment or use `uv run python`

### Support Channels

- 📖 **Documentation**: Check the guides above
- 🐛 **Issues**: [GitHub Issues](https://github.com/IBM/ibmdiagrams/issues)
- 💬 **Slack**: IBM internal Slack channel
- 📧 **Email**: Contact maintainers

---

## 📊 Example Statistics

| Category | Count |
|----------|-------|
| **Total Examples** | 8 |
| **Python Examples** | 4 |
| **Terraform Examples** | 3 |
| **Advanced Examples** | 1 |
| **Beginner-Friendly** | 2 |

---

## 🎯 Next Steps

1. **Choose an example** that matches your use case
2. **Run the example** to see it in action
3. **Modify the code** to match your needs
4. **Create your own** diagrams
5. **Share your examples** with the community

---

**Happy Diagramming! 🎉**

If you find these examples helpful, please ⭐ star the repository!