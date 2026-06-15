# Terraform to Python Conversion

Convert Terraform state files to editable Python code, enabling customization and creating reusable templates from existing infrastructure.

## Overview

This example demonstrates how to convert Terraform infrastructure to Python diagram-as-code using the `--python` flag. This creates editable Python files that you can:
- Customize and extend
- Use as templates for new projects
- Version control alongside your code
- Modify without changing Terraform

## Use Case

**Perfect for:**
- ✅ Creating diagram templates from existing infrastructure
- ✅ Customizing auto-generated diagrams
- ✅ Learning diagram-as-code from real infrastructure
- ✅ Bridging Terraform and diagram-as-code workflows
- ✅ Building reusable architecture patterns
- ✅ Documenting infrastructure with custom annotations

## Command

```bash
# Convert Terraform state to Python code
ibmdiagrams --python cloud.tfstate

# Output: cloud.py (editable Python code)
```

## Workflow

### Step 1: Apply Terraform

```bash
terraform init
terraform apply
```

### Step 2: Export State

```bash
terraform show -json > production.tfstate
```

### Step 3: Generate Python Code

```bash
ibmdiagrams --python production.tfstate
# Output: production.py
```

### Step 4: Customize the Code

```bash
# Edit the generated Python file
vim production.py

# Or use your favorite editor
code production.py
```

### Step 5: Generate Diagram

```bash
# Run the Python script
python production.py

# Output: production.drawio
```

### Step 6: Open in draw.io

```bash
open production.drawio  # macOS
start production.drawio  # Windows
xdg-open production.drawio  # Linux
```

## Example

### Original Terraform

```hcl
# main.tf
resource "ibm_is_vpc" "example" {
  name = "example-vpc"
}

resource "ibm_is_subnet" "web" {
  name            = "web-subnet"
  vpc             = ibm_is_vpc.example.id
  zone            = "us-south-1"
  ipv4_cidr_block = "10.10.10.0/24"
}

resource "ibm_is_instance" "web" {
  name    = "web-server"
  vpc     = ibm_is_vpc.example.id
  zone    = "us-south-1"
  profile = "bx2-2x8"
  
  primary_network_interface {
    subnet = ibm_is_subnet.web.id
  }
}
```

### Generated Python Code

```bash
# Generate Python from Terraform
terraform show -json > example.tfstate
ibmdiagrams --python example.tfstate
```

**Output (`example.py`):**

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet
from ibmdiagrams.ibmcloud.compute import VirtualServer

with Diagram("example"):
    with IBMCloud("IBM Cloud"):
        with Region("us-south"):
            with VPC("example-vpc"):
                with Zone("us-south-1", "10.10.0.0/18"):
                    with Subnet("web-subnet", "10.10.10.0/24"):
                        web = VirtualServer("web-server", "10.10.10.4")
```

### Customized Python Code

Now you can edit `example.py` to add features not in Terraform:

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet, SecurityGroup
from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.network import ApplicationLoadBalancer, PublicGateway
from ibmdiagrams.ibmcloud.observability import CloudLogs, Monitoring
from ibmdiagrams.ibmcloud.actors import User

with Diagram("example-enhanced", direction="TB"):
    # Add user actor (not in Terraform)
    user = User("End User")
    
    with IBMCloud("IBM Cloud"):
        with Region("us-south"):
            with VPC("example-vpc"):
                # Add load balancer (not in Terraform)
                alb = ApplicationLoadBalancer("Load Balancer")
                pgw = PublicGateway("Public Gateway")
                
                with Zone("us-south-1", "10.10.0.0/18"):
                    with Subnet("web-subnet", "10.10.10.0/24"):
                        with SecurityGroup("Web Security Group"):
                            # Enhanced label with more details
                            web = VirtualServer(
                                "web-server",
                                "10.10.10.4<br>bx2-2x8<br>Ubuntu 22.04"
                            )
                
                # Add observability (not in Terraform)
                logs = CloudLogs("Application Logs")
                mon = Monitoring("Infrastructure Monitoring")
```

## Common Customizations

### 1. Add Annotations and Comments

