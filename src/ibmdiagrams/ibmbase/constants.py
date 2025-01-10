# @file constants.py
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

from enum import Enum


# Initial Sizes

class ShapeSize(Enum):
   COLLAPSED = {'width': '48', 'height': '48'}
   EXPANDED = {'width': '240', 'height': '48'}
   LOCATION = {'width': '240', 'height': '152'}
   ITEM = {'width': '252', 'height': '16'}

# Format Style

class ShapeFormat(Enum):
   # Collapsed shapes.
   ACTOR = 'shape=mxgraph.ibmshapes.actor;%ICON%STROKE%FILL'
   PNODE = 'shape=mxgraph.ibmshapes.pnode;%ICON%STROKE%FILL'

   # Expanded and grouping shapes.
   EPNODE = 'shape=mxgraph.ibmshapes.epnode;%ICON%STROKE%FILL'
   PLOC = 'shape=mxgraph.ibmshapes.ploc;%ICON%STROKE%FILL'
   GPLOC = 'shape=mxgraph.ibmshapes.gploc;%ICON%STROKE%FILL'
   ZONE = 'shape=mxgraph.ibmshapes.zone;%ICON%STROKE%FILL'
   GZONE = 'shape=mxgraph.ibmshapes.gzone;%ICON%STROKE%FILL'

   # Static expanded and grouping shape.
   GROUP = 'group;%STROKE%FILL'

   # Image shape.
   IMAGE = 'shape=image;'

# Base Style

class BaseStyle(Enum):
   # Font properties.
   FONT = 'fontFamily=%FONT;fontSize=14;fontColor=#000000;html=1;'

   # Container properties.
   CONTAINER = 'container=1;collapsible=0;expand=0;recursiveResize=0;'
   NON_CONTAINER = 'container=0;collapsible=0;expand=0;recursiveResize=0;'

   # Zone border properties.
   ZONE = 'dashed=1;dashPattern=1 2;strokeWidth=2;'

   # Separate no image property to ensure placement at end of style.
   IMAGE = "image=;"

   # Collapsed shapes label properties.
   COLLAPSED_LABEL = 'align=center;verticalAlign=top;verticalLabelPosition=bottom;'

   # Expanded and grouping shapes with one line label.
   EPNODE_LABEL1 = 'align=left;verticalAlign=top;spacingLeft=56;spacingTop=8;'
   PLOC_LABEL1 = 'align=left;verticalAlign=top;spacingLeft=50;spacingTop=8;'
   GPLOC_LABEL1 = 'align=left;verticalAlign=top;spacingLeft=12;spacingTop=8;'
   ZONE_LABEL1 = 'align=left;verticalAlign=top;spacingLeft=50;spacingTop=8;'
   GZONE_LABEL1 = 'align=left;verticalAlign=top;spacingLeft=12;spacingTop=8;'

   # Expanded and grouping shapes with two line label.
   EPNODE_LABEL2 = 'align=left;verticalAlign=top;spacingLeft=56;spacingTop=0;'
   PLOC_LABEL2 = 'align=left;verticalAlign=top;spacingLeft=50;spacingTop=0;'
   GPLOC_LABEL2 = 'align=left;verticalAlign=top;spacingLeft=12;spacingTop=0;'
   ZONE_LABEL2 = 'align=left;verticalAlign=top;spacingLeft=50;spacingTop=0;'
   GZONE_LABEL2 = 'align=left;verticalAlign=top;spacingLeft=12;spacingTop=0;'

   # Expanded and grouping shapes with N line label.
   EPNODE_LABEL3 = 'align=left;verticalAlign=top;spacingLeft=56;spacingTop=-8;'
   PLOC_LABEL3 = 'align=left;verticalAlign=top;spacingLeft=50;spacingTop=-8;'
   GPLOC_LABEL3 = 'align=left;verticalAlign=top;spacingLeft=12;spacingTop=-8;'
   ZONE_LABEL3 = 'align=left;verticalAlign=top;spacingLeft=50;spacingTop=-8;'
   GZONE_LABEL3 = 'align=left;verticalAlign=top;spacingLeft=12;spacingTop=-8;'

# Combined Style

