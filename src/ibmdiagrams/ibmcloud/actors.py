# @file actors.py
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

from . import _IBMItem
from .colors import Colors

class _Actors(_IBMItem):
    def __init__(self, label, sublabel="", linecolor="", icon=""):
        super(_Actors, self).__init__(label=label, sublabel=sublabel, 
                                      linecolor=linecolor, 
                                      shape="actor", icon=icon)

class User(_Actors):
    def __init__(self, label, sublabel=""):
        super(User, self).__init__(label, sublabel=sublabel, 
                                   linecolor=Colors.lines["user"], 
                                   icon="User")

class Users(_Actors):
    def __init__(self, label, sublabel=""):
        super(Users, self).__init__(label, sublabel=sublabel, 
                                    linecolor=Colors.lines["user"], 
                                    icon="Group")

class Enterprise(_Actors):
    def __init__(self, label, sublabel=""):
        super(Enterprise, self).__init__(label, sublabel=sublabel, 
                                         linecolor=Colors.lines["user"], 
                                         icon="Enterprise")

class Application(_Actors):
    def __init__(self, label, sublabel=""):
        super(Application, self).__init__(label, sublabel=sublabel,
                                          linecolor=Colors.lines["applications"], 
                                          icon="Application")

class WebApplication(_Actors):
    def __init__(self, label, sublabel=""):
        super(WebApplication, self).__init__(label, sublabel=sublabel,
                                             linecolor=Colors.lines["applications"], 
                                             icon="Web Application")
class Microservice(_Actors):
    def __init__(self, label, sublabel=""):
        super(Microservice, self).__init__(label, sublabel=sublabel,
                                           linecolor=Colors.lines["applications"], 
                                           icon="Web Application")

# Aliases
App = Application
WebApp = WebApplication
