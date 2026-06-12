"""
Baseline diagram element definitions for testing.

This module contains all diagram elements used for baseline generation,
organized for easy maintenance and reuse across test modules.
"""

# ruff: noqa: F403, F405
from utils.baseline_utils import DiagramElement

from ibmdiagrams.ibmcloud.connectors import *
from ibmdiagrams.ibmcloud import (
    actors,
    ai,
    compute,
    containers,
    data,
    devops,
    groups,
    network,
    observability,
    security,
    storage,
)

def get_baseline_elements() -> list[DiagramElement]:
    """
    Return baseline diagram elements for testing.

    Only includes container/group elements that can be tested standalone.
    Node elements (VirtualServer, Database, User, etc.) require a container
    context and cannot be baseline tested in isolation.

    Returns:
        List of DiagramElement instances representing container/group
        IBM Cloud diagram components.
    """
    return [
        ###################################
        # Groups
        ###################################

        # Core Groups (_CoreGroup) - ordered as in groups.py
        DiagramElement(
            obj=groups.IBMCloud,
            slug="group:ibm-cloud",
            label="IBM Cloud",
        ),
        DiagramElement(
            obj=groups.VPC,
            slug="group:vpc",
            label="VPC",
        ),
        DiagramElement(
            obj=groups.Subnet,
            slug="group:subnet",
            label="Subnet",
        ),
        DiagramElement(
            obj=groups.EnterpriseNetwork,
            slug="group:enterprise-network",
            label="Enterprise<br>network",
        ),
        DiagramElement(
            obj=groups.PublicNetwork,
            slug="group:public-network",
            label="Public<br>network",
        ),
        DiagramElement(
            obj=groups.CloudServices,
            slug="group:cloud-services",
            label="Cloud<br>services",
        ),
        DiagramElement(
            obj=groups.InternetServices,
            slug="group:internet-services",
            label="Internet<br>services",
        ),
        DiagramElement(
            obj=groups.OverlayNetwork,
            slug="group:overlay-network",
            label="Overlay<br>network",
        ),
        DiagramElement(
            obj=groups.PowerWorkspace,
            slug="group:power-workspace",
            label="Power<br>workspace",
        ),
        DiagramElement(
            obj=groups.ZSystem,
            slug="group:z-system",
            label="Z System",
        ),
        DiagramElement(
            obj=groups.Internet,
            slug="group:internet",
            label="Internet",
        ),
        DiagramElement(
            obj=groups.VLAN,
            slug="group:vlan",
            label="VLAN",
        ),
        DiagramElement(
            obj=groups.ClassicVLAN,
            slug="group:classic-vlan",
            label="Classic<br>VLAN",
        ),
        DiagramElement(
            obj=groups.ClassicInfrastructure,
            slug="group:classic-infrastructure-group",
            label="Classic<br>infrastructure",
        ),
        DiagramElement(
            obj=groups.OpenShift,
            slug="group:openshift",
            label="OpenShift",
        ),
        DiagramElement(
            obj=groups.KubernetesServices,
            slug="group:kubernetes-services",
            label="Kubernetes<br>services",
        ),
        DiagramElement(
            obj=groups.ZContainers,
            slug="group:z-containers-group",
            label="Z Containers",
        ),
        DiagramElement(
            obj=groups.watsonx,
            slug="group:watsonx",
            label="watsonx",
        ),
        DiagramElement(
            obj=groups.watsonxCodeAssistant,
            slug="group:watsonx-code-assistant",
            label="watsonx Code<br>Assistant",
        ),
        DiagramElement(
            obj=groups.watsonxZCodeAssistant,
            slug="group:watsonx-z-code-assistant",
            label="watsonx Z<br>Code Assistant",
        ),
        DiagramElement(
            obj=groups.AuthorizationBoundary,
            slug="group:authorization-boundary",
            label="Authorization<br>boundary",
        ),
        DiagramElement(
            obj=groups.PointOfPresence,
            slug="group:point-of-presence",
            label="Point of<br>presence",
        ),
        DiagramElement(
            obj=groups.Region,
            slug="group:region",
            label="Region",
        ),
        # Control Groups (_ControlGroup) - ordered as in groups.py
        DiagramElement(
            obj=groups.AccessGroup,
            slug="group:access-group",
            label="Access<br>group",
        ),
        DiagramElement(
            obj=groups.AccountGroup,
            slug="group:account-group",
            label="Account<br>group",
        ),
        DiagramElement(
            obj=groups.InstanceGroup,
            slug="group:instance-group",
            label="Instance<br>group",
        ),
        DiagramElement(
            obj=groups.PlacementGroup,
            slug="group:placement-group",
            label="Placement<br>group",
        ),
        DiagramElement(
            obj=groups.ResourceGroup,
            slug="group:resource-group",
            label="Resource<br>group",
        ),
        DiagramElement(
            obj=groups.SecurityGroup,
            slug="group:security-group",
            label="Security<br>group",
        ),
        DiagramElement(
            obj=groups.AvailabilityZone,
            slug="group:availability-zone",
            label="Availability<br>zone",
        ),
        # Expanded Groups (_ExpandedGroup) - ordered as in groups.py
        DiagramElement(
            obj=groups.ExpandedVirtualServer,
            slug="group:expanded-virtual-server",
            label="Expanded<br>virtual server",
        ),
        DiagramElement(
            obj=groups.ExpandedPowerVirtualServer,
            slug="group:expanded-power-virtual-server",
            label="Expanded<br>power virtual server",
        ),
        DiagramElement(
            obj=groups.ExpandedClassicVirtualServer,
            slug="group:expanded-classic-virtual-server",
            label="Expanded<br>classic virtual server",
        ),
        DiagramElement(
            obj=groups.ExpandedBareMetalServer,
            slug="group:expanded-bare-metal-server",
            label="Expanded<br>bare metal server",
        ),
        DiagramElement(
            obj=groups.ExpandedClassicBareMetalServer,
            slug="group:expanded-classic-bare-metal-server",
            label="Expanded<br>classic bare metal server",
        ),
        DiagramElement(
            obj=groups.ExpandedApplication,
            slug="group:expanded-application",
            label="Expanded<br>application",
        ),
        DiagramElement(
            obj=groups.ExpandedMicroservice,
            slug="group:expanded-microservice",
            label="Expanded<br>microservice",
        ),
        # Actor Groups (aliases)
        DiagramElement(
            obj=groups.Enterprise,
            slug="group:enterprise",
            label="Enterprise",
        ),

        ###################################
        # Actors
        ###################################

        DiagramElement(
            obj=actors.User,
            slug="actor:user",
            label="Enterprise User",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=actors.Users,
            slug="actor:users",
            label="Enterprise<br>Users",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=actors.Enterprise,
            slug="actor:enterprise",
            label="Enterprise",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=actors.Application,
            slug="actor:application",
            label="Enterprise<br>Applications",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=actors.WebApplication,
            slug="actor:web-application",
            label="Web<br>Applications",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=actors.Microservice,
            slug="actor:microservice",
            label="Microservices",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),

        ###################################
        # AI
        ###################################

        DiagramElement(
            obj=ai.watsonx,
            slug="ai:watsonx",
            label="watsonx",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.watsonxAI,
            slug="ai:watsonx-ai",
            label="watsonx.ai",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.watsonxRuntime,
            slug="ai:watsonx-runtime",
            label="watsonx<br>Runtime",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.watsonxStudio,
            slug="ai:watsonx-studio",
            label="watsonx<br>Studio",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.watsonxData,
            slug="ai:watsonx-data",
            label="watsonx.data",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.watsonxGovernance,
            slug="ai:watsonx-governance",
            label="watsonx<br>Governance",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.watsonxOrchestrate,
            slug="ai:watsonx-orchestrate",
            label="watsonx<br>Orchestrate",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.watsonxAssistant,
            slug="ai:watsonx-assistant",
            label="watsonx<br>Assistant",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.watsonxCodeAssistant,
            slug="ai:watsonx-code-assistant",
            label="watsonx Code<br>Assistant",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.watsonxZCodeAssistant,
            slug="ai:watsonx-z-code-assistant",
            label="watsonx Z<br>Code Assistant",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.watsonxZRefactorCodeAssistant,
            slug="ai:watsonx-z-refactor-code-assistant",
            label="watsonx Z Refactor<br>Code Assistant",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.WatsonDiscovery,
            slug="ai:watson-discovery",
            label="Watson<br>Discovery",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.WatsonMachineLearning,
            slug="ai:watson-machine-learning",
            label="Watson Machine<br>Learning",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=ai.WatsonStudio,
            slug="ai:watson-studio",
            label="Watson<br>Studio",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),

        ###################################
        # Compute
        ###################################

        DiagramElement(
            obj=compute.VirtualServer,
            slug="compute:virtual-server",
            label="Virtual<br>Server",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=compute.PowerVirtualServer,
            slug="compute:power-virtual-server",
            label="Power Virtual<br>Server",
            wrapper_obj=groups.PowerWorkspace,
            wrapper_label="Power<br>workspace",
        ),
        DiagramElement(
            obj=compute.ClassicVirtualServer,
            slug="compute:classic-virtual-server",
            label="Classic Virtual<br>Server",
            wrapper_obj=groups.ClassicInfrastructure,
            wrapper_label="Classic<br>infrastructure",
        ),
        DiagramElement(
            obj=compute.BareMetalServer,
            slug="compute:bare-metal-server",
            label="Bare Metal<br>Server",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=compute.ClassicBareMetalServer,
            slug="compute:classic-bare-metal-server",
            label="Classic Bare Metal<br>Server",
            wrapper_obj=groups.ClassicInfrastructure,
            wrapper_label="Classic<br>infrastructure",
        ),
        DiagramElement(
            obj=compute.DedicatedHost,
            slug="compute:dedicated-host",
            label="Dedicated<br>Host",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=compute.ImageService,
            slug="compute:image-service",
            label="Image<br>Service",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=compute.Satellite,
            slug="compute:satellite",
            label="Satellite",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),

        ###################################
        # Containers
        ###################################

        DiagramElement(
            obj=containers.OpenShift,
            slug="containers:openshift",
            label="OpenShift",
            wrapper_obj=groups.OpenShift,
            wrapper_label="OpenShift",
        ),
        DiagramElement(
            obj=containers.CodeEngine,
            slug="containers:code-engine",
            label="Code<br>Engine",
            wrapper_obj=groups.KubernetesServices,
            wrapper_label="Kubernetes<br>services",
        ),
        DiagramElement(
            obj=containers.KubernetesService,
            slug="containers:kubernetes-service",
            label="Kubernetes<br>Service",
            wrapper_obj=groups.KubernetesServices,
            wrapper_label="Kubernetes<br>services",
        ),
        DiagramElement(
            obj=containers.ZContainers,
            slug="containers:z-containers",
            label="Z Containers",
            wrapper_obj=groups.ZContainers,
            wrapper_label="Z Containers",
        ),
        DiagramElement(
            obj=containers.ContainerRegistry,
            slug="containers:container-registry",
            label="Container<br>Registry",
            wrapper_obj=groups.KubernetesServices,
            wrapper_label="Kubernetes<br>services",
        ),

        ###################################
        # Data
        ###################################

        DiagramElement(
            obj=data.Db2,
            slug="data:db2",
            label="Db2",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=data.Db2Warehouse,
            slug="data:db2-warehouse",
            label="Db2<br>Warehouse",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=data.Cloudant,
            slug="data:cloudant",
            label="Cloudant",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=data.DataStax,
            slug="data:datastax",
            label="DataStax",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=data.Elasticsearch,
            slug="data:elasticsearch",
            label="Elasticsearch",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        # DiagramElement(
        #     obj=data.MongoDB,
        #     slug="data:mongodb",
        #     label="MongoDB",
        #     wrapper_obj=groups.VPC,
        #     wrapper_label="VPC",
        # ),
        DiagramElement(
            obj=data.MySQL,
            slug="data:mysql",
            label="MySQL",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=data.PostgreSQL,
            slug="data:postgresql",
            label="PostgreSQL",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=data.Rabbit,
            slug="data:rabbit",
            label="Rabbit",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=data.Redis,
            slug="data:redis",
            label="Redis",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=data.Database,
            slug="data:database",
            label="Database",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=data.EventStreams,
            slug="data:event-streams",
            label="Event<br>Streams",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=data.DataPak,
            slug="data:data-pak",
            label="Data<br>Pak",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),

        ###################################
        # DevOps
        ###################################

        DiagramElement(
            obj=devops.ContinuousDelivery,
            slug="devops:continuous-delivery",
            label="Continuous<br>Delivery",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=devops.ContinuousIntegration,
            slug="devops:continuous-integration",
            label="Continuous<br>Integration",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=devops.SourceCodeRepository,
            slug="devops:source-code-repository",
            label="Source Code<br>Repository",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=devops.Toolchain,
            slug="devops:toolchain",
            label="Toolchain",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=devops.MQ,
            slug="devops:mq",
            label="MQ",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=devops.Ansible,
            slug="devops:ansible",
            label="Ansible",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=devops.GitLab,
            slug="devops:gitlab",
            label="GitLab",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=devops.IntegrationPak,
            slug="devops:integration-pak",
            label="Integration<br>Pak",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),

        ###################################
        # Network
        ###################################

        DiagramElement(
            obj=network.LoadBalancer,
            slug="network:load-balancer",
            label="Load<br>Balancer",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=network.ApplicationLoadBalancer,
            slug="network:application-load-balancer",
            label="Application Load<br>Balancer",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=network.NetworkLoadBalancer,
            slug="network:network-load-balancer",
            label="Network Load<br>Balancer",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=network.GlobalLoadBalancer,
            slug="network:global-load-balancer",
            label="Global Load<br>Balancer",
            wrapper_obj=groups.PublicNetwork,
            wrapper_label="Public<br>network",
        ),
        DiagramElement(
            obj=network.ClassicLoadBalancer,
            slug="network:classic-load-balancer",
            label="Classic Load<br>Balancer",
            wrapper_obj=groups.ClassicInfrastructure,
            wrapper_label="Classic<br>infrastructure",
        ),
        DiagramElement(
            obj=network.FloatingIP,
            slug="network:floating-ip",
            label="Floating IP",
            wrapper_obj=groups.PublicNetwork,
            wrapper_label="Public<br>network",
        ),
        DiagramElement(
            obj=network.NetworkInterface,
            slug="network:network-interface",
            label="Network<br>Interface",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=network.EndpointGateway,
            slug="network:endpoint-gateway",
            label="Endpoint<br>Gateway",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=network.PublicGateway,
            slug="network:public-gateway",
            label="Public<br>Gateway",
            wrapper_obj=groups.PublicNetwork,
            wrapper_label="Public<br>network",
        ),
        DiagramElement(
            obj=network.TransitGateway,
            slug="network:transit-gateway",
            label="Transit<br>Gateway",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=network.DirectLinkConnect,
            slug="network:direct-link-connect",
            label="Direct Link<br>Connect",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=network.DirectLinkDedicated,
            slug="network:direct-link-dedicated",
            label="Direct Link<br>Dedicated",
            wrapper_obj=groups.EnterpriseNetwork,
            wrapper_label="Enterprise<br>Network",
        ),
        DiagramElement(
            obj=network.DNSServices,
            slug="network:dns-services",
            label="DNS<br>Services",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=network.InternetServices,
            slug="network:internet-services",
            label="Internet<br>Services",
            wrapper_obj=groups.InternetServices,
            wrapper_label="Internet<br>services",
        ),
        DiagramElement(
            obj=network.Internet,
            slug="network:internet",
            label="Internet",
            wrapper_obj=groups.Internet,
            wrapper_label="Internet",
        ),
        DiagramElement(
            obj=network.NTP,
            slug="network:ntp",
            label="NTP",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=network.Bridge,
            slug="network:bridge",
            label="Bridge",
            wrapper_obj=groups.VLAN,
            wrapper_label="VLAN",
        ),
        DiagramElement(
            obj=network.Router,
            slug="network:router",
            label="Router",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=network.VLAN,
            slug="network:vlan",
            label="VLAN",
            wrapper_obj=groups.VLAN,
            wrapper_label="VLAN",
        ),
        DiagramElement(
            obj=network.ClassicVLAN,
            slug="network:classic-vlan",
            label="Classic<br>VLAN",
            wrapper_obj=groups.ClassicVLAN,
            wrapper_label="Classic<br>VLAN",
        ),
        DiagramElement(
            obj=network.ProxyServer,
            slug="network:proxy-server",
            label="Proxy<br>Server",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=network.L2Switch,
            slug="network:l2-switch",
            label="L2<br>Switch",
            wrapper_obj=groups.VLAN,
            wrapper_label="VLAN",
        ),
        DiagramElement(
            obj=network.L3Switch,
            slug="network:l3-switch",
            label="L3<br>Switch",
            wrapper_obj=groups.VLAN,
            wrapper_label="VLAN",
        ),

        ###################################
        # Observability
        ###################################

        DiagramElement(
            obj=observability.CloudLogs,
            slug="observability:cloud-logs",
            label="Cloud<br>Logs",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=observability.FlowLogs,
            slug="observability:flow-logs",
            label="Flow<br>Logs",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),
        DiagramElement(
            obj=observability.Monitoring,
            slug="observability:monitoring",
            label="Monitoring",
            wrapper_obj=groups.VPC,
            wrapper_label="VPC",
        ),

        ###################################
        # Security
        ###################################

        DiagramElement(
            obj=security.AppID,
            slug="security:app-id",
            label="App ID",
            wrapper_obj=groups.SecurityGroup,
            wrapper_label="Security<br>group",
        ),
        DiagramElement(
            obj=security.KeyProtect,
            slug="security:key-protect",
            label="Key<br>Protect",
            wrapper_obj=groups.SecurityGroup,
            wrapper_label="Security<br>group",
        ),
        DiagramElement(
            obj=security.SecretsManager,
            slug="security:secrets-manager",
            label="Secrets<br>Manager",
            wrapper_obj=groups.SecurityGroup,
            wrapper_label="Security<br>group",
        ),
        DiagramElement(
            obj=security.SecurityComplianceCenter,
            slug="security:security-compliance-center",
            label="Security Compliance<br>Center",
            wrapper_obj=groups.SecurityGroup,
            wrapper_label="Security<br>group",
        ),
        DiagramElement(
            obj=security.SSHKey,
            slug="security:ssh-key",
            label="SSH<br>Key",
            wrapper_obj=groups.SecurityGroup,
            wrapper_label="Security<br>group",
        ),
        DiagramElement(
            obj=security.VPNGateway,
            slug="security:vpn-gateway",
            label="VPN<br>Gateway",
            wrapper_obj=groups.SecurityGroup,
            wrapper_label="Security<br>group",
        ),
        DiagramElement(
            obj=security.VPNConnection,
            slug="security:vpn-connection",
            label="VPN<br>Connection",
            wrapper_obj=groups.SecurityGroup,
            wrapper_label="Security<br>group",
        ),
        DiagramElement(
            obj=security.BastionHost,
            slug="security:bastion-host",
            label="Bastion<br>Host",
            wrapper_obj=groups.SecurityGroup,
            wrapper_label="Security<br>group",
        ),
        DiagramElement(
            obj=security.ACLRules,
            slug="security:acl-rules",
            label="ACL<br>Rules",
            wrapper_obj=groups.SecurityGroup,
            wrapper_label="Security<br>group",
        ),
        DiagramElement(
            obj=security.SecurityPak,
            slug="security:security-pak",
            label="Security<br>Pak",
            wrapper_obj=groups.SecurityGroup,
            wrapper_label="Security<br>group",
        ),

        ###################################
        # Storage
        ###################################

        DiagramElement(
            obj=storage.BlockStorage,
            slug="storage:block-storage",
            label="Block<br>Storage",
            wrapper_obj=groups.CloudServices,
            wrapper_label="Cloud<br>Services",
        ),
        DiagramElement(
            obj=storage.BlockStorageSnapshots,
            slug="storage:block-storage-snapshots",
            label="Block Storage<br>Snapshots",
            wrapper_obj=groups.CloudServices,
            wrapper_label="Cloud<br>Services",
        ),
        DiagramElement(
            obj=storage.FileStorage,
            slug="storage:file-storage",
            label="File<br>Storage",
            wrapper_obj=groups.CloudServices,
            wrapper_label="Cloud<br>Services",
        ),
        DiagramElement(
            obj=storage.ObjectStorage,
            slug="storage:object-storage",
            label="Object<br>Storage",
            wrapper_obj=groups.CloudServices,
            wrapper_label="Cloud<br>Services",
        ),
        DiagramElement(
            obj=storage.CloudBackup,
            slug="storage:cloud-backup",
            label="Cloud<br>Backup",
            wrapper_obj=groups.CloudServices,
            wrapper_label="Cloud<br>Services",
        ),
    ]
