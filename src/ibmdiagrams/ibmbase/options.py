# @file options.py
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
from os import path

class Providers(Enum):
   ANY = 'any'
   IBM = 'ibm'

class RunMode(Enum):
   BATCH = 'batch'
   GUI = 'gui'
   WEB = 'web'

class InputTypes(Enum):
   PYTHON = 'python'
   RIAS = 'rias'
   JSON = 'json'
   YAML = 'yaml'
   Terraform = 'terraform'

class LabelTypes(Enum):
   CUSTOM = 'CUSTOM'
   GENERAL = 'GENERAL'

class CodeTypes(Enum):
   DRAWIO = 'DRAWIO'
   PYTHON = 'PYTHON'

class Directions(Enum):
   LR = 'LR'
   TB = 'TB'

class FontNames(Enum):
   IBM_PLEX_SANS = 'IBM Plex Sans'
   IBM_PLEX_SANS_ARABIC = 'IBM Plex Sans Arabic'
   IBM_PLEX_SANS_DEVANAGARI = 'IBM Plex Sans Devanagari'
   IBM_PLEX_SANS_HEBREW = 'IBM Plex Sans Hebrew'
   IBM_PLEX_SANS_JP = 'IBM Plex Sans JP'
   IBM_PLEX_SANS_KR = 'IBM Plex Sans KR'
   IBM_PLEX_SANS_THAI = 'IBM Plex Sans Thai'

class Alternates(Enum):
   WHITE = 'WHITE'
   LIGHT = 'LIGHT'
   NONE = 'NONE'
   USER = 'USER'

class Regions(Enum):
   ALL = 'all'
   GERMANY = 'eu-de'
   OSAKA = 'jp-osa'
   SAOPAULO = 'br-sao'
   SYDNEY = 'au-syd'
   TOKYO = 'jp-tok'
   TORONTO = 'ca-tor'
   UNITEDKINGDOM = 'eu-gb'
   USEAST = 'us-east'
   USSOUTH = 'us-south'

