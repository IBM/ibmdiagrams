# @file security.py
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

class _Security(_IBMCollapsed):
    def __init__(self, label, sublabel="", icon=""):
        super(_Security, self).__init__(label=label, sublabel=sublabel, 
                                        linecolor=Colors.lines["security"], 
                                        shape="pnode", icon=icon)

class AppID(_Security):
    def __init__(self, label, sublabel=""):
        super(AppID, self).__init__(label, sublabel=sublabel, 
                                    icon="App ID Icon")

class KeyProtect(_Security):
    def __init__(self, label, sublabel=""):
        super(KeyProtect, self).__init__(label, sublabel=sublabel, 
                                         icon="Key Protect Icon")

class SecretsManager(_Security):
    def __init__(self, label, sublabel=""):
        super(SecretsManager, self).__init__(label, sublabel=sublabel, 
                                             icon="Secrets Manager Icon")

class SecurityComplianceCenter(_Security):
    def __init__(self, label, sublabel=""):
        super(SecurityComplianceCenter, self).__init__(label, sublabel=sublabel, 
                                                       icon="Security Compliance Center Icon")

class SSHKey(_Security):
    def __init__(self, label, sublabel=""):
        super(SSHKey, self).__init__(label, sublabel=sublabel, 
                                     icon="SSH Key Icon")

class VPNGateway(_Security):
    def __init__(self, label, sublabel=""):
        super(VPNGateway, self).__init__(label, sublabel=sublabel, 
                                         icon="VPN Gateway Icon")

class VPNConnection(_Security):
    def __init__(self, label, sublabel=""):
        super(VPNConnection, self).__init__(label, sublabel=sublabel, 
                                            icon="VPN Connection Icon")

class BastionHost(_Security):
    def __init__(self, label, sublabel=""):
        super(BastionHost, self).__init__(label, sublabel=sublabel, 
                                          icon="Bastion Host Icon")

class ACLRules(_Security):
    def __init__(self, label, sublabel=""):
        super(ACLRules, self).__init__(label, sublabel=sublabel, 
                                       icon="ACL Rules Icon")

class SecurityPak(_Security):
    def __init__(self, label, sublabel=""):
        super(SecurityPak, self).__init__(label, sublabel=sublabel, 
                                          icon="Security Pak Icon")

# Aliases
SCC = SecurityComplianceCenter
VPN = VPNGateway
