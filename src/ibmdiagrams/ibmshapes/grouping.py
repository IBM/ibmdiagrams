# @file grouping.py
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

from . import _IBMGrouping
from .colors import Colors

class _Grouping(_IBMGrouping):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", shape="", icon="", direction="LR"):
        super(_Grouping, self).__init__(label, sublabel=sublabel, 
                                        linecolor=linecolor, fillcolor=fillcolor,
                                        shape=shape, icon=icon, direction=direction)

# Core Groups

class _CoreGroups(_Grouping):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", icon="", direction="LR"):
        super(_CoreGroups, self).__init__(label, sublabel=sublabel,
                                          linecolor=linecolor, fillcolor=fillcolor, 
                                          shape = "gploc" if icon == "" else "ploc",
                                          icon=icon, direction=direction)

class PrescribedLocation(_CoreGroups):
    def __init__(self, label, sublabel="", linecolor=Colors.lines["backend"], fillcolor=Colors.fills["white"], icon="", direction="LR"):
        super(PrescribedLocation, self).__init__(label, sublabel=sublabel,
                                                 linecolor=linecolor, fillcolor=fillcolor,
                                                 icon=icon, direction=direction)

# Core Group Aliases
PLocation = PrescribedLocation


# Control Groups

class _ControlGroups(_Grouping):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", icon="", direction="LR"):
        super(_ControlGroups, self).__init__(label, sublabel=sublabel, 
                                             linecolor=linecolor, fillcolor=fillcolor,
                                             shape = "gzone" if icon == "" else "zone",
                                             icon=icon, direction=direction)

class Zone(_ControlGroups):
    def __init__(self, label, sublabel="", linecolor=Colors.lines["backend"], fillcolor="none", icon="", direction="LR"):
        super(Zone, self).__init__(label, sublabel=sublabel, 
                                   linecolor=linecolor, fillcolor=fillcolor,
                                   icon=icon, direction=direction)

# Control Group Aliases
