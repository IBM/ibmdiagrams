# @file storage.py
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

class _Storage(_IBMCollapsed):
    def __init__(self, label, sublabel="", icon=""):
        super(_Storage, self).__init__(label=label, sublabel=sublabel, 
                                       linecolor=Colors.lines["storage"], 
                                       shape="pnode", icon=icon)

class BlockStorage(_Storage):
    def __init__(self, label, sublabel=""):
        super(BlockStorage, self).__init__(label, sublabel=sublabel, 
                                           icon="Block Storage Icon")

class BlockStorageSnapshots(_Storage):
    def __init__(self, label, sublabel=""):
        super(BlockStorageSnapshots, self).__init__(label, sublabel=sublabel, 
                                                    icon="Block Storage Snapshotsi Icon")

class FileStorage(_Storage):
    def __init__(self, label, sublabel=""):
        super(FileStorage, self).__init__(label, sublabel=sublabel, 
                                          icon="Undefined Icon")

class ObjectStorage(_Storage):
    def __init__(self, label, sublabel=""):
        super(ObjectStorage, self).__init__(label, sublabel=sublabel, 
                                            icon="Object Storage Icon")

class CloudBackup(_Storage):
    def __init__(self, label, sublabel=""):
        super(CloudBackup, self).__init__(label, sublabel=sublabel, 
                                          icon="Cloud Backup Icon")

# Aliases
