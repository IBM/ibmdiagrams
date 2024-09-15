# @file properties.py
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

from enum import Enum

class Properties:
   def __init__(self):
      self.sequence = []
      self.sheets = {}
      self.diagrams = {}
      self.groups = {}
      self.items = {}
      self.connectors = {}

   def reset(self):
      self.sequence = []
      self.diagrams = {}
      self.groups = {}
      self.items = {}
      self.connectors = {}

   def getSequence(self):
      return self.sequence

   def getSheets(self):
      return self.sheets

   def getDiagrams(self):
      return self.diagrams

   def getGroups(self):
      return self.groups

   def getItems(self):
      return self.items

   def getConnectors(self):
      return self.connectors

   def setSheets(self, sheets):
      self.sheets = sheets

   def setDiagrams(self, diagrams):
      self.diagrams = diagrams

   def setGroups(self, groups):
      self.groups = groups

   def setItems(self, items):
      self.items = items

   def setConnectors(self, connectors):
      self.connectors = connectors

   def addSheets(self, diagramid, properties):
      self.sheets[diagramid] = properties

   def addDiagram(self, diagramid, properties):
      self.diagrams[diagramid] = properties

   def addGroup(self, groupid, properties):
      self.groups[groupid] = properties

   def addItem(self, nodeid, properties):
      self.items[nodeid] = properties

   def addConnector(self, connectorid, properties):
      self.connectors[connectorid] = properties

   def getConnectorLabel(self, shapeid):
      return self.connectors[shapeid]["label"]

   def getConnectorSourceID(self, shapeid):
      return self.connectors[shapeid]["sourceid"]

   def getConnectorTargetID(self, shapeid):
      return self.connectors[shapeid]["targetid"]

   def getConnectorStartArrow(self, shapeid):
      return self.connectors[shapeid]["startarrow"]

   def getConnectorEndArrow(self, shapeid):
      return self.connectors[shapeid]["endarrow"]

   def setConnectorSourceID(self, shapeid, sourceid):
      self.connectors[shapeid]["sourceid"] = sourceid 

   def setConnectorTargetID(self, shapeid, targetid):
      self.connectors[shapeid]["targetid"] = targetid

   def setConnectorStartArrow(self, shapeid, startarrow):
      self.connectors[shapeid]["startarrow"] = startarrow 

   def setConnectorEndArrow(self, shapeid, endarrow):
      self.connectors[shapeid]["endarrow"] = endarrow 

   def setConnectorStartFill(self, shapeid, startfill):
      self.connectors[shapeid]["startfill"] = startfill 

   def setConnectorEndFill(self, shapeid, endfill):
      self.connectors[shapeid]["endfill"] = endfill 

   def setConnectorOperator(self, shapeid, operator):
      self.connectors[shapeid]["operator"] = operator

   def printConnector(self, shapeid):
      print("printConnector:")
      print("label:")
      print(self.connectors[shapeid]["label"])
      print("sourceid:")
      print(self.connectors[shapeid]["sourceid"])
      print("targetid:")
      print(self.connectors[shapeid]["targetid"])
      print("startarrow:")
      print(self.connectors[shapeid]["startarrow"])
      print("endarrow:")
      print(self.connectors[shapeid]["endarrow"])
      print("startfill:")
      print(self.connectors[shapeid]["startfill"])
      print("endfill:")
      print(self.connectors[shapeid]["endfill"])
      print("operator:")
      print(self.connectors[shapeid]["operator"])

   def updateSequence(self, sequenceid):
      self.sequence.append(sequenceid)

   def getDiagramsProperties(self,
      attrtype = "diagrams",
      name = "",
      filename = ""):
    return {
      "type": attrtype,
      "name": name,
      "filename": filename}

   def getDiagramProperties(self,
      attrtype = "diagram",
      name = "",
      filename = "",
      output = "",
      input = "",
      direction = "",
      #alternate = "",
      #provider = "",
      icontype = ""):
      #outformat = ""):
    return {
      "type": attrtype,
      "name": name,
      "filename": filename,
      "output": output,
      "input": input,
      "direction": direction,
      "icontype": icontype}

   def getGroupProperties(self,
      attrtype = "group",
      label = "",
      sublabel = "",
      shape = "",
      linecolor = "",
      fillcolor = "",
      badgetext = "",
      badgeshape = "",
      badgelinecolor = "",
      badgefillcolor = "",
      icon = "",
      #icontype = "",
      hideicon = False,
      direction = "",
      #many = False,
      #alternate = "",
      #provider = "",
      fontname = "",
      fontsize = 0,
      data = None,
      parentid = None):
    return {
      "type": attrtype,
      "label": label,
      "sublabel": sublabel,
      "shape": shape,
      "linecolor": linecolor,
      "fillcolor": fillcolor,
      "badgetext": badgetext,
      "badgeshape": badgeshape,
      "badgelinecolor": badgelinecolor,
      "badgefillcolor": badgefillcolor,
      "icon": icon,
      #"icontype": icontype,
      "hideicon": hideicon,
      "direction": direction,
      "fontname": fontname,
      "fontsize": fontsize,
      "data": data,
      "parentid": parentid}

   def getItemProperties(self,
      attrtype = "node",
      label = "",
      sublabel = "",
      shape = "",
      linecolor = "",
      fillcolor = "",
      badgetext = "",
      badgeshape = "",
      badgelinecolor = "",
      badgefillcolor = "",
      icon = "",
      #icontype = "",
      hideicon = "",
      fontname = "",
      fontsize = 0,
      data = None,
      parentid = None):
    return {
      "type": attrtype,
      "label": label,
      "sublabel": sublabel,
      "shape": shape,
      "linecolor": linecolor,
      "fillcolor": fillcolor,
      "badgetext": badgetext,
      "badgeshape": badgeshape,
      "badgelinecolor": badgelinecolor,
      "badgefillcolor": badgefillcolor,
      "icon": icon,
      #"icontype": icontype,
      "hideicon": hideicon,
      "fontname": fontname,
      "fontsize": fontsize,
      "data": data,
      "parentid": parentid}

   def getConnectorProperties(self,
      attrtype = "connector",
      label = "",
      sourceid = "",
      targetid = "",
      color = "",
      style = "",
      startarrow = "",
      endarrow = "",
      startfill = "",
      endfill = "",
      operator = "",
      fontname = "",
      fontsize = 0):
    return {
      "type": attrtype,
      "label": label,
      "sourceid": sourceid,
      "targetid": targetid,
      "color": color,
      "style": style,
      "startarrow": startarrow,
      "endarrow": endarrow,
      "startfill": startfill,
      "endfill": endfill,
      "operator": operator,
      "fontname": fontname,
      "fontsize": fontsize}

   def getSingleArrowProperties(self,
      label = "",
      sourceid = "",
      targetid = "",
      color = "",
      fontname = "",
      fontsize = 0):
    return self.getConnectorProperties(
      label = label,
      sourceid = sourceid,
      targetid = targetid,
      color = color,
      endarrow = "Classic",
      endfill = True,
      fontname = fontname,
      fontsize = fontsize)

   def getDoubleArrowProperties(self,
      label = "",
      sourceid = "",
      targetid = "",
      color = "",
      fontname = "",
      fontsize = 0):
    return self.getConnectorProperties(
      label = label,
      sourceid = sourceid,
      targetid = targetid,
      color = color,
      startarrow = "Classic",
      endarrow = "Classic",
      startfill = True,
      endfill = True,
      fontname = fontname,
      fontsize = fontsize)

