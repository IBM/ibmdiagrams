# @file devops.py
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

class _DevOps(_IBMItem):
    def __init__(self, label, sublabel="", icon=""):
        super(_DevOps, self).__init__(label=label, sublabel=sublabel, 
                                      linecolor=Colors.lines["devops"], 
                                      shape="pnode", icon=icon)

class ContinuousDelivery(_DevOps):
    def __init__(self, label, sublabel=""):
        super(ContinuousDelivery, self).__init__(label, sublabel=sublabel, 
                                                 icon="Continuous Delivery")

class ContinuousIntegration(_DevOps):
    def __init__(self, label, sublabel=""):
        super(ContinuousIntegration, self).__init__(label, sublabel=sublabel, 
                                                    icon="Continuous Integration")

class SourceCodeRepository(_DevOps):
    def __init__(self, label, sublabel=""):
        super(SourceCodeRepository, self).__init__(label, sublabel=sublabel, 
                                                   icon="Source Code Repository")

class Toolchain(_DevOps):
    def __init__(self, label, sublabel=""):
        super(Toolchain, self).__init__(label, sublabel=sublabel, 
                                        icon="Toolchain")

class MQ(_DevOps):
    def __init__(self, label, sublabel=""):
        super(MQ, self).__init__(label, sublabel=sublabel, 
                                 icon="MQ")

class Ansible(_DevOps):
    def __init__(self, label, sublabel=""):
        super(Ansible, self).__init__(label, sublabel=sublabel, 
                                      icon="Ansible")

class GitLab(_DevOps):
    def __init__(self, label, sublabel=""):
        super(GitLab, self).__init__(label, sublabel=sublabel, 
                                     icon="GitLab")

class IntegrationPak(_DevOps):
    def __init__(self, label, sublabel=""):
        super(IntegrationPak, self).__init__(label, sublabel=sublabel, 
                                             icon="Integration Pak")

# Aliases
