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

from . import _IBMItem
from .colors import Colors

class _Network(_IBMItem):
    def __init__(self, label, sublabel="", icon=""):
        super(_Network, self).__init__(label=label, sublabel=sublabel, 
                                       linecolor=Colors.lines["network"], 
                                       shape="pnode", icon=icon)

class LoadBalancer(_Network):
    def __init__(self, label, sublabel=""):
        super(LoadBalancer, self).__init__(label, sublabel=sublabel, 
                                           icon="Load Balancer")

class ApplicationLoadBalancer(_Network):
    def __init__(self, label, sublabel=""):
        super(ApplicationLoadBalancer, self).__init__(label, sublabel=sublabel, 
                                                      icon="Application Load Balancer")

class NetworkLoadBalancer(_Network):
    def __init__(self, label, sublabel=""):
        super(NetworkLoadBalancer, self).__init__(label, sublabel=sublabel, 
                                                  icon="Network Load Balancer")

class GlobalLoadBalancer(_Network):
    def __init__(self, label, sublabel=""):
        super(GlobalLoadBalancer, self).__init__(label, sublabel=sublabel, 
                                                 icon="Global Load Balancer")

class ClassicLoadBalancer(_Network):
    def __init__(self, label, sublabel=""):
        super(ClassicLoadBalancer, self).__init__(label, sublabel=sublabel, 
                                                  icon="Classic Load Balancer")

class FloatingIP(_Network):
    def __init__(self, label, sublabel=""):
        super(FloatingIP, self).__init__(label, sublabel=sublabel, 
                                         icon="Floating IP")

class NetworkInterface(_Network):
    def __init__(self, label, sublabel=""):
        super(NetworkInterface, self).__init__(label, sublabel=sublabel, 
                                               icon="Network Interface")

class EndpointGateway(_Network):
    def __init__(self, label, sublabel=""):
        super(EndpointGateway, self).__init__(label, sublabel=sublabel, 
                                              icon="Endpoint Gateway")

class PublicGateway(_Network):
    def __init__(self, label, sublabel=""):
        super(PublicGateway, self).__init__(label, sublabel=sublabel, 
                                            icon="Public Gateway")

class TransitGateway(_Network):
    def __init__(self, label, sublabel=""):
        super(TransitGateway, self).__init__(label, sublabel=sublabel, 
                                             icon="Transit Gateway")

class DirectLinkConnect(_Network):
    def __init__(self, label, sublabel=""):
        super(DirectLinkConnect, self).__init__(label, sublabel=sublabel, 
                                                icon="Direct Link Connect")

class DirectLinkDedicated(_Network):
    def __init__(self, label, sublabel=""):
        super(DirectLinkDedicated, self).__init__(label, sublabel=sublabel, 
                                                  icon="Direct Link Dedicated")

class DNSServices(_Network):
    def __init__(self, label, sublabel=""):
        super(DNSServices, self).__init__(label, sublabel=sublabel, 
                                                  icon="DNS Services")

class InternetServices(_Network):
    def __init__(self, label, sublabel=""):
        super(InternetServices, self).__init__(label, sublabel=sublabel, 
                                               icon="Internet Services")

class Internet(_Network):
    def __init__(self, label, sublabel=""):
        super(Internet, self).__init__(label, sublabel=sublabel, 
                                              icon="Internet")

class NTP(_Network):
    def __init__(self, label, sublabel=""):
        super(NTP, self).__init__(label, sublabel=sublabel, 
                                  icon="Undefined")

class Bridge(_Network):
    def __init__(self, label, sublabel=""):
        super(Bridge, self).__init__(label, sublabel=sublabel, 
                                            icon="Bridge")

class Router(_Network):
    def __init__(self, label, sublabel=""):
        super(Router, self).__init__(label, sublabel=sublabel, 
                                            icon="Router")

class VLAN(_Network):
    def __init__(self, label, sublabel=""):
        super(VLAN, self).__init__(label, sublabel=sublabel, 
                                          icon="VLAN")

class ClassicVLAN(_Network):
    def __init__(self, label, sublabel=""):
        super(ClassicVLAN, self).__init__(label, sublabel=sublabel, 
                                          icon="Classic VLAN")

class ProxyServer(_Network):
    def __init__(self, label, sublabel=""):
        super(ProxyServer, self).__init__(label, sublabel=sublabel, 
                                          icon="Proxy Server")

class L2Switch(_Network):
    def __init__(self, label, sublabel=""):
        super(L2Switch, self).__init__(label, sublabel=sublabel, 
                                       icon="L2 Switch")

class L3Switch(_Network):
    def __init__(self, label, sublabel=""):
        super(L3Switch, self).__init__(label, sublabel=sublabel, 
                                       icon="L3 Switch")

# Aliases
DNS = DNSServices
FIP = FloatingIP
GLB = GlobalLoadBalancer
LB = LoadBalancer
TGW = TransitGateway
VPE = EndpointGateway
