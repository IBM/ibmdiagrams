# @file collapsed.py
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

class _Actors(_IBMCollapsed):
    def __init__(self, label, sublabel="", linecolor=Colors.lines["backend"], icon=""):
        super(_Actors, self).__init__(label=label, sublabel=sublabel, 
                                      linecolor=linecolor, 
                                      shape="actor", icon=icon)

class Actor(_Actors):
    def __init__(self, label, sublabel="", linecolor="", icon="Undefined Icon"):
        super(Actor, self).__init__(label, sublabel=sublabel, linecolor=linecolor, icon=icon)


class _PrescribedNodes(_IBMCollapsed):
    def __init__(self, label, sublabel="", linecolor="", icon=""):
        super(_PrescribedNodes, self).__init__(label=label, sublabel=sublabel, 
                                               linecolor=linecolor, 
                                               shape="pnode", icon=icon)

class PrescribedNode(_PrescribedNodes):
    def __init__(self, label, sublabel="", linecolor=Colors.lines["backend"], icon="Undefined Icon"):
        super(PrescribedNode, self).__init__(label, sublabel=sublabel, linecolor=linecolor, icon=icon)

# Aliases
PNode = PrescribedNode
