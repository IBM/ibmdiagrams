# Terraform to DrawIO (General Labels)

Generate simplified architecture diagrams from Terraform state files with general labels showing only resource types.

## Overview

This example demonstrates how to generate diagrams from Terraform infrastructure with **general labels** that show:
- Resource types only (e.g., "Virtual Server", "Subnet", "VPC")
- No specific names, IPs, or CIDR blocks
- Clean, simplified architecture overview

## Use Case

**Perfect for:**
- ✅ High-level architecture presentations
- ✅ Executive summaries
- ✅ Public-facing documentation
- ✅ Architecture proposals
- ✅ Simplified training materials
- ✅ Marketing and sales materials

## Command

```bash
# Generate diagram with general labels
ibmdiagrams --general cloud.tfstate

# Output: cloud.drawio
```

## Comparison: General vs Custom Labels

### Visual Difference

**Custom Labels (Default):**
```
VPC: "production-vpc"
├── Zone: "us-south-1" (10.10.0.0/18)
│   ├── Subnet: "web-subnet-zone1" (10.10.10.0/24)
│   │   └── Virtual Server: "web-server-1" (10.10.10.4)
│   └── Subnet: "app-subnet-zone1" (10.10.20.0/24)
│       └── Virtual Server: "app-server-1" (10.10.20.4)
```

**General Labels:**
```
VPC
├── Zone
│   ├── Subnet
│   │   └── Virtual Server
│   └── Subnet
│       └── Virtual Server
```

### Feature Comparison

| Feature | Custom Labels | General Labels |
|---------|---------------|----------------|
| **Resource Names** | ✅ "web-server-1" | ❌ "Virtual Server" |
| **IP Addresses** | ✅ "10.10.10.4" | ❌ Not shown |
| **CIDR Blocks** | ✅ "10.10.10.0/24" | ❌ Not shown |
| **Clarity** | Detailed | Simplified |
| **File Size** | Larger | Smaller |
| **Privacy** | Shows specifics | Hides specifics |
| **Best For** | Documentation | Presentations |

## Example Terraform Configuration

Using the same Terraform configuration as the [custom labels example](terraform-custom-labels.md):

```hcl
# main.tf
resource "ibm_is_vpc" "production" {
  name = "production-vpc"
}

resource "ibm_is_subnet" "web_zone1" {
  name            = "web-subnet-zone1"
  vpc             = ibm_is_vpc.production.id
  zone            = "us-south-1"
  ipv4_cidr_block = "10.10.10.0/24"
}

resource "ibm_is_instance" "web1" {
  name    = "web-server-1"
  vpc     = ibm_is_vpc.production.id
  zone    = "us-south-1"
  profile = "bx2-2x8"
  
  primary_network_interface {
    subnet = ibm_is_subnet.web_zone1.id
  }
}

# ... more resources
```

## Generate Diagram

### Step 1: Apply Terraform

```bash
terraform init
terraform apply
```

### Step 2: Export State

```bash
terraform show -json > production.tfstate
```

### Step 3: Generate with General Labels

```bash
# Use --general flag
ibmdiagrams --general production.tfstate

# Output: production.drawio
```

### Step 4: Open in draw.io

```bash
open production.drawio  # macOS
start production.drawio  # Windows
xdg-open production.drawio  # Linux
```

## Expected Output

The generated diagram will show:

### Generic Labels Only

- **VPC** (instead of "production-vpc")
- **Zone** (instead of "us-south-1")
- **Subnet** (instead of "web-subnet-zone1")
- **Virtual Server** (instead of "web-server-1")
- **Load Balancer** (instead of "web-load-balancer")
- **Public Gateway** (instead of "public-gateway-zone1")
- **Security Group** (instead of "web-security-group")

### No Technical Details

- ❌ No IP addresses
- ❌ No CIDR blocks
- ❌ No resource names
- ❌ No tags or metadata
- ✅ Only resource types and relationships

## Use Cases

### 1. Executive Presentations

```bash
# Generate clean diagram for C-level presentation
ibmdiagrams --general production.tfstate -output ./presentations

# Result: Simple, easy-to-understand architecture overview
```

**Benefits:**
- No technical clutter
- Focus on architecture patterns
- Easy to understand for non-technical audience

### 2. Public Documentation

```bash
# Generate diagram for public GitHub repository
ibmdiagrams --general infrastructure.tfstate -output ./docs

# Result: Architecture overview without exposing internal details
```

**Benefits:**
- No sensitive information (IPs, names)
- Safe to share publicly
- Professional appearance

### 3. Architecture Proposals

```bash
# Generate diagram for architecture review
ibmdiagrams --general proposed-architecture.tfstate

# Result: High-level design for stakeholder review
```

**Benefits:**
- Focus on design patterns
- Not distracted by implementation details
- Easier to discuss alternatives

### 4. Training Materials

```bash
# Generate simplified diagrams for training
ibmdiagrams --general example-architecture.tfstate -output ./training

# Result: Clear examples for learning
```

**Benefits:**
- Easier to understand for beginners
- Focus on concepts, not specifics
- Reusable across different scenarios

## Advanced Options

### Combine with Other Flags

```bash
# General labels + custom output directory
ibmdiagrams --general -output ./docs/architecture production.tfstate

# General labels + custom font
ibmdiagrams --general -font "IBM Plex Sans JP" production.tfstate

# All options combined
ibmdiagrams --general -output ./presentations -font "IBM Plex Sans KR" production.tfstate
```

