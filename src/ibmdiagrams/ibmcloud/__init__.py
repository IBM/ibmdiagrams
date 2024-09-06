# @file __init__.py
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

from ibmdiagrams import Diagram, Group, Item, Edge

class _IBMDiagram(Diagram):
    def __init__(self, name, filename="", direction="", output="", provider="ibm", icontype=""):
        super(_IBMDiagram, self).__init__(name=name, filename=filename, output=output,
                                          direction=direction, 
                                          icontype=icontype)

class _IBMGroup(Group):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", shape="", icon="", fontname="IBM Plex Sans", fontsize=14, direction=""):
        super(_IBMGroup, self).__init__(label=label, sublabel=sublabel, 
                                        linecolor=linecolor, fillcolor=fillcolor,
                                        shape=shape, icon=icon, 
                                        fontname=fontname, fontsize=fontsize,
                                        direction=direction) 

class _IBMItem(Item):
    def __init__(self, label, sublabel="", linecolor="", fillcolor="", shape="", icon="", fontname="IBM Plex Sans", fontsize=14):
        super(_IBMItem, self).__init__(label=label, sublabel=sublabel, 
                                       linecolor=linecolor, fillcolor=fillcolor, 
                                       shape=shape, icon=icon, 
                                       fontname=fontname, fontsize=fontsize)

class _IBMEdge(Edge):
    def __init__(self, label="", startarrow="", endarrow="", startfill=True, endfill=True, fontname="IBM Plexc Sans", fontsize=14):
        super(_IBMEdge, self).__init__(label=label, 
                                       startarrow=startarrow, endarrow=endarrow, 
				       startfill=startfill, endfill=endfill,
                                       fontname=fontname, fontsize=fontsize)
