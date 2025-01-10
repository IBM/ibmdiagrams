#h @file types.py
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

   def buildLink(self, id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta):
      if linetype.upper() == "DASHED":
         style = 'dashed=1;'
      elif linetype.upper() == "LONGDASHED":
         style = 'dashed=1;dashPattern=7 2;'
      elif linetype.upper() == "DOTTED":
         style = 'dashed=1;dashPattern=1 2;'
      else:
         style = 'dashed=0;'

      style += 'strokeWidth=' + str(linewidth) + ';fontFamily=' + fontname + ';fontSize=' + str(fontsize) + ';'

      # Note: Connectors overlap with edgeStyle so using direct point-to-point but need better connector layout.
      #style += 'html=1;rounded=0;jumpStyle=gap;edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;'
      style += 'html=1;rounded=0;jumpStyle=gap;'

      if linetype.upper() == "DOUBLE":
         style += 'shape=link;startArrow=none;endArrow=none;strokeColor=' + linecolor + ';'
      elif linetype.upper() == "TUNNEL":
         style += 'shape=flexArrow;startArrow=none;endArrow=none;strokeColor=none;fillColor=' + linecolor + ';'
      else:
         style += 'strokeColor=' + linecolor + ';'
         if startarrow == "":
            style += 'startArrow=none;startFill=0;'
         else:
            style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
            if startarrow == "oval":
              # Note: Default is for oval to be centered on border so add space to be next to border per design center.
              style += "sourcePerimeterSpacing=3;"
         if endarrow == "":
            style += 'endArrow=none;endFill=0;'
         else:
            style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
            if endarrow == "oval":
              # Note: Default is for oval to be centered on border so add space to be next to border per design center.
              style += "targetPerimeterSpacing=3;"

      data = {'header': {'id': id,
                         'label': ''},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
              'geo':    {'relative': '1',
                         'as': 'geometry'},
              'props':  {},
              'point':  {}}
      return data

   def buildSolidLink(self, id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta):
      if linetype.upper() == "DASHED":
         style = 'dashed=1;'
      elif linetype.upper() == "LONGDASHED":
         style = 'dashed=1;dashPattern=7 2;'
      elif linetype.upper() == "DOTTED":
         style = 'dashed=1;dashPattern=1 2;'
      else:
         style = 'dashed=0;'

      style += 'strokeWidth=' + str(linewidth) + ';fontFamily=' + fontname + ';fontSize=' + str(fontsize) + ';'

      # Note: Connectors overlap with edgeStyle so using direct point-to-point but need better connector layout.
      #style += 'html=1;rounded=0;jumpStyle=gap;edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;'
      style += 'html=1;rounded=0;jumpStyle=gap;'

      if linetype.upper() == "DOUBLE":
         style += 'shape=link;startArrow=none;endArrow=none;strokeColor=' + linecolor + ';'
      elif linetype.upper() == "TUNNEL":
         style += 'shape=flexArrow;startArrow=none;endArrow=none;strokeColor=none;fillColor=' + linecolor + ';'
      else:
         style += 'strokeColor=' + linecolor + ';'
         if startarrow == "":
            style += 'startArrow=none;startFill=0;'
         else:
            style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
            if startarrow == "oval":
              # Note: Default is for oval to be centered on border so add space to be next to border per design center.
              style += "sourcePerimeterSpacing=3;"
         if endarrow == "":
            style += 'endArrow=none;endFill=0;'
         else:
            style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
              # Note: Default is for oval to be centered on border so add space to be next to border per design center.
            if endarrow == "oval":
              style += "targetPerimeterSpacing=3;"

      data = {'header': {'id': id,
                         'label': label},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
              'geo':    {'relative': '1',
                         'as': 'geometry'},
              'props':  {},
              'point':  {}}
      return data

   def buildSolidLinkSingleArrow(self, id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta):
      if linetype.upper() == "DASHED":
         style = 'dashed=1;'
      elif linetype.upper() == "LONGDASHED":
         style = 'dashed=1;dashPattern=7 2;'
      elif linetype.upper() == "DOTTED":
         style = 'dashed=1;dashPattern=1 2;'
      else:
         style = 'dashed=0;'

      style += 'strokeWidth=' + str(linewidth) + ';fontFamily=' + fontname + ';fontSize=' + str(fontsize) + ';'

      # Note: Connectors overlap with edgeStyle so using direct point-to-point but need better connector layout.
      #style += 'html=1;rounded=0;jumpStyle=gap;edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;'
      style += 'html=1;rounded=0;jumpStyle=gap;'

      if linetype.upper() == "DOUBLE":
         style += 'shape=link;startArrow=none;endArrow=none;strokeColor=' + linecolor + ';'
      elif linetype.upper() == "TUNNEL":
         style += 'shape=flexArrow;startArrow=none;endArrow=none;strokeColor=none;fillColor=' + linecolor + ';'
      else:
         style += 'strokeColor=' + linecolor + ';'
         if startarrow == "":
            style += 'startArrow=none;startFill=0;'
         else:
            style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
            if startarrow == "oval":
              # Note: Default is for oval to be centered on border so add space to be next to border per design center.
              style += "sourcePerimeterSpacing=3;"
         if endarrow == "":
            style += 'endArrow=none;endFill=0;'
         else:
            style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
            if endarrow == "oval":
              # Note: Default is for oval to be centered on border so add space to be next to border per design center.
               style += "targetPerimeterSpacing=3;"

      data = {'header': {'id': id,
                         'label': label},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
               'geo':   {'relative': '1',
                         'as': 'geometry'},
               'props':  {},
               'point':  {}}
      return data

   def buildSolidLinkDoubleArrow(self, id, label, source, target, startarrow, endarrow, startfill, endfill, linetype, linewidth, linecolor, fontname, fontsize, meta):
      if linetype.upper() == "DASHED":
         style = 'dashed=1;'
      elif linetype.upper() == "LONGDASHED":
         style = 'dashed=1;dashPattern=7 2;'
      elif linetype.upper() == "DOTTED":
         style = 'dashed=1;dashPattern=1 2;'
      else:
         style = 'dashed=0;'

      style += 'strokeWidth=' + str(linewidth) + ';fontFamily=' + fontname + ';fontSize=' + str(fontsize) + ';'

      # Note: Connectors overlap with edgeStyle so using direct point-to-point but need better connector layout.
      #style += 'html=1;rounded=0;jumpStyle=gap;edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;'
      style += 'html=1;rounded=0;jumpStyle=gap;'

      if linetype.upper() == "DOUBLE":
         style += 'shape=link;startArrow=none;endArrow=none;strokeColor=' + linecolor + ';'
      elif linetype.upper() == "TUNNEL":
         style += 'shape=flexArrow;startArrow=none;endArrow=none;strokeColor=none;fillColor=' + linecolor + ';'
      else:
         style += 'strokeColor=' + linecolor + ';'
         if startarrow == "":
            style += 'startArrow=none;startFill=0;'
         else:
            style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
            if startarrow == "oval":
              # Note: Default is for oval to be centered on border so add space to be next to border per design center.
              style += "sourcePerimeterSpacing=3;"
         if endarrow == "":
            style += 'endArrow=none;endFill=0;'
         else:
            style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
            if endarrow == "oval":
              # Note: Default is for oval to be centered on border so add space to be next to border per design center.
              style += "targetPerimeterSpacing=3;"

      data = {'header': {'id': id,
                         'label': label},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
              'geo':    {'relative': '1',
                         'as': 'geometry'},
              'props':  {},
              'point':  {}}
      return data

   def buildStaticGroupSidebar(self, parentid, node):
      color = node["linecolor"]
      style = 'strokeColor=' + color + ';fillColor=' + color +';'

      #header = {'id': randomid(),
      #          'placeholders': '1'}

      cell = {'id': randomid(),
              'value': '',
              'style': style,
              'vertex': '1',
              'parent': parentid}

      geo = {'x': str(0),
             'y': str(0),
             'width': str(4),
             'height': str(48),
             'as': 'geometry'}

      #data = {'header': header, 'cell': cell, 'geo': geo, 'props': {}, 'point': {}}
      data = {'cell': cell, 'geo': geo, 'props': {}, 'point': {}}

      return data

   def buildStaticGroupIcon(self, parentid, node):
      image = node["image"]
      style = "shape=image;aspect=fixed;" + image

      #header = {'id': randomid(),
      #          'placeholders': '1'}

      cell = {'id': randomid(),
              'value': '',
              'style': style,
              'vertex': '1',
              'parent': parentid}

      geo = {'x': str(12),
             'y': str(12),
             'width': str(24),
             'height': str(24),
             'as': 'geometry'}

      #data = {'header': header, 'cell': cell, 'geo': geo, 'props':  {}, 'point':  {}}
      data = {'cell': cell, 'geo': geo, 'props':  {}, 'point':  {}}

      return data

   def buildStaticExpandedIcon(self, parentid, node):
      image = node["image"]
      #style = "shape=image;aspect=fixed;" + StaticShapeStyle.PNODE.value + image
      style = "shape=image;aspect=fixed;" + image

      #header = {'id': randomid(),
      #          'placeholders': '1'}

      cell = {'id': randomid(),
              'value': '',
              'style': style,
              'vertex': '1',
              'parent': parentid}

      geo = {'x': str(0),
             'y': str(0),
             'width': str(48),
             'height': str(48),
             'as': 'geometry'}

      #data = {'header': header, 'cell': cell, 'geo': geo, 'props':  {}, 'point': {}}
      data = {'cell': cell, 'geo': geo, 'props':  {}, 'point': {}}

      return data

   def buildStaticShape(self, id, node, x, y, width, height, meta, genflag, items):
      name = node["label"]
      subname = node["sublabel"]
      shape = node["shape"].lower()
      genname = node["genname"]

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
         color = node["linecolor"]
         styleStroke = "strokeColor=" + color + ';' 
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

      if genflag:
         shapelabel = "<b style='font-weight:600'>" + genname
         #shapelabel = genname
      else:
         shapelabel = "<b style='font-weight:600'>" + name + "</b><br>" + subname
         #shapelabel = name

      #header = {'id': id,
      #          'label': shapelabel,
      #          'placeholders': '1'}

      cell = {'id': id,
              'value': shapelabel,
              'style': style,
              'vertex': '1',
              'parent': parentid}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(width),
             'height': str(height),
             'as': 'geometry'}

      props = {}

      if meta != None:
         props.update(meta)

      #data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props, 'point': {}}
      data = {'cell': cell, 'geo': geo, 'props':  props, 'point': {}}

      return data

   def buildShape(self, id, node, x, y, width, height, meta, genflag):
      shape = node["shape"].lower()
      name = node["label"]
      subname = node["sublabel"]
      shape = node["shape"].lower()
      genname = node["genname"]

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

      color = node["linecolor"]
      styleStroke = "strokeColor=" + color + ';' 
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

      if genflag:
         shapelabel = "<b style='font-weight:600'>" + genname
      else:
         shapelabel = "<b style='font-weight:600'>" + name + "</b><br>" + subname

      #header = {'id': id,
      #          'label': shapelabel,
      #          'placeholders': '1'}

      cell = {'id': id,
              'value': shapelabel,
              'style': style,
              'vertex': '1',
              'parent': parentid}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(width),
             'height': str(height),
             'as': 'geometry'}

      props = {}

      if meta != None:
         props.update(meta)

      data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props, 'point': {}}

      return data

   def buildDrawioShape(self, id, node, x, y, width, height, meta, genflag):
      labelsize = 20
      shape = node["shape"].lower()
      name = node["label"]
      subname = node["sublabel"]
      shape = node["shape"].lower()
      genname = node["genname"]

      linecount = 0
      if len(name) > 0:
         linecount = linecount + 1 + name.count("<br")
      if len(subname) > 0:
         linecount = linecount + 1 + subname.count("<br")

      if len(name) > 0:
         name = self.common.truncateText(name, labelsize, '<br>')

      if len(subname) > 0:
         subname = self.common.truncateText(subname, labelsize, '<br>')

      if genflag:
         shapelabel = "<b style='font-weight:600'>" + genname
         #shapelabel = genname
      else:
         shapelabel = "<b style='font-weight:600'>" + name + "</b><br>" + subname
         #shapelabel = name

      if shape == "actor":
         data = self.buildActorShape(id, node, x, y, width, height, meta, shapelabel)
      elif shape == "pnode":
         data = self.buildPNodeShape(id, node, x, y, width, height, meta, shapelabel)
      elif shape == "epnode":
         data = self.buildEPNodeShape(id, node, x, y, width, height, meta, shapelabel)
      elif shape == "ploc":
         data = self.buildPLocShape(id, node, x, y, width, height, meta, shapelabel)
      #elif shape == "gploc":
      #   data = self.buildGPLocShape( id, node, x, y, width, height, meta, shapelabel)
      elif shape == "zone":
         data = self.buildZoneShape(id, node, x, y, width, height, meta, shapelabel)
      #elif shape == "gzone":
      #   data = self.buildGZoneShape(id, node, x, y, width, height, meta, shapelabel)
      else:
         data = self.buildPNodeShape(id, node, x, y, width, height, meta, shapelabel)
         
      return data

   def buildActorShape(self, id, node, x, y, width, height, meta, shapelabel):
      styleshape = "shape=ellipse;%FILL;aspect=fixed;resizable=0;html=1;labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;strokeColor=none;fontFamily=%FONT;fontSize=14;"
      fillcolor = node["fillcolor"]
      styleFill = "fillColor=" + fillcolor + ';' 
      styleshape = styleshape.replace("%FILL", styleFill)
      styleshape = styleshape.replace("%FONT", self.common.getFontName())

      parentid = node["parentid"]
      parentid = '1' if parentid == None else parentid

      #header = {'id': id,
      #          'placeholders': '1'}

      cell = {'id': id,
              'value': shapelabel,
              'style': styleshape,
              'vertex': '1',
              'parent': parentid}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(48),
             'height': str(48),
             'as': 'geometry'}

      props = {}

      if meta != None:
         props.update(meta)

      #datashape = {'header': header, 'cell': cell, 'geo': geo, 'props':  props, 'point': {}}
      datashape = {'cell': cell, 'geo': geo, 'props':  props, 'point': {}}

      icon = node["icon"]
      styleicon = "shape=mxgraph.ibm_cloud." + icon + ";fillColor=#ffffff;strokeColor=none;dashed=0;outlineConnect=0;part=1;movable=0;resizable=0;rotatable=0;"

      #header = {'id': id + '-icon',
      #          'placeholders': '1'}

      cell = {'id': id + '-icon',
              'value': '',
              'style': styleicon,
              'vertex': '1',
              'parent': id}

      geo = {'width': str(24),
             'height': str(24),
             'relative': str(1),
             'as': 'geometry'}

      point = {'x': str(12),
               'y': str(12),
               'as': 'offset'}

      #dataicon = {'header': header, 'cell': cell, 'geo': geo, 'props': {}, 'point': point}
      dataicon = {'cell': cell, 'geo': geo, 'props': {}, 'point': point}

      return [datashape, dataicon]

   def buildPNodeShape(self, id, node, x, y, width, height, meta, shapelabel):
      styleshape = "shape=rect;%FILL;aspect=fixed;resizable=0;html=1;labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;strokeColor=none;fontFamily=%FONT;fontSize=14;"
      fillcolor = node["fillcolor"]
      styleFill = "fillColor=" + fillcolor + ';' 
      styleshape = styleshape.replace("%FILL", styleFill)
      styleshape = styleshape.replace("%FONT", self.common.getFontName())

      parentid = node["parentid"]
      parentid = '1' if parentid == None else parentid

      #header = {'id': id,
      #          'placeholders': '1'}

      cell = {'id': id,
              'value': shapelabel,
              'style': styleshape,
              'vertex': '1',
              'parent': parentid}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(width),
             'height': str(height),
             'as': 'geometry'}

      props = {}

      if meta != None:
         props.update(meta)

      #datashape = {'header': header, 'cell': cell, 'geo': geo, 'props':  props, 'point': {}}
      datashape = {'cell': cell, 'geo': geo, 'props':  props, 'point': {}}

      icon = node["icon"]
      styleicon = "shape=mxgraph.ibm_cloud." + icon + ";fillColor=#ffffff;strokeColor=none;dashed=0;outlineConnect=0;part=1;movable=0;resizable=0;rotatable=0;"

      #header = {'id': id + '-icon',
      #          'placeholders': '1'}

      cell = {'id': id + '-icon',
              'value': '',
              'style': styleicon,
              'vertex': '1',
              'parent': id}

      geo = {'width': str(24),
             'height': str(24),
             'relative': str(1),
             'as': 'geometry'}

      point = {'x': str(12),
               'y': str(12),
               'as': 'offset'}

      #dataicon = {'header': header, 'cell': cell, 'geo': geo, 'props': {}, 'point': point}
      dataicon = {'cell': cell, 'geo': geo, 'props': {}, 'point': point}

      return [datashape, dataicon]

   def buildEPNodeShape(self, id, node, x, y, width, height, meta, shapelabel):
      fillcolor = node["fillcolor"]
      if fillcolor == "":
         fillcolor = "none"
      linecolor = node["linecolor"]
      styleshape = "container=1;collapsible=0;expand=0;recursiveResize=0;image=;strokeColor=" + linecolor + ";fillColor=" + fillcolor + ";"

      parentid = node["parentid"]
      parentid = '1' if parentid == None else parentid

      cell = {'id': id,
              'value': '',
              'style': styleshape,
              'vertex': '1',
              'parent': parentid}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(width),
             'height': str(height),
             'as': 'geometry'}

      props = {}

      if meta != None:
         props.update(meta)

      datashape = {'cell': cell, 'geo': geo, 'props':  props, 'point': {}}

      stylelabel = "shape=rect;strokeColor=none;fillColor=" + linecolor + ";aspect=fixed;resizable=0;html=1;labelPosition=right;verticalLabelPosition=middle;align=left;verticalAlign=middle;part=1;spacingLeft=5;fontFamily=%FONT;fontSize=14;"
      stylelabel = stylelabel.replace("%FONT", self.common.getFontName())

      cell = {'id': id + '-label',
              'value': shapelabel,
              'style': stylelabel,
              'vertex': '1',
              'parent': id}

      geo = {'width': str(48),
             'height': str(48),
             'relative': str(1),
             'as': 'geometry'}

      datalabel = {'cell': cell, 'geo': geo, 'props': {}, 'point': {}}

      icon = node["icon"]
      styleicon = "shape=mxgraph.ibm_cloud." + icon + ";fillColor=#ffffff;strokeColor=none;dashed=0;outlineConnect=0;html=1;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;part=1;movable=0;resizable=0;rotatable=0;"

      cell = {'id': id + '-icon',
              'value': '',
              'style': styleicon,
              'vertex': '1',
              'parent': id + '-label'}

      geo = {'width': str(24),
             'height': str(24),
             'relative': str(1),
             'as': 'geometry'}

      point = {'x': str(12),
               'y': str(12),
               'as': 'offset'}

      dataicon = {'cell': cell, 'geo': geo, 'props': {}, 'point': point}

      return [datashape, datalabel, dataicon]

   def buildPLocShape(self, id, node, x, y, width, height, meta, shapelabel):
      fillcolor = node["fillcolor"]
      if fillcolor == "":
         fillcolor = "none"
      linecolor = node["linecolor"]
      styleshape = "container=1;collapsible=0;expand=0;recursiveResize=0;image=;strokeColor=" + linecolor + ";fillColor=" + fillcolor + ";strokeWidth=1;"

      parentid = node["parentid"]
      parentid = '1' if parentid == None else parentid

      cell = {'id': id,
              'value': '',
              'style': styleshape,
              'vertex': '1',
              'parent': parentid}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(width),
             'height': str(height),
             'as': 'geometry'}

      props = {}

      if meta != None:
         props.update(meta)

      #datashape = {'header': header, 'cell': cell, 'geo': geo, 'props':  props, 'point': {}}
      datashape = {'cell': cell, 'geo': geo, 'props':  props, 'point': {}}

      stylelabel = "shape=rect;strokeColor=none;fillColor=none;aspect=fixed;resizable=0;html=1;labelPosition=right;verticalLabelPosition=middle;align=left;verticalAlign=middle;part=1;spacingLeft=5;fontFamily=%FONT;fontSize=14;"
      stylelabel = stylelabel.replace("%FONT", self.common.getFontName())

      cell = {'id': id + '-label',
              'value': shapelabel,
              'style': stylelabel,
              'vertex': '1',
              'parent': id}

      geo = {'width': str(48),
             'height': str(48),
             'relative': str(1),
             'as': 'geometry'}

      datalabel = {'cell': cell, 'geo': geo, 'props': {}, 'point': {}}

      icon = node["icon"]
      styleicon = "shape=mxgraph.ibm_cloud." + icon + ";strokeColor=none;fillColor=" + linecolor + ";aspect=fixed;resizable=0;rotatable=0;labelPosition=right;verticalLabelPosition=middle;align=left;verticalAlign=middle;part=1;dashed=0;outlineConnect=0;spacingLeft=5;"

      cell = {'id': id + '-icon',
              'value': '',
              'style': styleicon,
              'vertex': '1',
              'parent': id + '-label'}

      geo = {'width': str(24),
             'height': str(24),
             'relative': str(1),
             'as': 'geometry'}

      point = {'x': str(12),
               'y': str(12),
               'as': 'offset'}

      dataicon = {'cell': cell, 'geo': geo, 'props': {}, 'point': point}

      stylesidebar = "shape=rect;strokeColor=none;fillColor=" + linecolor + ";aspect=fixed;resizable=0;part=1;spacingLeft=5;"

      cell = {'id': id + '-sidebar',
              'value': '',
              'style': stylesidebar,
              'vertex': '1',
              'parent': id}

      geo = {'width': str(4),
             'height': str(48),
             'relative': str(1),
             'as': 'geometry'}

      datasidebar = {'cell': cell, 'geo': geo, 'props': {}, 'point': {}}

      return [datashape, datalabel, dataicon, datasidebar]

   def buildZoneShape(self, id, node, x, y, width, height, meta, shapelabel):
      fillcolor = node["fillcolor"]
      if fillcolor == "":
         fillcolor = "none"
      linecolor = node["linecolor"]
      styleshape = "container=0;collapsible=0;expand=0;recursiveResize=0;image=;strokeColor=" + linecolor + ";fillColor=" + fillcolor + ";dashed=1;dashPattern=1 3;strokeWidth=2;"

      parentid = node["parentid"]
      parentid = '1' if parentid == None else parentid

      cell = {'id': id,
              'value': '',
              'style': styleshape,
              'vertex': '1',
              'parent': parentid}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(width),
             'height': str(height),
             'as': 'geometry'}

      props = {}

      if meta != None:
         props.update(meta)

      datashape = {'cell': cell, 'geo': geo, 'props':  props, 'point': {}}

      stylelabel = "shape=rect;fillColor=none;aspect=fixed;resizable=0;html=1;labelPosition=right;verticalLabelPosition=middle;align=left;verticalAlign=middle;strokeColor=none;part=1;spacingLeft=5;fontFamily=%FONT;fontSize=14;"
      stylelabel = stylelabel.replace("%FONT", self.common.getFontName())

      cell = {'id': id + '-label',
              'value': shapelabel,
              'style': stylelabel,
              'vertex': '1',
              'parent': id}

      geo = {'width': str(48),
             'height': str(48),
             'relative': str(1),
             'as': 'geometry'}

      datalabel = {'cell': cell, 'geo': geo, 'props': {}, 'point': {}}

      icon = node["icon"]
      styleicon = "shape=mxgraph.ibm_cloud." + icon + ";fillColor=" + linecolor + ";strokeColor=none;dashed=0;outlineConnect=0;part=1;movable=0;resizable=0;rotatable=0;"

      header = {'id': id + '-icon',
                'label': shapelabel,
                'placeholders': '1'}

      cell = {'id': id + '-icon',
              'value': '',
              'style': styleicon,
              'vertex': '1',
              'parent': id + '-label'}

      geo = {'width': str(24),
             'height': str(24),
             'relative': str(1),
             'as': 'geometry'}

      point = {'x': str(12),
               'y': str(12),
               'as': 'offset'}

      dataicon = {'cell': cell, 'geo': geo, 'props': {}, 'point': point}

      return [datashape, datalabel, dataicon]

   def buildValue(self, id, parentid, name, parent, subname, text, x, y, width, height):
      shape = ibmshapes['text']
      style = shape['style']  
      data = {'cell': {'id': id,
                       'value': text,
                       'style': style,
                       'vertex': '1',
                       'parent': parentid},
              'geo':  {'x': str(x),
                       'y': str(y),
                       'width': str(width),
                       'height': str(height),
                       'as': 'geometry'}}
      return data

   def buildPage(self, name):
      data = {'header': {'id': self.common.compress(name),
                         'name': name},
              'graph':  {'dx': '1434',
                         'dy': '822',
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
