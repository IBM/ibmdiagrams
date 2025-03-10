# @file ibmdiagrams.py
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

from argparse import ArgumentParser
from configparser import ConfigParser
from os import path
from sys import exit as sys_exit

#from ibmdiagrams import Common, Compose, Load, ComposeJSON, LoadJSON
from ibmdiagrams import Common, Compose, Load

PROG = "ibmdiagrams"

def main():
   tfname = ''
   jsonname = ''
   yamlname = ''
   inputfile = ''
   outputfolder = ''
   labeltype = ''
   codetype = ''
   #direction = ''
   fontname = ''
   #fontsize = ''

   outputtype = 'drawio'
   common = None

   common = Common() 

   parser = ArgumentParser(prog='ibmdiagrams', 
                           description='Generate architecture diagrams following IBM Diagram Standard.',
                           epilog='https://github.com/IBM/ibmdiagrams')

   parser.add_argument('inputfile', help='required input file name (terraform file)')
   parser.add_argument('-output', dest='outputfolder', default='', help='output folder')
   #parser.add_argument('-direction', dest='direction', default='LR', help='layout direction (LR or TB)')
   parser.add_argument('--general', dest='labeltype', action='store_const', const='GENERAL', default='CUSTOM', help='general labels (default: custom labels)')
   parser.add_argument('--python', dest='codetype', action='store_const', const='PYTHON', default='DRAWIO', help='code type (default: drawio)')
   parser.add_argument('-font', dest='fontname', default='IBM Plex Sans', help='font name')
 
   args = parser.parse_args()

   inputfile = args.inputfile
   outputfolder = args.outputfolder
   labeltype = args.labeltype
   codetype = args.codetype
   fontname = args.fontname
   #fontsize = args.fontsize
   outputtype = 'drawio'

   common.setInputFile(inputfile)
   common.setOutputFolder(outputfolder)
   common.setFontName(fontname)

   if labeltype.upper() == "GENERAL":
      common.setGeneralLabels()
   else:
      common.setCustomLabels()

   if codetype.upper() == "PYTHON":
      common.setPythonCode()
   else:
      common.setDrawioCode()

   if inputfile != "chat":
      basename = path.basename(inputfile)
      inputbase = path.splitext(basename)[0]
      inputtype = path.splitext(basename)[1][1:]
      
      if inputtype == 'json':
         common.setInputJSON()
      elif inputtype == 'tfstate':
         common.setInputTerraform()
      else:
         common.printInvalidFile(inputfile)
         return
   
      if not path.isfile(common.getInputFile()):
         common.printInvalidFile(inputfile)
         return

      outputfile = inputbase + '.' + outputtype
      common.setOutputFile(outputfile)

      common.printStartFile(inputfile, common.getProvider().value.upper())
      data = Load(common)
      if data.loadData():
         compose = Compose(common, data)
         compose.composeDiagrams()
         if common.isDrawioCode():
            common.printDone(path.join(outputfolder, outputfile), common.getProvider().value.upper())
         elif common.isPythonCode():
            splitfile = path.splitext(outputfile)
            common.printDone(path.join(outputfolder, splitfile[0] + ".py"), common.getProvider().value.upper())
      else:
         common.printExit()
   else:
      print()

if __name__ == "__main__":
   main()