class CombinedStyle(Enum):
   # Collapsed shapes.
   ACTOR =  BaseStyle.FONT.value + BaseStyle.COLLAPSED_LABEL.value + BaseStyle.IMAGE.value
   PNODE = BaseStyle.FONT.value + BaseStyle.COLLAPSED_LABEL.value + BaseStyle.IMAGE.value
   IMAGE = BaseStyle.FONT.value + BaseStyle.COLLAPSED_LABEL.value + BaseStyle.IMAGE.value

   # Expanded and grouping shapes with one line label.
   EPNODE1 = BaseStyle.FONT.value + BaseStyle.EPNODE_LABEL1.value + BaseStyle.CONTAINER.value + BaseStyle.IMAGE.value
   PLOC1 = BaseStyle.FONT.value + BaseStyle.PLOC_LABEL1.value + BaseStyle.CONTAINER.value + BaseStyle.IMAGE.value
   GPLOC1 = BaseStyle.FONT.value + BaseStyle.GPLOC_LABEL1.value + BaseStyle.CONTAINER.value + BaseStyle.IMAGE.value
   ZONE1 = BaseStyle.FONT.value + BaseStyle.ZONE_LABEL1.value + BaseStyle.ZONE.value + BaseStyle.NON_CONTAINER.value + BaseStyle.IMAGE.value
   GZONE1 = BaseStyle.FONT.value + BaseStyle.GZONE_LABEL1.value + BaseStyle.ZONE.value + BaseStyle.NON_CONTAINER.value + BaseStyle.IMAGE.value

   # Expanded and grouping shapes with two line label.
   EPNODE2 = BaseStyle.FONT.value + BaseStyle.EPNODE_LABEL2.value + BaseStyle.CONTAINER.value + BaseStyle.IMAGE.value
   PLOC2 = BaseStyle.FONT.value + BaseStyle.PLOC_LABEL2.value + BaseStyle.CONTAINER.value + BaseStyle.IMAGE.value
   GPLOC2 = BaseStyle.FONT.value + BaseStyle.GPLOC_LABEL2.value + BaseStyle.CONTAINER.value + BaseStyle.IMAGE.value
   ZONE2 = BaseStyle.FONT.value + BaseStyle.ZONE_LABEL2.value + BaseStyle.ZONE.value + BaseStyle.NON_CONTAINER.value + BaseStyle.IMAGE.value
   GZONE2 = BaseStyle.FONT.value + BaseStyle.GZONE_LABEL2.value + BaseStyle.ZONE.value + BaseStyle.NON_CONTAINER.value + BaseStyle.IMAGE.value

   # Expanded and grouping shapes with N line label.
   EPNODE3 = BaseStyle.FONT.value + BaseStyle.EPNODE_LABEL3.value + BaseStyle.CONTAINER.value + BaseStyle.IMAGE.value
   PLOC3 = BaseStyle.FONT.value + BaseStyle.PLOC_LABEL3.value + BaseStyle.CONTAINER.value + BaseStyle.IMAGE.value
   GPLOC3 = BaseStyle.FONT.value + BaseStyle.GPLOC_LABEL3.value + BaseStyle.CONTAINER.value + BaseStyle.IMAGE.value
   ZONE3 = BaseStyle.FONT.value + BaseStyle.ZONE_LABEL3.value + BaseStyle.ZONE.value + BaseStyle.NON_CONTAINER.value + BaseStyle.IMAGE.value
   GZONE3 = BaseStyle.FONT.value + BaseStyle.GZONE_LABEL3.value + BaseStyle.ZONE.value + BaseStyle.NON_CONTAINER.value + BaseStyle.IMAGE.value

   # Test properties.
   TEXT = 'text;html=1;resizable=0;autosize=1;align=left;verticalAlign=middle;points=[];strokeColor=none;rounded=0;'

#  Shape Style

class ShapeStyle(Enum):
   # Collapsed shapes.
   ACTOR = ShapeFormat.ACTOR.value + CombinedStyle.ACTOR.value
   PNODE = ShapeFormat.PNODE.value + CombinedStyle.PNODE.value

   # Expanded and grouping shapes with one line label.
   EPNODE1 = ShapeFormat.EPNODE.value + CombinedStyle.EPNODE1.value
   PLOC1 = ShapeFormat.PLOC.value + CombinedStyle.PLOC1.value  
   GPLOC1 = ShapeFormat.GPLOC.value + CombinedStyle.GPLOC1.value  
   ZONE1 = ShapeFormat.ZONE.value + CombinedStyle.ZONE1.value
   GZONE1 = ShapeFormat.GZONE.value + CombinedStyle.GZONE1.value

   # Expanded and grouping shapes with two line label.
   EPNODE2 = ShapeFormat.EPNODE.value + CombinedStyle.EPNODE2.value
   PLOC2 = ShapeFormat.PLOC.value + CombinedStyle.PLOC2.value  
   GPLOC2 = ShapeFormat.GPLOC.value + CombinedStyle.GPLOC2.value  
   ZONE2 = ShapeFormat.ZONE.value + CombinedStyle.ZONE2.value
   GZONE2 = ShapeFormat.GZONE.value + CombinedStyle.GZONE2.value

   # Expanded and grouping shapes with N line label.
   EPNODE3 = ShapeFormat.EPNODE.value + CombinedStyle.EPNODE3.value
   PLOC3 = ShapeFormat.PLOC.value + CombinedStyle.PLOC3.value  
   GPLOC3 = ShapeFormat.GPLOC.value + CombinedStyle.GPLOC3.value  
   ZONE3 = ShapeFormat.ZONE.value + CombinedStyle.ZONE3.value
   GZONE3 = ShapeFormat.GZONE.value + CombinedStyle.GZONE3.value

   IMAGE = ShapeFormat.IMAGE.value + CombinedStyle.IMAGE.value

