from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet, CloudServices, ResourceGroup, SecurityGroup, ExpandedVirtualServer
from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.actors import User
from ibmdiagrams.ibmcloud.network import EndpointGateway, TransitGateway
from ibmdiagrams.ibmcloud.security import KeyProtect, VPNGateway
from ibmdiagrams.ibmcloud.storage import ObjectStorage

with Diagram("zone"):
  with Zone("Zone 1", "10.243.0.0/24", direction="TB"):
    vsi1 = ExpandedVirtualServer("VSI - Server", "10.243.0.5") 
    #user = User("Jay", "10.243.0.5")
