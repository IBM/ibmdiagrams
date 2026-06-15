# Diagram as Code

Create IBM-standard architecture diagrams using Python code. This approach enables version control, rapid iteration, and consistent styling across your infrastructure documentation.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Basic Concepts](#basic-concepts)
3. [API Reference](#api-reference)
4. [Examples](#examples)
5. [Best Practices](#best-practices)
6. [Advanced Techniques](#advanced-techniques)

---

## Overview

### Why Diagram as Code?

**Traditional Diagramming:**
- ❌ Manual positioning of elements
- ❌ Inconsistent styling
- ❌ Difficult to version control
- ❌ Time-consuming updates

**Diagram as Code:**
- ✅ Automatic layout and positioning
- ✅ IBM Design Language compliance
- ✅ Git-friendly text format
- ✅ Quick iterations and updates

### How It Works

```python
# 1. Import components
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, VPC
from ibmdiagrams.ibmcloud.compute import VirtualServer

# 2. Use context managers to define hierarchy
with Diagram("my-architecture"):
    with IBMCloud("IBM Cloud"):
        with VPC("Production VPC"):
            vsi = VirtualServer("Web Server")

# 3. Run the script
# python my-architecture.py
# Output: my-architecture.drawio
```

---

## Basic Concepts

### Context Manager Pattern

IBM Diagrams uses Python's `with` statement to define hierarchical relationships:

```python
with Parent("Parent Name"):
    with Child("Child Name"):
        grandchild = GrandChild("GrandChild Name")
```

This creates a visual hierarchy where:
- Child is **inside** Parent
- GrandChild is **inside** Child

### Shape Types

| Type | Purpose | Example |
|------|---------|---------|
| **Groups** | Containers (deployedOn) | VPC, Subnet, SecurityGroup |
| **Zones** | Logical groupings (deployedTo) | Zone, Region |
| **Nodes** | Standalone resources | VirtualServer, LoadBalancer |
| **Actors** | Users and external entities | User, Application |

### Direction Control

Control layout direction with the `direction` parameter:

```python
# Horizontal layout (default)
with VPC("My VPC", direction="LR"):  # Left to Right
    pass

# Vertical layout
with VPC("My VPC", direction="TB"):  # Top to Bottom
    pass
```

---

## API Reference

### Diagram

The root container for all diagrams.

```python
from ibmdiagrams.ibmcloud.diagram import Diagram

with Diagram(
    name="diagram-name",      # Required: Output filename (without .drawio)
    filename="custom-name",   # Optional: Override output filename
    output="./output",        # Optional: Output directory
    direction="LR",           # Optional: "LR" (default) or "TB"
    font="IBM Plex Sans"      # Optional: Font family
):
    pass
```

**Example:**
```python
with Diagram("my-architecture", direction="TB", output="./diagrams"):
    # Your diagram code here
    pass
# Output: ./diagrams/my-architecture.drawio
```

---

### Groups (Containers)

Groups represent "deployedOn" relationships and act as containers.

#### Core Groups

```python
from ibmdiagrams.ibmcloud.groups import (
    IBMCloud,           # Top-level IBM Cloud container
    Region,             # Geographic region
    VPC,                # Virtual Private Cloud
    Zone,               # Availability zone
    Subnet,             # Network subnet
    SecurityGroup,      # Security group
    ResourceGroup,      # Resource group
    CloudServices,      # Cloud services container
)

# Usage
with IBMCloud("IBM Cloud"):
    with Region("Dallas", direction="TB"):
        with VPC("Production VPC"):
            with Zone("Zone 1", "10.10.0.0/18"):
                with Subnet("App Subnet", "10.10.10.0/24"):
                    pass
```

**Parameters:**
- `label`: Primary label (SemiBold font)
- `sublabel`: Secondary label (Regular font) - often used for CIDR blocks
- `direction`: Layout direction ("LR" or "TB")
- `fontname`: Font family (default: "IBM Plex Sans")
- `fontsize`: Font size (default: 14)

#### Additional Groups

```python
from ibmdiagrams.ibmcloud.groups import (
    Enterprise,              # Enterprise container
    PublicNetwork,          # Public network
    EnterpriseNetwork,      # Enterprise network
    ClassicInfrastructure,  # Classic infrastructure
    PowerWorkspace,         # Power workspace
    LayoutGroup,            # Generic layout container
)
```

#### Expanded Shapes

Expanded shapes show detailed information:

```python
from ibmdiagrams.ibmcloud.groups import (
    ExpandedVirtualServer,
    ExpandedBareMetalServer,
    ExpandedPowerVirtualServer,
)

with ExpandedVirtualServer(
    label="Web Server",
    sublabel="Type: Dedicated<br>OS: Ubuntu 22.04<br>Profile: bx2-4x16<br>vCPU: 4<br>RAM: 16GiB"
):
    pass
```

---

### Compute Resources

```python
from ibmdiagrams.ibmcloud.compute import (
    VirtualServer,           # VPC virtual server
    PowerVirtualServer,      # Power virtual server
    BareMetalServer,         # Bare metal server
    ClassicVirtualServer,    # Classic virtual server
    DedicatedHost,           # Dedicated host
    ImageService,            # Image service
    Satellite,               # Satellite
)

# Usage
vsi = VirtualServer(
    label="Web Server",
    sublabel="10.10.10.4"
)

power = PowerVirtualServer(
    label="SAP HANA",
    sublabel="192.168.1.10"
)
```

---

### Network Components

```python
from ibmdiagrams.ibmcloud.network import (
    # Load Balancers
    LoadBalancer,
    ApplicationLoadBalancer,
    NetworkLoadBalancer,
    ClassicLoadBalancer,
    GlobalLoadBalancer,
    
    # Gateways
    PublicGateway,
    VPNGateway,
    EndpointGateway,
    TransitGateway,
    
    # Connectivity
    DirectLinkConnect,
    DirectLinkDedicated,
    
    # Other
    Internet,
    Router,
    DNSServices,
    VLAN,
)

# Usage
pgw = PublicGateway("Public Gateway")
alb = ApplicationLoadBalancer("App LB", "10.10.10.5")
tgw = TransitGateway("Transit Gateway")
```

---

### Security Services

```python
from ibmdiagrams.ibmcloud.security import (
    KeyProtect,              # Key Protect
    SecretsManager,          # Secrets Manager
    SecurityGroup,           # Security group
    VPNGateway,             # VPN gateway
    VPNConnection,          # VPN connection
    AppID,                  # App ID
    SecurityComplianceCenter, # Security & Compliance Center
)

# Usage
kp = KeyProtect("Encryption Keys")
sm = SecretsManager("API Keys")
vpn = VPNGateway("Site-to-Site VPN")
```

---

### Storage Services

```python
from ibmdiagrams.ibmcloud.storage import (
    ObjectStorage,           # Cloud Object Storage
    BlockStorage,            # Block Storage
    BlockStorageSnapshots,   # Block Storage Snapshots
    CloudBackup,             # Cloud Backup
)

# Usage
cos = ObjectStorage("Logs Bucket")
block = BlockStorage("Data Volume", "500GB")
```

---

### Observability

```python
from ibmdiagrams.ibmcloud.observability import (
    CloudLogs,              # Cloud Logs
    FlowLogs,               # Flow Logs
    Monitoring,             # Monitoring
)

# Usage
logs = CloudLogs("Application Logs")
flow = FlowLogs("VPC Flow Logs")
mon = Monitoring("Metrics")
```

---

### Data Services

```python
from ibmdiagrams.ibmcloud.data import (
    Database,               # Generic database
    DB2,                    # DB2
    DB2Warehouse,          # DB2 Warehouse
    PostgreSQL,            # PostgreSQL
    MySQL,                 # MySQL
    Redis,                 # Redis
    Cloudant,              # Cloudant
    EventStreams,          # Event Streams
)

# Usage
db = PostgreSQL("User Database", "10.10.20.5")
cache = Redis("Session Cache")
```

---

### Containers & Kubernetes

```python
from ibmdiagrams.ibmcloud.containers import (
    KubernetesService,      # IBM Kubernetes Service
    OpenShift,              # Red Hat OpenShift
    CodeEngine,             # Code Engine
    ContainerRegistry,      # Container Registry
)

# Usage
iks = KubernetesService("Production Cluster")
ocp = OpenShift("Dev Cluster")
```

---

### AI & Watson

```python
from ibmdiagrams.ibmcloud.ai import (
    WatsonX,                # watsonx
    WatsonXAI,             # watsonx.ai
    WatsonXData,           # watsonx.data
    WatsonXGovernance,     # watsonx.governance
    WatsonAssistant,       # Watson Assistant
    WatsonDiscovery,       # Watson Discovery
)

# Usage
wx = WatsonX("watsonx Platform")
assistant = WatsonAssistant("Customer Support Bot")
```

---

### Actors

```python
from ibmdiagrams.ibmcloud.actors import (
    User,                   # User
    Users,                  # Multiple users
    Application,            # Application
    Microservice,          # Microservice
)

# Usage
user = User("End User")
app = Application("Mobile App")
```

---

### Connectors

```python
from ibmdiagrams.ibmcloud.connectors import (
    SolidEdge,             # Solid line
    PrivateSolidEdge,      # Private solid line
    PublicSolidEdge,       # Public solid line
    DashedEdge,            # Dashed line
    DottedEdge,            # Dotted line
    DoubleEdge,            # Double line
    TunnelEdge,            # Tunnel line
)

# Usage
from ibmdiagrams.ibmcloud.connectors import SolidEdge

# Connect two resources
SolidEdge(source, target, label="HTTPS")

# With custom arrows
SolidEdge(
    source, 
    target,
    label="API Call",
    startarrow="circle",
    endarrow="arrow"
)
```

**Arrow Types:**
- `""` - No arrow
- `"arrow"` - Filled arrow (default)
- `"openarrow"` - Open arrow
- `"circle"` - Filled circle
- `"opencircle"` - Open circle
- `"diamond"` - Filled diamond
- `"opendiamond"` - Open diamond

---

## Examples

### Example 1: Simple VPC

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet
from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.network import PublicGateway

with Diagram("simple-vpc"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC("Production VPC"):
                pgw = PublicGateway("Public Gateway")
                
                with Zone("Zone 1", "10.10.0.0/18"):
                    with Subnet("Web Subnet", "10.10.10.0/24"):
                        web = VirtualServer("Web Server", "10.10.10.4")
```

[🔗 See full example](examples/python/simple-vpc.md)

---

### Example 2: Multi-Tier Application

```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet
from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.network import ApplicationLoadBalancer
from ibmdiagrams.ibmcloud.data import PostgreSQL

with Diagram("multi-tier-app", direction="TB"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC("Application VPC"):
                alb = ApplicationLoadBalancer("App LB")
                
                with Zone("Zone 1", "10.10.0.0/18", direction="TB"):
                    with Subnet("Web Subnet", "10.10.10.0/24"):
                        web1 = VirtualServer("Web-1", "10.10.10.4")
                    
                    with Subnet("App Subnet", "10.10.20.0/24"):
                        app1 = VirtualServer("App-1", "10.10.20.4")
                    
                    with Subnet("DB Subnet", "10.10.30.0/24"):
                        db1 = PostgreSQL("Primary DB", "10.10.30.4")
                
                with Zone("Zone 2", "10.10.64.0/18", direction="TB"):
                    with Subnet("Web Subnet", "10.10.74.0/24"):
                        web2 = VirtualServer("Web-2", "10.10.74.4")
                    
                    with Subnet("App Subnet", "10.10.84.0/24"):
                        app2 = VirtualServer("App-2", "10.10.84.4")
                    
                    with Subnet("DB Subnet", "10.10.94.0/24"):
                        db2 = PostgreSQL("Standby DB", "10.10.94.4")
```

---

### Example 3: Enterprise Landing Zone

See our comprehensive [VSI on VPC Landing Zone](examples/python/slzvsi.md) example featuring:
- Multi-zone deployment across 3 availability zones
- Management and workload VPCs
- VPN and VPE configuration
- Cloud services integration (logs, monitoring, storage)
- Security services (Key Protect)

![SLZ VSI Example](examples/python/slzvsi.drawio.svg)

---

## Best Practices

### 1. Use Meaningful Names

```python
# ❌ Bad
with VPC("vpc1"):
    with Subnet("sub1", "10.0.0.0/24"):
        v = VirtualServer("v1")

# ✅ Good
with VPC("Production VPC"):
    with Subnet("Web Tier Subnet", "10.10.10.0/24"):
        web_server = VirtualServer("Web Server", "10.10.10.4")
```

### 2. Use Sublabels for Technical Details

```python
# ✅ Good - Use sublabels for IPs, CIDRs, specs
zone = Zone("Zone 1", "10.10.0.0/18")
subnet = Subnet("App Subnet", "10.10.20.0/24")
vsi = VirtualServer("Web Server", "10.10.10.4")

# ✅ Good - Multi-line sublabels
vsi = VirtualServer(
    label="Database Server",
    sublabel="10.10.30.4<br>Ubuntu 22.04<br>4vCPU, 16GB RAM"
)
```

### 3. Choose Appropriate Direction

```python
# Horizontal for wide diagrams
with Region("Dallas", direction="LR"):
    with VPC("VPC-A"):
        pass
    with VPC("VPC-B"):
        pass

# Vertical for deep hierarchies
with VPC("Production VPC", direction="TB"):
    with Zone("Zone 1", direction="TB"):
        with Subnet("Subnet 1"):
            pass
        with Subnet("Subnet 2"):
            pass
```

### 4. Group Related Resources

```python
# ✅ Good - Use ResourceGroup or LayoutGroup
with ResourceGroup("Web Tier"):
    with Subnet("Web Subnet"):
        web1 = VirtualServer("Web-1")
        web2 = VirtualServer("Web-2")
        alb = ApplicationLoadBalancer("Web LB")
```

### 5. Keep It Simple

```python
# ❌ Too complex - hard to read
with IBMCloud("IBM Cloud"):
    with Region("Dallas"):
        with ResourceGroup("RG1"):
            with VPC("VPC1"):
                with Zone("Z1"):
                    with Subnet("S1"):
                        with SecurityGroup("SG1"):
                            vsi = VirtualServer("VSI1")

# ✅ Better - flatten where possible
with IBMCloud("IBM Cloud"):
    with Region("Dallas"):
        with VPC("Production VPC"):
            with Zone("Zone 1", "10.10.0.0/18"):
                with Subnet("App Subnet", "10.10.10.0/24"):
                    vsi = VirtualServer("App Server", "10.10.10.4")
```

### 6. Use Variables for Reusable Components

```python
# ✅ Good - Define reusable components
def create_web_tier(zone_name, subnet_cidr, ip_base):
    with Zone(zone_name, direction="TB"):
        with Subnet("Web Subnet", subnet_cidr):
            return VirtualServer("Web Server", ip_base)

with Diagram("scalable-app"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC("Production VPC"):
                web1 = create_web_tier("Zone 1", "10.10.10.0/24", "10.10.10.4")
                web2 = create_web_tier("Zone 2", "10.10.20.0/24", "10.10.20.4")
```

---

## Advanced Techniques

### Custom Fonts

Use IBM Plex Sans global variants:

```python
# Japanese
with Diagram("my-diagram", font="IBM Plex Sans JP"):
    pass

# Korean
with Diagram("my-diagram", font="IBM Plex Sans KR"):
    pass

# Arabic
with Diagram("my-diagram", font="IBM Plex Sans Arabic"):
    pass
```

### Multi-line Labels

Use `<br>` tags for multi-line labels:

```python
# Multi-line primary label
vsi = VirtualServer("Web Server<br>Production")

# Multi-line sublabel
vsi = VirtualServer(
    label="Database Server",
    sublabel="10.10.30.4<br>PostgreSQL 15<br>Primary Instance"
)

# Multiple services in one shape
services = ObjectStorage("Logs Bucket<br>Backup Bucket<br>Archive Bucket")
```

### Conditional Diagrams

```python
ENVIRONMENT = "production"  # or "development"

with Diagram(f"{ENVIRONMENT}-architecture"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC(f"{ENVIRONMENT.title()} VPC"):
                if ENVIRONMENT == "production":
                    # Production has 3 zones
                    for i in range(1, 4):
                        with Zone(f"Zone {i}"):
                            with Subnet(f"Subnet {i}"):
                                VirtualServer(f"Server-{i}")
                else:
                    # Development has 1 zone
                    with Zone("Zone 1"):
                        with Subnet("Dev Subnet"):
                            VirtualServer("Dev Server")
```

### Parameterized Diagrams

```python
def create_vpc_diagram(name, zones, subnets_per_zone):
    with Diagram(name):
        with IBMCloud("IBM Cloud"):
            with Region("Dallas"):
                with VPC(f"{name} VPC"):
                    for z in range(1, zones + 1):
                        with Zone(f"Zone {z}", f"10.{z}0.0.0/18"):
                            for s in range(1, subnets_per_zone + 1):
                                with Subnet(f"Subnet {s}", f"10.{z}{s}.0.0/24"):
                                    VirtualServer(f"VSI-{z}-{s}")

# Generate different architectures
create_vpc_diagram("small", zones=1, subnets_per_zone=2)
create_vpc_diagram("large", zones=3, subnets_per_zone=3)
```

### Getting XML String Output (No File Writing)

Generate diagrams as XML strings without writing to files - useful for APIs, databases, and dynamic generation:

```python
from ibmdiagrams import _data, _savediagrams
from ibmdiagrams.ibmbase.build import Build
from ibmdiagrams.ibmbase.common import Common
from ibmdiagrams.ibmcloud.diagram import Diagram

# Create diagram with filename="*" to prevent file writing
with Diagram("my-diagram", filename="*"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC("Production VPC"):
                vsi = VirtualServer("Web Server")

# Get XML string after diagram creation
common = Common()
common.setInputPython()
build = Build(common, _data)

if "my-diagram" in _savediagrams:
    xmldata = _savediagrams["my-diagram"]
    xml_string = build.getXMLString(xmldata, "my-diagram")
    
    # Use xml_string for:
    # - HTTP API responses
    # - Database storage
    # - In-memory processing
    # - Streaming to clients
```

**See:** [XML String Output Example](examples/python/xml-string-output.md) for complete documentation and use cases.

---

## Limitations

### Group Spanning

Diagram-as-code cannot represent groups spanning other groups:

```python
# ❌ Cannot do: Same security group across multiple subnets
# Must code as separate security groups with same name

with Subnet("Subnet 1"):
    with SecurityGroup("Web SG"):
        vsi1 = VirtualServer("Web-1")

with Subnet("Subnet 2"):
    with SecurityGroup("Web SG"):  # Separate group, same name
        vsi2 = VirtualServer("Web-2")
```

**Workaround**: Use descriptive names to indicate relationship:
```python
with Subnet("Subnet 1"):
    with SecurityGroup("Web SG (Zone 1)"):
        vsi1 = VirtualServer("Web-1")

with Subnet("Subnet 2"):
    with SecurityGroup("Web SG (Zone 2)"):
        vsi2 = VirtualServer("Web-2")
```

---

## Next Steps

- 📚 **[Examples](examples/)** - Explore more examples
- 🔄 **[Terraform Guide](terraform.md)** - Generate diagrams from Terraform
- 🎨 **[IBM Design Language](https://www.ibm.com/design/language/infographics/technical-diagrams/design)** - Learn the design standards

---

## License

This project is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
