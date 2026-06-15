# Terraform to DrawIO (Custom Labels)

Generate detailed architecture diagrams from Terraform state files with custom labels showing resource names, IP addresses, and CIDR blocks.

## Overview

This example demonstrates how to automatically generate diagrams from Terraform infrastructure with **custom labels** that include:
- Resource names (e.g., "production-vpc", "web-server-1")
- IP addresses (e.g., "10.10.10.4")
- CIDR blocks (e.g., "10.10.0.0/18")
- Custom tags and metadata

## Use Case

**Perfect for:**
- ✅ Detailed infrastructure documentation
- ✅ Troubleshooting and debugging
- ✅ Compliance and audit reports
- ✅ Team onboarding and knowledge transfer
- ✅ Change management documentation

## Terraform Configuration

### Example: Multi-Zone VPC

```hcl
# main.tf

terraform {
  required_providers {
    ibm = {
      source  = "IBM-Cloud/ibm"
      version = "~> 1.60"
    }
  }
}

provider "ibm" {
  region = "us-south"
}

# VPC
resource "ibm_is_vpc" "production" {
  name = "production-vpc"
  tags = ["environment:production", "team:platform"]
}

# Zone 1 Resources
resource "ibm_is_subnet" "web_zone1" {
  name            = "web-subnet-zone1"
  vpc             = ibm_is_vpc.production.id
  zone            = "us-south-1"
  ipv4_cidr_block = "10.10.10.0/24"
}

resource "ibm_is_subnet" "app_zone1" {
  name            = "app-subnet-zone1"
  vpc             = ibm_is_vpc.production.id
  zone            = "us-south-1"
  ipv4_cidr_block = "10.10.20.0/24"
}

resource "ibm_is_instance" "web1" {
  name    = "web-server-1"
  vpc     = ibm_is_vpc.production.id
  zone    = "us-south-1"
  profile = "bx2-2x8"
  
  primary_network_interface {
    subnet = ibm_is_subnet.web_zone1.id
  }
  
  tags = ["tier:web", "zone:1"]
}

resource "ibm_is_instance" "app1" {
  name    = "app-server-1"
  vpc     = ibm_is_vpc.production.id
  zone    = "us-south-1"
  profile = "bx2-4x16"
  
  primary_network_interface {
    subnet = ibm_is_subnet.app_zone1.id
  }
  
  tags = ["tier:app", "zone:1"]
}

# Zone 2 Resources
resource "ibm_is_subnet" "web_zone2" {
  name            = "web-subnet-zone2"
  vpc             = ibm_is_vpc.production.id
  zone            = "us-south-2"
  ipv4_cidr_block = "10.10.74.0/24"
}

resource "ibm_is_subnet" "app_zone2" {
  name            = "app-subnet-zone2"
  vpc             = ibm_is_vpc.production.id
  zone            = "us-south-2"
  ipv4_cidr_block = "10.10.84.0/24"
}

resource "ibm_is_instance" "web2" {
  name    = "web-server-2"
  vpc     = ibm_is_vpc.production.id
  zone    = "us-south-2"
  profile = "bx2-2x8"
  
  primary_network_interface {
    subnet = ibm_is_subnet.web_zone2.id
  }
  
  tags = ["tier:web", "zone:2"]
}

resource "ibm_is_instance" "app2" {
  name    = "app-server-2"
  vpc     = ibm_is_vpc.production.id
  zone    = "us-south-2"
  profile = "bx2-4x16"
  
  primary_network_interface {
    subnet = ibm_is_subnet.app_zone2.id
  }
  
  tags = ["tier:app", "zone:2"]
}

# Load Balancer
resource "ibm_is_lb" "web" {
  name    = "web-load-balancer"
  subnets = [ibm_is_subnet.web_zone1.id, ibm_is_subnet.web_zone2.id]
}

# Public Gateway
resource "ibm_is_public_gateway" "zone1" {
  name = "public-gateway-zone1"
  vpc  = ibm_is_vpc.production.id
  zone = "us-south-1"
}

resource "ibm_is_public_gateway" "zone2" {
  name = "public-gateway-zone2"
  vpc  = ibm_is_vpc.production.id
  zone = "us-south-2"
}

# Security Groups
resource "ibm_is_security_group" "web" {
  name = "web-security-group"
  vpc  = ibm_is_vpc.production.id
}

resource "ibm_is_security_group" "app" {
  name = "app-security-group"
  vpc  = ibm_is_vpc.production.id
}

# Security Group Rules
resource "ibm_is_security_group_rule" "web_inbound_https" {
  group     = ibm_is_security_group.web.id
  direction = "inbound"
  remote    = "0.0.0.0/0"
  
  tcp {
    port_min = 443
    port_max = 443
  }
}

resource "ibm_is_security_group_rule" "app_inbound_from_web" {
  group     = ibm_is_security_group.app.id
  direction = "inbound"
  remote    = ibm_is_security_group.web.id
  
  tcp {
    port_min = 8080
    port_max = 8080
  }
}
```

