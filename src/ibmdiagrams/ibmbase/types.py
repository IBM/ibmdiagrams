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

from .constants import ShapeKind, ShapeStyle
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

   def buildCatalogIcon(self, parentid, node):
      #style = "shape=image;"

      #linecolor = node["linecolor"]
      #styleStroke = "strokeColor=" + linecolor + ";" 
      #styleStroke = "strokeColor=none;" 

      #fillcolor = node["fillcolor"]
      #if fillcolor:
      #   #style += "fillColor=" + fillcolor + ";" 
      #   styleFill = "fillColor=" + fillcolor + ";" 
      #else:
      #   #style += "fillColor=none;" 
      #   styleFill = "fillColor=none;" 
      
      #style += "strokeColor=none;fillColor=none;"
      #style += styleStroke + styleFill

      image = node["image"] 
      #if image != "":
      #   style += image

      style = ShapeStyle.IMAGE.value + image

      name = node["label"]

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

   def buildCatalogNode(self, id, node, x, y, width, height, meta):
      style = ShapeStyle.GROUP.value

      linecolor = node["linecolor"]
      fillcolor = node["fillcolor"]
      #style += 'strokeColor=' + linecolor + ';fillColor=' + fillcolor +';'
      #style += 'strokeColor=' + linecolor + ';fillColor=' + fillcolor +';strokeWidth=2;'
      styleStroke = "strokeColor=" + linecolor + ';' 
      styleFill = "fillColor=" + fillcolor + ';' 
      style = style.replace("%STROKE", styleStroke)
      style = style.replace("%FILL", styleFill)
      #style += 'strokeWidth=2;'

      name = node["label"]
      subname = node["sublabel"]
      labelsize = 20

      if len(name) > 0:
         name = self.common.truncateText(name, labelsize, '<br>')

      if len(subname) > 0:
         subname = self.common.truncateText(subname, labelsize, '<br>')

      shapelabel = "<b style='font-weight:600'>" + name + "</b><br>" + subname

      parentid = node["parentid"]
      parentid = '1' if parentid == None else parentid

      header = {'id': id,
                'label': shapelabel,
                'placeholders': '1'}

      cell = {'parent': parentid,
              'style': style,
              'vertex': '1'}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(48),
             'height': str(48),
             'as': 'geometry'}

      props = {}

      data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props}

      return data

   def buildGroupIcon(self, parentid, node):
      style = "shape=image;"

      linecolor = node["linecolor"]
      #styleStroke = "strokeColor=" + linecolor + ";" 
      styleStroke = "strokeColor=none;" 

      fillcolor = node["fillcolor"]
      if fillcolor:
         #style += "fillColor=" + fillcolor + ";" 
         styleFill = "fillColor=" + fillcolor + ";" 
      else:
         #style += "fillColor=none;" 
         styleFill = "fillColor=none;" 
      
      #style += "strokeColor=none;fillColor=none;"
      style += styleStroke + styleFill

      image = node["image"] 
      if image != "":
         style += image

      name = node["label"]

      header = {'id': randomid(),
                'placeholders': '1'}

      cell = {'parent': parentid,
              'style': style,
              'vertex': '1'}

      #geo = {'x': str(15),
      #       'y': str(7),
      #       'width': str(24),
      #       'height': str(24),
      #       'as': 'geometry'}

      geo = {'x': str(14),
             'y': str(12),
             'width': str(24),
             'height': str(24),
             'as': 'geometry'}

      props = {}

      data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props}

      return data

   def buildSidebar(self, parentid, node):
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

   def buildNode(self, id, node, x, y, width, height, meta):
      shape = node["shape"].lower()
      if shape == "actor":
         style = ShapeStyle.ACTOR.value
      elif shape == "pnode":
         style = ShapeStyle.PNODE.value
      elif shape == "epnode":
         style = ShapeStyle.EPNODE.value
      elif shape == "ploc":
         style = ShapeStyle.PLOC.value
      elif shape == "gploc":
         style = ShapeStyle.GPLOC.value
      elif shape == "zone":
         style = ShapeStyle.ZONE.value
      elif shape == "gzone":
         style = ShapeStyle.GZONE.value
      else:
         style = ShapeStyle.PNODE.value

      linecolor = node["linecolor"]
      #style += "strokeColor=" + linecolor + ';' 
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

      #multiplicity = node["many"]
      #if multiplicity:
      #   style += "ibmMultiplicity=1;"

      name = node["label"]
      subname = node["sublabel"]

      badgetext = node["badgetext"]
      badgeshape = node["badgeshape"]
      badgelinecolor = node["badgelinecolor"]
      badgefillcolor = node["badgefillcolor"]

      #if "newparentid" in node:
      #   parentid = node["newparentid"]
      #else:
      parentid = node["parentid"]
      parentid = '1' if parentid == None else parentid

      #icon = node["icon"]
      #if icon != "":
      #   styleIcon = 'icon=' + icon + ';'
      #else:
      #   styleIcon = ""
      #style = style.replace("%ICON", styleIcon)

      image = node["image"] 
      if image != "":
         if shape == "actor" or shape == "pnode":
            style = ShapeStyle.IMAGE.value + image
         elif shape == "ploc":
            style = ShapeStyle.BPLOC.value
            style = style.replace("%STROKE", styleStroke)
            style = style.replace("%FILL", styleFill)
         elif shape == "epnode":
            style = ShapeStyle.EPNODE.value
            style = style.replace("%STROKE", styleStroke)
            style = style.replace("%FILL", styleFill)
         elif shape == "zone":
            style = ShapeStyle.BZONE.value
            style = style.replace("%STROKE", styleStroke)
            style = style.replace("%FILL", styleFill)

      else:
         icon = node["icon"]
         if icon != "":
            styleIcon = 'icon=' + icon + ';'
         else:
            styleIcon = ""
         style = style.replace("%ICON", styleIcon)

      #shapelabel = "<b style='font-weight:600'>%Primary-Label%</b><br>%Secondary-Text%"
      #labelsize = 30
      #labelsize = 24
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

      #props = {#'Badge-Text': badgetext,
      #         #'Icon-Name': iconname,
      #         #'Icon-Name': icon,
      #         'Primary-Label': name,
      #         'Secondary-Text': subname}

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
