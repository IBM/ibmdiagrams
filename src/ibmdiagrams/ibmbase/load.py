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
      if self.common.isInputTerraform():
         if not self.resources.loadResources():
            return False
      elif self.common.isInputJSON():
         if not self.resources.loadJSON():
            return False
      else:
         return False

      if not self.icons.mapResources(self.resources):
         return False

      return True

   def getIcons(self):
      return self.icons