# Valid attribute values.
# Valid attribute values.

class Directions(Enum):
   LR = 'LR'
   TB = 'TB'

class Alternates(Enum):
   WHITE = 'WHITE'  # white-to-light
   LIGHT = 'LIGHT'  # light-to-white
   NONE = 'NONE'     # all transparent
   USER = 'USER'     # all user-defined

class Providers(Enum):
   ANY = 'ANY'  # logical
   IBM = 'IBM'  # prescribed-ibm

# Items are collapsed layout.
class ItemTypes(Enum):
   ACTOR = 'ACTOR'
   PNODE = 'PRESCRIBED NODE'

# Groups are expanded layout.
class GroupTypes(Enum):
   EPNODE = 'PRESCRIBED NODE EXPANDED'
   PLOC = 'PRESCRIBED LOCATION'
   GPLOC = 'GENERIC PRESCRIBED LOCATION'
   ZONE = 'ZONE'
   GZONE = 'GENERIC ZONE'

class OutputFormats(Enum):
   JPG = 'JPG'
   PDF = 'PDF'
   PNG = 'PNG'
   SVG = 'SVG'
   XML = 'XML'

class IconTypes(Enum):
   BUILTIN = 'BUILTIN'
   CATALOG = 'CATALOG'
   STATIC = 'STATIC'

class Fonts(Enum):
   IBM_PLEX_SANS = 'IBM Plex Sans'
   IBM_PLEX_SANS_ARABIC = 'IBM Plex Sans Arabic'
   IBM_PLEX_SANS_DEVANAGARI = 'IBM Plex Sans Devanagari'
   IBM_PLEX_SANS_HEBREW = 'IBM Plex Sans Hebrew'
   IBM_PLEX_SANS_JP = 'IBM Plex Sans JP'
   IBM_PLEX_SANS_KR = 'IBM Plex Sans KR'
   IBM_PLEX_SANS_THAI = 'IBM Plex Sans Thai'

class ConnectorArrows(Enum):
   NONE = 'NONE'
   CLASSIC = 'CLASSIC'
   OVAL = 'OVAL'

class ConnectorStyles(Enum):
   SOLID = 'SOLID'
   DASHED = 'DASHED'

# Allows customization of lines and arrows.
class ExtendedConnectorStyles(Enum):
   SOLID_LINE = 'dashed=0;'
   DASHED_LINE = 'dashed=1;'
   NO_ARROW = 'endArrow=none;'
   SINGLE_ARROW = 'endArrow=block;endFill=1;'
   DOUBLE_ARROW = 'endArrow=block;endFill=1;startArrow=block;startFill=1;'


