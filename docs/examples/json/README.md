# JSON to DrawIO (Internal Format)

Generate diagrams from IBM Diagrams' internal JSON format. This format is primarily for internal use and advanced integrations.

## Overview

IBM Diagrams supports an internal JSON format for diagram generation. This format is:
- **Not externally documented** - Internal use only
- **Subject to change** - No API stability guarantees
- **For advanced users** - Requires understanding of internal structure
- **For tool integration** - Building custom tools on top of IBM Diagrams

## ⚠️ Important Notice

> **This format is for internal use and is not officially supported for external consumption.**
> 
> - The JSON schema may change without notice
> - No backward compatibility guarantees
> - Limited documentation available
> - Use Python API or Terraform integration instead for production use

## Use Case

**Intended for:**
- 🔧 Internal IBM Diagrams development
- 🔧 Custom tool integration
- 🔧 Advanced automation scenarios
- 🔧 Experimental features

**Not recommended for:**
- ❌ Production documentation
- ❌ End-user applications
- ❌ Long-term storage
- ❌ External integrations

## Example Files

This directory contains example JSON files in the resource-based format:

- [`cloud.json`](cloud.json) - Simple VPC with subnet and instance

## Command

```bash
# Generate diagram from JSON file
ibmdiagrams docs/examples/json/cloud.json

# Output: cloud.drawio (created in current directory)
# Move to examples directory if needed:
# mv cloud.drawio docs/examples/json/
```

## JSON Structure (Actual Format)

The JSON format expects a resource-based structure with `vpcs`, `subnets`, and `instances` at the top level:

```json
{
  "vpcs": [
    {
      "name": "Production VPC",
      "id": "vpc-prod-001",
      "region": "us-south"
    }
  ],
  "subnets": [
    {
      "name": "Web Subnet",
      "id": "subnet-web-001",
      "subnet": "10.10.10.0/24",
      "vpcId": "vpc-prod-001",
      "availabilityZone": "us-south-1"
    }
  ],
  "instances": [
    {
      "name": "Web Server",
      "id": "instance-web-001",
      "vpcId": "vpc-prod-001",
      "availabilityZone": "us-south-1",
      "networkInterfaces": [
        {
          "networkId": "subnet-web-001",
          "ip": "10.10.10.4"
        }
      ]
    }
  ]
}
```

**Note:** The diagram structure format shown in earlier versions (with `"diagram"` and `"elements"` keys) is not implemented. The actual JSON loader expects the resource-based format shown above.

## Why Use Python or Terraform Instead

### Python API (Recommended)

**Advantages:**
- ✅ Officially supported
- ✅ Type checking
- ✅ IDE autocomplete
- ✅ Comprehensive documentation
- ✅ Stable API
- ✅ Version control friendly

**Example:**
```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC
from ibmdiagrams.ibmcloud.compute import VirtualServer

with Diagram("example"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC("Production VPC"):
                vsi = VirtualServer("Web Server")
```

### Terraform Integration (Recommended)

**Advantages:**
- ✅ Automatic generation from infrastructure
- ✅ Always up-to-date
- ✅ No manual maintenance
- ✅ Multiple output formats

**Example:**
```bash
terraform show -json > infrastructure.tfstate
ibmdiagrams infrastructure.tfstate
```

## When JSON Might Be Useful

### 1. Custom Tool Integration

If you're building a tool that generates diagrams:

```python
# Your custom tool
import json

def generate_diagram_json(infrastructure_data):
    """Convert your data format to IBM Diagrams JSON"""
    diagram = {
        "diagram": {
            "name": "generated-diagram",
            "elements": []
        }
    }
    
    # Transform your data
    for resource in infrastructure_data:
        element = transform_to_element(resource)
        diagram["diagram"]["elements"].append(element)
    
    return diagram

# Generate JSON
diagram_json = generate_diagram_json(my_data)

# Save to file
with open("diagram.json", "w") as f:
    json.dump(diagram_json, f, indent=2)

# Generate diagram
# ibmdiagrams diagram.json
```

### 2. Programmatic Diagram Generation

If you need to generate diagrams programmatically from non-Terraform sources:

```python
import json
import subprocess

def create_diagram_from_api(api_data):
    """Generate diagram from API response"""
    
    # Transform API data to JSON format
    diagram_json = transform_api_to_json(api_data)
    
    # Save JSON
    with open("api-diagram.json", "w") as f:
        json.dump(diagram_json, f)
    
    # Generate diagram
    subprocess.run(["ibmdiagrams", "api-diagram.json"])
    
    return "api-diagram.drawio"
```

### 3. Batch Processing

For processing multiple diagrams:

```python
import json
import os

def batch_generate_diagrams(json_files):
    """Generate diagrams from multiple JSON files"""
    for json_file in json_files:
        # Validate JSON
        with open(json_file) as f:
            data = json.load(f)
        
        # Generate diagram
        os.system(f"ibmdiagrams {json_file}")
        
        print(f"Generated {json_file.replace('.json', '.drawio')}")

# Usage
json_files = ["diagram1.json", "diagram2.json", "diagram3.json"]
batch_generate_diagrams(json_files)
```

## Alternatives to JSON

### Alternative 1: Python API with Data

Instead of JSON, use Python with your data:

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, VPC
from ibmdiagrams.ibmcloud.compute import VirtualServer

# Your data (from API, database, etc.)
infrastructure = {
    "vpcs": [
        {
            "name": "production-vpc",
            "servers": [
                {"name": "web-1", "ip": "10.10.10.4"},
                {"name": "web-2", "ip": "10.10.10.5"}
            ]
        }
    ]
}

# Generate diagram from data
with Diagram("infrastructure"):
    with IBMCloud("IBM Cloud"):
        for vpc_data in infrastructure["vpcs"]:
            with VPC(vpc_data["name"]):
                for server in vpc_data["servers"]:
                    VirtualServer(server["name"], server["ip"])
```

### Alternative 2: Template-Based Generation

Use Python templates:

```python
def generate_vpc_diagram(vpc_config):
    """Generate VPC diagram from configuration"""
    from ibmdiagrams.ibmcloud.diagram import Diagram
    from ibmdiagrams.ibmcloud.groups import IBMCloud, VPC, Zone, Subnet
    from ibmdiagrams.ibmcloud.compute import VirtualServer
    
    with Diagram(vpc_config["name"]):
        with IBMCloud("IBM Cloud"):
            with VPC(vpc_config["vpc_name"]):
                for zone in vpc_config["zones"]:
                    with Zone(zone["name"], zone["cidr"]):
                        for subnet in zone["subnets"]:
                            with Subnet(subnet["name"], subnet["cidr"]):
                                for server in subnet["servers"]:
                                    VirtualServer(server["name"], server["ip"])

# Use the template
config = {
    "name": "my-infrastructure",
    "vpc_name": "production-vpc",
    "zones": [
        {
            "name": "Zone 1",
            "cidr": "10.10.0.0/18",
            "subnets": [
                {
                    "name": "Web Subnet",
                    "cidr": "10.10.10.0/24",
                    "servers": [
                        {"name": "web-1", "ip": "10.10.10.4"}
                    ]
                }
            ]
        }
    ]
}

generate_vpc_diagram(config)
```

## Best Practices

### 1. Use Supported Methods First

```bash
# ✅ Recommended: Python API
python my-diagram.py

# ✅ Recommended: Terraform
ibmdiagrams infrastructure.tfstate

# ⚠️ Use with caution: JSON
ibmdiagrams diagram.json
```

### 2. Document JSON Usage

If you must use JSON, document it:

```python
"""
Custom Diagram Generator

This tool generates IBM Diagrams JSON format from our internal
infrastructure database.

WARNING: Uses internal JSON format which may change.
Fallback: Can generate Python code instead if JSON format changes.

Last tested with: ibmdiagrams v3.1.10
"""
```

### 3. Have a Fallback Plan

```python
def generate_diagram(data, use_json=False):
    """Generate diagram with fallback"""
    if use_json:
        try:
            # Try JSON method
            json_data = convert_to_json(data)
            save_json(json_data)
            run_ibmdiagrams_json()
        except Exception as e:
            print(f"JSON method failed: {e}")
            print("Falling back to Python API")
            use_json = False
    
    if not use_json:
        # Fallback to Python API
        generate_with_python_api(data)
```

## Getting Help

If you need to use the JSON format for a specific use case:

1. **Check if Python API can solve it**: Most use cases are better served by the Python API
2. **Consider Terraform**: If you're documenting infrastructure
3. **Open an issue**: Describe your use case - there might be a better way
4. **Contact maintainers**: For internal IBM use cases

## Related Documentation

- [Diagram as Code](../diagram-as-code.md) - Python API (recommended)
- [Terraform Integration](../terraform.md) - Terraform to diagrams (recommended)
- [Simple VPC Example](../python/simple-vpc.md) - Python API example
- [Terraform to Python](../terraform/terraform-to-python.md) - Convert Terraform to Python

## Summary

**Key Takeaways:**

1. ✅ **Use Python API** for diagram-as-code
2. ✅ **Use Terraform integration** for infrastructure documentation
3. ⚠️ **JSON format is internal** - not recommended for external use
4. 🔧 **JSON might be useful** for custom tool integration
5. 📚 **Better alternatives exist** for most use cases

**Recommended Approach:**

```bash
# For new diagrams
python my-diagram.py

# For existing infrastructure
ibmdiagrams infrastructure.tfstate

# For customization
ibmdiagrams --python infrastructure.tfstate
# Edit the generated Python file
python infrastructure.py
```

## License

This application is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).