## Generate Diagram

### Step 1: Apply Terraform

```bash
# Initialize Terraform
terraform init

# Plan the deployment
terraform plan

# Apply the configuration
terraform apply
```

### Step 2: Export State

```bash
# Export Terraform state as JSON
terraform show -json > production.tfstate
```

### Step 3: Generate Diagram with Custom Labels

```bash
# Generate diagram (custom labels is the default)
ibmdiagrams production.tfstate

# Output: production.drawio
```

### Step 4: Open in draw.io

```bash
# macOS
open production.drawio

# Windows
start production.drawio

# Linux
xdg-open production.drawio
```

## Expected Output

The generated diagram will show:

### VPC Level
- **VPC Name**: "production-vpc"
- **Tags**: environment:production, team:platform

### Zone Level
- **Zone 1**: "us-south-1" with CIDR "10.10.0.0/18"
- **Zone 2**: "us-south-2" with CIDR "10.10.64.0/18"

### Subnet Level
- **web-subnet-zone1**: 10.10.10.0/24
- **app-subnet-zone1**: 10.10.20.0/24
- **web-subnet-zone2**: 10.10.74.0/24
- **app-subnet-zone2**: 10.10.84.0/24

### Instance Level
- **web-server-1**: 10.10.10.4 (bx2-2x8)
- **app-server-1**: 10.10.20.4 (bx2-4x16)
- **web-server-2**: 10.10.74.4 (bx2-2x8)
- **app-server-2**: 10.10.84.4 (bx2-4x16)

### Network Components
- **web-load-balancer**: Spans both zones
- **public-gateway-zone1**: Zone 1 internet access
- **public-gateway-zone2**: Zone 2 internet access

### Security Groups
- **web-security-group**: HTTPS (443) from internet
- **app-security-group**: Port 8080 from web tier only

## Diagram Features

### Custom Labels Show

1. **Resource Names**: Exact names from Terraform
   ```
   VPC: "production-vpc"
   Subnet: "web-subnet-zone1"
   Instance: "web-server-1"
   ```

2. **IP Addresses**: Assigned IPs for instances
   ```
   Virtual Server: "web-server-1"
   IP: 10.10.10.4
   ```

3. **CIDR Blocks**: Network ranges for subnets and zones
   ```
   Subnet: "web-subnet-zone1"
   CIDR: 10.10.10.0/24
   ```

4. **Resource Metadata**: Profiles, types, configurations
   ```
   Instance: "web-server-1"
   Profile: bx2-2x8
   vCPU: 2, RAM: 8GB
   ```

## Advanced Options

### Specify Output Directory

```bash
ibmdiagrams -output ./docs/architecture production.tfstate
# Output: ./docs/architecture/production.drawio
```

### Use Custom Font

```bash
ibmdiagrams -font "IBM Plex Sans JP" production.tfstate
# Uses Japanese font variant
```

### Combine Options

```bash
ibmdiagrams -output ./diagrams -font "IBM Plex Sans KR" production.tfstate
# Korean font + custom output directory
```

## Comparison: Custom vs General Labels

