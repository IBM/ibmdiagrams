# @file containers.py
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

class _Containers(_IBMItem):
    def __init__(self, label, sublabel="", icon=""):
        super(_Containers, self).__init__(label=label, sublabel=sublabel, 
                                          linecolor=Colors.lines["compute"], 
                                          shape="pnode", icon=icon)

class OpenShift(_Containers):
    def __init__(self, label, sublabel=""):
        super(OpenShift, self).__init__(label, sublabel=sublabel, 
                                        icon="OpenShift")

class KubernetesService(_Containers):
    def __init__(self, label, sublabel=""):
        super(KubernetesService, self).__init__(label, sublabel=sublabel, 
                                                icon="Kubernetes Service")

class ZContainers(_Containers):
    def __init__(self, label, sublabel=""):
        super(ZContainers, self).__init__(label, sublabel=sublabel, 
                                          icon="Z Containers")

class ContainerRegistry(_Containers):
    def __init__(self, label, sublabel=""):
        super(ContainerRegistry, self).__init__(label, sublabel=sublabel, 
                                                icon="Container Registry")

# Aliases
