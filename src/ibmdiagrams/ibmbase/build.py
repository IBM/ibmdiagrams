# @file build.py
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

# Hierarchy:
#   ibmdiagrams/__init__.py - defines diagram-as-code for python, invokes build.py
#   ibmdiagrams/ibmbase/compose.py - composes Terraform and JSON use cases, invokes build.py
#   ibmdiagrams/ibmbase/build.py - build diagram objects for all use cases, invokes shapes.py
#   ibmdiagrams/ibmbase/shapes.py - build ibm types, invokes types.py
#   ibmdiagrams/ibmbase/types.py - build drawio types, invokes elements.py
#   ibmdiagrams/ibmbase/elements.py - build drawio objects  

from os import path
from math import isnan, floor
from copy import copy

from .colors import Colors
from .common import Common
from .properties import Properties, Alternates, GroupTypes, Directions, EdgeArrows, EdgeStyles, Fonts, ItemTypes, OutputFormats, IconTypes, Providers
from .constants import ComponentFill, FillPalette, ShapeKind, ShapeName, ShapePos, ZoneCIDR
from .shapes import Shapes
from .icons import Icons

DIAGRAM_NAME_DEFAULT = "diagram"
DIAGRAM_DIRECTION_DEFAULT = "LR"
DIAGRAM_ALTERNATE_DEFAULT = "WHITE"
DIAGRAM_PROVIDER_DEFAULT = "IBM"
DIAGRAM_FONTNAME_DEFAULT = "IBM Plex Sans"
DIAGRAM_FONTSIZE_DEFAULT = 14
DIAGRAM_OUTFORMAT_DEFAULT = "SVG"
DIAGRAM_ICONS_DEFAULT = "BUILTIN"

GROUP_LABEL_DEFAULT = "Group"
GROUP_DIRECTION_DEFAULT = "LR"
GROUP_ALTERNATE_DEFAULT = "WHITE"
GROUP_PROVIDER_DEFAULT = "IBM"
GROUP_SHAPE_DEFAULT = "PLOC"
GROUP_ICON_DEFAULT = "Undefined Group"
GROUP_ICONS_DEFAULT = "BUILTIN"
GROUP_FONTNAME_DEFAULT = "IBM Plex Sans"
GROUP_FONTSIZE_DEFAULT = 14

ITEM_LABEL_DEFAULT = "Node"
ITEM_DIRECTION_DEFAULT = "LR"
ITEM_PROVIDER_DEFAULT = "IBM"
ITEM_SHAPE_DEFAULT = "PNODE"
ITEM_ICON_DEFAULT = "Undefined Node"
ITEM_ICONS_DEFAULT = "BUILTIN"
ITEM_FONTNAME_DEFAULT = "IBM Plex Sans"
ITEM_FONTSIZE_DEFAULT = 14

EDGE_COLOR_DEFAULT = "black"
EDGE_ARROW_DEFAULT = "classic"
EDGE_STYLE_DEFAULT = "solid"
EDGE_FONTNAME_DEFAULT = "IBM Plex Sans"
EDGE_FONTSIZE_DEFAULT = 12

