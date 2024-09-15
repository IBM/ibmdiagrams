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

from sys import exit as sys_exit
from contextvars import ContextVar
from enum import Enum
from uuid import uuid4

from .ibmbase.properties import Properties
from .ibmbase.build import Build
from .ibmbase.common import Common
from .ibmbase.compose import Compose
from .ibmbase.load import Load


_diagrams = ContextVar("diagrams")
_diagram = ContextVar("diagram")
_group = ContextVar("group")

#_diagrams = {} # Dictionary of diagrams.
#_groups = {} # Dictionary of groups.
#_items = {}    # Dictionary of items.
#_connectors = {}    # Dictionary of connectors.

_data = Properties()
_savediagrams = {}


def getDiagrams():
   try:
      return _diagrams.get()
   except LookupError:
      return None

def setDiagrams(diagrams):
   _diagrams.set(diagrams)

def saveDiagram(name, xmldata):
   if not name in _savediagrams:
      _savediagrams[name] = xmldata 

def getDiagram():
   try:
      return _diagram.get()
   except LookupError:
      return None

def setDiagram(diagram):
   _diagram.set(diagram)

def getGroup():
   try:
      return _group.get()
   except LookupError:
      return None

def setGroup(group):
   _group.set(group)


# Return a unique id for groupid and itemid.
@staticmethod
def randomid():
   return uuid4().hex


class Diagrams:
   common = None
   properties = {}
   diagramid = None

   def __init__(self, 
                name = "",
                filename = ""):
      self.common = Common()
      self.common.setInputPython()
      self.diagramid = randomid()

      self.properties = _data.getDiagramsProperties(name=name, filename=filename)
      _data.addSheets(self.diagramid, self.properties)
      return

   def __enter__(self):
      setDiagrams(self)
      return self

   def __exit__(self, exception_type, exception_value, traceback):
      build = Build(self.common, _data)
      build.buildSheets(self.properties, _savediagrams)
      del build
      setDiagrams(None)
      return

class Diagram:
   common = None
   properties = {}
   diagramid = None
   name = ""

   def __init__(self, 
                name = "",
                filename = "",
                output = "",
                #input = "",
                direction = "LR",
                icontype = "STATIC"):
      self.common = Common()
      self.common.setInputPython()
      self.diagramid = randomid()
      self.name = name

      if icontype.upper()  == "BUILTIN":
         self.common.setBuiltinIcons()
      elif icontype.upper() == "CATALOG":
         self.common.setCatalogIcons()
      elif icontype.upper() == "STATIC":
         self.common.setStaticIcons()
      else:
         self.common.setStaticIcons()

      if direction.upper() == "LR":
         self.common.setDirectionLR()
      elif direction.upper() == "TB":
         self.common.setDirectionTB()
      else:
         self.common.setDirectionLR()

      if getDiagrams() != None:
         filename = "*"

      self.properties = _data.getDiagramProperties(name=name, filename=filename, output=output, direction=direction, icontype=icontype)
      #_diagrams[self.diagramid] = self.properties
      _data.addDiagram(self.diagramid, self.properties)
      _data.updateSequence(self.diagramid)
      return

   def __enter__(self):
      setDiagram(self)
      return self

   def __exit__(self, exception_type, exception_value, traceback):
      build = Build(self.common, _data)
      xmldata = build.buildDiagrams()
      if xmldata == None:
         self.common.printExit()
      else:
         saveDiagram(self.name, xmldata)
      del build
      _data.reset()
      setDiagram(None)
      #setGroup(None)
      return

