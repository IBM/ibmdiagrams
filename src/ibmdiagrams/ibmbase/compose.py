# @file compose.py
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

import pandas as pd
import subprocess
import sys

from os import path, remove
from math import isnan
from uuid import uuid4

from .common import Common
from .build import Build
from .properties import Properties

@staticmethod
def randomid():
   return uuid4().hex

class Compose:
   common = None
   data = None
   icons = None
   top = None
   provider = None
   properties = None
   outputfile = None
   outputfolder = None
   diagramname = None
   savegroups = {}
   indent = -2
   
   def __init__(self, common, data):
      self.common = common
      self.data = data
      self.icons = data.getIcons()
      self.top = None
      self.properties = Properties()
      self.provider = self.common.getProvider().value.upper()
      self.diagramname = path.splitext(path.basename(self.common.getOutputFile()))[0]
      self.outputfile = self.diagramname + ".py"
      self.outputfolder = self.common.getOutputFolder()

   def composeDiagrams(self):
      self.top = self.composeTree()
      filelocation = path.join(self.outputfolder, self.outputfile)
      pythonfile = open(filelocation, "w")
      self.composeIncludes(pythonfile)
      self.composeResources(self.top, True, pythonfile)
      pythonfile.close()
      if self.common.isDrawioCode():
         #exec(open(filelocation).read())
         result = subprocess.run([sys.executable, filelocation], capture_output=True, text=True)
         #print(result.stdout)
         #print(result.stderr)
         remove(filelocation)
      return

   def composeTree(self):
      diagramdata = {"label": [self.diagramname]}
      frame = pd.DataFrame(diagramdata)
      fontname = self.common.getFontName()
      diagram = TreeNode("Diagram Group", randomid(), 'LR', fontname, frame.iloc[0])
      top = self.composeIconTree(diagram)
      return top

   def composeIconTree(self, top):
      iconDictionary = self.icons.getIconDictionary()
      for childName, childIcon in iconDictionary.items():
         if childName.find("Icon") == -1:
            continue

         if not 'data' in childIcon:
            continue

         childData = childIcon['data'] 
        
         if not 'deployedOn' in childIcon:
            continue

         parentGroup = childIcon['deployedOn']

         childDirection = childIcon['direction']

         if parentGroup == 'none':
            continue

         for childKey, childRow in childData.iterrows():
            childID = childRow['id']
            childNode = TreeNode(childName, childID, childDirection, None, childRow)
            parentNode = self.composeGroupTree(childNode, childIcon)
            if parentNode != None:
               top.addNode(parentNode)

      return top

   def composeGroupTree(self, childNode, childIcon):
      if childNode == None:
         return None

      deployedOnNode = None
      childData = childNode.data

      deployedOnGroup = childIcon['deployedOn'] 
      deployedOnID = childData[deployedOnGroup]
      deployedOnIcon = self.icons.getResourceIcon(deployedOnGroup)
      deployedOnData = deployedOnIcon['data']
      deployedOnDirection = deployedOnIcon['direction']
      nextDeployedOnGroup = deployedOnIcon['deployedOn']

      deployedToGroup = childIcon['deployedTo'] 
      if deployedToGroup != "none":
         deployedToID = childData[deployedToGroup]
         deployedToIcon = self.icons.getResourceIcon(deployedToGroup)
         deployedToData = deployedToIcon['data']
         deployedToDirection = deployedToIcon['direction']

      for deployedOnKey, deployedOnRow in deployedOnData.iterrows():
         if deployedOnID == deployedOnRow['id']:
            if deployedToGroup != 'none':
               childNode = self.insertDeployedTo(childNode, deployedToData, deployedToGroup, deployedToID, deployedToDirection)

            if deployedOnID in self.savegroups:
               deployedOnNode = self.savegroups[deployedOnID]
               deployedOnNode.addNode(childNode)
               deployedOnNode = None
            else:
               deployedOnNode = TreeNode(deployedOnGroup, deployedOnID, deployedOnDirection, None, deployedOnRow)
               self.savegroups[deployedOnID] = deployedOnNode
               deployedOnNode.addNode(childNode)
               if nextDeployedOnGroup != "none":
                  deployedOnNode = self.composeGroupTree(deployedOnNode, deployedOnIcon)
            break

      return deployedOnNode

   def insertDeployedTo(self, childNode, deployedToData, deployedToGroup, deployedToID, deployedToDirection):
      deployedToNode = None

      for deployedToKey, deployedToRow in deployedToData.iterrows():
         if deployedToID == deployedToRow['id']:
            if deployedToID in self.savegroups:
               deployedToNode = self.savegroups[deployedToID]
               deployedToNode.addNode(childNode)
            else:
               deployedToNode = TreeNode(deployedToGroup, deployedToID, deployedToDirection, None, deployedToRow)
               self.savegroups[deployedToID] = deployedToNode
               deployedToNode.addNode(childNode)
            break

      return deployedToNode

   def composeIncludes(self, pythonfile):
      print("from ibmdiagrams.ibmcloud.diagram import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.groups import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.actors import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.ai import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.compute import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.containers import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.data import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.devops import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.network import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.observability import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.security import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.storage import *", file=pythonfile)
      print("from ibmdiagrams.ibmcloud.connectors import *", file=pythonfile)
      print(file=pythonfile)

   def composeResources(self, parent, useCustomLabel, pythonfile):
      self.indent += 2
      #print(" " * self.indent + self.top.name)
      #print(" " * self.indent + self.top.id)
      name = parent.name
      id = parent.id
      direction = parent.direction
      fontname = parent.fontname
      data =  parent.data

      if fontname == None:
         fontname = ""
      else:
         fontname = ", font='" + fontname + "'"

      index = name.find("Group")
      if index != -1:
         name = name[0:index-1] 

         if self.common.isCustomLabels() or useCustomLabel:
            label = data["label"]
            if "sublabel" in data:
               sublabel = ", '" + data["sublabel"] + "'"
            else:
               sublabel = ""
         else:
            label = name
            sublabel = ""

         name = name.replace(" ", "") 

         if direction == 'LR':
            direction = ""
         else:
            direction = ", direction='" + direction + "'"

         print(" " * self.indent + "with " + name + "('" + label + "'" + sublabel + direction + fontname + "):", file=pythonfile)

      index = name.find("Icon")
      if index != -1:
         name = name[0:index-1] 

         if self.common.isCustomLabels() or useCustomLabel:
            label = data["label"]
            if "sublabel" in data:
               sublabel = ", '" + data["sublabel"] + "'"
            else:
               sublabel = ""
         else:
            label = name
            sublabel = ""

         name = name.replace(" ", "") 

         print(" " * self.indent + name + "('" + label + "'" + sublabel + fontname + ")", file=pythonfile)

      for child in parent.children:
         self.composeResources(child, False, pythonfile)

      self.indent -= 2

      return

class TreeNode:
   def __init__(self, name, id, direction, fontname, data):
      self.name = name
      self.id = id
      self.direction = direction
      self.fontname = fontname
      self.data = data
      self.children = []

   def addNode(self, child):
      for existing in self.children:
         if existing.id == child.id:
            return
      self.children.append(child)

   def printTree(self):
      print()
      print("TreeNode::name:")
      print(self.name)
      print("TreeNode::id:")
      print(self.id)
      print("TreeNode::direction:")
      print(self.direction)
      print("TreeNode::fontname:")
      print(self.fontname)
      print("TreeNode::data:")
      print(self.data)
      print("TreeNode::children:")
      for child in self.children:
         print(child.name)
         print(child.id)
         child.printTree()
