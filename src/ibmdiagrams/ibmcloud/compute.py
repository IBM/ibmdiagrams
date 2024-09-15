# @file compute.py
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

from . import _IBMCollapsed
from .colors import Colors

class _Compute(_IBMCollapsed):
    def __init__(self, label, sublabel="", icon=""):
        super(_Compute, self).__init__(label=label, sublabel=sublabel, 
                                      linecolor=Colors.lines["compute"], 
                                      shape="pnode", icon=icon)

class VirtualServer(_Compute):
    def __init__(self, label, sublabel=""):
        super(VirtualServer, self).__init__(label, sublabel=sublabel, 
                                            icon="Virtual Server")

class PowerVirtualServer(_Compute):
    def __init__(self, label, sublabel=""):
        super(PowerVirtualServer, self).__init__(label, sublabel=sublabel, 
                                                 icon="Power Virtual Server")
class ClassicVirtualServer(_Compute):
    def __init__(self, label, sublabel=""):
        super(ClassicVirtualServer, self).__init__(label, sublabel=sublabel, 
                                                   icon="Classic Virtual Server")
class BareMetalServer(_Compute):
    def __init__(self, label, sublabel=""):
        super(BareMetalServer, self).__init__(label, sublabel=sublabel, 
                                              icon="Bare Metal Server")
class ClassicBareMetalServer(_Compute):
    def __init__(self, label, sublabel=""):
        super(ClassicBareMetalServer, self).__init__(label, sublabel=sublabel, 
                                                     icon="Classic Bare Metal Server")
class DedicatedHost(_Compute):
    def __init__(self, label, sublabel=""):
        super(DedicatedHost, self).__init__(label, sublabel=sublabel, 
                                            icon="Dedicated Host")

class ImageService(_Compute):
    def __init__(self, label, sublabel=""):
        super(ImageService, self).__init__(label, sublabel=sublabel, 
                                           icon="Image Service")

class Satellite(_Compute):
    def __init__(self, label, sublabel=""):
        super(Satellite, self).__init__(label, sublabel=sublabel, 
                                        icon="Satellite")

# Aliases
