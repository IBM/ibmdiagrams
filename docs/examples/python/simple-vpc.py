"""
Simple VPC Example

This example demonstrates a basic VPC architecture with:
- Single VPC in Dallas region
- One availability zone
- Two subnets (web and app tiers)
- Virtual servers in each subnet
- Public gateway for internet access
- Security group configuration

Usage:
    python simple-vpc.py

Output:
    simple-vpc.drawio
"""

from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import VPC, IBMCloud, Region, SecurityGroup, Subnet, Zone
from ibmdiagrams.ibmcloud.network import ApplicationLoadBalancer, PublicGateway

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