# Static Shape Style

class StaticShapeStyle(Enum):
   # Collapsed shapes.
   ACTOR = CombinedStyle.ACTOR.value
   PNODE = CombinedStyle.PNODE.value

   # Expanded and grouping shapes with one line label.
   EPNODE1 = ShapeFormat.GROUP.value + CombinedStyle.EPNODE1.value
   PLOC1 = ShapeFormat.GROUP.value + CombinedStyle.PLOC1.value  
   GPLOC1 = ShapeFormat.GROUP.value + CombinedStyle.GPLOC1.value  
   ZONE1 = ShapeFormat.GROUP.value + CombinedStyle.ZONE1.value
   GZONE1 = ShapeFormat.GROUP.value + CombinedStyle.GZONE1.value

   # Expanded and grouping shapes with two line label.
   EPNODE2 = ShapeFormat.GROUP.value + CombinedStyle.EPNODE2.value
   PLOC2 = ShapeFormat.GROUP.value + CombinedStyle.PLOC2.value  
   GPLOC2 = ShapeFormat.GROUP.value + CombinedStyle.GPLOC2.value  
   ZONE2 = ShapeFormat.GROUP.value + CombinedStyle.ZONE2.value
   GZONE2 = ShapeFormat.GROUP.value + CombinedStyle.GZONE2.value

   # Expanded and grouping shapes with N line label.
   EPNODE3 = ShapeFormat.GROUP.value + CombinedStyle.EPNODE3.value
   PLOC3 = ShapeFormat.GROUP.value + CombinedStyle.PLOC3.value  
   GPLOC3 = ShapeFormat.GROUP.value + CombinedStyle.GPLOC3.value  
   ZONE3 = ShapeFormat.GROUP.value + CombinedStyle.ZONE3.value
   GZONE3 = ShapeFormat.GROUP.value + CombinedStyle.GZONE3.value

   IMAGE = ShapeFormat.IMAGE.value + CombinedStyle.IMAGE.value

# Color Style

class ColorPalette(Enum):
   BLACK = 'strokeColor=#000000;'
   BLUE = 'strokeColor=#0f62fe;'
   CYAN = 'strokeColor=#1192e8;'
   GRAY = 'strokeColor=#878d96;'
   GREEN = 'strokeColor=#198038;'
   MAGENTA = 'strokeColor=#ee5396;'
   PURPLE = 'strokeColor=#a56eff;'
   RED = 'strokeColor=#fa4d56;'
   TEAL = 'strokeColor=#009d9a;'

class FillPalette(Enum):
   BLACK = 'fillColor=#f2f4f8;'
   BLUE = 'fillColor=#edf5ff;'
   CYAN = 'fillColor=#e5f6ff;'
   GRAY = 'fillColor=#f2f4f8;'
   GREEN = 'fillColor=#defbe6;'
   MAGENTA = 'fillColor=#fff0f7;'
   PURPLE = 'fillColor=#f6f2ff;'
   TEAL = 'fillColor=#d9fbfb;'
   RED = 'fillColor=#fff1f1;'
   WHITE = 'fillColor=#ffffff;'
   NONE = 'fillColor=none;'

class ComponentColor(Enum): 
   APPLICATION = ColorPalette.PURPLE.value
   BACKEND = ColorPalette.GRAY.value
   COMPUTE = ColorPalette.GREEN.value
   DATA = ColorPalette.BLUE.value
   DEVOP = ColorPalette.MAGENTA.value
   MANAGEMENT = ColorPalette.TEAL.value
   NETWORK = ColorPalette.CYAN.value
   SECURITY = ColorPalette.RED.value
   STORAGE = ColorPalette.BLUE.value
   USER = ColorPalette.BLACK.value

class ComponentFill(Enum):
   APPLICATION = FillPalette.PURPLE.value
   BACKEND = FillPalette.GRAY.value
   COMPUTE = FillPalette.GREEN.value
   DATA = FillPalette.BLUE.value
   DEVOP = FillPalette.MAGENTA.value
   MANAGEMENT = FillPalette.TEAL.value
   NETWORKL = FillPalette.CYAN.value
   SECURITY = FillPalette.RED.value
   STORAGE = FillPalette.BLUE.value
   USER = FillPalette.BLACK.value

