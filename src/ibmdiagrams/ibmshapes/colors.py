# @file colors.py
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

class Colors:
   names = {
      "none": "none", "default": "default", 
      "white": "#ffffff", 
      "lightblack": "#f2f4f8", "black": "#000000",
      "lightred": "#fff1f1", "red": "#fa4d56", "darkred": "#a2191f",
      "lightmagenta": "#fff0f7", "magenta": "#ee5396", "darkmagenta": "#9f1853",
      "lightpurple": "#f6f2ff", "purple": "#a56eff", "darkpurple": "#6929c4",
      "lightblue": "#edf5ff", "blue": "#0f62fe", "darkblue": "#002d9c",
      "lightcyan": "#e5f6ff", "cyan": "#1192e8", "darkcyan": "#00539a",
      "lightteal": "#d9fbfb", "teal": "#009d9a", "darkteal": "#005d5d",
      "lightgreen": "#defbe6", "green": "#198038", "darkgreen": "#044317",
      "lightyellow": "#fcf4d6", "yellow": "#b28600", "darkyellow": "#684e00",
      "lightorange": "#fff2e8", "orange": "#eb6200", "darkorange": "#8a3800",
      "lightcoolgray": "#f2f4f8", "coolgray": "#878d96", "darkcoolgray": "#4d5358",
      "lightgray": "#f4f4f4", "gray": "#8d8d8d", "darkgray": "#525252",
      "lightwarmgray": "#f7f3f2", "warmgray": "#8f8b8b", "darkwarmgray": "#565151",
   
      "#ffffff": "white", 
      "#f2f4f8": "lightblack", "#000000": "black",
      "#fff1f1": "lightred", "#fa4d56": "red", "#a2191f": "darkred",
      "#fff0f7": "lightmagenta", "#ee5396": "magenta", "#9f1853": "darkmagenta",
      "#f6f2ff": "lightpurple", "#a56eff": "purple", "#6929c4": "darkpurple",
      "#edf5ff": "lightblue", "#0f62fe": "blue", "#002d9c": "darkblue",
      "#e5f6ff": "lightcyan", "#1192e8": "cyan", "#00539a": "darkcyan",
      "#d9fbfb": "lightteal", "#009d9a": "teal", "#005d5d": "darkteal",
      "#defbe6": "lightgreen", "#198038": "green", "#044317": "darkgreen",
      "#fcf4d6": "lightyellow", "#b28600": "yellow", "#684e00": "darkyellow",
      "#fff2e8": "lightorange", "#eb6200": "orange", "#8a3800": "darkorange",
      "#f2f4f8": "lightcoolgray", "#878d96": "coolgray", "#4d5358": "darkcoolgray",
      "#f4f4f4": "lightgray", "#8d8d8d": "gray", "#525252": "darkgray",
      "#f7f3f2": "lightwarmgray", "#8f8b8b": "warmgray", "#565151": "darkwarmgray"
   }

   lines = {
      # Component line colors (recommended).
      "applications": names["purple"],
      "backend": names["coolgray"],
      "compute": names["green"],
      "data": names["blue"],
      "devops": names["magenta"],
      "industry": names["coolgray"],
      "location": names["coolgray"],
      "management": names["teal"],
      "network": names["cyan"],
      "security": names["red"],
      "services": names["green"],
      "storage": names["blue"],
      "user": names["black"],

      # Medium line colors by name.
      "red": names["red"],
      "magenta": names["magenta"],
      "purple": names["purple"],
      "blue": names["blue"],
      "cyan": names["cyan"],
      "teal": names["teal"],
      "green": names["green"],
      "yellow": names["yellow"],
      "orange": names["orange"],
      "coolgray": names["coolgray"],
      "gray": names["gray"],
      "warmgray": names["warmgray"],
      "black": names["black"],

      # Medium line colors by number.
      "red50": names["red"],
      "magenta50": names["magenta"],
      "purple50": names["purple"],
      "blue60": names["blue"],
      "cyan50": names["cyan"],
      "teal50": names["teal"],
      "green60": names["green"],
      "yellow50": names["yellow"],
      "orange50": names["orange"],
      "coolgray50": names["coolgray"],
      "gray50": names["gray"],
      "warmgray50": names["warmgray"],

      # Medium line colors by hex.
      names["red"]: names["red"],
      names["magenta"]: names["magenta"],
      names["purple"]: names["purple"],
      names["blue"]: names["blue"],
      names["cyan"]: names["cyan"],
      names["teal"]: names["teal"],
      names["green"]: names["green"],
      names["yellow"]: names["yellow"],
      names["orange"]: names["orange"],
      names["coolgray"]: names["coolgray"],
      names["gray"]: names["gray"],
      names["warmgray"]: names["warmgray"],
      names["black"]: names["black"],

      # Dark line colors by name.
      "darkred": names["darkred"],
      "darkmagenta": names["darkmagenta"],
      "darkpurple": names["darkpurple"],
      "darkblue": names["darkblue"],
      "darkcyan": names["darkcyan"],
      "darkteal": names["darkteal"],
      "darkgreen": names["darkgreen"],
      "darkyellow": names["darkyellow"],
      "darkorange": names["darkorange"],
      "darkcoolgray": names["darkcoolgray"],
      "darkgray": names["darkgray"],
      "darkwarmgray": names["darkwarmgray"],

      # Dark line colors by number.
      "red70": names["red"],
      "magenta70": names["magenta"],
      "purple70": names["purple"],
      "blue80": names["blue"],
      "cyan70": names["cyan"],
      "teal70": names["teal"],
      "green80": names["green"],
      "yellow70": names["yellow"],
      "orange70": names["orange"],
      "coolgray70": names["coolgray"],
      "gray70": names["gray"],
      "warmgray70": names["warmgray"],

      # Dark line colors by hex.
      names["darkred"]: names["darkred"],
      names["darkmagenta"]: names["darkmagenta"],
      names["darkpurple"]: names["darkpurple"],
      names["darkblue"]: names["darkblue"],
      names["darkcyan"]: names["darkcyan"],
      names["darkteal"]: names["darkteal"],
      names["darkgreen"]: names["darkgreen"],
      names["darkyellow"]: names["darkyellow"],
      names["darkorange"]: names["darkorange"],
      names["darkcoolgray"]: names["darkcoolgray"],
      names["darkgray"]: names["darkgray"],
      names["darkwarmgray"]: names["darkwarmgray"]
   }

   fills = {
      # Component fill colors (recommended).
      "applications": names["lightpurple"],
      "backend": names["lightcoolgray"],
      "compute": names["lightgreen"],
      "data": names["lightblue"],
      "devops": names["lightmagenta"],
      "industry": names["lightcoolgray"],
      "location": names["lightcoolgray"],
      "management": names["lightteal"],
      "network": names["lightcyan"],
      "security": names["lightred"],
      "services": names["lightgreen"],
      "storage": names["lightblue"],
      "user": names["lightcoolgray"],

      # Light fill colors by name plus white and transparent.
      "lightred": names["lightred"],
      "lightmagenta": names["lightmagenta"],
      "lightpurple": names["lightpurple"],
      "lightblue": names["lightblue"],
      "lightcyan": names["lightcyan"],
      "lightteal": names["lightteal"],
      "lightgreen": names["lightgreen"],
      "lightyellow": names["lightyellow"],
      "lightorange": names["lightorange"],
      "lightcoolgray": names["lightcoolgray"],
      "lightgray": names["lightgray"],
      "lightwarmgray": names["lightwarmgray"],
      "lightblack": names["lightcoolgray"],
      "white" : names["white"],
      "none" : names["none"],

      # Light fill colors by number.
      "red10": names["lightred"],
      "magenta10": names["lightmagenta"],
      "purple10": names["lightpurple"],
      "blue10": names["lightblue"],
      "cyan10": names["lightcyan"],
      "teal10": names["lightteal"],
      "green10": names["lightgreen"],
      "yellow10": names["lightyellow"],
      "orange10": names["lightorange"],
      "coolgray10": names["lightcoolgray"],
      "gray10": names["lightgray"],
      "warmgray10": names["lightwarmgray"],

      # Light fill colors by hex.
      names["lightred"]: names["lightred"],
      names["lightmagenta"]: names["lightmagenta"],
      names["lightpurple"]: names["lightpurple"],
      names["lightblue"]: names["lightblue"],
      names["lightcyan"]: names["lightcyan"],
      names["lightteal"]: names["lightteal"],
      names["lightgreen"]: names["lightgreen"],
      names["lightyellow"]: names["lightyellow"],
      names["lightorange"]: names["lightorange"],
      names["lightcoolgray"]: names["lightcoolgray"],
      names["lightgray"]: names["lightgray"],
      names["lightwarmgray"]: names["lightwarmgray"],
      names["lightblack"]: names["lightcoolgray"],
      names["white"] : names["white"]
   }