```python
# Generated code
with VPC("production-vpc"):
    with Subnet("web-subnet", "10.10.10.0/24"):
        web = VirtualServer("web-server", "10.10.10.4")

# Customized with comments
with VPC("production-vpc"):
    # Frontend tier - handles HTTP/HTTPS traffic
    with Subnet("web-subnet", "10.10.10.0/24"):
        # Primary web server - serves static content
        web = VirtualServer(
            "web-server",
            "10.10.10.4<br>Nginx 1.24<br>2vCPU, 8GB RAM"
        )
```

### 2. Change Layout Direction

```python
# Generated (default horizontal)
with Diagram("example"):
    with IBMCloud("IBM Cloud"):
        pass

# Customized (vertical layout)
with Diagram("example", direction="TB"):
    with IBMCloud("IBM Cloud", direction="TB"):
        pass
```

### 3. Add Missing Components

```python
# Generated from Terraform
with VPC("production-vpc"):
    with Subnet("app-subnet"):
        app = VirtualServer("app-server")

# Add components not in Terraform
from ibmdiagrams.ibmcloud.actors import User
from ibmdiagrams.ibmcloud.network import ApplicationLoadBalancer

user = User("End User")  # External actor

with VPC("production-vpc"):
    alb = ApplicationLoadBalancer("Load Balancer")  # Add LB
    
    with Subnet("app-subnet"):
        app = VirtualServer("app-server")
```

### 4. Enhance Labels

```python
# Generated (basic labels)
vsi = VirtualServer("web-server-1", "10.10.10.4")

# Enhanced (detailed labels)
vsi = VirtualServer(
    label="web-server-1",
    sublabel="10.10.10.4<br>Type: Dedicated<br>OS: Ubuntu 22.04 LTS<br>Profile: bx2-4x16<br>vCPU: 4<br>RAM: 16GiB<br>Bandwidth: 8Gbps"
)
```

### 5. Add Connectors

```python
from ibmdiagrams.ibmcloud.connectors import SolidEdge

# Define resources
with Subnet("web-subnet"):
    web = VirtualServer("web-server")

with Subnet("app-subnet"):
    app = VirtualServer("app-server")

# Add connection (not in Terraform)
SolidEdge(web, app, label="HTTPS")
```

### 6. Create Reusable Functions

```python
def create_tier(tier_name, zone_name, subnet_cidr, server_count):
    """Create a tier with multiple servers"""
    with Zone(zone_name):
        with Subnet(f"{tier_name} Subnet", subnet_cidr):
            servers = []
            for i in range(1, server_count + 1):
                server = VirtualServer(
                    f"{tier_name} Server {i}",
                    f"{subnet_cidr.split('.')[0]}.{subnet_cidr.split('.')[1]}.{subnet_cidr.split('.')[2]}.{i+3}"
                )
                servers.append(server)
            return servers

# Use the function
with VPC("production-vpc"):
    web_servers = create_tier("Web", "Zone 1", "10.10.10.0/24", 3)
    app_servers = create_tier("App", "Zone 1", "10.10.20.0/24", 2)
```

## Advanced Use Cases

### Use Case 1: Template Creation

```bash
# 1. Generate Python from production infrastructure
ibmdiagrams --python production.tfstate

# 2. Generalize the code
vim production.py
# Remove specific IPs, names
# Add parameters for customization

# 3. Save as template
mv production.py templates/vpc-template.py

# 4. Use template for new projects
cp templates/vpc-template.py new-project.py
# Edit new-project.py with project-specific values
python new-project.py
```

### Use Case 2: Documentation Enhancement

```bash
# 1. Generate from Terraform
ibmdiagrams --python infrastructure.tfstate

# 2. Add documentation elements
vim infrastructure.py
# Add: User actors, external systems, data flows, annotations

# 3. Generate enhanced diagram
python infrastructure.py

# 4. Export for documentation
# Open in draw.io and export as PNG/SVG
```

### Use Case 3: Multi-Environment Diagrams

```python
# Generated base from Terraform
def create_environment(env_name, zone_count):
    with Diagram(f"{env_name}-architecture"):
        with IBMCloud("IBM Cloud"):
            with Region("Dallas"):
                with VPC(f"{env_name}-vpc"):
                    for z in range(1, zone_count + 1):
                        with Zone(f"Zone {z}"):
                            with Subnet(f"Subnet {z}"):
                                VirtualServer(f"{env_name}-server-{z}")

# Generate diagrams for each environment
create_environment("dev", 1)
create_environment("staging", 2)
create_environment("production", 3)
```

### Use Case 4: Comparison Diagrams

