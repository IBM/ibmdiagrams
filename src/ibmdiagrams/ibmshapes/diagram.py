# @file diagram.py
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

from . import _IBMDiagram
from .colors import Colors

class IBMDiagram(_IBMDiagram):
    def __init__(self, name, filename="", output="", direction=""):
        if filename == "":
            filename = name

        super(IBMDiagram, self).__init__(name=name, filename=filename, output=output,
                                         direction=direction)

# Aliases
Diagram = IBMDiagram
