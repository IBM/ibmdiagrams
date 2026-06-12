# @file expanded.py
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

from . import _IBMExpanded
from .colors import Colors

# Expanded Groups

class _ExpandedGroups(_IBMExpanded):
    def __init__(self, label, sublabel="", linecolor=Colors.lines["backend"], fillcolor=Colors.fills["white"], icon="", direction="LR"):
        super(_ExpandedGroups, self).__init__(label, sublabel=sublabel,
                                              linecolor=linecolor, fillcolor=fillcolor, 
                                              shape="epnode",  
                                              icon=icon, direction=direction)

class ExpandedPrescribedNode(_ExpandedGroups):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", icon="Undefined Icon", direction="LR"):
        super(ExpandedPrescribedNode, self).__init__(label, sublabel=sublabel, 
                                                     linecolor=linecolor, fillcolor=fillcolor,
                                                     icon=icon, direction=direction)

# Expanded Group Aliases
ExpandedPNode = ExpandedPrescribedNode
