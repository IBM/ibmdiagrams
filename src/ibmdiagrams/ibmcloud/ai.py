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
        super().__init__(
            label=label,
            sublabel=sublabel, 
            linecolor=Colors.lines["applications"], 
            shape="pnode",
            icon=icon,
        )

class watsonx(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel, 
            icon="watsonx Icon",
        )

class watsonxAI(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="watsonx.ai Icon",
        )


class watsonxRuntime(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="watsonx.ai Icon",
        )


class watsonxStudio(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="watsonx.ai Icon",
        )


class watsonxData(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="watsonx.data Icon",
        )


class watsonxGovernance(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="watsonx.governance Icon",
        )


class watsonxOrchestrate(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="watsonx Orchestrate Icon",
        )


class watsonxAssistant(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="watsonx Assistant Icon",
        )


class watsonxCodeAssistant(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="watsonx Code Assistant Icon",
        )


class watsonxZCodeAssistant(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="watsonx Z Code Assistant Icon",
        )


class watsonxZRefactorCodeAssistant(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="watsonx Z Refactor Code Assistant Icon",
        )


class WatsonDiscovery(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="Watson Discovery Icon",
        )


class WatsonMachineLearning(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="Watson Machine Learning Icon",
        )


class WatsonStudio(_AI):
    def __init__(self, label, sublabel=""):
        super().__init__(
            label=label,
            sublabel=sublabel,
            icon="Watson Studio Icon",
        )

# Aliases
