# SLZ VSI Terraform Example

Generate a comprehensive Secure Landing Zone (SLZ) architecture diagram from Terraform state, featuring multi-zone VPCs, VPN gateway, Virtual Private Endpoints, and cloud services.

## Architecture Overview

This example demonstrates a complete IBM Cloud Secure Landing Zone for VSI (Virtual Server Instance) deployment with:

### Management VPC
- **3 Availability Zones** (us-south-1, us-south-2, us-south-3)
- **VPE Subnets** in each zone for Virtual Private Endpoints
- **VPN Subnet** in Zone 1 with VPN Gateway
- **VSI Subnets** in each zone with Management Virtual Servers

### Workload VPC
- **3 Availability Zones** (us-south-1, us-south-2, us-south-3)
- **VPE Subnets** in each zone for Virtual Private Endpoints
- **VSI Subnets** in each zone with Workload Virtual Servers

### Cloud Services
- **Transit Gateway** for VPC interconnection
- **Cloud Logs** for centralized logging
- **Flow Logs** for Management and Workload VPCs
- **Object Storage** buckets (Logs, Management, Workload)
- **Key Protect** encryption keys (Log, ROKS, SLZ, VSI Volume)

## Diagram

![SLZ VSI Terraform Diagram](slzvsi-terraform.drawio.svg)

## Generate Diagram

### Prerequisites

- IBM Diagrams installed ([Setup Guide](../../setup.md))
- Terraform state file (provided: `slzvsi.tfstate`)

### Generate with Custom Labels (Default)

```bash
# Navigate to terraform examples directory
cd docs/examples/terraform

# Generate diagram with detailed labels
ibmdiagrams slzvsi.tfstate

# Output: slzvsi.drawio
```

**Shows:**
- Resource names (e.g., "Management VPC", "Workload VPC")
- IP addresses (e.g., "10.10.40.4")
- CIDR blocks (e.g., "10.10.20.0/24")
- All resource details

### Generate with General Labels

```bash
# Generate simplified diagram
ibmdiagrams --general slzvsi.tfstate

# Output: slzvsi.drawio
```

**Shows:**
- Generic resource types only (e.g., "VPC", "Virtual Server")
- No specific names or IPs
- Clean architecture overview

### Generate Python Code

```bash
# Convert to editable Python code
ibmdiagrams --python slzvsi.tfstate

# Output: slzvsi.py (editable)
```

Then customize and run:
```bash
# Edit the generated Python file
vim slzvsi.py

# Generate diagram from Python
python slzvsi.py

# Output: slzvsi.drawio
```

## Architecture Details

### Network Configuration

| Component | CIDR Block | Purpose |
|-----------|------------|---------|
| **Management VPC - Zone 1** | 10.24.0.0/18 | Management zone 1 |
| **Management VPC - Zone 2** | 10.240.64.0/18 | Management zone 2 |
| **Management VPC - Zone 3** | 10.240.128.0/18 | Management zone 3 |
| **Workload VPC - Zone 1** | 10.240.0.0/24 | Workload zone 1 |
| **Workload VPC - Zone 2** | 10.240.64.0/24 | Workload zone 2 |
| **Workload VPC - Zone 3** | 10.240.128.0/24 | Workload zone 3 |

### Management VPC Subnets

| Zone | Subnet Type | CIDR | IP Address |
|------|-------------|------|------------|
| Zone 1 | VPE Subnet | 10.10.20.0/24 | 10.10.20.4 |
| Zone 1 | VPN Subnet | 10.10.30.0/24 | - |
| Zone 1 | VSI Subnet | 10.10.40.0/24 | 10.10.40.4 |
| Zone 2 | VPE Subnet | 10.20.20.0/24 | 10.20.20.4 |
| Zone 2 | VSI Subnet | 10.20.30.0/24 | 10.20.30.4 |
| Zone 3 | VPE Subnet | 10.30.20.0/24 | 10.30.20.4 |
| Zone 3 | VSI Subnet | 10.30.30.0/24 | 10.30.30.4 |

### Workload VPC Subnets

| Zone | Subnet Type | CIDR | IP Address |
|------|-------------|------|------------|
| Zone 1 | VPE Subnet | 10.40.20.0/24 | 10.40.20.4 |
| Zone 1 | VSI Subnet | 10.40.30.0/24 | 10.40.30.4 |
| Zone 2 | VPE Subnet | 10.50.20.0/24 | 10.50.20.4 |
| Zone 2 | VSI Subnet | 10.50.30.0/24 | 10.50.30.4 |
| Zone 3 | VPE Subnet | 10.60.20.0/24 | 10.60.20.4 |
| Zone 3 | VSI Subnet | 10.60.30.0/24 | 10.60.30.4 |

### Resource Groups

- **Management RG**: Contains Management VPC and related resources
- **Workload RG**: Contains Workload VPC and related resources
- **Services RG**: Contains shared cloud services (Transit Gateway, Cloud Logs, Object Storage, Key Protect)

