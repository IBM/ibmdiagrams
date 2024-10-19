# @file connectors.py
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

from . import _IBMConnector
from .colors import Colors

# linetype = Solid, Dashed, Dotted, Double, Tunnel
# startarrow/endarrow = Arrow, OpenArrow, Circle, OpenCircle, Diamond, OpenDiamond

class _Connector(_IBMConnector):
    def __init__(self, label="", startarrow="", endarrow="", linetype="solid", linewidth=1, linecolor="#000000", fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(_Connector, self).__init__(label=label,
                                         startarrow=startarrow, endarrow=endarrow,
                                         linetype=linetype, linewidth=linewidth, linecolor=linecolor,
                                         fontname=fontname, fontsize=fontsize,
                                         operator=operator, sourceid=sourceid, targetid=targetid)

class SolidEdge(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(SolidEdge, self).__init__(label,
                                        startarrow=startarrow, endarrow=endarrow,
                                        linetype="solid", linewidth=2, linecolor="#000000",
                                        fontname=fontname, fontsize=fontsize,
                                        operator=operator, sourceid=sourceid, targetid=targetid)

class PrivateSolidEdge(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(PrivateSolidEdge, self).__init__(label,
                                               startarrow=startarrow, endarrow=endarrow,
                                               linetype="solid", linewidth=2, linecolor="#198038",
                                               fontname=fontname, fontsize=fontsize,
                                               operator=operator, sourceid=sourceid, targetid=targetid)

class PublicSolidEdge(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(PublicSolidEdge, self).__init__(label,
                                              startarrow=startarrow, endarrow=endarrow,
                                              linetype="solid", linewidth=2, linecolor="#0F62F3",
                                              fontname=fontname, fontsize=fontsize,
                                              operator=operator, sourceid=sourceid, targetid=targetid)

class DashedEdge(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(DashedEdge, self).__init__(label,
                                         startarrow=startarrow, endarrow=endarrow,
                                         linetype="dashed", linewidth=2, linecolor="#000000",
                                         fontname=fontname, fontsize=fontsize,
                                         operator=operator, sourceid=sourceid, targetid=targetid)

class DottedEdge(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(DottedEdge, self).__init__(label,
                                         startarrow=startarrow, endarrow=endarrow,
                                         linetype="dotted", linewidth=2, linecolor="#000000",
                                         fontname=fontname, fontsize=fontsize,
                                         operator=operator, sourceid=sourceid, targetid=targetid)

class DoubleEdge(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(DoubleEdge, self).__init__(label,
                                         startarrow=startarrow, endarrow=endarrow,
                                         linetype="double", linewidth=2, linecolor="#000000",
                                         fontname=fontname, fontsize=fontsize,
                                         operator=operator, sourceid=sourceid, targetid=targetid)

class TunnelEdge(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(TunnelEdge, self).__init__(label,
                                         startarrow=startarrow, endarrow=endarrow,
                                         linetype="tunnel", linewidth=2, linecolor="#FFCCCC",
                                         fontname=fontname, fontsize=fontsize,
                                         operator=operator, sourceid=sourceid, targetid=targetid)


# Aliases