class Group:
   common = None
   icons = None
   shapeid = None
   parentid = None
   sourceid = None
   targetid = None
   parent = None
   item = None
   connector = None
   properties = {}

   def __init__(self, 
                label = "",
                sublabel = "",
                linecolor = "",
                fillcolor = "",
                shape = "",
                icon = "",
                hideicon = "",
                fontname = "IBM Plex Sans",
                fontsize = 14,
                direction = ""):
      self.common = Common()
      self.shapeid = randomid()

      self.parent = getGroup()
      if self.parent:
         self.parentid = self.parent.shapeid
      else:
         #self.diagram = getDiagram()
         #if self.diagram:
         #   self.parentid = self.diagram.shapeid
         #else:
         self.parent = None

      self.properties = _data.getGroupProperties(label=label, sublabel=sublabel, linecolor=linecolor, fillcolor=fillcolor, shape=shape, icon=icon, hideicon=hideicon, fontname=fontname, fontsize=fontsize, direction=direction, parentid=self.parentid)
      _data.updateSequence(self.shapeid)

      return

   def __enter__(self):
      setGroup(self)
      return self

   def __exit__(self, exception_type, exception_value, traceback):
      _data.addGroup(self.shapeid, self.properties)
      #if self.parent:
      setGroup(self.parent)
      return

   def __sub__(self, shape = None):
      # group - group or group - item or group - connector
      if isinstance(shape, Group) or isinstance(shape, Item):
         connector = Connector(sourceid=self.shapeid, targetid=shape.shapeid, startarrow="", endarrow="", operator="sub")
      else:  # isinstance(shape, Connector)
         shape.sourceid = self.shapeid
         #shape.startarrow = ""
         #shape.endarrow = ""
         shape.operator = "sub"
      return shape

   def __lshift__(self, shape = None):
      # shape << shape or shape << connector
      if isinstance(shape, Group) or isinstance(shape, Item):
         connector = Connector(sourceid=shape.shapeid, targetid=self.shapeid, startarrow="", endarrow="classic", operator="lshift")
      else:  # isinstance(shape, Connector)
         shape.sourceid = self.shapeid
         #shape.startarrow = ""
         #shape.endarrow = ""
         shape.operator = "lshift"
      return shape

   def __rshift__(self, shape = None):
      # shape >> shape or shape >> connector
      if isinstance(shape, Group) or isinstance(shape, Item):
         connector = Connector(sourceid=self.shapeid, targetid=shape.shapeid, startarrow="", endarrow="classic", operator="rshift")
      else:  # isinstance(shape, Connector)
         shape.sourceid = self.shapeid
         #shape.startarrow = ""
         #shape.endarrow = ""
         shape.operator = "rshift"
      return shape

