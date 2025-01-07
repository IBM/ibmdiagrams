# @file network.py
#
# Copyright contributors to the ibmdiagrams project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from . import _IBMCollapsed
from .colors import Colors

class _Network(_IBMCollapsed):
    def __init__(self, label, sublabel="", icon=""):
        super(_Network, self).__init__(label=label, sublabel=sublabel, 
                                       linecolor=Colors.lines["network"], 
                                       shape="pnode", icon=icon)

class LoadBalancer(_Network):
    def __init__(self, label, sublabel=""):
        super(LoadBalancer, self).__init__(label, sublabel=sublabel, 
                                           icon="Load Balancer Icon")

class ApplicationLoadBalancer(_Network):
    def __init__(self, label, sublabel=""):
        super(ApplicationLoadBalancer, self).__init__(label, sublabel=sublabel, 
                                                      icon="Application Load Balancer Icon")

class NetworkLoadBalancer(_Network):
    def __init__(self, label, sublabel=""):
        super(NetworkLoadBalancer, self).__init__(label, sublabel=sublabel, 
                                                  icon="Network Load Balancer Icon")

class GlobalLoadBalancer(_Network):
    def __init__(self, label, sublabel=""):
        super(GlobalLoadBalancer, self).__init__(label, sublabel=sublabel, 
                                                 icon="Global Load Balancer Icon")

class ClassicLoadBalancer(_Network):
    def __init__(self, label, sublabel=""):
        super(ClassicLoadBalancer, self).__init__(label, sublabel=sublabel, 
                                                  icon="Classic Load Balancer Icon")

class FloatingIP(_Network):
    def __init__(self, label, sublabel=""):
        super(FloatingIP, self).__init__(label, sublabel=sublabel, 
                                         icon="Floating IP Icon")

class NetworkInterface(_Network):
    def __init__(self, label, sublabel=""):
        super(NetworkInterface, self).__init__(label, sublabel=sublabel, 
                                               icon="Network Interface Icon")

class EndpointGateway(_Network):
    def __init__(self, label, sublabel=""):
        super(EndpointGateway, self).__init__(label, sublabel=sublabel, 
                                              icon="Endpoint Gateway Icon")

class PublicGateway(_Network):
    def __init__(self, label, sublabel=""):
        super(PublicGateway, self).__init__(label, sublabel=sublabel, 
                                            icon="Public Gateway Icon")

class TransitGateway(_Network):
    def __init__(self, label, sublabel=""):
        super(TransitGateway, self).__init__(label, sublabel=sublabel, 
                                             icon="Transit Gateway Icon")

class DirectLinkConnect(_Network):
    def __init__(self, label, sublabel=""):
        super(DirectLinkConnect, self).__init__(label, sublabel=sublabel, 
                                                icon="Direct Link Connect Icon")

class DirectLinkDedicated(_Network):
    def __init__(self, label, sublabel=""):
        super(DirectLinkDedicated, self).__init__(label, sublabel=sublabel, 
                                                  icon="Direct Link Dedicated Icon")

class DNSServices(_Network):
    def __init__(self, label, sublabel=""):
        super(DNSServices, self).__init__(label, sublabel=sublabel, 
                                                  icon="DNS Services Icon")

class InternetServices(_Network):
    def __init__(self, label, sublabel=""):
        super(InternetServices, self).__init__(label, sublabel=sublabel, 
                                               icon="Internet Services Icon")

class Internet(_Network):
    def __init__(self, label, sublabel=""):
        super(Internet, self).__init__(label, sublabel=sublabel, 
                                              icon="Internet Icon")

class NTP(_Network):
    def __init__(self, label, sublabel=""):
        super(NTP, self).__init__(label, sublabel=sublabel, 
                                  icon="Undefined Icon")

class Bridge(_Network):
    def __init__(self, label, sublabel=""):
        super(Bridge, self).__init__(label, sublabel=sublabel, 
                                            icon="Bridge Icon")

class Router(_Network):
    def __init__(self, label, sublabel=""):
        super(Router, self).__init__(label, sublabel=sublabel, 
                                            icon="Router Icon")

class VLAN(_Network):
    def __init__(self, label, sublabel=""):
        super(VLAN, self).__init__(label, sublabel=sublabel, 
                                          icon="VLAN Icon")

class ClassicVLAN(_Network):
    def __init__(self, label, sublabel=""):
        super(ClassicVLAN, self).__init__(label, sublabel=sublabel, 
                                          icon="Classic VLAN Icon")

class ProxyServer(_Network):
    def __init__(self, label, sublabel=""):
        super(ProxyServer, self).__init__(label, sublabel=sublabel, 
                                          icon="Proxy Server Icon")

class L2Switch(_Network):
    def __init__(self, label, sublabel=""):
        super(L2Switch, self).__init__(label, sublabel=sublabel, 
                                       icon="L2 Switch Icon")

class L3Switch(_Network):
    def __init__(self, label, sublabel=""):
        super(L3Switch, self).__init__(label, sublabel=sublabel, 
                                       icon="L3 Switch Icon")

# Aliases
DNS = DNSServices
FIP = FloatingIP
GLB = GlobalLoadBalancer
LB = LoadBalancer
TGW = TransitGateway
VPE = EndpointGateway
