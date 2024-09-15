# @file ai.py
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

class _AI(_IBMCollapsed):
    def __init__(self, label, sublabel="", icon=""):
        super(_AI, self).__init__(label=label, sublabel=sublabel, 
                                  linecolor=Colors.lines["applications"], 
                                  shape="pnode", icon=icon)

class watsonx(_AI):
    def __init__(self, label, sublabel=""):
        super(watsonx, self).__init__(label, sublabel=sublabel, 
                                      icon="watsonx")

class watsonxAI(_AI):
    def __init__(self, label, sublabel=""):
        super(watsonxAI, self).__init__(label, sublabel=sublabel, 
                                        icon="watsonx.ai")

class watsonxData(_AI):
    def __init__(self, label, sublabel=""):
        super(watsonxData, self).__init__(label, sublabel=sublabel, 
                                           icon="watsonx.data")

class watsonxGovernance(_AI):
    def __init__(self, label, sublabel=""):
        super(watsonxGovernance, self).__init__(label, sublabel=sublabel, 
                                                 icon="watsonx.governance")

class watsonxOrchestrate(_AI):
    def __init__(self, label, sublabel=""):
        super(watsonxOrchestrate, self).__init__(label, sublabel=sublabel, 
                                                 icon="watsonx Orchestrate")

class watsonxAssistant(_AI):
    def __init__(self, label, sublabel=""):
        super(watsonxAssistant, self).__init__(label, sublabel=sublabel, 
                                               icon="watsonx Assistant")

class watsonxCodeAssistant(_AI):
    def __init__(self, label, sublabel=""):
        super(watsonxCodeAssistant, self).__init__(label, sublabel=sublabel, 
                                                   icon="watsonx Code Assistant")

class watsonxZCodeAssistant(_AI):
    def __init__(self, label, sublabel=""):
        super(watsonxZCodeAssistant, self).__init__(label, sublabel=sublabel, 
                                                    icon="watsonx Z Code Assistant")

class watsonxZRefactorCodeAssistant(_AI):
    def __init__(self, label, sublabel=""):
        super(watsonxZRefactorCodeAssistant, self).__init__(label, sublabel=sublabel, 
                                                            icon="watsonx Z Refactor Code Assistant")

class WatsonDiscovery(_AI):
    def __init__(self, label, sublabel=""):
        super(WatsonDiscovery, self).__init__(label, sublabel=sublabel, 
                                              icon="Watson Discovery")

class WatsonMachineLearning(_AI):
    def __init__(self, label, sublabel=""):
        super(WatsonMachineLearning, self).__init__(label, sublabel=sublabel, 
                                                    icon="Watson Machine Learning")
class WatsonStudio(_AI):
    def __init__(self, label, sublabel=""):
        super(WatsonStudio, self).__init__(label, sublabel=sublabel, 
                                           icon="Watson Studio")

# Aliases
