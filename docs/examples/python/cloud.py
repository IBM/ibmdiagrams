from ibmdiagrams.ibmcloud.actors import User
from ibmdiagrams.ibmcloud.applications import Applications, UserDirectory
from ibmdiagrams.ibmcloud.compute import EnterpriseData
from ibmdiagrams.ibmcloud.devops import ClassicInfrastructure
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import (
    VPC,
    EnterpriseNetwork,
    ExpandedVirtualServer,
    IBMCloud,
    LayoutGroup,
    PublicNetwork,
    Region,
    Subnet,
    Zone,
)
from ibmdiagrams.ibmcloud.network import (
    FIP,
    TGW,
    DirectLinkConnect,
    Internet,
    NetworkLoadBalancer,
    PublicGateway,
    Router,
)
from ibmdiagrams.ibmcloud.security import (
    VPNConnection,
    VPNGateway,
)


def main():
    with Diagram("cloud"):
        with PublicNetwork("Public<br>network", direction="TB"):
            User(label="User")
            Internet(label="Internet")
            VPNConnection("VPN<br>connection")

        with IBMCloud("IBM Cloud"):
            with Region("Dallas Region", direction="TB"):
                with VPC("VPC A"):
                    with Zone("Dallas Zone 1", sublabel="10.10.0.0/18", direction="LR"):
                        PublicGateway(label="Public<br>gateway")
                        FIP(label="Floating IP")
                        VPNGateway(label="VPN<br>gateway")

                        with LayoutGroup(direction="TB"):
                            with Subnet("Subnet 1", sublabel="10.10.10.0/24<br>Frontend ACL"):
                                with ExpandedVirtualServer(
                                    label="VSI 1",
                                    sublabel="Type: Dedicated<br>OS: Redhat 8.x<br>Profile: Balanced bx2-2x8<br>vCPU: 2<br>RAM: 8GiB<br>Bandwith: 4Gbps",
                                ):
                                    pass
                            with Subnet("Subnet 2", sublabel="10.10.20.0/24<br>Backend ACL"):
                                with ExpandedVirtualServer(
                                    label="VSI 2",
                                    sublabel="Type: Dedicated<br>OS: Redhat 8.x<br>Profile: Balanced bx2-2x8<br>vCPU: 2<br>RAM: 8GiB<br>Bandwith: 4Gbps",
                                ):
                                    pass

                    NetworkLoadBalancer("Public load<br>balancer")
                    NetworkLoadBalancer("Private load<br>balancer")

                    with Zone("Dallas Zone 2", sublabel="10.10.0.0/18", direction="TB"):
                        with Subnet("Subnet 3", sublabel="10.10.10.0/24<br>Frontend ACL"):
                            with ExpandedVirtualServer(
                                label="VSI 3",
                                sublabel="Type: Dedicated<br>OS: Redhat 8.x<br>Profile: Balanced bx2-2x8<br>vCPU: 2<br>RAM: 8GiB<br>Bandwith: 4Gbps",
                            ):
                                pass
                        with Subnet("Subnet 4", sublabel="10.10.20.0/24<br>Backend ACL"):
                            with ExpandedVirtualServer(
                                label="VSI 4",
                                sublabel="Type: Dedicated<br>OS: Redhat 8.x<br>Profile: Balanced bx2-2x8<br>vCPU: 2<br>RAM: 8GiB<br>Bandwith: 4Gbps",
                            ):
                                pass
                        pass
                    pass

            ClassicInfrastructure("Classic<br>infrastructure")
            TGW("Transit<br>Gateway")
            DirectLinkConnect("Direct Link")
            Router("Implicit<br>router")

        with EnterpriseNetwork("Enterprise<br>network", direction="TB"):
            UserDirectory(label="Enterprise user<br>directory")
            User(label="Enterprise<br>user")
            Applications(label="Enterprise<br>applications")
            EnterpriseData(label="Enterprise<br>data")


if __name__ == "__main__":
    main()
