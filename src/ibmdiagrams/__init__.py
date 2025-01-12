#i @file __init__.py
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
from .ibmbase.composejson import ComposeJSON
from .ibmbase.loadjson import LoadJSON


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
   fontname = None
   name = ""

   def __init__(self, 
                name = "",
                filename = "",
                output = "",
                #input = "",
                #icontype = "STATIC",
                font = "IBM Plex Sans",
                direction = "LR"):
      self.common = Common()
      self.common.setInputPython()
      self.diagramid = randomid()
      self.name = name

      self.fontname = font
      self.common.setFontName(self.fontname)

      if direction.upper() == "LR":
         self.common.setDirectionLR()
      elif direction.upper() == "TB":
         self.common.setDirectionTB()
      else:
         self.common.setDirectionLR()

      if getDiagrams() != None:
         filename = "*"

      self.properties = _data.getDiagramProperties(name=name, filename=filename, output=output, fontname=self.fontname, direction=direction)
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
   fontname = None
   fontsize = 14
   properties = {}

   def __init__(self, 
                label = "",
                sublabel = "",
                linecolor = "",
                fillcolor = "",
                shape = "",
                icon = "",
                hideicon = "",
                direction = ""):
      self.common = Common()
      self.shapeid = randomid()

      self.fontname = self.common.getFontName()

      self.parent = getGroup()
      if self.parent:
         self.parentid = self.parent.shapeid
      else:
         #self.diagram = getDiagram()
         #if self.diagram:
         #   self.parentid = self.diagram.shapeid
         #else:
         self.parent = None

      self.properties = _data.getGroupProperties(label=label, sublabel=sublabel, linecolor=linecolor, fillcolor=fillcolor, shape=shape, icon=icon, hideicon=hideicon, fontname=self.fontname, fontsize=self.fontsize, direction=direction, parentid=self.parentid)
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
         connector = Connector(sourceid=shape.shapeid, targetid=self.shapeid, startarrow="", endarrow="arrow", operator="lshift")
      else:  # isinstance(shape, Connector)
         shape.sourceid = self.shapeid
         #shape.startarrow = ""
         #shape.endarrow = ""
         shape.operator = "lshift"
      return shape

   def __rshift__(self, shape = None):
      # shape >> shape or shape >> connector
      if isinstance(shape, Group) or isinstance(shape, Item):
         connector = Connector(sourceid=self.shapeid, targetid=shape.shapeid, startarrow="", endarrow="arrow", operator="rshift")
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
   fontname = None
   fontsize = 14
   properties = {}

   def __init__(self, 
                label = "", 
                sublabel = "", 
                linecolor = "",
                fillcolor = "",
                shape = "",
                icon = "",
                hideicon = ""):
                #many = False,
                #provider = ""):      # Not currently used.
      self.common = Common()
      self.shapeid = randomid()

      self.parent = getGroup()
      self.parentid = self.parent.shapeid
      setGroup(self.parent)

      self.fontname = self.common.getFontName()

      self.properties = _data.getItemProperties(label=label, sublabel=sublabel, linecolor=linecolor, fillcolor=fillcolor, shape=shape, icon=icon, hideicon=hideicon, fontname=self.fontname, fontsize=self.fontsize, parentid=self.parentid)

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
         connector = Connector(sourceid=self.shapeid, targetid=shape.shapeid, startarrow="", endarrow="", operator="sub")
      else:  # isinstance(shape, Connector)
         shape.sourceid = self.shapeid
         shape.operator = "sub"
      return shape

   def __lshift__(self, shape = None):
      # shape << shape or shape << connector
      if isinstance(shape, Group) or isinstance(shape, Item):
         connector = Connector(sourceid=shape.shapeid, targetid=self.shapeid, startarrow="", endarrow="arrow", operator="lshift")

      else:  # isinstance(shape, Connector)
         shape.sourceid = self.shapeid
         shape.operator = "lshift"

         connectorid = shape.getConnectorID()
         _data.setConnectorSourceID(connectorid, shape.shapeid)
         _data.setConnectorTargetID(connectorid, self.shapeid)
         #NEW _data.setConnectorEndArrow(connectorid, "block")
         _data.setConnectorOperator(connectorid, "lshift")

      return shape

   def __rshift__(self, shape = None):
      # shape >> shape or shape >> connector
      if isinstance(shape, Group) or isinstance(shape, Item):

         connector = Connector(sourceid=self.shapeid, targetid=shape.shapeid, startarrow="", endarrow="arrow", operator="rshift")

      else:  # isinstance(shape, Connector)
         shape.targetid = self.shapeid
         shape.operator = "rshift"

         connectorid = shape.getConnectorID()
         _data.setConnectorSourceID(connectorid, shape.shapeid)
         _data.setConnectorTargetID(connectorid, self.shapeid)
         #_data.setConnectorStartArrow(connectorid, "block")
         _data.setConnectorOperator(connectorid, "rshift")

      return shape

class EndTypes(Enum):
   NONE = "NONE"  # arrow=none
   ARROW = "ARROW"  # arrow=block
   OPENARROW = "OPENARROW" # arrow=open
   CIRCLE = "CIRCLE"  # arrow=oval
   OPENCIRCLE = "OPENCIRCLE"  # arrow=oval with fill=0
   DIAMOND = "DIAMOND"  # arrow=diamond
   OPENDIAMOND = "OPENDIAMOND"  # arrow=diamond with fill=0