| Aspect | Custom Labels | General Labels |
|--------|---------------|----------------|
| **Resource Names** | ✅ "web-server-1" | ❌ "Virtual Server" |
| **IP Addresses** | ✅ "10.10.10.4" | ❌ Not shown |
| **CIDR Blocks** | ✅ "10.10.10.0/24" | ❌ Not shown |
| **Detail Level** | High | Low |
| **Use Case** | Documentation, troubleshooting | Presentations, overviews |
| **File Size** | Larger | Smaller |

## Best Practices

### 1. Use Descriptive Names in Terraform

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

### 2. Add Meaningful Tags

```hcl
resource "ibm_is_instance" "web" {
  name = "web-server-1"
  tags = [
    "environment:production",
    "tier:web",
    "team:platform",
    "cost-center:engineering"
  ]
}
```

### 3. Use Consistent Naming Conventions

```hcl
# Pattern: <tier>-<resource>-<zone>
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

### 4. Document CIDR Allocation

```hcl
# Document your IP allocation strategy
# Zone 1: 10.10.0.0/18 (16,384 IPs)
#   - Web:  10.10.10.0/24 (256 IPs)
#   - App:  10.10.20.0/24 (256 IPs)
#   - DB:   10.10.30.0/24 (256 IPs)
# Zone 2: 10.10.64.0/18 (16,384 IPs)
#   - Web:  10.10.74.0/24 (256 IPs)
#   - App:  10.10.84.0/24 (256 IPs)
#   - DB:   10.10.94.0/24 (256 IPs)
```

### 5. Regenerate After Changes

```bash
# After any Terraform changes
terraform apply
terraform show -json > production.tfstate
ibmdiagrams production.tfstate

# Commit both state and diagram
git add production.tfstate production.drawio
git commit -m "docs: update infrastructure diagram"
```

## Automation

### CI/CD Integration

```yaml
# .github/workflows/terraform-docs.yml
name: Update Architecture Diagrams

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
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v2
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install IBM Diagrams
        run: pip install ibmdiagrams-*.whl
      
      - name: Export Terraform State
        run: terraform show -json > infrastructure.tfstate
      
      - name: Generate Diagram
        run: ibmdiagrams infrastructure.tfstate
      
      - name: Commit Diagram
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add infrastructure.drawio
          git commit -m "docs: update architecture diagram [skip ci]" || true
          git push
```

## Troubleshooting

### Issue: Missing Resources

**Problem**: Some resources don't appear in the diagram

**Solution**:
1. Verify resources are in state file:
   ```bash
   terraform state list
   ```

2. Check if resource type is supported:
   ```bash
   terraform state list | grep ibm_is
   ```

3. Ensure resources are created:
   ```bash
   terraform apply
   ```

### Issue: Labels Are Truncated

**Problem**: Long resource names are cut off

**Solution**:
1. Use shorter names in Terraform
2. Generate Python code and customize:
   ```bash
   ibmdiagrams --python production.tfstate
   # Edit production.py to adjust labels
   python production.py
   ```

### Issue: Diagram Is Too Complex

**Problem**: Too many resources make diagram hard to read

**Solution**:
1. Use general labels for overview:
   ```bash
   ibmdiagrams --general production.tfstate
   ```

2. Generate separate diagrams per module:
   ```bash
   terraform state pull | jq '.resources[] | select(.module == "module.vpc")' > vpc.tfstate
   ibmdiagrams vpc.tfstate
   ```

## Related Examples

- [Terraform General Labels](terraform-general-labels.md) - Simplified diagrams
- [Terraform to Python](terraform-to-python.md) - Convert to editable code
- [Simple VPC](../python/simple-vpc.md) - Diagram-as-code equivalent

## Next Steps

1. **Try general labels**: See [Terraform General Labels](terraform-general-labels.md)
2. **Customize diagrams**: Convert to Python with `--python` flag
3. **Automate**: Set up CI/CD to regenerate diagrams automatically
4. **Export**: Use draw.io to export as PNG, SVG, or PDF

## License

This application is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).