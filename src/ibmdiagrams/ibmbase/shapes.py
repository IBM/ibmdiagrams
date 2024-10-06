# @file shapes.py
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

from .types import Types

class Shapes:
   common = None
   types = None

   def __init__(self, common):
      self.common = common
      self.types = Types(common)

   def buildStaticShape(self, id, properties, x, y, width, height, meta, items):
      node = self.types.buildStaticShape(id, properties, x, y, width, height, meta, items)
      return node

   def buildShape(self, id, properties, x, y, width, height, meta):
      node = self.types.buildShape(id, properties, x, y, width, height, meta)
      return node

   def buildLink(self, id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta):
       return self.types.buildLink(id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta)

   def buildSolidLink(self, id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta):
       return self.types.buildSolidLink(id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta)

   def buildDoubleArrow(self, id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta):
       return self.types.buildSolidLinkDoubleArrow(id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta)

   def buildSingleArrow(self, id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta):
       return self.types.buildSolidLinkSingleArrow(id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta)

   def buildXML(self, vpcdata, pagename):
      self.types.buildXML(vpcdata, self.types.buildPage(pagename))

   def dumpXML(self, file, folder):
      self.types.dumpXML(file, folder)

   def resetXML(self):
      self.types.resetXML()