```bash
# Generate Python from different states
ibmdiagrams --python before.tfstate
mv before.py diagrams/before.py

ibmdiagrams --python after.tfstate
mv after.py diagrams/after.py

# Customize both for comparison
# Add highlights, annotations, etc.

# Generate both diagrams
python diagrams/before.py
python diagrams/after.py

# Compare visually in draw.io
```

## Best Practices

### 1. Version Control Python Files

```bash
# Add generated Python to git
git add infrastructure.py
git commit -m "docs: add infrastructure diagram code"

# Track changes over time
git log infrastructure.py
git diff HEAD~1 infrastructure.py
```

### 2. Separate Generated and Custom Code

```python
# infrastructure_base.py (generated, don't edit)
# Generated from Terraform on 2024-01-15

from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, VPC
from ibmdiagrams.ibmcloud.compute import VirtualServer

def create_base_infrastructure():
    with IBMCloud("IBM Cloud"):
        with VPC("production-vpc"):
            vsi = VirtualServer("web-server")
    return vsi

# infrastructure_custom.py (custom additions)
from infrastructure_base import create_base_infrastructure
from ibmdiagrams.ibmcloud.actors import User
from ibmdiagrams.ibmcloud.observability import CloudLogs

with Diagram("infrastructure-complete"):
    user = User("End User")
    vsi = create_base_infrastructure()
    logs = CloudLogs("Application Logs")
```

### 3. Document Customizations

```python
"""
Infrastructure Diagram

Generated from: production.tfstate
Generated on: 2024-01-15
Last updated: 2024-01-20

Customizations:
- Added user actors for external access
- Enhanced labels with instance profiles
- Added observability components
- Changed layout to vertical (TB)
- Added security group annotations
"""

from ibmdiagrams.ibmcloud.diagram import Diagram
# ... rest of code
```

### 4. Create Makefile for Automation

```makefile
# Makefile

.PHONY: generate-python generate-diagram update-all

# Generate Python from Terraform
generate-python:
	terraform show -json > infrastructure.tfstate
	ibmdiagrams --python infrastructure.tfstate
	@echo "Generated infrastructure.py"

# Generate diagram from Python
generate-diagram:
	python infrastructure.py
	@echo "Generated infrastructure.drawio"

# Update everything
update-all: generate-python generate-diagram
	@echo "Updated all diagrams"

# Clean generated files
clean:
	rm -f infrastructure.tfstate infrastructure.drawio
```

Usage:
```bash
make generate-python  # Generate Python from Terraform
make generate-diagram  # Generate diagram from Python
make update-all       # Do both
```

## Troubleshooting

### Issue: Generated Code Has Errors

**Problem**: Python code doesn't run

**Solution**:
```bash
# Check Python syntax
python -m py_compile infrastructure.py

# Run with verbose output
python -v infrastructure.py

# Check imports
python -c "from ibmdiagrams.ibmcloud.diagram import Diagram"
```

### Issue: Missing Resources

**Problem**: Some Terraform resources not in Python code

**Solution**:
1. Check if resource type is supported
2. Verify resource is in state file:
   ```bash
   terraform state list
   ```
3. Add manually if needed:
   ```python
   # Add missing resource
   from ibmdiagrams.ibmcloud.storage import ObjectStorage
   cos = ObjectStorage("Backup Bucket")
   ```

### Issue: Layout Doesn't Look Right

**Problem**: Generated layout is not optimal

**Solution**:
```python
# Try different directions
with Diagram("infrastructure", direction="TB"):  # Top to Bottom
    pass

with Diagram("infrastructure", direction="LR"):  # Left to Right
    pass

# Adjust individual container directions
with VPC("production-vpc", direction="TB"):
    with Zone("Zone 1", direction="LR"):
        pass
```

## Related Examples

- [Terraform Custom Labels](terraform-custom-labels.md) - Direct Terraform to DrawIO
- [Terraform General Labels](terraform-general-labels.md) - Simplified diagrams
- [Simple VPC](../python/simple-vpc.md) - Pure diagram-as-code approach

## Next Steps

1. **Generate Python code**: Use `--python` flag with your Terraform state
2. **Customize**: Edit the generated Python file
3. **Create templates**: Generalize for reuse
4. **Automate**: Set up scripts to regenerate as needed
5. **Share**: Version control your diagram code

## License

This application is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).