class ShapeKind(Enum):
   ACTOR = 'actor'
   NODE = 'node'
   COMPONENT = 'component'
   LOCATION = 'location'
   ZONE = 'zone'

# Name Constants

class ShapeName(Enum):
   CLOUD = "Cloud"
   IBM_CLOUD = "IBM Cloud"
   INTERNET = 'Internet'
   PUBLIC_NETWORK = 'Public<br>Network'
   PUBLIC_USER = 'User'
   ENTERPRISE_NETWORK = 'Enterprise<br>Network'
   ENTERPRISE_USER = 'Enterprise User'
   NO_PARENT = '1'

# Positioning Constants

class ShapePos(Enum):
   ICON_WIDTH = 48
   ICON_HEIGHT = 48

   GROUP_WIDTH = 240
   GROUP_HEIGHT = 152

   MIN_GROUP_WIDTH = 240
   MIN_GROUP_HEIGHT = 48

   GROUP_SPACE = 30
   TOP_SPACE = 70
   TEXT_GROUP_SPACE = 10
   TEXT_TOP_SPACE = 70
   ICON_SPACE = 48

   LEFT_SPACE = ICON_SPACE * 3

   # Public network icon locations:
   #    First x,y is User icon.
   #    Second x,y is Internet icon.

   # Enterprise network icon locations:
   #    First x,y is User icon.

   # VPC icon locations:
   #    First x,y is Router icon.
   #    Second x,y is ALB icon.
   #    Third x,y is VPN Gateway icon.

   # Zone icon locations:
   #    First x,y is Public Gateway icon.
   #    Second x,y is NLB icon.

   FIRST_ICON_X = ICON_SPACE
   FIRST_ICON_Y = TOP_SPACE

   SECOND_ICON_X = ICON_SPACE
   SECOND_ICON_Y = FIRST_ICON_Y + ICON_HEIGHT + ICON_SPACE

   THIRD_ICON_X = ICON_SPACE
   THIRD_ICON_Y = SECOND_ICON_Y + ICON_HEIGHT + ICON_SPACE

   FOURTH_ICON_X = ICON_SPACE
   FOURTH_ICON_Y = THIRD_ICON_Y + ICON_HEIGHT + ICON_SPACE

   PUBLIC_ICON_COUNT = 2
   PUBLIC_NETWORK_WIDTH = ICON_SPACE * 3
   PUBLIC_NETWORK_HEIGHT = TOP_SPACE + (ICON_SPACE * PUBLIC_ICON_COUNT) + (ICON_HEIGHT * PUBLIC_ICON_COUNT)

   ENTERPRISE_ICON_COUNT = 1
   ENTERPRISE_NETWORK_WIDTH = ICON_SPACE * 3
   ENTERPRISE_NETWORK_HEIGHT = TOP_SPACE + (ICON_SPACE * ENTERPRISE_ICON_COUNT) + (ICON_HEIGHT * ENTERPRISE_ICON_COUNT)

# Zone CIDRs

class ZoneCIDR(Enum):
   AU_SYD_1 = '10.245.0.0/18'
   AU_SYD_2 = '10.245.64.0/18'
   AU_SYD_3 = '10.245.128.0/18'

   BR_SAO_1 = '10.250.0.0/18'
   BR_SAO_2 = '10.250.64.0/18'
   BR_SAO_3 = '10.250.128.0/18'

   CA_TOR_1 = '10.249.0.0/18'
   CA_TOR_2 = '10.249.64.0/18'
   CA_TOR_3 = '10.249.128.0/18'

   EU_DE_1 = '10.243.0.0/18'
   EU_DE_2 = '10.243.64.0/18'
   EU_DE_3 = '10.243.128.0/18'

   EU_GB_1 = '10.242.0.0/18'
   EU_GB_2 = '10.242.64.0/18'
   EU_GB_3 = '10.242.128.0/18'

   JP_OSA_1 = '10.248.0.0/18'
   JP_OSA_2 = '10.248.64.0/18'
   JP_OSA_3 = '10.248.128.0/18'

   JP_TOK_1 = '10.244.0.0/18'
   JP_TOK_2 = '10.244.64.0/18'
   JP_TOK_3 = '10.244.128.0/18'

   US_EAST_1 = '10.241.0.0/18'
   US_EAST_2 = '10.241.64.0/18'
   US_EAST_3 = '10.241.128.0/18'

   US_SOUTH_1 = '10.240.0.0/18'
   US_SOUTH_2 = '10.240.64.0/18'
   US_SOUTH_3 = '10.240.128.0/18'

   NONE = ''
