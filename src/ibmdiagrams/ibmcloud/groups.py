# @file groups.py
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

from . import _IBMGrouping, _IBMExpanded
from .colors import Colors

class _Grouping(_IBMGrouping):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", shape="", icon="", direction="LR"):
        super(_Grouping, self).__init__(label, sublabel=sublabel, 
                                        linecolor=linecolor, fillcolor=fillcolor, 
                                        shape=shape, icon=icon, direction=direction)

# Core Groups

class _CoreGroup(_Grouping):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", icon="", direction="LR"):
        super(_CoreGroup, self).__init__(label, sublabel=sublabel, 
                                         linecolor=linecolor, fillcolor=fillcolor,
                                         shape="ploc", icon=icon, direction=direction)

class IBMCloud(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(IBMCloud, self).__init__(label, sublabel=sublabel,
                                       linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                       icon="IBM Cloud", direction=direction)

class VPC(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(VPC, self).__init__(label, sublabel=sublabel, 
                                  linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                  icon="VPC", direction=direction)

class Subnet(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(Subnet, self).__init__(label, sublabel=sublabel, 
                                     linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                     icon="Subnet", direction=direction) 

class PublicNetwork(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(PublicNetwork, self).__init__(label, sublabel=sublabel, 
                                            linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                            icon="Public Network", direction="LR") 

class EnterpriseNetwork(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(EnterpriseNetwork, self).__init__(label, sublabel=sublabel, 
                                                linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                                icon="Enterprise Network", direction=direction) 

class CloudServices(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(CloudServices, self).__init__(label, sublabel=sublabel, 
                                            linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                            icon="Cloud Services", direction="LR") 

class InternetServices(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(InternetServices, self).__init__(label, sublabel=sublabel, 
                                               linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                               icon="Internet Services", direction="LR") 

class OverlayNetwork(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(OverlayNetwork, self).__init__(label, sublabel=sublabel, 
                                             linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                             icon="Overlay Network", direction="LR") 

class PowerWorkspace(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(PowerWorkspace, self).__init__(label, sublabel=sublabel, 
                                             linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                             icon="Power Workspace", direction="LR") 

class ZSystem(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ZSystem, self).__init__(label, sublabel=sublabel, 
                                      linecolor=Colors.lines["network"], fillcolor=Colors.fills["compute"],
                                      icon="Z System", direction="LR") 

class Internet(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(Internet, self).__init__(label, sublabel=sublabel, 
                                       linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                       icon="Internet", direction="LR") 

class VLAN(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(VLAN, self).__init__(label, sublabel=sublabel, 
                                   linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                   icon="VLAN", direction="LR") 

class ClassicVLAN(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(Classic_VLAN, self).__init__(label, sublabel=sublabel, 
                                           linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                           icon="Classic VLAN", direction="LR") 

class ClassicInfrastructure(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ClassicInfrastructure, self).__init__(label, sublabel=sublabel, 
                                                    linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                                    icon="Classic Infrastructure", direction="LR") 

class OpenShift(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(OpenShift, self).__init__(label, sublabel=sublabel, 
                                        linecolor=Colors.lines["compute"], fillcolor=Colors.fills["compute"],
                                        icon="OpenShift", direction="LR") 

class KubernetesServices(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(KubernetesServices, self).__init__(label, sublabel=sublabel, 
                                                 linecolor=Colors.lines["compute"], fillcolor=Colors.fills["compute"],
                                                 icon="Kubernetes Services", direction="LR") 

class ZContainers(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ZContainers, self).__init__(label, sublabel=sublabel, 
                                          linecolor=Colors.lines["compute"], fillcolor=Colors.fills["compute"],
                                          icon="Z Containers", direction="LR") 

class watsonx(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(watsonx, self).__init__(label, sublabel=sublabel, 
                                      linecolor=Colors.lines["network"], fillcolor=Colors.fills["white"],
                                      icon="watsonx", direction="LR") 

class AuthorizationBoundary(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(AuthorizationBoundary, self).__init__(label, sublabel=sublabel, 
                                                    linecolor=Colors.lines["security"], fillcolor=Colors.fills["security"],
                                                    icon="Authorization Boundary", direction="LR") 

class PointOfPresence(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(PointOfPresence, self).__init__(label, sublabel=sublabel, 
                                              linecolor=Colors.lines["location"], fillcolor=Colors.fills["white"],
                                              icon="Point of Presence", direction="LR") 

class Region(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(Region, self).__init__(label, sublabel=sublabel, 
                                      linecolor=Colors.lines["location"], fillcolor=Colors.fills["location"], 
                                      icon="Region", direction=direction) 

# Core Group Aliases
Enterprise = EnterpriseNetwork
Public = PublicNetwork
PoP = PointOfPresence


# Control Groups

class _ControlGroup(_Grouping):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", icon="", direction="LR"):
        super(_ControlGroup, self).__init__(label, sublabel=sublabel, 
                                            linecolor=linecolor, fillcolor=fillcolor, 
                                            shape="zone", icon=icon, direction=direction)

class AccessGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(AccessGroup, self).__init__(label, sublabel=sublabel,
                                          linecolor=Colors.lines["security"], fillcolor=Colors.fills["none"],
                                          icon="Access Group", direction=direction)

class AccountGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(AccountGroup, self).__init__(label, sublabel=sublabel,
                                           linecolor=Colors.lines["security"], fillcolor=Colors.fills["none"],
                                           icon="Account Group", direction=direction)

class InstanceGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(InstanecGroup, self).__init__(label, sublabel=sublabel,
                                            linecolor=Colors.lines["compute"], fillcolor=Colors.fills["none"],
                                            icon="Instance Group", direction=direction)

class PlacementGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(PlacementGroup, self).__init__(label, sublabel=sublabel,
                                             linecolor=Colors.lines["compute"], fillcolor=Colors.fills["none"],
                                             icon="Placement Group", direction=direction)

class ResourceGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ResourceGroup, self).__init__(label, sublabel=sublabel,
                                            linecolor=Colors.lines["security"], fillcolor=Colors.fills["none"],
                                            icon="Resource Group", direction=direction)

class SecurityGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(SecurityGroup, self).__init__(label, sublabel=sublabel,
                                            linecolor=Colors.lines["security"], fillcolor=Colors.fills["none"],
                                            icon="Security Group", direction=direction)

class AvailabilityZone(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super(AvailabilityZone, self).__init__(label, sublabel=sublabel,
                                               linecolor=Colors.lines["location"], fillcolor=Colors.fills["location"], 
                                               icon="Availability Zone", direction=direction) 

# Zone Group Aliases
Zone = AvailabilityZone


# Expanded Groups

class _ExpandedGroups(_IBMExpanded):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", icon="", direction="LR"):
        super(_ExpandedGroups, self).__init__(label, sublabel=sublabel, 
                                              linecolor=linecolor, fillcolor=fillcolor, 
                                              shape="epnode", icon=icon, direction=direction)

class ExpandedVirtualServer(_ExpandedGroups):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ExpandedVirtualServer, self).__init__(label, sublabel=sublabel,
                                                    linecolor=Colors.lines["compute"], fillcolor=Colors.fills["compute"],
                                                    icon="Virtual Server", direction="LR")

class ExpandedBareMetalServer(_ExpandedGroups):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ExpandedBareMetalServer, self).__init__(label, sublabel=sublabel,
                                                      linecolor=Colors.lines["compute"], fillcolor=Colors.fills["compute"],
                                                      icon="Bare Metal Server", direction="LR")

class ExpandedPowerVirtualServer(_ExpandedGroups):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ExpandedPowerVirtualServer, self).__init__(label, sublabel=sublabel,
                                                         linecolor=Colors.lines["compute"], fillcolor=Colors.fills["compute"],
                                                         icon="Power Virtual Server", direction="LR")

class ExpandedClassicVirtualServer(_ExpandedGroups):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ExpandedClassicVirtualServer, self).__init__(label, sublabel=sublabel,
                                                           linecolor=Colors.lines["compute"], fillcolor=Colors.fills["compute"],
                                                           icon="Classic Virtual Server", direction="LR")

class ExpandedClassicBareMetalServer(_ExpandedGroups):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ExpandedClassicBareMetalServer, self).__init__(label, sublabel=sublabel,
                                                             linecolor=Colors.lines["compute"], fillcolor=Colors.fills["compute"],
                                                             icon="Classic Bare Metal Server", direction="LR")

class ExpandedApplication(_ExpandedGroups):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ExpandedApplication, self).__init__(label, sublabel=sublabel,
                                                  linecolor=Colors.lines["applications"], fillcolor=Colors.fills["applications"],
                                                  icon="Application", direction="LR")

class ExpandedMicroservice(_ExpandedGroups):
    def __init__(self, label, sublabel="", direction="LR"):
        super(ExpandedMicroservice, self).__init__(label, sublabel=sublabel,
                                                   linecolor=Colors.lines["applications"], fillcolor=Colors.fills["applications"],
                                                   icon="Microservice", direction="LR")

# Expanded Group Aliases