class Item:
   common = None
   icon = None
   shapeid = None
   parentid = None
   sourceid = None
   targetid = None
   parent = None
   startarrow = ""
   endarrow = ""
   operator = ""
   style = ""
   item = None
   connector = None
   properties = {}

   def __init__(self, 
                label = "", 
                sublabel = "", 
                linecolor = "",
                fillcolor = "",
                shape = "",
                icon = "",
                hideicon = "",
                fontname = "IBM Plex Sans",
                fontsize = 14):
                #many = False,
                #provider = ""):      # Not currently used.
      self.common = Common()
      self.shapeid = randomid()

      self.parent = getGroup()
      self.parentid = self.parent.shapeid
      setGroup(self.parent)

      self.properties = _data.getItemProperties(label=label, sublabel=sublabel, linecolor=linecolor, fillcolor=fillcolor, shape=shape, icon=icon, hideicon=hideicon, fontname=fontname, fontsize=fontsize, parentid=self.parentid)

      #_items[self.shapeid] = self.properties
      _data.addItem(self.shapeid, self.properties)
      _data.updateSequence(self.shapeid)

      return

   #def __repr__(self):
   #   print("repr:")
   #   print(self.properties)

   #def __str__(self):
   #   print("str:")
   #   return self.properties["label"]

   def __sub__(self, shape = None):
      # item - item or item - connector
      if isinstance(shape, Group) or isinstance(shape, Item):
         #connector = Connector(sourceid=self.shapeid, targetid=shape.shapeid, startarrow="", endarrow="", operator="sub", fontname=self.fontname, fontsize=12)
         connector = Connector(sourceid=self.shapeid, targetid=shape.shapeid, startarrow="", endarrow="", operator="sub")
      else:  # isinstance(shape, Connector)
         shape.sourceid = self.shapeid
         #shape.startarrow = ""
         #shape.endarrow = ""
         shape.operator = "sub"
      return shape

   def __lshift__(self, shape = None):
      # shape << shape or shape << connector
      if isinstance(shape, Group) or isinstance(shape, Item):
         #connector = Connector(sourceid=shape.shapeid, targetid=self.shapeid, operator="lshift", fontname=self.fontname, fontsize=12)
         #connector = Connector(sourceid=shape.shapeid, targetid=self.shapeid, startarrow="", endarrow="classic", operator="lshift", fontname=self.fontname, fontsize=12)
         connector = Connector(sourceid=shape.shapeid, targetid=self.shapeid, startarrow="", endarrow="classic", operator="lshift")

      else:  # isinstance(shape, Connector)
         shape.sourceid = self.shapeid
         #shape.startarrow = ""
         #shape.endarrow = "classic"
         shape.operator = "lshift"

         connectorid = shape.getConnectorID()
         _data.setConnectorSourceID(connectorid, shape.shapeid)
         _data.setConnectorTargetID(connectorid, self.shapeid)
         _data.setConnectorEndArrow(connectorid, "classic")

         #print("__init::lshift printConnector:")
         #_data.printConnector(connectorid)

      return shape

   def __rshift__(self, shape = None):
      # shape >> shape or shape >> connector
      if isinstance(shape, Group) or isinstance(shape, Item):
         #connector = Connector(sourceid=self.shapeid, targetid=shape.shapeid, color = "", operator="rshift", fontname=self.fontname, fontsize=12)
         #connector = Connector(sourceid=self.shapeid, targetid=shape.shapeid, startarrow="", endarrow="classic", operator="rshift", fontname=self.fontname, fontsize=12)

         connector = Connector(sourceid=self.shapeid, targetid=shape.shapeid, startarrow="", endarrow="classic", operator="rshift")

      else:  # isinstance(shape, Connector)
         shape.targetid = self.shapeid
         #shape.startarrow = ""
         #shape.endarrow = "classic"
         shape.startarrow = "classic"
         shape.endarrow = "" 
         shape.operator = "rshift"

         if self.targetid != None:
            _data.setConnectorSourceID(self.shapeid, self.targetid)
            _data.setConnectorTargetID(self.shapeid, self.sourceid)
            _data.setConnectorStartArrow(self.shapeid, self.startarrow)
            _data.setConnectorEndArrow(self.shapeid, self.endarrow)
            _data.setConnectorStartFill(self.shapeid, self.startfill)
            _data.setConnectorEndFill(self.shapeid, self.endfill)
            _data.setConnectorOperator(self.shapeid, shape.operator)

      return shape

