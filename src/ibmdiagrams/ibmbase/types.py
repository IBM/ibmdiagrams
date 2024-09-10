# @file types.py
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

import random
import time

from uuid import uuid4

from .common import Common

from .constants import ShapeKind, ShapeStyle, StaticShapeStyle
from .elements import Elements

@staticmethod
def randomid():
   return uuid4().hex

class Types:
   common = None
   data = None
   elements = None
   icons = None

   def __init__(self, common):
      self.common = common
      self.data = {'header': {'type': 'device',
                              'compressed': 'false'}}
      self.elements = Elements(self.data)
      random.seed(time.time())

   def buildLink(self, id, label, source, target, startarrow, endarrow, startfill, endfill, meta):
      style = 'dashed=0;'

      if startarrow != "":
         style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
         if startarrow == "oval":
           style += "sourcePerimeterSpacing=4;"

      if endarrow != "":
         style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
         if endarrow == "oval":
           style += "targetPerimeterSpacing=4;"

      data = {'header': {'id': id,
                         'label': ''},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
              'geo':    {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildSolidLink(self, id, label, source, target, startarrow, endarrow, startfill, endfill, meta):
      style = 'dashed=0;'

      if startarrow == "":
         style += 'startArrow=none;startFill=0;'
      else:
         style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
         if startarrow == "oval":
           style += "sourcePerimeterSpacing=4;"

      if endarrow == "":
         style += 'endArrow=none;endFill=0;'
      else:
         style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
         if endarrow == "oval":
           style += "targetPerimeterSpacing=4;"

      data = {'header': {'id': id,
                         'label': label},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
              'geo':    {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildSolidLinkSingleArrow(self, id, label, source, target, startarrow, endarrow, startfill, endfill, meta):
      style = 'dashed=0;'

      if startarrow != "":
         style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
         if startarrow == "oval":
           style += "sourcePerimeterSpacing=4;"

      if endarrow != "":
         style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
         if endarrow == "oval":
           style += "targetPerimeterSpacing=4;"

      data = {'header': {'id': id,
                         'label': label},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
               'geo':   {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildSolidLinkDoubleArrow(self, id, label, source, target, startarrow, endarrow, startfill, endfill, meta):
      style = 'dashed=0;'

      if startarrow != "":
         style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
         if startarrow == "oval":
           style += "sourcePerimeterSpacing=4;"

      if endarrow != "":
         style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
         if endarrow == "oval":
           style += "targetPerimeterSpacing=4;"

      data = {'header': {'id': id,
                         'label': label},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
              'geo':    {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildStaticGroupSidebar(self, parentid, node):
      linecolor = node["linecolor"]
      style = 'strokeColor=' + linecolor + ';fillColor=' + linecolor +';'

      header = {'id': randomid(),
                'placeholders': '1'}

      cell = {'parent': parentid,
              'style': style,
              'vertex': '1'}

      geo = {'x': str(0),
             'y': str(0),
             'width': str(4),
             'height': str(48),
             'as': 'geometry'}

      props = {}

      data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props}

      return data

   def buildStaticGroupIcon(self, parentid, node):
      image = node["image"]
      style = "shape=image;aspect=fixed;" + image

      header = {'id': randomid(),
                'placeholders': '1'}

      cell = {'parent': parentid,
              'style': style,
              'vertex': '1'}

      geo = {'x': str(12),
             'y': str(12),
             'width': str(24),
             'height': str(24),
             'as': 'geometry'}

      props = {}

      data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props}

      return data

   def buildStaticExpandedIcon(self, parentid, node):
      image = node["image"]
      #style = "shape=image;aspect=fixed;" + StaticShapeStyle.PNODE.value + image
      style = "shape=image;aspect=fixed;" + image

      header = {'id': randomid(),
                'placeholders': '1'}

      cell = {'parent': parentid,
              'style': style,
              'vertex': '1'}

      geo = {'x': str(0),
             'y': str(0),
             'width': str(48),
             'height': str(48),
             'as': 'geometry'}

      props = {}

      data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props}

      return data

   def buildStaticShape(self, id, node, x, y, width, height, meta, items):
      name = node["label"]
      subname = node["sublabel"]
      shape = node["shape"].lower()

      linecount = 0
      if len(name) > 0:
         linecount = linecount + 1 + name.count("<br")
      if len(subname) > 0:
         linecount = linecount + 1 + subname.count("<br")

      if shape == "actor":
         image = node["image"]
         style = "shape=image;aspect=fixed;" + StaticShapeStyle.ACTOR.value + image
      elif shape == "pnode":
         image = node["image"]
         style = "shape=image;aspect=fixed;" + StaticShapeStyle.PNODE.value + image
      elif shape == "epnode":
         if linecount == 0 or linecount == 1:
            style = StaticShapeStyle.EPNODE1.value
         elif linecount == 2:
            style = StaticShapeStyle.EPNODE2.value
         else:
           style = StaticShapeStyle.EPNODE3.value
         shapenode = self.buildStaticExpandedIcon(id, node) 
         items.append(shapenode)
      elif shape == "ploc":
         if linecount == 0 or linecount == 1:
            style = StaticShapeStyle.PLOC1.value
         elif linecount == 2:
            style = StaticShapeStyle.PLOC2.value
         else:
           style = StaticShapeStyle.PLOC3.value
         shapenode = self.buildStaticGroupSidebar(id, node) 
         items.append(shapenode)
         shapenode = self.buildStaticGroupIcon(id, node) 
         items.append(shapenode)
      elif shape == "gploc":
         if linecount == 0 or linecount == 1:
            style = StaticShapeStyle.GPLOC1.value
         elif linecount == 2:
            style = StaticShapeStyle.GPLOC2.value
         else:
           style = StaticShapeStyle.GPLOC3.value
         shapenode = self.buildStaticGroupSidebar(id, node) 
         items.append(shapenode)
      elif shape == "zone":
         if linecount == 0 or linecount == 1:
            style = StaticShapeStyle.ZONE1.value
         elif linecount == 2:
            style = StaticShapeStyle.ZONE2.value
         else:
           style = StaticShapeStyle.ZONE3.value
         shapenode = self.buildStaticGroupIcon(id, node) 
         items.append(shapenode)
      elif shape == "gzone":
         if linecount == 0 or linecount == 1:
            style = StaticShapeStyle.GZONE1.value
         elif linecount == 2:
            style = StaticShapeStyle.GZONE2.value
         else:
           style = StaticShapeStyle.GZONE3.value
      else:
         style = StaticShapeStyle.PNODE.value

      if shape != "actor" and shape != "pnode":
         linecolor = node["linecolor"]
         styleStroke = "strokeColor=" + linecolor + ';' 
         style = style.replace("%STROKE", styleStroke)

         fillcolor = node["fillcolor"]
         if fillcolor:
            styleFill = "fillColor=" + fillcolor + ';' 
         else:
            styleFill = "fillColor=none;" 
         style = style.replace("%FILL", styleFill)

      parentid = node["parentid"]
      parentid = '1' if parentid == None else parentid

      labelsize = 20

      if len(name) > 0:
         name = self.common.truncateText(name, labelsize, '<br>')

      if len(subname) > 0:
         subname = self.common.truncateText(subname, labelsize, '<br>')

      shapelabel = "<b style='font-weight:600'>" + name + "</b><br>" + subname

      header = {'id': id,
                'label': shapelabel,
                'placeholders': '1'}

      cell = {'parent': parentid,
              'style': style,
              'vertex': '1'}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(width),
             'height': str(height),
             'as': 'geometry'}

      props = {}

      if meta != None:
         props.update(meta)

      data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props}

      return data

   def buildShape(self, id, node, x, y, width, height, meta):
      shape = node["shape"].lower()
      name = node["label"]
      subname = node["sublabel"]
      shape = node["shape"].lower()

      linecount = 0
      if len(name) > 0:
         linecount = linecount + 1 + name.count("<br")
      if len(subname) > 0:
         linecount = linecount + 1 + subname.count("<br")

      if shape == "actor":
         style = ShapeStyle.ACTOR.value
      elif shape == "pnode":
         style = ShapeStyle.PNODE.value
      elif shape == "epnode":
         if linecount == 0 or linecount == 1:
            style = ShapeStyle.EPNODE1.value
         elif linecount == 2:
            style = ShapeStyle.EPNODE2.value
         else:
           style = ShapeStyle.EPNODE3.value
      elif shape == "ploc":
         if linecount == 0 or linecount == 1:
            style = ShapeStyle.PLOC1.value
         elif linecount == 2:
            style = ShapeStyle.PLOC2.value
         else:
           style = ShapeStyle.PLOC3.value
      elif shape == "gploc":
         if linecount == 0 or linecount == 1:
            style = ShapeStyle.GPLOC1.value
         elif linecount == 2:
            style = ShapeStyle.GPLOC2.value
         else:
           style = ShapeStyle.GPLOC3.value
      elif shape == "zone":
         if linecount == 0 or linecount == 1:
            style = ShapeStyle.ZONE1.value
         elif linecount == 2:
            style = ShapeStyle.ZONE2.value
         else:
           style = ShapeStyle.ZONE3.value
      elif shape == "gzone":
         if linecount == 0 or linecount == 1:
            style = ShapeStyle.GZONE1.value
         elif linecount == 2:
            style = ShapeStyle.GZONE2.value
         else:
           style = ShapeStyle.GZONE3.value
      else:
         style = ShapeStyle.PNODE.value

      linecolor = node["linecolor"]
      styleStroke = "strokeColor=" + linecolor + ';' 
      style = style.replace("%STROKE", styleStroke)

      fillcolor = node["fillcolor"]
      if fillcolor:
         #style += "fillColor=" + fillcolor + ';' 
         styleFill = "fillColor=" + fillcolor + ';' 
      else:
         #style += "fillColor=none;" 
         styleFill = "fillColor=none;" 
      style = style.replace("%FILL", styleFill)

      name = node["label"]
      subname = node["sublabel"]

      parentid = node["parentid"]
      parentid = '1' if parentid == None else parentid

      image = node["image"] 
      if image != "":
         style = ShapeStyle.IMAGE.value + image
      else:
         icon = node["icon"]
         if icon != "":
            styleIcon = 'icon=' + icon + ';'
         else:
            styleIcon = ""
         style = style.replace("%ICON", styleIcon)

      labelsize = 20

      if len(name) > 0:
         name = self.common.truncateText(name, labelsize, '<br>')

      if len(subname) > 0:
         subname = self.common.truncateText(subname, labelsize, '<br>')

      shapelabel = "<b style='font-weight:600'>" + name + "</b><br>" + subname

      header = {'id': id,
                'label': shapelabel,
                'placeholders': '1'}

      cell = {'parent': parentid,
              'style': style,
              'vertex': '1'}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(width),
             'height': str(height),
             'as': 'geometry'}

      props = {}

      if meta != None:
         props.update(meta)

      data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props}

      return data

   def buildValue(self, id, parentid, name, parent, subname, text, x, y, width, height):
      shape = ibmshapes['text']
      style = shape['style']  
      data = {'cell': {'id': id,
                       'value': text,
                       'style': style,
                       'parent': parentid,
                       'vertex': '1'},
              'geo':  {'x': str(x),
                       'y': str(y),
                       'width': str(width),
                       'height': str(height),
                       'as': 'geometry'}}
      return data

   def buildPage(self, name):
      data = {'header': {'id': self.common.compress(name),
                         'name': name},
              'graph':  {'dx': '1326',
                         'dy': '846',
                         'grid': '1',
                         'gridSize': '10',
                         'guides': '1',
                         'tooltips': '1',
                         'connect': '1',
                         'arrows': '1',
                         'fold': '1',
                         'page': '1',
                         'pageScale': '1',
                         'pageWidth': '850',
                         'pageHeight': '1100',
                         'math': '0',
                         'shadow': '0'},
              'cell0':  {'id': '0'},
              'cell1':  {'id': '1',
                         'parent': '0'}}
      return data

   def buildXML(self, vpcdata, pagedata):
      self.elements.buildXML(vpcdata, pagedata)

   def dumpXML(self, file, folder):
      self.elements.dumpXML(file, folder)

   def resetXML(self):
      self.data = {'header': {'type': 'device',
                         'compressed': 'false'}}
      self.elements.resetXML(self.data)