class Options:
   runMode = None
   inputType = None
   accountID = ''
   apiKey = ''
   region = None
   inputFile = ''
   inputFolder = ''
   outputFile = ''
   outputFolder = ''
   iconType = ''
   labelType = ''
   codeType = ''
   fontname = ''
   quietmode = ''
   icons = None
   direction = ''
   alternate = None
   provider = None
   allicons = False

   def __init__(self):
      self.runMode = RunMode.BATCH
      self.inputType = InputTypes.JSON
      self.region = Regions.ALL
      self.alternate = Alternates.WHITE
      self.provider = Providers.IBM
      self.labelType = LabelTypes.CUSTOM
      self.codeType = CodeTypes.DRAWIO
      self.direction = Directions.LR
      self.fontname = FontNames.IBM_PLEX_SANS
      #self.inputFile = 'input.json'
      #self.inputFolder = path.join(path.expanduser('~'), 'Documents', toolName)
      #self.outputFile = 'diagram.xml'
      #self.outputFolder = path.join(path.expanduser('~'), 'Documents', toolName)
      return

   def getAccountID(self):
      return self.accountID

   def setAccountID(self, value):
      self.accountID = value

   def getAPIKey(self):
      return self.apiKey

   def setAPIKey(self, value):
      self.apiKey = value

   def getInputFile(self):
      return self.inputFile

   def setInputFile(self, value):
      self.inputFile = value

   def getInputFolder(self):
      return self.outputFile

   def setInputFolder(self, value):
      self.inputFolder = value

   def getOutputFile(self):
      return self.outputFile

   def setOutputFile(self, value):
      self.outputFile = value

   def getOutputFolder(self):
      return self.outputFolder

   def setOutputFolder(self, value):
      self.outputFolder = value

   def getOutputBase(self):
      return path.splitext(self.outputFile)[0]

   def getOutputIcons(self):
      return self.options.getOutputIcons()

   def setOutputIcons(self, value):
      return self.options.setOutputIcons(value)

   def getProvider(self):
      return self.options.getProvider()

   def setProvider(self, value):
      self.provider = value

   def setProviderAny(self):
      self.provider = Provider.ANY

   def setProviderIBM(self):
      self.provider = Provider.IBM

   def isProviderAny(self):
      return self.provider == Provider.Any

   def isProviderIBM(self):
      return self.provider == Provider.IBM

   def isBatchMode(self):
      return self.runMode == RunMode.BATCH

   def isGUIMode(self):
      return self.runMode == RunMode.GUI

   def isWebMode(self):
      return self.runMode == RunMode.WEB

   def isBatchMode(self, value):
      return value == RunMode.BATCH.value

   def isGUIMode(self, value):
      return value == RunMode.GUI.value

   def isWebMode(self, value):
      return value == RunMode.WEB.value

   def getRunMode(self):
      return self.runMode

   def setRunMode(self, value):
      self.runMode = value

   def isInputPython(self):
      return self.inputType == InputTypes.PYTHON

   def isInputRIAS(self):
      return self.inputType == InputTypes.RIAS

   def isInputJSON(self):
      return self.inputType == InputTypes.JSON

   def isInputYAML(self):
      return self.inputType == InputTypes.YAML

   def isInputTerraform(self):
      return self.inputType == InputTypes.Terraform

   def setInputPython(self):
      self.inputType = InputTypes.PYTHON

   def setInputRIAS(self):
      self.inputType = InputTypes.RIAS

   def setInputJSON(self):
      self.inputType = InputTypes.JSON

   def setInputYAML(self):
      self.inputType = InputTypes.YAML

   def setInputTerraform(self):
      self.inputType = InputTypes.Terraform

   #def getInputType(self):
   #   return self.inputType

   def getIconType(self):
      return self.iconType

   def setIconType(self, value):
       self.iconType = value

   def isCustomLabels(self):
      return self.labelType == LabelTypes.CUSTOM

   def isGeneralLabels(self):
      return self.labelType == LabelTypes.GENERAL

   def setCustomLabels(self):
      self.labelType = LabelTypes.CUSTOM

   def setGeneralLabels(self):
      self.labelType = LabelTypes.GENERAL

   def isDrawioCode(self):
      return self.codeType == CodeTypes.DRAWIO

   def isPythonCode(self):
      return self.codeType == CodeTypes.PYTHON

   def setPythonCode(self):
      self.codeType = CodeTypes.PYTHON

   def setDrawioCode(self):
      self.codeType = CodeTypes.DRAWIO

   def getFontName(self):
      return self.fontname.value

   def setFontName(self, fontname):
      fontname = fontname.upper()
      if fontname == 'IBM PLEX SANS':
         self.fontname = FontNames.IBM_PLEX_SANS
      elif fontname == 'IBM PLEX SANS ARABIC':
         self.fontname = FontNames.IBM_PLEX_SANS_ARABIC
      elif fontname == 'IBM PLEX SANS DEVANAGARI':
         self.fontname = FontNames.IBM_PLEX_SANS_DEVANAGARI
      elif fontname == 'IBM PLEX SANS HEBREW':
         self.fontname = FontNames.IBM_PLEX_SANS_HEBREW
      elif fontname == 'IBM PLEX SANS JP':
         self.fontname = FontNames.IBM_PLEX_SANS_JP
      elif fontname == 'IBM PLEX SANS KR':
         self.fontname = FontNames.IBM_PLEX_SANS_KR
      elif fontname == 'IBM PLEX SANS THAI':
         self.fontname = FontNames.IBM_PLEX_SANS_THAI
      else:
         self.fontname = FontNames.IBM_PLEX_SANS

   def getIcons(self):
      return self.icons

   def setAllIcons(self):
      self.allicons = True

   def isAllIcons(self):
      return self.allicons == True

   def getDirection(self):
      return self.direction

   def setDirectionLR(self):
      self.direction = Directions.LR 

   def setDirectionTB(self):
      self.direction = Directions.TB 

   def isDirectionLR(self):
      return self.direction == Directions.LR 

   def isDirectionTB(self):
      return self.direction == Directions.TB 

   def setAlternateWhite(self):
      self.alternate = Alternates.WHITE

   def setAlternateLight(self):
      self.alternate = Alternates.LIGHT

   def setAlternateNone(self):
      self.alternate = Alternates.NONE

   def setAlternateUser(self):
      self.alternate = Alternates.USER

   def isAlternateWhite(self):
      return self.alternate == Alternates.WHITE

   def isAlternateLight(self):
      return self.alternate == Alternates.LIGHT

   def setDirection(self, value):
      self.direction = value

   def setDirectionLR(self):
      self.direction = Directions.LR 

   def setDirectionTB(self):
      self.direction = Directions.TB 

   def isDirectionLR(self):
      return self.direction == Directions.LR 

   def isDirectionTB(self):
      return self.direction == Directions.TB 

   def setAlternateWhite(self):
      self.alternate = Alternates.WHITE

   def setAlternateLight(self):
      self.alternate = Alternates.LIGHT

   def setAlternateNone(self):
      self.alternate = Alternates.NONE

   def setAlternateUser(self):
      self.alternate = Alternates.USER

   def isAlternateWhite(self):
      return self.alternate == Alternates.WHITE

   def isAlternateLight(self):
      return self.alternate == Alternates.LIGHT

   def isAlternateNone(self):
      return self.alternate == Alternates.NONE

   def isAlternateUser(self):
      return self.alternate == Alternates.USER

   def getProvider(self):
      return self.provider 

   def setProviderAny(self):
      self.provider = Providers.ANY 

   def setProviderIBM(self):
      self.provider = Providers.IBM 

   def isProviderAny(self):
      return self.provider == Providers.ANY 

   def isProviderIBM(self):
      return self.provider == Providers.IBM 

   def setAllRegion(self):
      self.region = Regions.ALL

   def setGermanyRegion(self):
      self.region = Regions.GERMANY

   def setOsakaRegion(self):
      self.region = Regions.OSAKA

   def setSaoPauloRegion(self):
      self.region = Regions.SAOPAULO

   def setSydneyRegion(self):
      self.region = Regions.SYDNEY

   def setTokyoRegion(self):
      self.region = Regions.TOKYO

   def setTorontoRegion(self):
      self.region = Regions.TORONTO

   def setUnitedKingdomRegion(self):
      self.region = Regions.UNITEDKINGDOM

   def setUSEastRegion(self):
      self.region = Regions.USEAST

   def setUSSouthRegion(self):
      self.region = Regions.USSOUTH

   def getRegion(self):
      return self.region

   def setRegion(self, value):
      self.region = value