class Build:
   common = None
   shapes = None
   icons = None
   icontype = None
   cloudname = ""
   diagrams = {}
   groups = {}
   items = {}
   edges = {}
   sequence = []
   tops = []
   bottoms = []
   filename = ""

   def __init__(self, common, data):
      self.common = common
      self.shapes = Shapes(self.common)
      self.icons = Icons(self.common)
      self.icontype = common.getIconType()
      self.diagrams = data.getDiagrams()
      self.groups = data.getGroups()
      self.items = data.getItems()
      self.edges = data.getEdges()
      self.sequence = data.getSequence()
      self.tops = []
      self.bottoms = []
      return

   def buildSheets(self, properties, diagrams):
      provider = self.common.getProvider().value.upper()
      diagramname = properties["name"]
      outputfile = properties["filename"]
      outputfile = outputfile if outputfile != "" else diagramname + ".drawio"
      outputfolder = self.common.getOutputFolder()
      
      self.common.printStartDiagram(diagramname, provider)

      for name, diagram in diagrams.items():
         self.shapes.buildXML(diagram, name)

      self.shapes.dumpXML(outputfile, outputfolder)
      self.shapes.resetXML()

      self.common.printDone(path.join(outputfolder, outputfile), provider)

      return

   def buildDiagrams(self):
      self.checkAll()

      if self.diagrams == None or self.groups == None or self.items == None or self.edges == None:
         return None

      provider = self.common.getProvider().value.upper()

      properties = (list(self.diagrams.items())[0])[1]

      self.filename = properties["filename"]

      if properties["filename"] != "*":
         outputfile = properties["filename"] + ".drawio"
         diagramname = properties["name"]
         self.common.printStartDiagram(diagramname, provider)

      self.setupAll()

      if self.diagrams == None or self.groups == None or self.items == None or self.edges == None:
         return None

      if properties["filename"] != "*":
         outputfolder = self.common.getOutputFolder()
         if outputfolder != "" and outputfolder[-1] != '/':
            self.common.setOutputFolder(outputfolder + '/')

      items, links, values = self.buildAll()
      xmldata = {"items": items, "links": links, "values": values}

      if properties["filename"] != "*":
         self.shapes.buildXML(xmldata, properties["name"])
         self.shapes.dumpXML(outputfile, outputfolder)
         self.shapes.resetXML()
         self.common.printDone(path.join(outputfolder, outputfile), provider)

      return xmldata

   def checkAll(self):
      self.diagrams = self.checkDiagrams(self.diagrams)
      self.groups = self.checkGroups(self.groups)
      self.items = self.checkItems(self.items)
      self.edges = self.checkEdges(self.edges)

   def setupAll(self):
      self.addKeys()
      self.addChildren()

      #if not self.common.isAlternateUser():
      #   self.alternateFills()

      self.calculateGeometry()
      self.eliminateZoneParents()

      '''
      if self.filename == "*":
         resetwidth = 0
         tops = self.tops
         tops.reverse()
         for groupid in tops:
            group = self.groups[groupid]
            geometry = group["geometry"]
            x = resetwidth
            y = geometry[1]
            width = geometry[2]
            height = geometry[3]
            self.groups[groupid]["geometry"] = [x, y, width, height]
            resetwidth += width + 20
      '''

      #self.printSequence()
      #self.printDiagrams()
      #self.printGroups()
      #self.printItems()
      #self.printEdges()
      #self.printTops()
      #self.printBottoms()

      return

   def buildAll(self):
      items = []
      links = []
      values = []

      for groupid in self.tops:
         groupitems, grouplinks, groupvalues = self.buildGroups([groupid])
         items += groupitems
         links += grouplinks
         values += groupvalues

      for edgeid, properties in self.edges.items():
         edgeitems, edgelinks, edgevalues = self.buildEdgeShape(edgeid, properties)
         items += edgeitems
         links += edgelinks
         values += edgevalues

      return items, links, values

   def buildGroups(self, groupids):
      items = []
      links = []
      values = []

      for groupid in groupids:
         properties = self.groups[groupid]
         childids = properties["children"]

         groupitems, grouplinks, groupvalues = self.buildGroupShape(groupid, properties)
         items += groupitems
         links += grouplinks
         values += groupvalues

         if len(childids) > 0:
            groupitems, grouplinks, groupvalues = self.buildGroups(childids)
            items += groupitems
            links += grouplinks
            values += groupvalues
         #else:
         #groupitems, grouplinks, groupvalues = self.buildGroupShape(groupid, properties)
         #items += groupitems
         #links += grouplinks
         #values += groupvalues

      return items, links, values

   def buildGroupShape(self, groupid, properties):
      items = []
      links = []
      values = []

      #properties = self.moveZoneParent(groupid, properties)

      geometry = properties["geometry"]
      x = geometry[0]
      y = geometry[1]
      width = geometry[2]
      height = geometry[3]

      meta = properties["data"]

      shape = properties["shape"].lower()

      if self.common.isStaticIcons() or self.common.isCatalogIcons():
         shapenode = self.shapes.buildStaticShape(groupid, properties, x, y, width, height, meta, items)
         items.append(shapenode)
      else:
         shapenode = self.shapes.buildShape(groupid, properties, x, y, width, height, meta)
         items.append(shapenode)

      return items, links, values

   def buildEdgeShape(self, edgeid, properties):
      items = []
      links = []
      values = []

      sourceid = properties["sourceid"]
      targetid = properties["targetid"]
      startarrow = properties["startarrow"]
      endarrow = properties["endarrow"]
      startfill = properties["startfill"]
      endfill = properties["endfill"]
      label = properties["label"]

      '''
      if arrow == "none":
         edgenode = self.shapes.buildSolidLink(edgeid, label, sourceid, targetid, None)
      elif arrow == "single":
         edgenode = self.shapes.buildSingleArrow(edgeid, label, sourceid, targetid, None)
      else:  # "double"
         edgenode = self.shapes.buildDoubleArrow(edgeid, label, sourceid, targetid, None)
      '''

      if startarrow == "" and endarrow == "":
         edgenode = self.shapes.buildSolidLink(edgeid, label, sourceid, targetid, startarrow, endarrow, startfill, endfill, None)
      elif startarrow != "" and endarrow != "":
         edgenode = self.shapes.buildDoubleArrow(edgeid, label, sourceid, targetid, startarrow, endarrow, startfill, endfill, None)
      #elif startarrow != "" or endarrow != "":
      else:
         edgenode = self.shapes.buildSingleArrow(edgeid, label, sourceid, targetid, startarrow, endarrow, startfill, endfill, None)

      links.append(edgenode)

      return items, links, values

   def checkDiagrams(self, diagrams):
      for diagramid, properties in diagrams.items():
         name = properties["name"]
         if name == "":
            name = DIAGRAM_NAME_DEFAULT
         diagrams[diagramid]["name"] = name

         filename = properties["filename"]
         if filename == "":
            diagrams[diagramid]["filename"] = name
            self.common.setOutputFile(name + ".drawio")
         elif filename != "*":
            self.common.setOutputFile(filename + ".drawio")

         #direction = properties["direction"]
         #if direction == "":
         #   direction = DIAGRAM_DIRECTION_DEFAULT
         #elif not direction.upper() in [parm.value for parm in Directions]:
         #   self.common.printInvalidDirection(direction)
         #   return None
         #diagrams[diagramid]["direction"] = direction
         diagrams[diagramid]["direction"] = self.common.getDirection()

         #alternate = properties["alternate"]
         #if alternate == "":
         #   alernate = DIAGRAM_ALTERNATE_DEFAULT
         #elif not alternate.upper() in [parm.value for parm in Alternates]:
         #   self.common.printInvalidAlternate(alternate)
         #   return None
         #diagrams[diagramid]["alternate"] = alternate

         #provider = properties["provider"]
         #if provider == "":
         #   provider = DIAGRAM_PROVIDER_DEFAULT
         #elif not provider.upper() in [parm.value for parm in Providers]:
         #   self.common.printInvalidProvider(provider)
         #   return None
         #diagrams[diagramid]["provider"] = provider

         #fontname = properties["fontname"]
         #if fontname == "":
         #   fontname = DIAGRAM_FONTNAME_DEFAULT
         #elif not fontname in [parm.value for parm in Fonts]:
         #   self.common.printInvalidFontName(fontname)
         #   return None
         #diagrams[diagramid]["fontname"] = fontname

         #fontsize = properties["fontsize"]
         #if fontsize == 0:
         #   fontsize = DIAGRAM_FONTSIZE_DEFAULT
         #diagrams[diagramid]["fontsize"] = fontsize

         #outformat = properties["outformat"]
         #if outformat == "":
         #   outformat = DIAGRAM_OUTFORMAT_DEFAULT
         #elif not outformat.upper() in [parm.value for parm in OutputFormats]:
         #   self.common.printInvalidOutputFormat(outformat)
         #   return None
         #diagrams[diagramid]["outformat"] = outformat

         #icontype = properties["icontype"]
         #if icontype == "":
         #   icontype = DIAGRAM_ICONS_DEFAULT
         #elif not icontype.upper() in [parm.value for parm in IconTypes]:
         #   self.common.printInvalidIconType(icontype)
         #   return None
         #diagrams[diagramid]["icontype"] = icontype
         diagrams[diagramid]["icontype"] = self.common.getIconType()

         #if icontype.upper() == "BUILTIN":
         #   self.common.setBuiltinIcons()
         #elif icontype.upper() == "CATALOG":
         #   self.common.setCatalogIcons()
         #elif icontype.upper() == "STATIC":
         #   self.common.setStaticIcons()

         #if direction.upper() == "LR":
         #   self.common.setDirectionLR()
         #elif direction.upper() == "TB":
         #   self.common.setDirectionTB()

         #if alternate.upper() == "WHITE":
         #   self.common.setAlternateWhite()
         #elif alternate.upper() == "LIGHT":
         #   self.common.setAlternateLight()
         #elif alternate.upper() == "NONE":
         #   self.common.setAlternateNone()
         #elif alternate.upper() == "USER":
         #   self.common.setAlternateUser()

         #if provider.upper() == "ANY":
         #   self.common.setProviderAny()
         #elif provider.upper() == "IBM":
         #   self.common.setProviderIBM()

      return diagrams

   def checkGroups(self, groups):
      for groupid, properties in groups.items():
         label = properties["label"]
         if label == "":
            label = GROUP_LABEL_DEFAULT
         groups[groupid]["label"] = label

         #icose = properties["icons"]
         #if icons == "":
         #   icons = GROUP_ICONS_DEFAULT
         #elif not icons.upper() in [parm.value for parm in IconTypes]:
         #   self.common.printInvalidIcons(icons)
         #   return None
         #groups[groupid]["icons"] = icons

         iconType = self.common.getIconType()
         groups[groupid]["icontype"] = iconType

         direction = properties["direction"]
         # TBD if groups direction not set then use diagram direction if set.
         if direction == "":
            direction = GROUP_DIRECTION_DEFAULT
         elif not direction.upper() in [parm.value for parm in Directions]:
            self.common.printInvalidDirection(direction)
            return None
         groups[groupid]["direction"] = direction

         #alternate = properties["alternate"]
         #if alternate == "":
         #   alternate = GROUP_ALTERNATE_DEFAULT
         #elif not alternate.upper() in [parm.value for parm in Alternates]:
         #   self.common.printInvalidAlternate(alternate)
         #   return None
         #groups[groupid]["alternate"] = alternate

         #provider = properties["provider"]
         #if provider == "":
         #   provider = GROUP_PROVIDER_DEFAULT
         #elif not provider.upper() in [parm.value for parm in Providers]:
         #   self.common.printInvalidProvider(provider)
         #   return None
         #groups[groupid]["provider"] = provider

         fontname = properties["fontname"]
         if fontname == "":
            fontname = GROUP_FONTNAME_DEFAULT
         elif not fontname in [parm.value for parm in Fonts]:
            self.common.printInvalidFont(fontname)
            return None
         groups[groupid]["fontname"] = fontname

         fontsize = properties["fontsize"]
         if fontsize == 0:
            fontsize = GROUP_FONTSIZE_DEFAULT
         groups[groupid]["fontsize"] = fontsize

         hideicon = False
         icon = properties["icon"]
         if icon == "":
            #icon = GROUP_ICON_DEFAULT
            parentid = properties["parentid"]
            if parentid == None:
              icon = GROUP_ICON_DEFAULT
            else:
              parentproperties = groups[parentid]
              icon = parentproperties["icon"]
              groups[groupid]["hideicon"] = True
              hideicon = True
         elif not self.icons.validIcon(icon):
            self.common.printInvalidIcon(icon)
            return None

         iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon(icon)
         userlinecolor = properties["linecolor"]
         if userlinecolor != "":
            #iconname, linecolor, iconshape, hideicon = self.icons.getIcon(icon)
            linecolor = userlinecolor
         userfillcolor = properties["fillcolor"]
         if userfillcolor != "":
            fillcolor = userfillcolor

         iconimage = ""
         if self.common.isStaticIcons():
            if staticicon != "":
               iconimage = self.icons.getStaticIcon("(Group) " + staticicon)
         elif self.common.isCatalogIcons():
            if catalogicon != "":
               iconimage = self.icons.getCatalogIcon(catalogicon)
         properties["image"] = iconimage

         shape = properties["shape"]
         if shape == "":
            groups[groupid]["shape"] = GROUP_SHAPE_DEFAULT
            #if iconshape == "":
            #   groups[groupid]["shape"] = GROUP_SHAPE_DEFAULT
            #else:
            #   '''
            #   shapesplit = iconshape.split("-")
            #   iconshape = shapesplit[0]
            #   if len(shapesplit) == 2 and shapesplit[1] == "hideicon":
            #      iconname = ""
            #   '''
            #   groups[groupid]["shape"] = iconshape
         # TBD: Revisit following which doesn't work for dac.
         #elif not shape.upper() in [parm.value for parm in GroupTypes]:
         #   elif not shape.upper() in [parm.value for parm in GroupTypes]:
         #   self.common.printInvalidGroupShape(shape)
         #   return None

         # TBD: Revisit hideicon to use generic in new rendition.
         #if properties["hideicon"] == "" and hideicon == True:
         #if properties["hideicon"] == "":
         #   groups[groupid]["icon"] = ""
         #else:
         #   groups[groupid]["icon"] = iconname

         if properties["hideicon"] == "":
            hideicon = False
         else:
            hideicon = properties["hideicon"]

         if hideicon == True:
            groups[groupid]["icon"] = ""
         else:
            groups[groupid]["icon"] = iconname

         hexlinecolor = self.checkLineColor(linecolor)
         if hexlinecolor == None:
            self.common.printInvalidLineColor(linecolor)
            return None
         groups[groupid]["linecolor"] = hexlinecolor

         #hexfillcolor = "#ffffff"
         fillcolor = properties["fillcolor"]
         hexfillcolor = fillcolor
         '''
         if self.common.isAlternateUser() and fillcolor != "" and fillcolor != "none":
            hexfillcolor = self.checkFillColor(hexlinecolor, fillcolor)
            if hexfillcolor == None:
               self.common.printInvalidFillColor(fillcolor)
               return None
         '''
         groups[groupid]["fillcolor"] = hexfillcolor

      return groups

   def checkItems(self, items):
      for nodeid, properties in items.items():
         label = properties["label"]
         if label == "":
            label = ITEM_LABEL_DEFAULT
         items[nodeid]["label"] = label

         #icons = properties["icons"]
         #if icons == "":
         #   icons = ITEM_ICONS_DEFAULT
         #elif not icons.upper() in [parm.value for parm in IconTypes]:
         #   self.common.printInvalidIconType(icons)
         #   return None
         #items[nodeid]["icons"] = icons

         icons = self.common.getIcons()
         items[nodeid]["icons"] = icons

         #direction = properties["direction"]
         #if direction == "":
         #   direction = ITEM_DIRECTION_DEFAULT
         #elif not direction.upper() in [parm.value for parm in Directions]:
         #   self.common.printInvalidDirection(direction)
         #   return None
         #items[nodeid]["direction"] = direction

         fontname = properties["fontname"]
         if fontname == "":
            fontname = ITEM_FONTNAME_DEFAULT
         elif not fontname in [parm.value for parm in Fonts]:
            self.common.printInvalidFont(fontname)
            return None
         items[nodeid]["fontname"] = fontname

         fontsize = properties["fontsize"]
         if fontsize == 0:
            fontsize = ITEM_FONTSIZE_DEFAULT
         items[nodeid]["fontsize"] = fontsize

         hideicon = False
         icon = properties["icon"]
         if icon == "":
            #icon = ITEM_ICON_DEFAULT
            parentid = properties["parentid"]
            if parentid == None:
              icon = ITEM_ICON_DEFAULT
            else:
              parentproperties = groups[parentid]
              icon = parentproperties["icon"]
              groups[groupid]["hideicon"] = True
              hideicon = True
         elif not self.icons.validIcon(icon):
            self.common.printInvalidIcon(icon)
            return None

         iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon(icon)
         userlinecolor = properties["linecolor"]
         if userlinecolor != "":
            #iconname, linecolor, iconshape, hideicon  = self.icons.getIcon(icon)
            #iconname, linecolor = self.icons.getIcon(icon)
            linecolor = userlinecolor

         iconimage = ""
         if self.common.isStaticIcons():
            if staticicon != "":
               iconimage = self.icons.getStaticIcon(staticicon)
         elif self.common.isCatalogIcons():
            if catalogicon != "":
               iconimage = self.icons.getCatalogIcon(catalogicon)
         properties["image"] = iconimage

         shape = properties["shape"]
         if shape == "":
            items[nodeid]["shape"] = ITEM_SHAPE_DEFAULT
            #if iconshape == "":
            #   items[nodeid]["shape"] = ITEM_SHAPE_DEFAULT
            #else:
            #   items[nodeid]["shape"] = iconshape
         # TBD: FOLLOWING DOESN"T WORK FOR DAC.
         #else:
         #   if not shape.upper() in [parm.value for parm in ItemTypes]:
         #      self.common.printInvalidNodeShape(shape)
         #      return None

         #if properties["hideicon"] == "" and hideicon == True:
         #if properties["hideicon"] == "":
         #   items[nodeid]["icon"] = ""
         #else:
         #   items[nodeid]["icon"] = iconname

         if properties["hideicon"] == "":
            hideicon = False
         else:
            hideicon = properties["hideicon"]

         if hideicon == True:
            items[nodeid]["icon"] = ""
         else:
            items[nodeid]["icon"] = iconname

         hexlinecolor = self.checkLineColor(linecolor)
         if hexlinecolor == None:
            self.common.printInvalidLineColor(linecolor)
            return None
         items[nodeid]["linecolor"] = hexlinecolor

         hexfillcolor = linecolor
         fillcolor = properties["fillcolor"]
         if fillcolor != "":
            hexfillcolor = self.checkFillColor(hexlinecolor, fillcolor)
            if hexfillcolor == None:
               self.common.printInvalidFillColor(fillcolor)
               return None
         items[nodeid]["fillcolor"] = hexfillcolor

      return items

   def checkEdges(self, edges):
      for edgeid, properties in edges.items():
         color = properties["color"]
         if color != "":
            hexcolor = self.checkLineColor(color)
            self.common.printInvalidLineColor(color)
            return None
         else:
            color = self.checkLineColor("black")

         style = properties["style"]
         if style == "":
            style = EDGE_STYLE_DEFAULT
         elif not style.upper() in [parm.value for parm in EdgeStyles]:
            self.common.printInvalidEdgeStyle(style)
            return None
         edges[edgeid]["style"] = style

         '''
         startarrow = properties["startarrow"]
         if startarrow == "":
            startarrow = EDGE_ARROW_DEFAULT
         elif not startarrow.upper() in [parm.value for parm in EdgeArrows]:
            self.common.printInvalidEdgeArrow(startarrow)
            return None
         edges[edgeid]["startarrow"] = startarrow.lower()
         '''
         startarrow = properties["startarrow"]
         if startarrow != "": 
            if not startarrow.upper() in [parm.value for parm in EdgeArrows]:
               self.common.printInvalidEdgeArrow(startarrow)
               return None
            edges[edgeid]["startarrow"] = startarrow.lower()

         '''
         endarrow = properties["endarrow"]
         if endarrow == "":
            endarrow = EDGE_ARROW_DEFAULT
         elif not endarrow.upper() in [parm.value for parm in EdgeArrows]:
            self.common.printInvalidEdgeArrow(endarrow)
            return None
         edges[edgeid]["endarrow"] = endarrow.lower()
         '''
         endarrow = properties["endarrow"]
         if endarrow != "":
            if not endarrow.upper() in [parm.value for parm in EdgeArrows]:
               self.common.printInvalidEdgeArrow(endarrow)
               return None
            edges[edgeid]["endarrow"] = endarrow.lower()

         fontname = properties["fontname"]
         if fontname == "":
            fontname = EDGE_FONTNAME_DEFAULT
         elif not fontname in [parm.value for parm in Fonts]:
            self.common.printInvalidFont(fontname)
            return None
         edges[edgeid]["fontname"] = fontname

         fontsize = properties["fontsize"]
         if fontsize == 0:
            fontsize = EDGE_FONTSIZE_DEFAULT
         edges[edgeid]["fontsize"] = fontsize

      return edges

   # Line color must be from IBM Color Palette and can be component name, color name, or hex value.
   def checkLineColor(self, linecolor):
      hexvalue = None 
      if linecolor.lower() in Colors.lines:
         hexvalue = Colors.lines[linecolor.lower()]
      return hexvalue

   # Family color ensures that fill color is from same family as line color or transparent or white..
   def checkFamilyColor(self, hexlinecolor, hexfillcolor):
      fillcolor = Colors.names[hexfillcolor]
      if fillcolor == "white" or fillcolor == "none":
         return hexfillcolor

      linecolor = Colors.names[hexlinecolor]
      lightlinecolor = "light" + linecolor

      if fillcolor == lightlinecolor:
         return hexfillcolor

      return None

   # Fill color must be from IBM Color Palette and can be transparent, white, or light color from same family as line color.
   def checkFillColor(self, hexlinecolor, fillcolor):
      hexbgvalue = None 
      if fillcolor.lower() in Colors.fills:
         hexbgvalue = Colors.fills[fillcolor.lower()]
         hexbgvalue = validFamilyColor(hexlinecolor, hexfillcolor) 
      return hexbgvalue

   def addKeys(self):
      # Add additional keys to group dictionary.
      for groupid, properties in self.groups.items():
          self.groups[groupid]["geometry"] = [0, 0, 0, 0]
          self.groups[groupid]["children"] = []
          self.groups[groupid]["items"] = []
          self.groups[groupid]["final"] = False

      # Add additional keys to node dictionaries.
      for nodeid, properties in self.items.items():
          self.items[nodeid]["geometry"] = [0, 0, 0, 0]
          self.items[nodeid]["children"] = []
          self.items[nodeid]["items"] = []
          self.items[nodeid]["final"] = False

      return

   def addChildren(self):
      for groupid, properties in self.groups.items():
         parentid = properties["parentid"] 
         if parentid != None:
            # Add children list to group dictionary.
            self.groups[parentid]["children"].append(groupid)
         else:
            # Add group to outermost list since no parent. 
            self.tops.append(groupid)

      parents = []
      for groupid, properties in self.groups.items():
         children = properties["children"] 
         parentid = properties["parentid"]
         if len(children) == 0 and not parentid in parents:
            # Add group to innermost list since no children and not same parent.
            self.bottoms.append(groupid)
            parents.append(groupid)

      return

   def addItems(self):
      # Add node list to group dictionary.`
      for nodeid, properties in self.items.items():
         parentid = properties["parentid"] 
         if parentid != None:
            self.groups[parentid]["items"].append(nodeid)
      return

   def mergeItems(self):
      # Combine node list with children list.
      for groupid, properties in self.groups.items():
         items = properties["items"] 
         for nodeid in items:
            self.groups[groupid]["children"].insert(0, nodeid)

      # Combine node dictionary with group dictionary. 
      for nodeid, properties in self.items.items():
         self.groups[nodeid] = properties

      # Delete node list from groups. 
      for groupid, properties in self.groups.items():
         del self.groups[groupid]["items"]

      return

   def sequenceChildren(self):
      # Sort children by sequence index.
      for groupid, properties in self.groups.items():
         childids = properties["children"]
         childcount = len(childids)

         if childcount == 0 or childcount == 1:
            continue

         templist = []
         newlist = []

         for childid in childids:
            templist.append({"id": childid, "index": self.sequence.index(childid)}) 

         templist.sort(key=lambda index: index['index'])

         for item in templist:
            itemid = item["id"]
            newlist.append(itemid)

         nodelist = []
         finallist = []

         for itemid in newlist:
            if self.groups[itemid]["type"] == "node":
               nodelist.append(itemid)
            else:
               if nodelist:
                  finallist.append(nodelist)
                  nodelist = []
               finallist.append(itemid)

         if nodelist:
           finallist.append(nodelist)

         self.groups[groupid]["children"] = finallist

      return

   def sequenceTops(self):
      # Sort tops by sequence index.
      templist = []
      newlist = []
      for topid in self.tops:
         templist.append({"id": topid, "index": self.sequence.index(topid)}) 

      templist.sort(key=lambda index: index['index'])

      for item in templist:
         itemid = item["id"]
         newlist.append(itemid)

      self.sequence = newlist

      return

   def eliminateNesting(self):
      # Combine node list with children list.
      for groupid, properties in self.groups.items():
         children = properties["children"] 
         childcount = len(children)
         newlist = []
         if childcount > 0:
            for childids in children:
               if isinstance(childids, list):
                  for childid in childids:
                     newlist.append(childid)
               else:
                   childid = childids
                   newlist.append(childid)

            if newlist:
               self.groups[groupid]["children"] = newlist

      return

   def calculateIsolatedItems(self):
      mintopspace = 60
      minshapespace = 20
      #minitemspace = 60
      minitemspace = 80
      minnodewidth = 48
      minnodeheight = 48
      mingroupwidth = 240
      mingroupheight = 152

      for groupid, properties in self.groups.items():
         direction = properties["direction"]

         childids = properties["children"]
         childcount = len(childids)

         nodeids = properties["items"]
         nodecount = len(nodeids)

         if childcount > 0:
            # Defer mix of items and groups.
            continue

         if nodecount == 0:
            # Set empty group geometry
            x = minshapespace
            y = mintopspace
            width = mingroupwidth
            height = minnodeheight
            self.groups[groupid]["final"] = True
            self.groups[groupid]["geometry"] = [0, 0, width, height]
            continue

         nodeindex = 0

         nodewidth = minnodewidth
         nodeheight = minnodeheight

         groupwidth = (minnodewidth + (2 * minitemspace)) if direction == "TB" else minitemspace
         groupheight = mintopspace

         # Set node geometry.
         # If no children then follow direction and center single node.
         ## Defer to later: If children then make all items vertical and ignore direction.
         # Add group width and height with items to group.
         #if childcount == 0:
         for nodeid in nodeids:
            nodeindex += 1
            if direction == "LR":
               if nodecount == 1:
                  # Center single node in group.
                  x = (mingroupwidth / 2) - (minnodewidth / 2)
                  y = mintopspace
                  groupwidth = mingroupwidth
                  groupheight = mintopspace + minnodeheight + minitemspace 
               elif nodecount > 1:
                  # Left justify items horizontally in group.
                  # Future: Wrap long list of items to multiple rows.
                  x = ((nodeindex - 1) * minnodewidth) + (nodeindex * minitemspace)
                  y = mintopspace
                  groupwidth += minnodewidth + minitemspace
                  groupheight = mintopspace + minnodeheight + minitemspace 

            elif direction == "TB":
               # Left justify items vertically in group.
               # Center multiple items in group.
               x = (mingroupwidth / 2) - (minnodewidth / 2)
               if nodeindex == 1:
                  y = mintopspace
               else:
                  y = mintopspace + ((nodeindex - 1) * minnodeheight) + ((nodeindex - 1) * minitemspace)
               groupwidth = mingroupwidth
               groupheight += minnodeheight + minitemspace

            self.items[nodeid]["geometry"] = [x, y, nodewidth, nodeheight]

            self.groups[groupid]["final"] = True

         self.groups[groupid]["geometry"] = [0, 0, groupwidth, groupheight]

      return

   def calculateLeftRightGroups(self, parentid):
      mintopspace = 60
      minshapespace = 20
      #minitemspace = 60
      minitemspace = 80
      minnodewidth = 48
      minnodeheight = 48
      mingroupwidth = 240
      mingroupheight = 152

      parent = self.groups[parentid]
      parentgeometry = parent["geometry"]
      parentx = parentgeometry[0]
      parenty = parentgeometry[1]
      parentwidth = parentgeometry[2]
      parentheight = parentgeometry[3]
      parentchildren = parent["children"]
      parentdirection = parent["direction"]
      parentfinal = parent["final"]

      savex = 0
      savey = 0
      savewidth = 0
      saveheight = 0

      newparentwidth = 0
      newparentheight = 0

      position = 0

      for childids in parentchildren:
         position += 1

         if isinstance(childids, list):
            continue

         childid = childids
         child = self.groups[childid]
        
         children = child["children"]

         if len(children) > 0:
            childgeometry = self.calculateChildren(childid)
            self.groups[childid]["final"] = True
         else: 
            childgeometry = child["geometry"]

         childx = childgeometry[0]
         childy = childgeometry[1]
         childwidth = childgeometry[2]
         childheight = childgeometry[3]
         childfinal = child["final"]

         if position == 1:
            savex = minshapespace
            savey = mintopspace
            savewidth += childwidth
            saveheight = max(saveheight, childgeometry[3] + (2 * minshapespace))
            if childfinal:
               self.groups[childid]["geometry"] = [savex, savey, childwidth, childheight]
               newparentwidth += childwidth + savex
               newparentheight += childheight + savey
            else:
               self.groups[childid]["final"] = True
               self.groups[childid]["geometry"] = [savex, savey, savewidth, saveheight]
               newparentwidth += savewidth + savex
               newparentheight += saveheight + savey
         else:
            savex = savewidth + (position * minshapespace)
            savey = mintopspace
            savewidth += childwidth
            saveheight += childheight
            if childfinal:
               self.groups[childid]["geometry"] = [savex, savey, childwidth, childheight]
               newparentwidth += childwidth + minshapespace
               newparentheight = max(newparentheight, childheight + savey)
            else:
               self.groups[childid]["final"] = True
               self.groups[childid]["geometry"] = [savex, savey, savewidth, saveheight]
               newparentwidth += savewidth + savex
               newparentheight += saveheight + savey

      newparentwidth -= (3 * minshapespace)
      newparentheight += minshapespace

      newparentwidth = max(parentwidth, newparentwidth)
      newparentheight = max(parentheight, newparentheight)

      return [0, 0, newparentwidth, newparentheight]

   def calculateTopBottomGroups(self, parentid):
      mintopspace = 60
      minshapespace = 20
      #minitemspace = 60
      minitemspace = 80
      minnodewidth = 48
      minnodeheight = 48
      mingroupwidth = 240
      mingroupheight = 152

      parent = self.groups[parentid]
      parentgeometry = parent["geometry"]
      parentx = parentgeometry[0]
      parenty = parentgeometry[1]
      parentwidth = parentgeometry[2]
      parentheight = parentgeometry[3]
      parentchildren = parent["children"]
      parentdirection = parent["direction"]
      parentfinal = parent["final"]

      savex = 0
      savey = 0
      savewidth = 0
      saveheight = 0

      newparentwidth = 0
      newparentheight = 0

      position = 0

      for childids in parentchildren:
         position += 1

         if isinstance(childids, list):
            continue

         childid = childids
         child = self.groups[childid]

         children = child["children"]

         if len(children) > 0:
            childgeometry = self.calculateChildren(childid)
            self.groups[childid]["final"] = True
         else: 
            childgeometry = child["geometry"]

         childx = childgeometry[0]
         childy = childgeometry[1]
         childwidth = childgeometry[2]
         childheight = childgeometry[3]
         childfinal = child["final"]

         if position == 1:
            savex = minshapespace
            savey = mintopspace
            savewidth = max(savewidth, childgeometry[2] + (2 * minshapespace))
            saveheight += childheight
            if childfinal:
               self.groups[childid]["geometry"] = [savex, savey, childwidth, childheight]
               newparentwidth = childwidth + savex
               newparentheight = childheight + savey
            else:
               self.groups[childid]["final"] = True
               self.groups[childid]["geometry"] = [savex, savey, savewidth, saveheight]
               newparentwidth += savewidth + savex
               newparentheight += saveheight + savey
         else:
            savex = minshapespace
            savey = saveheight + mintopspace + ((position - 1) * minshapespace)
            savewidth += childwidth
            saveheight += childheight
            if childfinal:
               self.groups[childid]["geometry"] = [savex, savey, childwidth, childheight]
               newparentwidth = max(newparentwidth, childwidth + savex)
               newparentheight += childheight + minshapespace
            else:
               self.groups[childid]["final"] = True
               self.groups[childid]["geometry"] = [savex, savey, savewidth, saveheight]
               newparentwidth += savewidth + savex
               newparentheight += saveheight + savey

      newparentwidth += minshapespace
      newparentheight -= minshapespace

      newparentwidth = max(parentwidth, newparentwidth)
      newparentheight = max(parentheight, newparentheight)

      return [0, 0, newparentwidth, newparentheight]

   def calculateLeftRightItems(self, parentid, parentgeometry):
      mintopspace = 60
      minshapespace = 20
      #minitemspace = 60
      minitemspace = 80
      minnodewidth = 48
      minnodeheight = 48
      mingroupwidth = 240
      mingroupheight = 152

      parent = self.groups[parentid]
      parentchildren = parent["children"]
      parentx = parentgeometry[0]
      parenty = parentgeometry[1]
      parentwidth = parentgeometry[2]
      parentheight = parentgeometry[3]

      nodeheight = minnodeheight + minitemspace + minshapespace
      itemsets = 0
      adjustwidth = 0
      adjustheight = 0
      adjusty = 0

      childx = 0
      childy = 0

      newparentwidth = parentwidth
      newparentheight = parentheight

      position = 0

      for childids in parentchildren:
         position += 1

         if isinstance(childids, list):
            itemsets += 1
            nodeindex = 0
            nodecount = len(childids)
            minimalwidth = (2 * minshapespace) + (nodecount * minnodeheight) + (nodecount * minitemspace)
            if parentwidth > minimalwidth:
               widthspacing = floor(parentwidth / nodecount)
            else:
               widthspacing = floor(minimalwidth / nodecount)

            childy = adjusty + minitemspace

            for childid in childids:
               nodeindex += 1

               if nodeindex == 1:
                  childx = floor((widthspacing / 2) - minshapespace)
               else:
                  childx += widthspacing

               self.groups[childid]["geometry"] = [childx, childy, minnodewidth, minnodeheight]

            if position == 1:
               adjustheight += nodeheight - (2 * minshapespace)
            elif position == len(parentchildren):
               adjustheight += nodeheight + (2 * minshapespace)
            else:
               adjustheight += nodeheight

            adjustwidth = max(adjustwidth, minitemspace + (nodeindex * minnodewidth) + (nodeindex * minitemspace))

         else:
            childid = childids
            childgeometry = self.groups[childid]["geometry"]
            childx = childgeometry[0]
            childy = childgeometry[1] + adjustheight
            childwidth = childgeometry[2]
            childheight = childgeometry[3]
            adjusty = childy + childheight

            if position == len(parentchildren):
               adjustheight += 2 * minshapespace

            self.groups[childid]["geometry"] = [childx, childy, childwidth, childheight]

      if adjustheight > 0:
         newparentheight += adjustheight + (itemsets * minshapespace) + (2 * minshapespace)

      newparentwidth = max(newparentwidth, adjustwidth)

      return [0, 0, newparentwidth, newparentheight]

   def calculateTopBottomItems(self, parentid, parentgeometry):
      mintopspace = 60
      minshapespace = 20
      #minitemspace = 60
      minitemspace = 80
      minnodewidth = 48
      minnodeheight = 48
      mingroupwidth = 240
      mingroupheight = 152

      parent = self.groups[parentid]
      parentchildren = parent["children"]
      parentx = parentgeometry[0]
      parenty = parentgeometry[1]
      parentwidth = parentgeometry[2]
      parentheight = parentgeometry[3]

      nodewidth = minnodewidth + minitemspace + minshapespace
      itemsets = 0
      adjustwidth = 0
      adjustheight = 0
      adjustx = 0

      childx = 0
      childy = 0

      newparentwidth = parentwidth
      newparentheight = parentheight

      position = 0

      for childids in parentchildren:
         position += 1

         if isinstance(childids, list):
            itemsets += 1
            nodeindex = 0
            nodecount = len(childids)
            minimalheight = mintopspace + minshapespace + (nodecount * minnodeheight) + (nodecount * minitemspace)
            if parentheight > minimalheight:
               heightspacing = floor(parentheight / nodecount)
            else:
               heightspacing = floor(minimalheight / nodecount)

            childx = adjustx + minitemspace

            for childid in childids:
               nodeindex += 1

               if nodeindex == 1:
                  childy = floor(heightspacing / 2) - minshapespace
               else:
                  childy += heightspacing

               self.groups[childid]["geometry"] = [childx, childy, minnodewidth, minnodeheight]

            if position == len(parentchildren):
               adjustwidth += nodewidth - minshapespace + minitemspace
            else:
               adjustwidth += nodewidth

            adjustheight = max(adjustheight, mintopspace + (nodeindex * minnodeheight) + (nodeindex * minitemspace))

         else:
            childid = childids
            childgeometry = self.groups[childid]["geometry"]
            childx = childgeometry[0] + adjustwidth
            childy = childgeometry[1]
            childwidth = childgeometry[2]
            childheight = childgeometry[3]
            adjustx = childx + childwidth

            if position == len(parentchildren):
               adjustwidth += 2 * minshapespace

            self.groups[childid]["geometry"] = [childx, childy, childwidth, childheight]

      if adjustwidth > 0:
         newparentwidth += adjustwidth + ((itemsets + 2) * minshapespace)

      newparentheight = max(newparentheight, adjustheight)

      return [0, 0, newparentwidth, newparentheight]

   def calculateChildren(self, parentid):
      parent = self.groups[parentid]
      parentgeometry = parent["geometry"]
      parentchildren = parent["children"]
      parentdirection = parent["direction"]
      parentfinal = parent["final"]
      geometry = [0, 0, 0, 0]
      
      if len(parentchildren) == 0 or parentfinal:
         # Already final or no children so return parent geometry as is.
         geometry = parentgeometry

      elif parentdirection == "LR":
         # Parent direction is LR and node direction is TB which are left-justified vertically.
         geometry = self.calculateLeftRightGroups(parentid)
         geometry = self.calculateTopBottomItems(parentid, geometry)
         self.groups[parentid]["final"] = True

      elif parentdirection == "TB":
         # Parent direction is TB and node direction is LR which are left-justified horizontally.
         geometry = self.calculateTopBottomGroups(parentid)
         geometry = self.calculateLeftRightItems(parentid, geometry)
         self.groups[parentid]["final"] = True

      return geometry

   def calculateGeometry(self):
      self.addItems()
      self.calculateIsolatedItems()
      self.mergeItems()
      self.sequenceChildren()

      for groupid in self.bottoms:
         # Loop through parents until no parent.
         parentid = self.groups[groupid]["parentid"]
         while parentid != None:
            geometry = self.calculateChildren(parentid)
            self.groups[parentid]["geometry"] = geometry
            parentid = self.groups[parentid]["parentid"] 

      self.eliminateNesting()

      resetwidth = 0
      for groupid in self.tops:
         group = self.groups[groupid]
         geometry = group["geometry"]
         x = geometry[0] + resetwidth
         y = geometry[1]
         width = geometry[2]
         height = geometry[3]
         self.groups[groupid]["geometry"] = [x, y, width, height]
         resetwidth += width + 20

      return

   def alternateChild(self, groupid, lastColor):
      properties = self.groups[groupid]
      shape = properties["shape"].upper()
      if shape == "ZONE" or shape == "GZONE" or self.common.isAlternateNone():
         properties["fillcolor"] = "none"
      elif lastColor == "WHITE":
         linecolor = properties["linecolor"]
         hexvalue = Colors.lines[linecolor]
         fillname = "light" + Colors.names[hexvalue]
         hexvalue = Colors.names[fillname]
         self.groups[groupid]["fillcolor"] = hexvalue
         lastColor = "LIGHT"
      elif lastColor == "LIGHT":
         self.groups[groupid]["fillcolor"] = "#ffffff"
         lastColor = "WHITE"

      children = properties["children"]
      for childid in children:
         properties = self.groups[childid]
         self.alternateChild(childid, lastColor)

      return

   def alternateFills(self):
      for topid in self.tops:
         properties = self.groups[topid]
         lastColor = properties["fillcolor"]
         # Handle top-level zone.
         shape = properties["shape"].upper()
         if shape == "ZONE" or shape == "GZONE" or self.common.isAlternateNone():
            self.groups[topid]["fillcolor"] = "none"
         elif self.common.isAlternateLight():
            linecolor = properties["linecolor"]
            hexvalue = Colors.lines[linecolor]
            fillname = "light" + Colors.names[hexvalue]
            hexvalue = Colors.names[fillname]
            properties["fillcolor"] = hexvalue
            self.groups[topid]["fillcolor"] = hexvalue
            lastColor = "LIGHT"
         elif self.common.isAlternateWhite():
            self.groups[topid]["fillcolor"] = "#ffffff"
            lastColor = "WHITE"

         children = properties["children"]
         for childid in children:
            properties = self.groups[childid]
            self.alternateChild(childid, lastColor)
      return

   # For containers nested inside zones:
   #   Set nested container parent to first container outside of zone.
   #   Set nested container x, y to be relative to first container outside of zone.
   def eliminateZoneParents(self):
      for bottomid in self.bottoms:
         childid = bottomid
         childproperties = self.groups[childid]
         childshape = childproperties["shape"].upper()
         if childshape == "ZONE" or childshape == "GZONE":
            continue
        
         parentid = childproperties["parentid"] 
         while parentid != None:
            parentproperties = self.groups[parentid]

            savex = 0
            savey = 0
            zonesFound = False

            parentshape = parentproperties["shape"].upper()
            while parentshape == "ZONE" or parentshape == "GZONE":
               zoneid = parentid
               zoneproperties = parentproperties
               zonegeometry = zoneproperties["geometry"]
               savex += zonegeometry[0]
               savey += zonegeometry[1]
               parentid = zoneproperties["parentid"] 
               parentproperties = self.groups[parentid]
               parentshape = parentproperties["shape"].upper()
               self.groups[zoneid]["parentid"] = parentid
               zonesFound = True
               
            if zonesFound == True:
               zonegeometry = zoneproperties["geometry"]
               childgeometry = childproperties["geometry"]
               direction = childproperties["direction"]
               childx = savex + childgeometry[0]
               childy = savey + childgeometry[1]
               childwidth = childgeometry[2]
               childheight = childgeometry[3]
               self.groups[childid]["geometry"] = [childx, childy, childwidth, childheight]
               self.groups[childid]["parentid"] = parentid
               savex = 0
               savey = 0

            childid = parentid
            childproperties = self.groups[childid]
            parentid = childproperties["parentid"] 

      return

   # For containers nested inside zones:
   #   Set nested container parent to first container outside of zone.
   #   Set nested container x, y to be relative to first container outside of zone.
   '''
   def moveZoneParent(self, groupid, properties):
      mintopspace = 60
      minshapespace = 20

      shape = properties["shape"].upper()
      geometry = properties["geometry"]
      x = geometry[0]
      y = geometry[1]
      width = geometry[2]
      height = geometry[3]

      if shape == "ZONE" or shape == "GZONE":
         parentid = properties["parentid"] 
         parentproperties = self.groups[parentid]
         parentshape = parentproperties["shape"].upper()
         parentgeometry = parentproperties["geometry"]

         while parentshape == "ZONE" or parentshape == "GZONE": 
            parentid = parentproperties["parentid"] 
            parentproperties = self.groups[parentid]
            parentshape = parentproperties["shape"].upper()
            parentgeometry = parentproperties["geometry"]

            x += minshapespace
            y += mintopspace

         properties["geometry"] = [x, y, width, height]
         properties["newparentid"] = parentid

      else:

         parentid = properties["parentid"] 
         if parentid == None:
            return properties

         parentproperties = self.groups[parentid]
         parentshape = parentproperties["shape"].upper()

         while parentshape == "ZONE" or parentshape == "GZONE": 
            parentid = parentproperties["parentid"] 
            parentproperties = self.groups[parentid]
            parentshape = parentproperties["shape"].upper()

            x += minshapespace
            y += mintopspace

         properties["geometry"] = [x, y, width, height]
         properties["newparentid"] = parentid

      return properties
   '''

   def printSequence(self):
      for sequenceid in self.sequence:
         if sequenceid in self.diagrams:
            label = "Diagram " + self.diagrams[sequenceid]["name"]
         elif sequenceid in self.groups:
            label = "Group " + self.groups[sequenceid]["label"]
         elif sequenceid in self.items:
            label = "Node " + self.items[sequenceid]["label"]
         else:
            label = "None"
         print("")
         print(f'"{sequenceid}": {label}')
      return

   def printDiagrams(self):
      print("")
      print("Diagrams:")
      for key, value in self.diagrams.items():
         print("")
         print(f'"{key}": {value}')
      return

   def printGroups(self):
      print("")
      print("Groups:")
      for key, value in self.groups.items():
         print("")
         print(f'"{key}": {value}')
      return

   def printItems(self):
      print("")
      print("Items:")
      for key, value in self.items.items():
         print("")
         print(f'"{key}": {value}')
      return

   def printEdges(self):
      print("")
      print("Edges:")
      for key, value in self.edges.items():
         print("")
         print(f'"{key}": {value}')
      return

   def printBottoms(self):
      print("")
      print("Bottoms:")
      for groupid in self.bottoms:
         print("")
         print(f'"{groupid}"')
      return

   def printTops(self):
      print("")
      print("Tops:")
      for groupid in self.tops:
         print("")
         print(f'"{groupid}"')
      return

   # Get zone CIDR.
   def getZoneCIDR(self, zone):
      match zone:
         case 'au-syd-1': cidr = ZoneCIDR.AU_SYD_1
         case 'au-syd-2': cidr = ZoneCIDR.AU_SYD_2
         case 'au-syd-3': cidr = ZoneCIDR.AU_SYD_3

         case 'br-sao-1': cidr = ZoneCIDR.BR_SAO_1
         case 'br-sao-2': cidr = ZoneCIDR.BR_SAO_2
         case 'br-sao-3': cidr = ZoneCIDR.BR_SAO_3

         case 'ca-tor-1': cidr = ZoneCIDR.CA_TOR_1
         case 'ca-tor-2': cidr = ZoneCIDR.CA_TOR_2
         case 'ca-tor-3': cidr = ZoneCIDR.CA_TOR_3

         case 'eu-de-1': cidr = ZoneCIDR.EU_DE_1
         case 'eu-de-2': cidr = ZoneCIDR.EU_DE_2
         case 'eu-de-3': cidr = ZoneCIDR.EU_DE_3

         case 'eu-gb-1': cidr = ZoneCIDR.EU_GB_1
         case 'eu-gb-2': cidr = ZoneCIDR.EU_GB_2
         case 'eu-gb-3': cidr = ZoneCIDR.EU_GB_3

         case 'jp-osa-1': cidr = ZoneCIDR.JP_OSA_1
         case 'jp-osa-2': cidr = ZoneCIDR.JP_OSA_2
         case 'jp-osa-3': cidr = ZoneCIDR.JP_OSA_3

         case 'jp-tok-1': cidr = ZoneCIDR.JP_TOK_1
         case 'jp-tok-2': cidr = ZoneCIDR.JP_TOK_2
         case 'jp-tok-3': cidr = ZoneCIDR.JP_TOK_3

         case 'us-east-1': cidr = ZoneCIDR.US_EAST_1
         case 'us-east-2': cidr = ZoneCIDR.US_EAST_2
         case 'us-east-3': cidr = ZoneCIDR.US_EAST_3

         case 'us-south-1': cidr = ZoneCIDR.US_SOUTH_1
         case 'us-south-2': cidr = ZoneCIDR.US_SOUTH_2
         case 'us-south-3': cidr = ZoneCIDR.US_SOUTH_3

         case _: cidr = ZoneCIDR.NONE

      return cidr.value
