# @file load.py
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

import pandas as pd

from .common import Common
from .icons import Icons
from .resources import Resources

class Load:
   common = None
   icons = None
   resources = None

   def __init__(self, common):
      self.common = common
      self.icons = Icons(common)
      self.resources = Resources(common)

   def loadData(self):
      if not self.resources.loadResources():
         return False

      if not self.icons.mapResources(self.resources):
         return False

      #if not self.icons.groupResources(self.resources):
      #   return False

      return True

   '''
   def mapData(self):
      for entry in self.icons.iconDictionary:
         icon = self.icons.iconDictionary[entry]
         resource = icon['resource']
         if resource != 'none':
            resource = self.resources.getResource(resource)
            fields = icon['fields']

            lists = []
            for index, row in resource.iterrows():
               list = {}
               for newname, oldname in fields.items():
                  templist = oldname.split()
                  tempdata = row[templist[0]]
                  if len(templist) == 1:
                     element = tempdata
                  else:
                     tempindex = 1
                     while tempindex < len(templist):
                        tempdata = tempdata[0]
                        tempdata = tempdata[templist[tempindex]]
                        tempindex += 1
                  list[newname] = tempdata
               lists.append(list)

            df = pd.DataFrame(lists)
            icon['data'] = df

      return True
   '''

   def getIcons(self):
      return self.icons
