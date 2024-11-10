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

from ibmdiagrams import Compose, Common, Load

PROG = "ibmdiagrams"

def main():
   tfname = ''
   jsonname = ''
   yamlname = ''
   inputfile = ''
   outputfolder = ''
   icontype = ''
   direction = ''
   #fontname = ''
   #fontsize = ''

   outputtype = 'drawio'
   common = None

   common = Common() 

   parser = ArgumentParser(prog='ibmdiagrams', 
                           description='Generate architecture diagrams following IBM Diagram Standard.',
                           epilog='https://github.com/IBM/ibmdiagrams')

   parser.add_argument('inputfile', help='required input file name (terraform file)')
   parser.add_argument('-output', dest='outputfolder', default='', help='output folder')
   parser.add_argument('-icontype', dest='icontype', default='static', help='icon type (static only)')
   parser.add_argument('-direction', dest='direction', default='LR', help='layout direction (LR or TB)')
   parser.add_argument('--general', dest='labeltype', action='store_const', const='GENERAL', default='CUSTOM', help='general labels (default: custom labels)')
   #parser.add_argument('-fontname', dest='fontname', default=common.getFontName(), help='font name')
   #parser.add_argument('-fontsize', dest='fontsize', default=common.getFpntSize()', help='font size')
 
   args = parser.parse_args()

   inputfile = args.inputfile
   outputfolder = args.outputfolder
   icontype = args.icontype
   labeltype = args.labeltype
   direction = args.direction
   #fontname = args.fontname
   #fontsize = args.fontsize
   outputtype = 'drawio'

   common.setInputFile(inputfile)
   common.setOutputFolder(outputfolder)

   #if icontype.upper() == "BUILTIN":
   #   common.setBuiltinIcons()
   #elif icontype.upper() == "CATALOG":
   #   common.setCatalogIcons()
   #elif icontype.upper() == "STATIC":
   #   common.setStaticIcons()
   #else:
   #   common.setStaticIcons()

   common.setStaticIcons()

   if labeltype.upper() == "GENERAL":
      common.setGeneralLabels()
   else:
      common.setCustomLabels()

   #common.setFontName(fontname)
   #common.setFontSize(fontsize)

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
   
      outputfile = inputbase + '.' + outputtype
      common.setOutputFile(outputfile)

      common.printStartFile(inputfile, common.getProvider().value.upper())

      data = Load(common)
      if data.loadData():
         compose = Compose(common, data)
         compose.composeDiagrams()
         common.printDone(path.join(outputfolder, outputfile), common.getProvider().value.upper())
      else:
         common.printExit()

   else:
      print()

if __name__ == "__main__":
   main()