### Security & Connectivity

- **VPN Gateway**: Secure remote access in Management VPC Zone 1
- **Virtual Private Endpoints (VPE)**: Private connectivity to IBM Cloud services in all zones
- **Transit Gateway**: Connects Management and Workload VPCs
- **Flow Logs**: Network traffic monitoring for both VPCs

### Observability & Storage

- **Cloud Logs**: Centralized logging service
- **Flow Logs**: Separate collectors for Management and Workload VPCs
- **Object Storage Buckets**:
  - Logs Bucket: Flow logs storage
  - Mgmt Bucket: Management VPC data
  - Workload Bucket: Workload VPC data

### Encryption

- **Key Protect Keys**:
  - Log Key: Encrypts logging data
  - ROKS Key: Kubernetes cluster encryption
  - SLZ Key: Landing zone encryption
  - VSI Volume Key: Virtual server volume encryption

## Use Cases

### 1. Documentation

```bash
# Generate detailed diagram for internal documentation
ibmdiagrams slzvsi.tfstate -output ./docs/architecture

# Result: Complete infrastructure documentation
```

### 2. Compliance Audits

```bash
# Generate diagram showing all security controls
ibmdiagrams slzvsi.tfstate

# Shows: VPN, VPEs, encryption keys, flow logs, etc.
```

### 3. Architecture Presentations

```bash
# Generate simplified diagram for stakeholders
ibmdiagrams --general slzvsi.tfstate -output ./presentations

# Result: Clean, high-level architecture overview
```

### 4. Template Creation

```bash
# Convert to Python for customization
ibmdiagrams --python slzvsi.tfstate

# Edit slzvsi.py to create reusable template
# Use for new landing zone deployments
```

## Comparison with Python Example

This Terraform state file generates a diagram equivalent to the [Python SLZ VSI example](../python/slzvsi.md).

| Aspect | Terraform Approach | Python Approach |
|--------|-------------------|-----------------|
| **Input** | Terraform state file | Python code |
| **Source** | Existing infrastructure | Manual coding |
| **Labels** | Actual resource names/IPs | Custom labels |
| **Use Case** | Document existing | Plan new architecture |
| **Flexibility** | Fixed (from state) | Fully customizable |
| **Speed** | Instant generation | Requires coding |

## Advanced Options

### Custom Output Directory

```bash
ibmdiagrams slzvsi.tfstate -output ./architecture-docs
# Output: ./architecture-docs/slzvsi.drawio
```

### Custom Font (for global variants)

```bash
ibmdiagrams slzvsi.tfstate -font "IBM Plex Sans JP"
# Uses Japanese font variant
```

### Combine Options

```bash
ibmdiagrams --general slzvsi.tfstate -output ./presentations -font "IBM Plex Sans KR"
# Korean font + simplified labels + custom output
```

## Terraform State File Structure

The `slzvsi.tfstate` file contains:

- **3 Resource Groups**: Management, Workload, Services
- **2 VPCs**: Management VPC, Workload VPC
- **18 Subnets**: 9 per VPC (3 zones × 3 subnet types)
- **6 Virtual Servers**: 3 Management + 3 Workload
- **12 Virtual Private Endpoints**: 6 per VPC (2 per zone)
- **1 VPN Gateway**: In Management VPC Zone 1
- **1 Transit Gateway**: Connecting both VPCs
- **1 Cloud Logs Instance**: Centralized logging
- **2 Flow Log Collectors**: One per VPC
- **3 Object Storage Buckets**: Logs, Management, Workload
- **4 Key Protect Keys**: Log, ROKS, SLZ, VSI Volume

## Related Examples

- [Python SLZ VSI](../python/slzvsi.md) - Equivalent diagram-as-code approach
- [Terraform Custom Labels](terraform-custom-labels.md) - Detailed labeling guide
- [Terraform General Labels](terraform-general-labels.md) - Simplified diagrams
- [Terraform to Python](terraform-to-python.md) - Convert for customization

## Next Steps

1. **Generate the diagram**: Run `ibmdiagrams slzvsi.tfstate`
2. **Open in draw.io**: View and edit the generated diagram
3. **Customize**: Use `--python` flag to create editable code
4. **Integrate**: Add to your documentation or CI/CD pipeline

## Troubleshooting

### Issue: Diagram is too complex

**Solution**: Use general labels for simplified view
```bash
ibmdiagrams --general slzvsi.tfstate
```

### Issue: Need to customize labels

**Solution**: Convert to Python and edit
```bash
ibmdiagrams --python slzvsi.tfstate
vim slzvsi.py
python slzvsi.py
```

### Issue: Missing resources in diagram

**Solution**: Verify Terraform state is complete
```bash
# Check state file
cat slzvsi.tfstate | jq '.resources[].type' | sort | uniq
```

## License

This application is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).