class Connector:
   common = None
   shapeid = None
   parentid = None
   #sourceid = None
   #targetid = None
   parent = None
   color = ""
   startarrow = ""
   endarrow = ""
   startfill = ""
   endfill = ""
   #operator = ""
   #style = ""
   item = None
   connector = None
   properties = {}

   def __init__(self, 
                label = "", 
                forward = False,   # Not currently used.
                reverse = False,   # Not currently used.
                color = "",        # Not currently used.
                style = "",        # Not currently used.
                startarrow = "classic",
                endarrow = "classic",
                startfill = True,
                endfill = True,
                fontname = "IBM Plex Sans",
                fontsize = 14,
                operator = "",     # Internal use only.
                sourceid = None,   # Internal use only.
                targetid = None):  # Internal use only.
      self.common = Common()
      self.shapeid = randomid()

      self.color = color

      self.startarrow = startarrow
      self.endarrow = endarrow
      self.startfill = startfill
      self.endfill = endfill

      self.properties = _data.getConnectorProperties(label=label, sourceid=sourceid, targetid=targetid, color=color, style=style, startarrow=startarrow, endarrow=endarrow, startfill=startfill, endfill=endfill, fontname=fontname, fontsize=fontsize)
      _data.addConnector(self.shapeid, self.properties)
      _data.updateSequence(self.shapeid)

      #print("__init::connector::init printConnector:")
      #_data.printConnector(self.shapeid)

      return

   def getConnectorID(self):
      return self.shapeid

   def __sub__(self, shape = None):
      # connector - shape
      if isinstance(shape, Group) or isinstance(shape, Item):
         if self.sourceid != None:
            _data.setConnectorSourceID(self.shapeid, self.sourceid)
            _data.setConnectorTargetID(self.shapeid, shape.shapeid)
            _data.setConnectorStartArrow(self.shapeid, self.startarrow)
            _data.setConnectorEndArrow(self.shapeid, self.endarrow)
            _data.setConnectorStartFill(self.shapeid, self.startfill)
            _data.setConnectorEndFill(self.shapeid, self.endfill)
            _data.setConnectorOperator(self.shapeid, self.operator)
         else:
            # Minus has precedence over << and sourceid hasn't been set.
            # Set dummy value for source to prevent serialization error in dumpXML.
            _data.setConnectorSourceID(self.shapeid, self.shapeid)
            _data.setConnectorTargetID(self.shapeid, shape.shapeid)
            _data.setConnectorStartArrow(self.shapeid, self.startarrow)
            _data.setConnectorEndArrow(self.shapeid, self.endarrow)
            _data.setConnectorStartFill(self.shapeid, self.startfill)
            _data.setConnectorEndFill(self.shapeid, self.endfill)
            _data.setConnectorOperator(self.shapeid, self.operator)
            print("Connector.__sub__: shape << connector - shape not supported")
            sys_exit()
      else:
         print("Connector.__sub__: connector - shape not supported")
         sys_exit()

      return shape

   def __lshift__(self, shape = None):
      # connector << shape
      if isinstance(shape, Group) or isinstance(shape, Item):
         _data.setConnectorSourceID(self.shapeid, shape.shapeid)
         _data.setConnectorTargetID(self.shapeid, self.sourceid)
         _data.setConnectorOperator(self.shapeid, self.operator)
         #arrow = "double" if self.operator == "rshift" else "single" 
         if self.operator == "rshift":
            # Double arrow.
            _data.setConnectorStartArrow(self.shapeid, self.startarrow)
            _data.setConnectorEndArrow(self.shapeid, self.endarrow)
            _data.setConnectorStartFill(self.shapeid, self.startfill)
            _data.setConnectorEndFill(self.shapeid, self.endfill)
         else:
            # Single arrow.
            _data.setConnectorStartArrow(self.shapeid, self.startarrow)
            _data.setConnectorEndArrow(self.shapeid, self.endarrow)
            _data.setConnectorStartFill(self.shapeid, self.startfill)
            _data.setConnectorEndFill(self.shapeid, self.endfill)
      else:
         print("Connector.__lshift__: connector << shape not supported")
         sys_exit()
      return shape

   def __rshift__(self, shape = None):
      # connector >> shape
      if isinstance(shape, Group) or isinstance(shape, Item):
         #_data.setConnectorSourceID(self.shapeid, self.sourceid)
         #_data.setConnectorTargetID(self.shapeid, shape.shapeid)
         #_data.setConnectorOperator(self.shapeid, self.operator)
         _data.setConnectorSourceID(self.shapeid, shape.shapeid)
         #arrow = "double" if self.operator == "lshift" else "single" 
         if self.operator == "lshift":
            # Double arrow.
            #_data.setConnectorStartArrow(self.shapeid, self.startarrow)
            _data.setConnectorStartArrow(self.shapeid, "classic")
            #_data.setConnectorEndArrow(self.shapeid, self.endarrow)
            #_data.setConnectorStartFill(self.shapeid, self.startfill)
            #_data.setConnectorEndFill(self.shapeid, self.endfill)

            #print("__init::lshift printConnector:")
            #_data.printConnector(self.shapeid)

         else:
            # Single arrow.
            _data.setConnectorStartArrow(self.shapeid, self.startarrow)
            _data.setConnectorEndArrow(self.shapeid, self.endarrow)
            _data.setConnectorStartFill(self.shapeid, self.startfill)
            _data.setConnectorEndFill(self.shapeid, self.endfill)

      else:
         print("Connector.__rshift__: connector >> shape not supported")
         sys_exit()
      return shape