class EndMapping(Enum):
   NONE = ""  # arrow=none
   ARROW = "block"  # arrow=block
   OPENARROW = "block" # arrow=block with fill=0
   CIRCLE = "oval"  # arrow=oval
   OPENCIRCLE = "oval"  # arrow=oval with fill=0
   DIAMOND = "diamond"  # arrow=diamond
   OPENDIAMOND = "diamond"  # arrow=diamond with fill=0

class Connector:
   common = None
   shapeid = None
   parentid = None
   #sourceid = None
   #targetid = None
   parent = None
   linetype = "solid"
   linewidth = 1
   linecolor = ""
   startarrow = ""
   endarrow = ""
   startfill = True
   endfill = True
   #operator = ""
   item = None
   connector = None
   fontname = None
   fontsize = 14
   properties = {}

   def __init__(self, 
                label = "", 
                startarrow = "",
                endarrow = "",
                linetype = "solid",
                linewidth = 1,
                linecolor = "#000000",
                operator = "",     # Internal use only.
                sourceid = None,   # Internal use only.
                targetid = None):  # Internal use only.
      self.common = Common()
      self.shapeid = randomid()

      self.linecolor = linecolor

      self.fontname = self.common.getFontName()

      if startarrow != "":
         if not startarrow.upper() in [parm.value for parm in EndTypes]:
            print("Connector.__init__: startarrow not supported: " + startarrow)
            sys_exit()

         if startarrow.upper().startswith("OPEN"):
            self.startfill = 0
         else:
            self.startfill = 1
         
         if startarrow.upper() == "ARROW" or startarrow.upper() == "OPENARROW":
            self.startarrow = "block" 
         elif startarrow.upper() == "CIRCLE" or startarrow.upper() == "OPENCIRCLE":
            self.startarrow = "oval" 
         elif startarrow.upper() == "DIAMOND" or startarrow.upper() == "OPENDIAMOND":
            self.startarrow = "diamond" 
         else:
            self.startarrow = ""

      if endarrow != "":
         if not endarrow.upper() in [parm.value for parm in EndTypes]:
            print("Connector.__init__: endarrow not supported: " + endarrow)
            sys_exit()

         if endarrow.upper().startswith("OPEN"):
            self.endfill = 0
         else:
            self.endfill = 1

         if endarrow.upper() == "ARROW" or endarrow.upper() == "OPENARROW":
            self.endarrow = "block" 
         elif endarrow.upper() == "CIRCLE" or endarrow.upper() == "OPENCIRCLE":
            self.endarrow = "oval" 
         elif endarrow.upper() == "DIAMOND" or endarrow.upper() == "OPENDIAMOND":
            self.endarrow = "diamond" 
         else:
            self.endarrow = ""

      self.properties = _data.getConnectorProperties(label=label, sourceid=sourceid, targetid=targetid, startarrow=self.startarrow, endarrow=self.endarrow, startfill=self.startfill, endfill=self.endfill, linetype=linetype, linewidth=linewidth, linecolor=linecolor, fontname=self.fontname, fontsize=self.fontsize)

      _data.addConnector(self.shapeid, self.properties)
      _data.updateSequence(self.shapeid)

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
         _data.setConnectorOperator(self.shapeid, self.operator)
         if self.operator == "rshift":
            # Double arrow.
            _data.setConnectorStartArrow(self.shapeid, self.startarrow)
            _data.setConnectorEndArrow(self.shapeid, self.endarrow)
            _data.setConnectorStartFill(self.shapeid, self.startfill)
            _data.setConnectorEndFill(self.shapeid, self.endfill)
            _data.setConnectorOperator(self.shapeid, "lshift")
         else:
            # Single arrow.
            _data.setConnectorEndArrow(self.shapeid, "block")
            _data.setConnectorEndFill(self.shapeid, self.endfill)
            _data.setConnectorOperator(self.shapeid, "lshift")
      else:
         print("Connector.__lshift__: connector << shape not supported")
         sys_exit()
      return shape

   def __rshift__(self, shape = None):
      # connector >> shape
      if isinstance(shape, Group) or isinstance(shape, Item):
         _data.setConnectorSourceID(self.shapeid, shape.shapeid)
         _data.setConnectorOperator(self.shapeid, "rshift")
         if self.operator == "lshift":
            # Double arrow.
            _data.setConnectorStartArrow(self.shapeid, "block")

         else:
            # Single arrow.
            sourceid = _data.getConnectorSourceID(self.shapeid)
            targetid = _data.getConnectorTargetID(self.shapeid)
            _data.setConnectorSourceID(self.shapeid, targetid)
            _data.setConnectorTargetID(self.shapeid, sourceid)
            _data.setConnectorStartArrow(self.shapeid, "")
            _data.setConnectorEndArrow(self.shapeid, "block")
            _data.setConnectorEndFill(self.shapeid, self.endfill)

      else:
         print("Connector.__rshift__: connector >> shape not supported")
         sys_exit()
      return shape
