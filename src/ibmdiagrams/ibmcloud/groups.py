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

from . import _IBMExpanded, _IBMGrouping  # noqa: F401
from .colors import Colors


class _Grouping(_IBMGrouping):
    def __init__(
        self, label, sublabel="", linecolor="", fillcolor="", shape="", icon="", direction="LR"
    ):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=linecolor,
            fillcolor=fillcolor,
            shape=shape,
            icon=icon,
            direction=direction,
        )


####################################
# Core Groups
####################################


class _CoreGroup(_Grouping):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", icon="", direction="LR"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=linecolor,
            fillcolor=fillcolor,
            shape="ploc",
            icon=icon,
            direction=direction,
        )


class IBMCloud(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="IBM Cloud Group",
            direction=direction,
        )


class VPC(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="VPC Group",
            direction=direction,
        )


class Subnet(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="Subnet Group",
            direction=direction,
        )


class EnterpriseNetwork(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="Enterprise Network Group",
            direction=direction,
        )


class PublicNetwork(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="Public Network Group",
            direction=direction,
        )


class CloudServices(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="Cloud Services Group",
            direction=direction,
        )


# class VPCServices(_CoreGroup):
#    def __init__(self, label, sublabel="", direction="LR", background="network"):
#         super().__init__(
#             label=label,
#             sublabel=sublabel,
#             linecolor=Colors.lines["network"],
#             fillcolor=Colors.fills[background],
#             icon="VPC Services Group",
#             direction=direction,
#         )


class InternetServices(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="Internet Services Group",
            direction=direction,
        )


class OverlayNetwork(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="Overlay Network Group",
            direction=direction,
        )


class PowerWorkspace(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="Power Workspace Group",
            direction=direction,
        )


class ZSystem(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="compute"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills[background],
            icon="Z System Group",
            direction=direction,
        )


class Internet(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="Internet Group",
            direction=direction,
        )


class VLAN(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="VLAN Group",
            direction=direction,
        )


class ClassicVLAN(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="Classic VLAN Group",
            direction=direction,
        )


class ClassicInfrastructure(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="network"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["network"],
            fillcolor=Colors.fills[background],
            icon="Classic Infrastructure Group",
            direction=direction,
        )


class OpenShift(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="compute"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills[background],
            icon="OpenShift Group",
            direction=direction,
        )


class KubernetesServices(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="compute"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills[background],
            icon="Kubernetes Service Group",
            direction=direction,
        )


class ZContainers(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="compute"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills[background],
            icon="Z Containers Group",
            direction=direction,
        )


class watsonx(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="applications"):
        super().__init__(
            label,
            sublabel=sublabel,
            linecolor=Colors.lines["applications"],
            fillcolor=Colors.fills[background],
            icon="watsonx Group",
            direction=direction,
        )


class watsonxCodeAssistant(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="applications"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["applications"],
            fillcolor=Colors.fills[background],
            icon="watsonx Code Assistant Group",
            direction=direction,
        )


class watsonxZCodeAssistant(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="applications"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["applications"],
            fillcolor=Colors.fills[background],
            icon="watsonx Z Code Assistant Group",
            direction=direction,
        )


class AuthorizationBoundary(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="security"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["security"],
            fillcolor=Colors.fills[background],
            icon="Authorization Boundary Group",
            direction=direction,
        )


class PointOfPresence(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="white"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["location"],
            fillcolor=Colors.fills[background],
            icon="Point of Presence Group",
            direction=direction,
        )


class Region(_CoreGroup):
    def __init__(self, label, sublabel="", direction="LR", background="white"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["location"],
            fillcolor=Colors.fills[background],
            icon="Region Group",
            direction=direction,
        )


# Core Group Aliases
Enterprise = EnterpriseNetwork
Public = PublicNetwork
PoP = PointOfPresence

####################################
# Control Groups
####################################


class _ControlGroup(_Grouping):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", icon="", direction="LR"):
        super().__init__(
            label,
            sublabel=sublabel,
            linecolor=linecolor,
            fillcolor=fillcolor,
            shape="zone",
            icon=icon,
            direction=direction,
        )


class AccessGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["security"],
            fillcolor=Colors.fills["none"],
            icon="Access Group",
            direction=direction,
        )


class AccountGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["security"],
            fillcolor=Colors.fills["none"],
            icon="Account Group",
            direction=direction,
        )


class InstanceGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills["none"],
            icon="Instance Group",
            direction=direction,
        )


class PlacementGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills["none"],
            icon="Placement Group",
            direction=direction,
        )


class LayoutGroup(_Grouping):
    """
    A layout group component that provides positioning without visual boundaries.

    Use LayoutGroup when you need to organize elements hierarchically for layout and
    positioning purposes but don't want any visual container styling (no borders, icons,
    or fill colors) in the final diagram output.

    Args:
        direction: Layout direction for child elements ("LR" for left-to-right, "TB" for top-to-bottom)

    Example:
        with LayoutGroup(direction="TB"):
            server1 = VirtualServer("Server 1")
            server2 = VirtualServer("Server 2")
    """

    def __init__(self, *, direction="LR"):
        # Call base Group class directly to access hideicon parameter
        from ibmdiagrams import Group

        Group.__init__(
            self,
            label="",
            sublabel="",
            linecolor="",
            fillcolor=Colors.fills["none"],
            shape="zone",
            icon="",
            hideicon="true",
            direction=direction,
        )


class ResourceGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["security"],
            fillcolor=Colors.fills["none"],
            icon="Resource Group",
            direction=direction,
        )


class SecurityGroup(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["security"],
            fillcolor=Colors.fills["none"],
            icon="Security Group",
            direction=direction,
        )


class AvailabilityZone(_ControlGroup):
    def __init__(self, label, sublabel="", direction="LR", background="white"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["location"],
            fillcolor=Colors.fills[background],
            icon="Classic Bare Metal Server Icon",
            direction=direction,
        )


# Zone Group Aliases
Zone = AvailabilityZone


####################################
# Expanded Groups
####################################

# class _ExpandedGroups(_IBMExpanded):
#    def __init__(self, label, sublabel="", linecolor="", fillcolor="", icon="", direction="LR"):
#        super().__init__(
#             label=label,
#             sublabel=sublabel,
#             linecolor=linecolor,
#             fillcolor=fillcolor,
#             shape="epnode",
#             icon=icon,
#             direction=direction,
#         )


class _ExpandedGroup(_Grouping):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", icon="", direction="LR"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=linecolor,
            fillcolor=fillcolor,
            shape="epnode",
            icon=icon,
            direction=direction,
        )


class ExpandedVirtualServer(_ExpandedGroup):
    def __init__(self, label, sublabel="", direction="LR", background="white"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills[background],
            icon="Virtual Server Icon",
            direction=direction,
        )


class ExpandedPowerVirtualServer(_ExpandedGroup):
    def __init__(self, label, sublabel="", direction="LR", background="white"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills[background],
            icon="Power Virtual Server Icon",
            direction=direction,
        )


class ExpandedClassicVirtualServer(_ExpandedGroup):
    def __init__(self, label, sublabel="", direction="LR", background="white"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills[background],
            icon="Classic Virtual Server Icon",
            direction=direction,
        )


class ExpandedBareMetalServer(_ExpandedGroup):
    def __init__(self, label, sublabel="", direction="LR", background="white"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills[background],
            icon="Bare Metal Server Icon",
            direction=direction,
        )


class ExpandedClassicBareMetalServer(_ExpandedGroup):
    def __init__(self, label, sublabel="", direction="LR", background="white"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["compute"],
            fillcolor=Colors.fills[background],
            icon="Classic Bare Metal Server Icon",
            direction=direction,
        )


class ExpandedApplication(_ExpandedGroup):
    def __init__(self, label, sublabel="", direction="LR", background="white"):
        super().__init__(
            label=label,
            sublabel=sublabel,
            linecolor=Colors.lines["applications"],
            fillcolor=Colors.fills[background],
            icon="Application Icon",
            direction=direction,
        )


class ExpandedMicroservice(_ExpandedGroup):
    def __init__(self, label, sublabel="", direction="LR", background="white"):
        super().__init__(
            label,
            sublabel=sublabel,
            linecolor=Colors.lines["applications"],
            fillcolor=Colors.fills[background],
            icon="Microservice Icon",
            direction=direction,
        )


# Expanded Group Aliases