### Generate Both Versions

```bash
# Detailed version for internal use
ibmdiagrams production.tfstate -output ./internal
# Output: ./internal/production.drawio (with custom labels)

# Simplified version for presentations
ibmdiagrams --general production.tfstate -output ./public
# Output: ./public/production.drawio (with general labels)
```

## Best Practices

### 1. Use for Different Audiences

```bash
# Internal team: Custom labels
ibmdiagrams infrastructure.tfstate -output ./docs/internal

# External stakeholders: General labels
ibmdiagrams --general infrastructure.tfstate -output ./docs/external
```

### 2. Version Control Both Versions

```bash
# Generate both versions
ibmdiagrams infrastructure.tfstate -output ./docs/detailed
ibmdiagrams --general infrastructure.tfstate -output ./docs/overview

# Commit both
git add docs/detailed/ docs/overview/
git commit -m "docs: update architecture diagrams"
```

### 3. Use in CI/CD

```yaml
# .github/workflows/diagrams.yml
name: Generate Diagrams

on:
  push:
    paths:
      - '**.tf'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install IBM Diagrams
        run: pip install ibmdiagrams-*.whl
      
      - name: Export Terraform State
        run: terraform show -json > infrastructure.tfstate
      
      - name: Generate Detailed Diagram
        run: ibmdiagrams infrastructure.tfstate -output ./docs/detailed
      
      - name: Generate Overview Diagram
        run: ibmdiagrams --general infrastructure.tfstate -output ./docs/overview
      
      - name: Commit Diagrams
        run: |
          git add docs/
          git commit -m "docs: update diagrams [skip ci]"
          git push
```

### 4. Document the Difference

```markdown
# Architecture Documentation

## Diagrams

We maintain two versions of our architecture diagrams:

### Detailed Version (Internal)
- Location: `docs/detailed/infrastructure.drawio`
- Includes: Resource names, IPs, CIDR blocks
- Audience: Engineering team
- Update: Automatically on Terraform changes

### Overview Version (Public)
- Location: `docs/overview/infrastructure.drawio`
- Includes: Resource types only
- Audience: Stakeholders, public documentation
- Update: Automatically on Terraform changes

## Generating Diagrams

```bash
# Detailed
ibmdiagrams infrastructure.tfstate -output ./docs/detailed

# Overview
ibmdiagrams --general infrastructure.tfstate -output ./docs/overview
```
```

## When to Use General Labels

### ✅ Use General Labels When:

1. **Presenting to executives** - Focus on architecture, not details
2. **Public documentation** - Avoid exposing internal information
3. **Architecture proposals** - Discuss design patterns
4. **Training materials** - Teach concepts, not specifics
5. **Marketing materials** - Show capabilities without details
6. **Initial planning** - High-level design discussions

### ❌ Use Custom Labels When:

1. **Internal documentation** - Team needs specific details
2. **Troubleshooting** - Need IPs and names for debugging
3. **Compliance audits** - Require complete information
4. **Change management** - Track specific resource changes
5. **Onboarding** - New team members need full context
6. **Operations** - Day-to-day infrastructure management

## Switching Between Modes

### From General to Custom

```bash
# Start with general for presentation
ibmdiagrams --general infrastructure.tfstate

# Need details? Regenerate with custom labels
ibmdiagrams infrastructure.tfstate
```

### From Custom to General

```bash
# Have detailed diagram
ibmdiagrams infrastructure.tfstate

# Need simplified version? Add --general flag
ibmdiagrams --general infrastructure.tfstate
```

### Convert to Python for Customization

```bash
# Generate Python code (always uses custom labels)
ibmdiagrams --python infrastructure.tfstate

# Edit the Python file to customize labels
vim infrastructure.py

# Run to create diagram
python infrastructure.py
```

## Troubleshooting

### Issue: Diagram Still Shows Details

**Problem**: Using `--general` but still seeing resource names

**Solution**:
```bash
# Verify you're using the --general flag
ibmdiagrams --general infrastructure.tfstate

# Check the command output
ibmdiagrams --general --verbose infrastructure.tfstate
```

### Issue: Need Some Details

**Problem**: General labels too simple, custom labels too detailed

**Solution**:
```bash
# Generate Python code
ibmdiagrams --python infrastructure.tfstate

# Edit to show only what you need
vim infrastructure.py

# Example: Keep names but remove IPs
# Change: VirtualServer("web-server-1", "10.10.10.4")
# To: VirtualServer("web-server-1")

# Generate diagram
python infrastructure.py
```

### Issue: Diagram Looks Empty

**Problem**: General labels make diagram look too sparse

**Solution**:
1. This is expected - general labels are minimal
2. Add annotations in draw.io if needed
3. Use custom labels for more detail
4. Consider hybrid approach with Python code

## Related Examples

- [Terraform Custom Labels](terraform-custom-labels.md) - Detailed diagrams
- [Terraform to Python](terraform-to-python.md) - Customizable diagrams
- [Simple VPC](../python/simple-vpc.md) - Diagram-as-code approach

## Next Steps

1. **Compare both modes**: Generate diagrams with and without `--general`
2. **Choose appropriate mode**: Based on your audience
3. **Automate generation**: Set up CI/CD for both versions
4. **Customize further**: Use `--python` flag for full control

## License

This application is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).