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

# dashstyle = Solid, Dashed1 (large), Dashed2 (small), Dotted, Double, Tunnel
# startarrow/endarrow = T, Arrow, OpenArrow, Circle, OpenCircle, Diamond, OpenDiamond

class _Connector(_IBMConnector):
    def __init__(self, label="", startarrow="arrow", endarrow="arrow", startfill=True, endfill=True, fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(_Connector, self).__init__(label=label,
                                         startarrow=startarrow, endarrow=endarrow,
                                         startfill=startfill, endfill=endfill,
                                         fontname=fontname, fontsize=fontsize,
                                         operator=operator, sourceid=sourceid, targetid=targetid)

class SolidLine(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", startfill=True, endfill=True, fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(SolidLine, self).__init__(label,
                                        startarrow=startarrow, endarrow=endarrow,
                                        startfill=startfill, endfill=endfill,
                                        fontname=fontname, fontsize=fontsize,
                                        operator=operator, sourceid=sourceid, targetid=targetid)

class DashedLine(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", startfill=True, endfill=True, fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(DashedLine, self).__init__(label,
                                         startarrow=startarrow, endarrow=endarrow,
                                         startfill=startfill, endfill=endfill,
                                         fontname=fontname, fontsize=fontsize,
                                         operator=operator, sourceid=sourceid, targetid=targetid)

class DottedLine(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", startfill=True, endfill=True, fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(DottedLine, self).__init__(label,
                                         startarrow=startarrow, endarrow=endarrow,
                                         startfill=startfill, endfill=endfill,
                                         fontname=fontname, fontsize=fontsize,
                                         operator=operator, sourceid=sourceid, targetid=targetid)

class DoubleLine(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", startfill=True, endfill=True, fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(DoubleLine, self).__init__(label,
                                         startarrow=startarrow, endarrow=endarrow,
                                         startfill=startfill, endfill=endfill,
                                         fontname=fontname, fontsize=fontsize,
                                         operator=operator, sourceid=sourceid, targetid=targetid)

class TunnelLine(_Connector):
    def __init__(self, label="", startarrow="", endarrow="", startfill=True, endfill=True, fontname="IBM Plex Sans", fontsize=14, operator="", sourceid=None, targetid=None):
        super(TunnelLine, self).__init__(label,
                                         startarrow=startarrow, endarrow=endarrow,
                                         startfill=startfill, endfill=endfill,
                                         fontname=fontname, fontsize=fontsize,
                                         operator=operator, sourceid=sourceid, targetid=targetid)


# Aliases
Line = SolidLine
