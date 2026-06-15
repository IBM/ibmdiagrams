# Terraform Integration

Automatically generate IBM-standard architecture diagrams from your Terraform state files. Perfect for documenting existing infrastructure, compliance audits, and onboarding new team members.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Command Options](#command-options)
4. [Label Modes](#label-modes)
5. [Output Formats](#output-formats)
6. [Examples](#examples)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

---

## Overview

### Why Use Terraform Integration?

**Manual Documentation:**
- ❌ Time-consuming to create
- ❌ Quickly becomes outdated
- ❌ Inconsistent across teams
- ❌ Difficult to maintain

**Automated from Terraform:**
- ✅ Instant visualization
- ✅ Always up-to-date
- ✅ IBM Design Language compliance
- ✅ Zero manual effort

### How It Works

```bash
# 1. Run Terraform to create infrastructure
terraform apply

# 2. Generate state file
terraform show -json > terraform.tfstate

# 3. Create diagram
ibmdiagrams terraform.tfstate

# 4. Open in draw.io
open terraform.drawio
```

---

## Quick Start

### Prerequisites

1. **Terraform state file** (`.tfstate` or JSON format)
2. **IBM Diagrams installed** ([Setup Guide](setup.md))
3. **draw.io Desktop** ([Download](https://github.com/jgraph/drawio-desktop/releases))

### Basic Usage

```bash
# Generate diagram with custom labels (default)
ibmdiagrams cloud.tfstate
# Output: cloud.drawio

# Open in draw.io
open cloud.drawio  # macOS
start cloud.drawio  # Windows
xdg-open cloud.drawio  # Linux
```

---

## Command Options

### Full Command Syntax

```bash
ibmdiagrams [OPTIONS] <tfstate-file>
```

### Available Options

| Option | Description | Example |
|--------|-------------|---------|
| `--general` | Use general labels (resource types only) | `ibmdiagrams --general cloud.tfstate` |
| `--python` | Generate Python code instead of drawio | `ibmdiagrams --python cloud.tfstate` |
| `-output <dir>` | Specify output directory | `ibmdiagrams -output ./diagrams cloud.tfstate` |
| `-font <name>` | Use custom font | `ibmdiagrams -font "IBM Plex Sans JP" cloud.tfstate` |
| `--help` | Show help message | `ibmdiagrams --help` |

### Examples

```bash
# Custom labels with specific output folder
ibmdiagrams -output ./architecture-docs cloud.tfstate

# General labels with Japanese font
ibmdiagrams --general -font "IBM Plex Sans JP" cloud.tfstate

# Generate Python code for customization
ibmdiagrams --python cloud.tfstate
# Output: cloud.py (editable Python code)

# Combine multiple options
ibmdiagrams --general -output ./docs -font "IBM Plex Sans KR" cloud.tfstate
```

---

## Label Modes

### Custom Labels (Default)

Shows specific resource details like names, IPs, and CIDRs.

```bash
ibmdiagrams cloud.tfstate
```

**Output includes:**
- Resource names (e.g., "web-server-1")
- IP addresses (e.g., "10.10.10.4")
- CIDR blocks (e.g., "10.10.0.0/18")
- Custom tags and labels

**Best for:**
- ✅ Detailed documentation
- ✅ Troubleshooting
- ✅ Compliance audits
- ✅ Team onboarding

**Example Output:**
```
VPC: "production-vpc"
├── Zone: "us-south-1" (10.10.0.0/18)
│   ├── Subnet: "web-subnet" (10.10.10.0/24)
│   │   └── VSI: "web-server-1" (10.10.10.4)
│   └── Subnet: "app-subnet" (10.10.20.0/24)
│       └── VSI: "app-server-1" (10.10.20.4)
```

---

### General Labels

Shows only resource types without specific details.

```bash
ibmdiagrams --general cloud.tfstate
```

**Output includes:**
- Resource types (e.g., "Virtual Server")
- Generic labels (e.g., "Subnet", "VPC")
- No IP addresses or specific names

**Best for:**
- ✅ High-level overviews
- ✅ Architecture presentations
- ✅ Simplified documentation
- ✅ Public-facing diagrams

**Example Output:**
```
VPC
├── Zone
│   ├── Subnet
│   │   └── Virtual Server
│   └── Subnet
│       └── Virtual Server
```

---

## Output Formats

### DrawIO Format (Default)

```bash
ibmdiagrams cloud.tfstate
# Output: cloud.drawio
```

**Features:**
- ✅ Editable in draw.io desktop
- ✅ IBM Design Language styling
- ✅ Automatic layout
- ✅ Export to PNG, SVG, PDF

**Use Cases:**
- Final documentation
- Presentations
- Compliance reports
- Team sharing

---

### Python Code Format

```bash
ibmdiagrams --python cloud.tfstate
# Output: cloud.py
```

**Features:**
- ✅ Editable Python code
- ✅ Version control friendly
- ✅ Customizable
- ✅ Reusable as template

**Use Cases:**
- Creating diagram templates
- Customizing generated diagrams
- Learning diagram-as-code
- Building on existing infrastructure

**Workflow:**
```bash
# 1. Generate Python code
ibmdiagrams --python cloud.tfstate

# 2. Edit the generated code
vim cloud.py

# 3. Run to create diagram
python cloud.py
# Output: cloud.drawio
```

---

## Examples

### Example 1: Simple VPC

**Terraform Configuration:**
```hcl
resource "ibm_is_vpc" "example" {
  name = "example-vpc"
}

resource "ibm_is_subnet" "example" {
  name            = "example-subnet"
  vpc             = ibm_is_vpc.example.id
  zone            = "us-south-1"
  ipv4_cidr_block = "10.240.0.0/24"
}

resource "ibm_is_instance" "example" {
  name    = "example-vsi"
  vpc     = ibm_is_vpc.example.id
  zone    = "us-south-1"
  profile = "bx2-2x8"
  
  primary_network_interface {
    subnet = ibm_is_subnet.example.id
  }
}
```

**Generate Diagram:**
```bash
# Apply Terraform
terraform apply

# Export state
terraform show -json > example.tfstate

# Generate diagram
ibmdiagrams example.tfstate
# Output: example.drawio
```

[🔗 See full example](examples/terraform/terraform-custom-labels.md)

---

### Example 2: Multi-Zone VPC

**Terraform Configuration:**
```hcl
resource "ibm_is_vpc" "multi_zone" {
  name = "multi-zone-vpc"
}

resource "ibm_is_subnet" "zone1" {
  name            = "zone1-subnet"
  vpc             = ibm_is_vpc.multi_zone.id
  zone            = "us-south-1"
  ipv4_cidr_block = "10.10.0.0/24"
}

resource "ibm_is_subnet" "zone2" {
  name            = "zone2-subnet"
  vpc             = ibm_is_vpc.multi_zone.id
  zone            = "us-south-2"
  ipv4_cidr_block = "10.20.0.0/24"
}

resource "ibm_is_instance" "web1" {
  name    = "web-server-1"
  vpc     = ibm_is_vpc.multi_zone.id
  zone    = "us-south-1"
  profile = "bx2-2x8"
  
  primary_network_interface {
    subnet = ibm_is_subnet.zone1.id
  }
}

resource "ibm_is_instance" "web2" {
  name    = "web-server-2"
  vpc     = ibm_is_vpc.multi_zone.id
  zone    = "us-south-2"
  profile = "bx2-2x8"
  
  primary_network_interface {
    subnet = ibm_is_subnet.zone2.id
  }
}
```

**Generate Diagrams:**
```bash
# Custom labels (detailed)
ibmdiagrams multi-zone.tfstate
# Output: multi-zone.drawio

# General labels (simplified)
ibmdiagrams --general multi-zone.tfstate
# Output: multi-zone.drawio
```

[🔗 See full example](examples/terraform/terraform-custom-labels.md)

---

### Example 3: Enterprise Landing Zone

See our comprehensive [VSI on VPC Landing Zone](examples/terraform/slzvsi.md) example generated from Terraform, featuring:
- Multi-zone deployment
- Management and workload VPCs
- VPN and VPE configuration
- Cloud services integration
- Security and observability

![SLZ VSI Terraform Example](examples/terraform/slzvsi-terraform.drawio.svg)

---

## Best Practices

### 1. Use Descriptive Resource Names

```hcl
# ❌ Bad - Generic names
resource "ibm_is_vpc" "vpc1" {
  name = "vpc1"
}

# ✅ Good - Descriptive names
resource "ibm_is_vpc" "production" {
  name = "production-vpc"
}
```

### 2. Add Tags for Better Organization

```hcl
resource "ibm_is_vpc" "production" {
  name = "production-vpc"
  
  tags = [
    "environment:production",
    "team:platform",
    "cost-center:engineering"
  ]
}
```

### 3. Use Consistent Naming Conventions

```hcl
# ✅ Good - Consistent pattern
resource "ibm_is_subnet" "web_zone1" {
  name = "web-subnet-zone1"
}

resource "ibm_is_subnet" "web_zone2" {
  name = "web-subnet-zone2"
}

resource "ibm_is_subnet" "app_zone1" {
  name = "app-subnet-zone1"
}
```

### 4. Generate Diagrams in CI/CD

```yaml
# .github/workflows/terraform-docs.yml
name: Generate Architecture Diagrams

on:
  push:
    paths:
      - '**.tf'
      - 'terraform.tfstate'

jobs:
  generate-diagrams:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install IBM Diagrams
        run: pip install ibmdiagrams-*.whl
      
      - name: Generate Diagrams
        run: |
          ibmdiagrams terraform.tfstate
          ibmdiagrams --general terraform.tfstate -output ./docs
      
      - name: Upload Diagrams
        uses: actions/upload-artifact@v3
        with:
          name: architecture-diagrams
          path: '*.drawio'
```

### 5. Keep State Files Secure

```bash
# ❌ Don't commit state files to git
echo "*.tfstate" >> .gitignore
echo "*.tfstate.backup" >> .gitignore

# ✅ Use remote state
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}

# Generate diagrams from remote state
terraform state pull > temp.tfstate
ibmdiagrams temp.tfstate
rm temp.tfstate
```

### 6. Document Diagram Generation

```markdown
# Architecture Documentation

## Generating Diagrams

To regenerate architecture diagrams:

1. Ensure Terraform state is up-to-date:
   ```bash
   terraform refresh
   ```

2. Export state:
   ```bash
   terraform show -json > infrastructure.tfstate
   ```

3. Generate diagrams:
   ```bash
   # Detailed diagram
   ibmdiagrams infrastructure.tfstate
   
   # High-level diagram
   ibmdiagrams --general infrastructure.tfstate
   ```

4. Open in draw.io:
   ```bash
   open infrastructure.drawio
   ```
```

---

## Troubleshooting

### Common Issues

<details>
<summary><b>Issue: No resources found in state file</b></summary>

**Symptoms:**
```bash
$ ibmdiagrams cloud.tfstate
Warning: No IBM Cloud resources found in state file
```

**Solutions:**

1. **Verify state file format**
   ```bash
   # Check if it's JSON format
   cat cloud.tfstate | jq .
   
   # If not JSON, export as JSON
   terraform show -json > cloud.tfstate
   ```

2. **Ensure resources are created**
   ```bash
   terraform apply
   terraform show
   ```

3. **Check for IBM Cloud resources**
   ```bash
   # State should contain ibm_is_* resources
   terraform state list | grep ibm_is
   ```

</details>

<details>
<summary><b>Issue: Diagram is empty or incomplete</b></summary>

**Symptoms:**
- Diagram opens but shows no resources
- Some resources are missing

**Solutions:**

1. **Check supported resources**
   - Currently supports VPC resources (ibm_is_*)
   - Classic infrastructure support is limited

2. **Verify state file**
   ```bash
   # List all resources
   terraform state list
   
   # Show specific resource
   terraform state show ibm_is_vpc.example
   ```

3. **Use verbose output**
   ```bash
   ibmdiagrams --verbose cloud.tfstate
   ```

</details>

<details>
<summary><b>Issue: Labels are truncated or overlapping</b></summary>

**Symptoms:**
- Long resource names are cut off
- Labels overlap with shapes

**Solutions:**

1. **Use general labels**
   ```bash
   ibmdiagrams --general cloud.tfstate
   ```

2. **Generate Python code and customize**
   ```bash
   ibmdiagrams --python cloud.tfstate
   # Edit cloud.py to adjust labels
   python cloud.py
   ```

3. **Use shorter resource names in Terraform**
   ```hcl
   resource "ibm_is_instance" "web" {
     name = "web-1"  # Instead of "web-server-production-zone1"
   }
   ```

</details>

<details>
<summary><b>Issue: Unsupported resource type</b></summary>

**Symptoms:**
```bash
Warning: Unsupported resource type: ibm_xyz
```

**Solutions:**

1. **Check supported resources**
   - See [Supported Resources](#supported-resources) section

2. **Generate Python code and add manually**
   ```bash
   ibmdiagrams --python cloud.tfstate
   # Edit cloud.py to add missing resources
   ```

3. **Request feature**
   - Open an issue on GitHub
   - Include resource type and use case

</details>

---

## Supported Resources

Based on the [Terraform Checklist](terraform-checklist.md), the following resources are currently supported:

### VPC Infrastructure

| Resource | Description |
|----------|-------------|
| `ibm_is_vpc` | Virtual Private Cloud |
| `ibm_is_subnet` | VPC Subnet |
| `ibm_is_instance` | Virtual Server Instance |
| `ibm_is_floating_ip` | Floating IP |
| `ibm_is_public_gateway` | Public Gateway |
| `ibm_is_vpn_gateway` | VPN Gateway |
| `ibm_is_virtual_endpoint_gateway` | Virtual Private Endpoint Gateway |
| `ibm_is_network_acl` | Network ACL |
| `ibm_is_security_group` | Security Group |
| `ibm_is_lb` | Load Balancer |
| `ibm_is_flow_log` | Flow Logs |

### Cloud Services

| Resource | Description |
|----------|-------------|
| `ibm_cos_bucket` | Cloud Object Storage Bucket |
| `ibm_kms_key` | Key Management Service Key |
| `ibm_container_vpc_cluster` | Kubernetes Service Cluster |
| `ibm_tg_gateway` | Transit Gateway |
| `ibm_resource_group` | Resource Group |

### Continuous Delivery

| Resource | Description |
|----------|-------------|
| `ibm_cd_toolchain` | Continuous Delivery Toolchain |
| `ibm_cd_toolchain_tool_pipeline` | Toolchain Pipeline Tool |
| `ibm_cd_toolchain_tool_hostedgit` | Toolchain Hosted Git Tool |
| `ibm_cd_tekton_pipeline` | Tekton Pipeline |

### Additional Resources

For a complete and up-to-date list of supported resources, see the [Terraform Checklist](terraform-checklist.md).

**Note:** The codebase includes definitions for many more Terraform resources (200+), but diagram generation support is actively being expanded. Check the terraform-checklist.md file for the latest supported resources.

---

## Advanced Usage

### Filtering Resources

```bash
# Generate diagram for specific workspace
terraform workspace select production
terraform show -json > production.tfstate
ibmdiagrams production.tfstate

# Generate diagram for specific module
terraform state pull | jq '.resources[] | select(.module == "module.vpc")' > vpc.tfstate
ibmdiagrams vpc.tfstate
```

### Comparing Environments

```bash
# Generate diagrams for each environment
terraform workspace select dev
terraform show -json > dev.tfstate
ibmdiagrams dev.tfstate

terraform workspace select staging
terraform show -json > staging.tfstate
ibmdiagrams staging.tfstate

terraform workspace select production
terraform show -json > production.tfstate
ibmdiagrams production.tfstate

# Compare visually in draw.io
```

### Automating Documentation Updates

```bash
#!/bin/bash
# update-diagrams.sh

# Export Terraform state
terraform show -json > infrastructure.tfstate

# Generate detailed diagram
ibmdiagrams infrastructure.tfstate -output ./docs/diagrams

# Generate high-level diagram
ibmdiagrams --general infrastructure.tfstate -output ./docs/diagrams

# Convert to PNG for README
# (requires draw.io CLI)
drawio -x -f png -o docs/diagrams/infrastructure.png docs/diagrams/infrastructure.drawio

# Commit changes
git add docs/diagrams/
git commit -m "docs: update architecture diagrams"
```

---

## Next Steps

- 📝 **[Diagram as Code](diagram-as-code.md)** - Customize generated diagrams
- 📚 **[Examples](examples/)** - See more Terraform examples
- 🎨 **[IBM Design Language](https://www.ibm.com/design/language/infographics/technical-diagrams/design)** - Learn the design standards

---

## License

This application is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
