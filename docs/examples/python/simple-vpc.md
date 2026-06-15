# Simple VPC Example

A basic VPC architecture demonstrating fundamental IBM Cloud infrastructure components.

## Architecture Overview

This example creates a simple production VPC with:
- **Region**: Dallas
- **Availability Zones**: 1
- **Subnets**: 2 (Web tier and App tier)
- **Virtual Servers**: 2 (one per subnet)
- **Network**: Public Gateway and Application Load Balancer
- **Security**: Security Groups for each tier

## Diagram

![Simple VPC Diagram](simple-vpc.drawio.svg)

## Use Case

Perfect for:
- Learning IBM Diagrams basics
- Small production workloads
- Development environments
- Proof of concept deployments

## Python Code

[View Source Code](simple-vpc.py)

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet, SecurityGroup
from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.network import PublicGateway, ApplicationLoadBalancer

with Diagram("simple-vpc"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas", direction="TB"):
            with VPC("Production VPC"):
                # Public gateway for internet access
                pgw = PublicGateway("Public Gateway")
                
                # Application load balancer
                alb = ApplicationLoadBalancer("App Load Balancer")
                
                with Zone("Zone 1", "10.10.0.0/18", direction="TB"):
                    # Web tier subnet
                    with Subnet("Web Subnet", "10.10.10.0/24"):
                        with SecurityGroup("Web Security Group"):
                            web = VirtualServer("Web Server", "10.10.10.4")
                    
                    # Application tier subnet
                    with Subnet("App Subnet", "10.10.20.0/24"):
                        with SecurityGroup("App Security Group"):
                            app = VirtualServer("App Server", "10.10.20.4")
```

## How to Run

### Prerequisites

- IBM Diagrams installed ([Setup Guide](../setup.md))
- Python 3.11+
- draw.io Desktop

### Steps

1. **Save the code** to `simple-vpc.py`

2. **Run the script**:
   ```bash
   # Using uv
   uv run python simple-vpc.py
   
   # Using pip
   python simple-vpc.py
   ```

3. **Open the diagram**:
   ```bash
   # macOS
   open simple-vpc.drawio
   
   # Windows
   start simple-vpc.drawio
   
   # Linux
   xdg-open simple-vpc.drawio
   ```

## Architecture Details

### Network Configuration

| Component | CIDR Block | Purpose |
|-----------|------------|---------|
| **VPC** | - | Production VPC container |
| **Zone 1** | 10.10.0.0/18 | Availability zone (16,384 IPs) |
| **Web Subnet** | 10.10.10.0/24 | Web tier (256 IPs) |
| **App Subnet** | 10.10.20.0/24 | Application tier (256 IPs) |

### Resources

| Resource | Name | IP Address | Purpose |
|----------|------|------------|---------|
| **Public Gateway** | Public Gateway | - | Internet access for private subnets |
| **Load Balancer** | App Load Balancer | - | Distribute traffic to web servers |
| **Virtual Server** | Web Server | 10.10.10.4 | Web application frontend |
| **Virtual Server** | App Server | 10.10.20.4 | Application backend |

### Security Groups

- **Web Security Group**: Protects web tier
  - Inbound: HTTPS (443), HTTP (80)
  - Outbound: All traffic
  
- **App Security Group**: Protects application tier
  - Inbound: Application port (e.g., 8080) from web tier only
  - Outbound: Database access, external APIs

## Customization Ideas

### 1. Add Database Tier

```python
from ibmdiagrams.ibmcloud.data import PostgreSQL

with Subnet("DB Subnet", "10.10.30.0/24"):
    with SecurityGroup("DB Security Group"):
        db = PostgreSQL("Database", "10.10.30.4")
```

### 2. Add Multiple Zones for High Availability

```python
with Zone("Zone 2", "10.10.64.0/18", direction="TB"):
    with Subnet("Web Subnet", "10.10.74.0/24"):
        with SecurityGroup("Web Security Group"):
            web2 = VirtualServer("Web Server 2", "10.10.74.4")
```

### 3. Add Monitoring and Logging

```python
from ibmdiagrams.ibmcloud.observability import CloudLogs, Monitoring

logs = CloudLogs("Application Logs")
mon = Monitoring("Infrastructure Monitoring")
```

### 4. Add Object Storage

```python
from ibmdiagrams.ibmcloud.storage import ObjectStorage

cos = ObjectStorage("Static Assets")
```

## Related Examples

- [Multi-Tier Application](multi-tier-app.md) - Three-tier architecture with database
- [SLZ VSI](slzvsi.md) - Enterprise landing zone with multiple VPCs
- [High Availability](ha-vpc.md) - Multi-zone deployment with failover

## Next Steps

1. **Customize the diagram**: Modify the code to match your architecture
2. **Add more resources**: Explore other components in the [API Reference](../diagram-as-code.md#api-reference)
3. **Create variations**: Try different layouts with `direction="LR"` or `direction="TB"`
4. **Export to other formats**: Use draw.io to export as PNG, SVG, or PDF

## Troubleshooting

### Issue: Diagram doesn't open

**Solution**: Ensure draw.io Desktop is installed and set as the default application for `.drawio` files.

### Issue: Fonts look wrong

**Solution**: Install IBM Plex Sans fonts from [Google Fonts](https://fonts.google.com/?query=Plex).

### Issue: Layout is cramped

**Solution**: Try changing the direction parameter:
```python
with VPC("Production VPC", direction="LR"):  # Horizontal layout
```

## License

This application is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).