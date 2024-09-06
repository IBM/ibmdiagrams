# @file observability.py
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

class _Observability(_IBMItem):
    def __init__(self, label, sublabel="", icon=""):
        super(_Observability, self).__init__(label=label, sublabel=sublabel, 
                                             linecolor=Colors.lines["management"], 
                                             shape="pnode", icon=icon)

class CloudLogs(_Observability):
    def __init__(self, label, sublabel=""):
        super(CloudLogs, self).__init__(label, sublabel=sublabel, 
                                        icon="Cloud Logs")

class FlowLogs(_Observability):
    def __init__(self, label, sublabel=""):
        super(FlowLogs, self).__init__(label, sublabel=sublabel, 
                                       icon="Flow Logs")

class Monitoring(_Observability):
    def __init__(self, label, sublabel=""):
        super(Monitoring, self).__init__(label, sublabel=sublabel, 
                                         icon="Monitoring")

# Aliases
