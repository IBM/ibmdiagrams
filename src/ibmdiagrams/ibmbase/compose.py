# @file compose.py
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

# Hierarchy:
#   ibmdiagrams/__init__.py - defines diagram-as-code for python, invokes build.py
#   ibmdiagrams/ibmbase/compose.py - composes Terraform and JSON use cases, invokes build.py
#   ibmdiagrams/ibmbase/build.py - build diagram objects for all use cases, invokes shapes.py
#   ibmdiagrams/ibmbase/shapes.py - build ibm types, invokes types.py
#   ibmdiagrams/ibmbase/types.py - build drawio types, invokes elements.py
#   ibmdiagrams/ibmbase/elements.py - build drawio objects


from math import isnan
from uuid import uuid4

from .common import Common

from .properties import Properties
from .build import Build
from .constants import ComponentFill, FillPalette, ShapeKind, ShapeName, ShapePos, ZoneCIDR
from .shapes import Shapes
from .icons import Icons

@staticmethod
def randomid():
   return uuid4().hex

class Compose:
   data = None
   properties = None
   diagrams = {}
   groups = {}
   items = {}
   edges = {}
   tgwid = 0

   common = None
   shapes = None
   icons = None
   icontype = None
   cloudname = ""

   def __init__(self, common, data):
      self.common = common
      self.shapes = Shapes(self.common)
      self.icons = Icons(self.icons)
      self.icontype = self.common.getIconType()
      self.data = data
      self.properties = Properties()
      self.cloudname = ShapeName.CLOUD.value if self.common.isProviderAny() else ShapeName.IBM_CLOUD.value

   def composeDiagrams(self):
      validdata = False
      diagrams = {}
      groups = {}
      items = {}
      edges = {}

      regionname = "Region"

      if self.common.isInputTerraform():
         diagramid = randomid()
         self.properties.updateSequence(self.common.compress(diagramid))

         # TBD Review whether public or internet is needed with Terraform.
         publicid = randomid()
         internetid = randomid()
         #self.properties.updateSequence(self.common.compress(publicid))
         #groups, items, edges = self.composePublic(groups, items, edges, publicid, internetid)

         cloudid = randomid()
         self.properties.updateSequence(self.common.compress(cloudid))

         #regionid = randomid()
         #self.properties.updateSequence(self.common.compress(regionid))

         #regionname = "Region"

         addresses = self.data.getAddresses()
         for addressesindex, addressesframe in addresses.iterrows():
            addressesid = addressesframe['id']
            addressesname = addressesframe['name']
            addressescidr = addressesframe['cidr']
            addresseszone = addressesframe['zone']
            regionname = addresseszone[:-2]

         if self.data.hasServices():
            regionid = randomid()
            self.properties.updateSequence(self.common.compress(regionid))

            resourceid = randomid()
            resourcename = "Cloud Services RG"
            # TBD Use user-defined name.
            if self.data.hasTransitGateways():
               transitGateways = self.data.getTransitGateways()
               for transitindex, transitframe in transitGateways.iterrows():
                  transitresourceid = transitframe["resource_group_name"]
                  break

               resourceGroups = self.data.getResourceGroups()
               for rgindex, rgframe in resourceGroups.iterrows():
                  resourcegroupid = rgframe["id"]
                  if transitresourceid == resourcegroupid:
                     resourcename = rgframe["name"]
                     break

            self.properties.updateSequence(self.common.compress(resourceid))
            groups, items, edges = self.composeResourceGroup(regionid, groups, items, edges, resourceid, resourcename)

            servicesid = randomid()
            self.properties.updateSequence(self.common.compress(servicesid))
            groups, items, edges = self.composeServices(groups, items, edges, servicesid, resourceid)

            #properties = self.properties.getGroupProperties(label=vpcname, icon='VPC', direction='LR', parentid=self.common.compress(regionid))
            #groups[self.common.compress(vpcid)] = properties
            iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Region')
            properties = self.properties.getGroupProperties(label=regionname, linecolor=linecolor, fillcolor=fillcolor, icon='Region',direction='TB', parentid=self.common.compress(cloudid))
            groups[self.common.compress(regionid)] = properties

      regionid = randomid()
      self.properties.updateSequence(self.common.compress(regionid))

      vpcs = self.data.getVPCs()
      for vpcindex, vpcframe in vpcs.iterrows():
         #diagrams = {}
         #groups = {}
         #items = {}
         #edges = {}

         vpcid = vpcframe['id']
         vpcname = vpcframe['name']
         vpcresourcename = ""
         vpcresourceid = ""

         if self.common.isInputTerraform():
            vpcresourcename = vpcframe['resource_group_name']
            vpcresourceid = vpcframe['resource_group']

         vpcTable = self.data.getVPCTable() 
         if not vpcid in vpcTable:
            self.common.printInvalidVPC(vpcid)
            continue

         if not self.common.isInputTerraform():
            diagramid = randomid()
            self.properties.updateSequence(self.common.compress(diagramid))

            publicid = randomid()
            internetid = randomid()
            self.properties.updateSequence(self.common.compress(publicid))
            groups, items, edges = self.composePublic(groups, items, edges, publicid, internetid)

            cloudid = "Cloud" + ":" + vpcid
            self.properties.updateSequence(self.common.compress(cloudid))

            regionid = "Region" + ":" + vpcid
            self.properties.updateSequence(self.common.compress(regionid))

            #if self.data.hasServices():
            #   servicesid = randomid()
            #   self.properties.updateSequence(self.common.compress(servicesid))
            #   groups, items, edges = self.composeServices(groups, items, edges, servicesid, regionid, vpcid)

         self.properties.updateSequence(self.common.compress(vpcid))
         groups, items, edges = self.composeLoadBalancers(vpcname, vpcid, groups, items, edges, internetid)

         # TBD
         #if not self.common.isInputTerraform():
         #   groups, items, edges = self.composeNetworkACLs(vpcname, vpcid, groups, items, edges, internetid)

         #routername = vpcname + '-router'
         #self.properties.updateSequence(self.common.compress(routername))

         #internetid = randomid()
         self.properties.updateSequence(self.common.compress(internetid))

         publicedgeid = randomid()
         self.properties.updateSequence(self.common.compress(publicedgeid))

         for regionzonename in vpcTable[vpcid]:
            zoneid = self.common.compress(regionzonename)
            self.properties.updateSequence(zoneid)

            groups, items, edges = self.composeSubnets(regionzonename, vpcname, groups, items, edges, internetid)

            zonename = regionzonename.split(':')[1]

            if 'availabilityZones' in vpcframe:
               usercidrs = vpcframe['availabilityZones']
            else:
               usercidrs = None

            if usercidrs != None:
               for usercidr in usercidrs:
                   if zonename == usercidr['name']:
                      zonecidr = usercidr['addressPrefix']
                      break
                   else:
                      zonecidr = ''
            else:
               zonecidr = self.getZoneCIDR(zonename)

            # Zone properties with parent vpcid
            iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Availability Zone')
            properties = self.properties.getGroupProperties(label=zonename, sublabel=zonecidr, linecolor=linecolor, fillcolor=fillcolor, icon='Availability Zone', shape='Zone', direction='TB', parentid=self.common.compress(vpcid))

            #zoneid = self.common.compress(regionzonename)
            groups[zoneid] = properties

         if self.common.isInputTerraform():
            self.properties.updateSequence(self.common.compress(vpcresourceid))
            groups, items, edges = self.composeResourceGroup(regionid, groups, items, edges, vpcresourceid, vpcresourcename)
            iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('VPC')
            properties = self.properties.getGroupProperties(label=vpcname, linecolor=linecolor, fillcolor=fillcolor, icon='VPC', direction='LR', parentid=self.common.compress(vpcresourceid))
            groups[self.common.compress(vpcid)] = properties

            if self.tgwid != 0:
               properties = self.properties.getSingleArrowProperties(sourceid=self.common.compress(self.tgwid), targetid=self.common.compress(vpcid))
               edgeid = randomid()
               edges[self.common.compress(edgeid)] = properties
               self.properties.updateSequence(self.common.compress(edgeid))
         else:
            # VPC properties with parent region:vpcid
            #regionid = "Region" + ":" + vpcid
            iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('VPC')
            properties = self.properties.getGroupProperties(label=vpcname, linecolor=linecolor, fillcolor=fillcolor, icon='VPC', direction='LR', parentid=self.common.compress(regionid))
            groups[self.common.compress(vpcid)] = properties

         # Region properties with parent cloud:vpcid
         #cloudid = "Cloud" + ":" + vpcid
         iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Region')
         properties = self.properties.getGroupProperties(label=regionname, linecolor=linecolor, fillcolor=fillcolor, icon='Region', direction='TB', parentid=self.common.compress(cloudid))
         groups[self.common.compress(regionid)] = properties

         iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('IBM Cloud')
         properties = self.properties.getGroupProperties(label='IBM Cloud', linecolor=linecolor, fillcolor=fillcolor, icon='IBM Cloud', parentid=None)
         groups[self.common.compress(cloudid)] = properties

         #routername = vpcname + '-router'

         #properties = {"type": "node", "label": routername, "sublabel": '', "shape": '', "linecolor": '', "fillcolor": '', "badgetext": '', "badgeshape": '', "badgelinecolor": '', "badgefillcolor": '', "icon": 'router', "hideicon": '', "direction": '', "many": '', "provider": '', "fontname": '', "fontsize": 0, "parentid": self.common.compress(vpcid)}
         #items[self.common.compress(routername)] = properties

         #groups, items, edges = self.composeLoadBalancers(vpcname, vpcid, groups, items, edges, internetid)

         #groups, items, edges = self.composePublic(groups, items, edges, publicid, internetid)

         #properties = {"type": "edge", "label": '', "sourceid": self.common.compress(publicuserid), "targetid": self.common.compress(internetid), "style": '', "arrow": '', "fontname": '', "fontsize": 0}

         #publicedgeid = randomid()
         #edges[self.common.compress(publicedgeid)] = properties

         if not self.common.isInputTerraform():
            properties = self.properties.getDiagramProperties(name=vpcname, filename='*')
            #diagramid = randomid()
            diagrams[diagramid] = properties

            self.properties.setDiagrams(diagrams)
            self.properties.setGroups(groups)
            self.properties.setItems(items)
            self.properties.setEdges(edges)

            build = Build(self.common, self.properties)
            xmldata = build.buildDiagrams()
            if xmldata == None:
               self.common.printInvalidVPC(vpcid)
            else:
               self.shapes.buildXML(xmldata, vpcname)
               validdata = True

            diagrams = {}
            groups = {}
            items = {}
            edges = {}

      if self.common.isInputTerraform():
         #if self.data.hasServices():
         #   servicesid = randomid()
         #   self.properties.updateSequence(self.common.compress(servicesid))
         #   groups, items, edges = self.composeServices(groups, items, edges, servicesid, cloudid)

         basename = self.common.getOutputBase()
         properties = self.properties.getDiagramProperties(name=basename, filename='*')
         #diagramid = randomid()
         diagrams[diagramid] = properties

         self.properties.setDiagrams(diagrams)
         self.properties.setGroups(groups)
         self.properties.setItems(items)
         self.properties.setEdges(edges)

         build = Build(self.common, self.properties)
         xmldata = build.buildDiagrams()
         if xmldata == None:
            self.common.printInvalidVPC(vpcid)
         else:
            self.shapes.buildXML(xmldata, basename)
            validdata = True

      if validdata:
         self.shapes.dumpXML(self.common.getOutputFile(), self.common.getOutputFolder())
         self.shapes.resetXML()

      return

   def composeServices(self, groups, items, edges, servicesid, parentid):
      iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Cloud Services')
      properties = self.properties.getGroupProperties(label='Cloud Services', linecolor=linecolor, fillcolor=fillcolor, icon='Cloud Services', direction='TB', parentid=self.common.compress(parentid))
      groups[self.common.compress(servicesid)] = properties

      #resourceid = randomid()
      #resourcename = "Resource Group"
      #self.properties.updateSequence(self.common.compress(resourceid))
      #groups, items, edges = self.composeResourceGroup(servicesid, groups, items, edges, resourceid, resourcename)

      if self.data.hasActivityTrackers():
         activitytrackers = self.data.getActivityTrackers()
         activityname = ""
         for activityindex, activityframe in activitytrackers.iterrows():
            activityid = activityframe["id"]
            if activityname == "":
               activityname = activityframe["name"]
            else:
               activityname = activityname + "<br>" +  activityframe["name"]

         #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Cloud Logs')
         #properties = self.properties.getItemProperties(label=activityname, linecolor=linecolor, fillcolor=fillcolor, icon='Cloud Logs', parentid=self.common.compress(servicesid))
         properties = self.properties.getItemProperties(label=activityname, icon='Cloud Logs', parentid=self.common.compress(servicesid))
         trackerid = randomid()
         items[self.common.compress(trackerid)] = properties
         self.properties.updateSequence(self.common.compress(trackerid))

         #properties = self.properties.getItemProperties(label="Cloud Logs", icon='Cloud Logs', parentid=self.common.compress(servicesid))
         #trackerid2 = randomid()
         #items[self.common.compress(trackerid2)] = properties
         #self.properties.updateSequence(self.common.compress(trackerid2))

      if self.data.hasKeyManagement():
         keymgmts = self.data.getKeyManagements()
         keyname = ""
         for keyindex, keyframe in keymgmts.iterrows():
            keyid = keyframe["id"]
            if keyname == "":
               keyname = keyframe["key_name"]
            else:
               keyname = keyname + "<br>" +  keyframe["key_name"]

         #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Key Protect')
         #properties = self.properties.getItemProperties(label=keyname, linecolor=linecolor, fillcolor=fillcolor, icon='Key Protect', parentid=self.common.compress(servicesid))
         properties = self.properties.getItemProperties(label=keyname, icon='Key Protect', parentid=self.common.compress(servicesid))
         keymgmtid = randomid()
         items[self.common.compress(keymgmtid)] = properties
         self.properties.updateSequence(self.common.compress(keymgmtid))

      if self.data.hasObjectBuckets():
         objectBuckets = self.data.getObjectBuckets()
         objectname = ""
         for objectindex, objectframe in objectBuckets.iterrows():
            #objectid = objectframe["id"]
            if objectname == "":
               objectname = objectframe["bucket_name"]
            else:
               objectname = objectname + "<br>" +  objectframe["bucket_name"]

         #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Object Storage')
         #properties = self.properties.getItemProperties(label=objectname, linecolor=linecolor, fillcolor=fillcolor, icon='Object Storage', parentid=self.common.compress(servicesid))
         properties = self.properties.getItemProperties(label=objectname, icon='Object Storage', parentid=self.common.compress(servicesid))
         objectid = randomid()
         items[self.common.compress(objectid)] = properties
         self.properties.updateSequence(self.common.compress(objectid))

      if self.data.hasFlowLogs():
         flowLogs = self.data.getFlowLogs()
         logname = ""
         for logindex, logframe in flowLogs.iterrows():
            if self.common.isInputTerraform():
               logvpcid = logframe["vpc"]
            else: 
               logvpcid = logframe["vpcId"]
            #if vpcid == None or vpcid == logvpcid: 
            #   if self.common.isInputTerraform():
            #       properties = self.properties.getGroupProperties(label='Cloud Services', icon='Cloud Services', direction='TB', parentid=self.common.compress(resourceid))
            #       groups[self.common.compress(resourceid)] = properties

            logid = logframe["id"]

            if logname == "":
               logname = logframe["name"]
            else:
               logname = logname + "<br>" +  logframe["name"]

         #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Flow Logs')
         #properties = self.properties.getItemProperties(label=logname, linecolor=linecolor, fillcolor=fillcolor, icon='Flow Logs', parentid=self.common.compress(servicesid))
         properties = self.properties.getItemProperties(label=logname, icon='Flow Logs', parentid=self.common.compress(servicesid))
         flowlogsid = randomid()
         items[self.common.compress(flowlogsid)] = properties
         self.properties.updateSequence(self.common.compress(flowlogsid))

         #properties = self.properties.getItemnttributes(label='Workload Flow Log Collector', icon='Flow Logs', parentid=self.common.compress(servicesid))
         #flowlogsid2 = randomid()
         #items[self.common.compress(flowlogsid2)] = properties
         #self.properties.updateSequence(self.common.compress(flowlogsid2))

      if self.data.hasTransitGateways():
         transitGateways = self.data.getTransitGateways()
         transitname = ""
         for transitindex, transitframe in transitGateways.iterrows():
            transitid = transitframe["id"]
            if transitname == "":
               transitname = transitframe["name"]
            else:
               transitname = transitname + "<br>" +  transitframe["name"]

         #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Transit Gateway')
         #properties = self.properties.getItemProperties(label=transitname, linecolor=linecolor, fillcolor=fillcolor, icon='Transit Gateway', parentid=self.common.compress(servicesid))
         properties = self.properties.getItemProperties(label=transitname, icon='Transit Gateway', parentid=self.common.compress(servicesid))
         self.tgwid = randomid()
         items[self.common.compress(self.tgwid)] = properties
         self.properties.updateSequence(self.common.compress(self.tgwid))

      return groups, items, edges

   def composeResourceGroup(self, parentid, groups, items, edges, resourceid, resourcename):
      #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Resource Group')
      #properties = self.properties.getGroupProperties(label=resourcename, linecolor=linecolor, fillcolor=fillcolor, icon='Resource Group', shape='ZONE', direction='TB', parentid=self.common.compress(parentid))
      properties = self.properties.getGroupProperties(label=resourcename, icon='Resource Group', shape='ZONE', direction='TB', parentid=self.common.compress(parentid))

      groups[self.common.compress(resourceid)] = properties

      return groups, items, edges

   def composePublic(self, groups, items, edges, publicid, internetid):
      iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Public Network')
      properties = self.properties.getGroupProperties(label='Public Network', linecolor=linecolor, fillcolor=fillcolor, icon='Public Network', direction='TB', parentid=None)

      #publicid = randomid()
      groups[self.common.compress(publicid)] = properties

      # TBD Set shape to Actor otherwise PNODE is used, this didn't use to happen.
      #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('User')
      #properties = self.properties.getItemProperties(label='User', linecolor=linecolor, fillcolor=fillcolor, icon='User', shape='Actor', parentid=self.common.compress(publicid))
      properties = self.properties.getItemProperties(label='User', icon='User', shape='Actor', parentid=self.common.compress(publicid))

      userid = randomid()
      items[self.common.compress(userid)] = properties
      self.properties.updateSequence(self.common.compress(userid))

      #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Internet')
      #properties = self.properties.getItemProperties(label='Internet', linecolor=linecolor, fillcolor=fillcolor,  icon='Internet', parentid=self.common.compress(publicid))
      properties = self.properties.getItemProperties(label='Internet', icon='Internet', parentid=self.common.compress(publicid))

      items[self.common.compress(internetid)] = properties
      self.properties.updateSequence(self.common.compress(internetid))

      properties = self.properties.getDoubleArrowProperties(sourceid=self.common.compress(userid), targetid=self.common.compress(internetid))

      internetedgeid = randomid()
      edges[self.common.compress(internetedgeid)] = properties
      self.properties.updateSequence(self.common.compress(internetedgeid))

      return groups, items, edges

   def composeEnterprise(self, groups, items, edges, enterpriseid):
      iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Enterprise Network')
      properties = self.properties.getGroupProperties(label='Enterprise Network', linecolor=linecolor, fillcolor=fillcolor, icon='Enterprise Network', direction='TB', parentid=None)

      #enterpriseid = randomid()
      groups[enterpriseid] = properties

      #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('User')
      #properties = self.properties.getItemProperties(label='User', linecolor=linecolor, fillcolor=fillcolor,  icon='User', parentid=self.common.compress(enterpriseid))
      properties = self.properties.getItemProperties(label='User', icon='User', parentid=self.common.compress(enterpriseid))
      userid = randomid()
      items[userid] = properties

      return groups, items, edges

   def composeSubnets(self, regionzonename, vpcname, groups, items, edges, internetid): 
      properties = {}

      zoneTable = self.data.getZoneTable()
      save_subnetpubgateid = None

      for insubnetid in zoneTable[regionzonename]:
         pubgateid = None

         subnetframe = self.data.getSubnet(insubnetid)
         subnetname = subnetframe['name']
         subnetid = subnetframe['id']

         subnetzonename = subnetframe['zone.name']
         subnetregion = 'us-south-1'
         subnetvpcid = subnetframe['vpc.id']
         subnetvpcname = subnetframe['vpc.name']
         subnetcidr = subnetframe['ipv4_cidr_block']

         vpcframe = self.data.getVPC(subnetvpcid)
         subnetvpcname = subnetframe['name']

         regionname = regionzonename.split(':')[0]
         #regionzonename = regionname + ':' + subnetzonename;

         '''
         if self.common.isLinks():
            zonelink = self.shapes.buildLink(regionzonename + ':' + subnetname, regionzonename, subnetname, None)
         '''

         if self.common.isInputTerraform():
            subnetpubgateid = subnetframe['public_gateway']
         elif 'public_gateway.id' in subnetframe:
            subnetpubgateid = subnetframe['public_gateway.id']
         else:
            subnetpubgateid = None

         pubgatefipip = None
         pubgatename = None
         if subnetpubgateid != None:
            pubgateframe = self.data.getPublicGateway(subnetpubgateid)
            if len(pubgateframe) > 0:
               if self.common.isInputRIAS():
                  pubgatefipip = pubgateframe['floating_ip.address']
               elif self.common.isInputTerraform(): 
                  pubgatefip = pubgateframe['floating_ip']
                  pubgatefipip = pubgatefip['address']
               else: # yaml
                  pubgatefipip = pubgateframe['floatingIP']
               pubgatename = pubgateframe['name']

         groups, items, edges = self.composeSubnetIcons(subnetid, subnetname, subnetvpcname, vpcname, groups, items, edges, internetid)

         bastion = False
         if subnetname.lower().find("bastion") != -1:
            bastion = True

         iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Subnet')
         properties = self.properties.getGroupProperties(label=subnetname, sublabel=subnetcidr, linecolor=linecolor, fillcolor=fillcolor, icon='Subnet', direction='TB', parentid=self.common.compress(regionzonename))

         #subnetid = self.common.compress(subnetid)
         #self.properties.updateSequence(self.common.compress(subnetid))
         groups[self.common.compress(subnetid)] = properties

         if pubgatefipip != None:

            if save_subnetpubgateid == None:
               save_subnetpubgateid = subnetpubgateid

               #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Public Gateway')
               #properties = self.properties.getItemProperties(label=pubgatename, sublabel=pubgatefipip, linecolor=linecolor, fillcolor=fillcolor, icon='Public Gateway', parentid=self.common.compress(regionzonename))
               properties = self.properties.getItemProperties(label=pubgatename, sublabel=pubgatefipip, icon='Public Gateway', parentid=self.common.compress(regionzonename))
               #pubgateid = randomid()
               items[self.common.compress(subnetpubgateid)] = properties
               self.properties.updateSequence(self.common.compress(subnetpubgateid))

               properties = self.properties.getSingleArrowProperties(sourceid=self.common.compress(subnetid), targetid=self.common.compress(subnetpubgateid))

               edgeid = randomid()
               edges[self.common.compress(edgeid)] = properties
               self.properties.updateSequence(self.common.compress(edgeid))

               #routername = vpcname + '-router'
               properties = self.properties.getSingleArrowProperties(sourceid=self.common.compress(subnetpubgateid), targetid=self.common.compress(internetid))

               edgeid = randomid()
               edges[self.common.compress(edgeid)] = properties
               self.properties.updateSequence(self.common.compress(edgeid))

            elif subnetpubgateid != save_subnetpubgateid:
               self.common.printInvalidPublicGateway(subnetpubgateid)

            else:
               properties = self.properties.getSingleArrowProperties(sourceid=self.common.compress(subnetid), targetid=self.common.compress(subnetpubgateid))

               edgeid = randomid()
               edges[self.common.compress(edgeid)] = properties
               self.properties.updateSequence(self.common.compress(edgeid))

         self.properties.updateSequence(self.common.compress(subnetid))

      return groups, items, edges

   def composeSubnetIcons(self, subnetid, subnetname, subnetvpcname, vpcname, groups, items, edges, internetid):
      properties = {}

      icons = self.data.getSubnetIconTable(subnetid)

      for iconframe in icons:
         iconname = iconframe['name']
         iconid = iconframe['id']
         icontype = iconframe['type']

         if icontype.lower() == 'instance':
            instancename = iconname
            instanceid = iconid
            instanceframe = iconframe
            icontype = "Virtual Server"

            if instancename.lower().find("bastion") != -1:
               icontype = "Bastion Host"

            nics = self.data.getNICTable(subnetid, instanceid)

            nicips = ''
            nicid = ''
            nicfipid = None
            nicfipip = None
            nicfipname = None
            nicfips = ''

            for nicframe in nics:
               if not 'name' in nicframe:
                  # TBD Handle VNIs which don't have a name in nicframe.
                  continue
               nicname = nicframe['name']
               if self.common.isInputTerraform():
                  nicinstanceid = nicframe["id"]
                  nicip = nicframe['primary_ipv4_address']
               else:
                  nicinstanceid = instanceframe['id'] if self.common.isInputRIAS() else nicframe['instanceId']
                  nicip = nicframe['primary_ip']['address'] if self.common.isInputRIAS() else nicframe['ip']
               if nicips == '':
                  nicips = nicip
               else:
                  nicips = nicips + '<br>' + nicip
               nicid = nicframe['id']

               fipframe = self.data.getFloatingIP(nicid)
               if len(fipframe) > 0:
                  nicfipid = fipframe['id']
                  nicfipip = fipframe['address']
                  nicfipname = fipframe['name']
                  if nicfips == '':
                     nicfips = nicfipip
                  else:
                     nicfips = nicfips + '<br>' + nicfipip

            # TBD Test generic name.
            #secondarytext = nicips
            secondarytext = nicips

            meta = {}

            if 'image.name' in instanceframe:
               instanceOS = instanceframe['image.name']
               if instanceOS == None:
                  instanceOS = 'Unknown OS'
               meta = meta | {'Operating-System': instanceOS}

            if 'profile.name' in instanceframe:
               instanceprofile = instanceframe['profile.name'] 
               meta = meta | {'Profile': instanceprofile}

            if 'memory' in instanceframe:
               instancememory = instanceframe['memory']
               meta = meta | {'Memory': str(instancememory)}

            if 'bandwidth' in instanceframe:
               bandwidth = instanceframe['bandwidth']
               if bandwidth == '' or (isinstance(bandwidth, float) and isnan(bandwidth)):
                  instancecpuspeed = 0
               else:
                  instancecpuspeed = int(instanceframe['bandwidth'] / 1000)
               meta = meta | {'CPU-Speed': str(instancecpuspeed)}

            if 'vcpu.count' in instanceframe:
               instancecpucount = instanceframe['vcpu.count']
               meta = meta | {'CPU-Count': str(instancecpucount)}

            if meta:
               meta = meta | {'Boot-Volume': '100GB/3000IOPS'}
            else:
               meta = None

            if nicfipip != None:
               #if self.common.isLinks():
               routername = vpcname + '-router'
               iplabel =  "fip:" + nicfipip
               #fiplink = self.shapes.buildDoubleArrow(iplabel, instanceid, routername, None)
               #links.append(fiplink)

               properties = self.properties.getDoubleArrowProperties(label=iplabel, sourceid=self.common.compress(instanceid), targetid=self.common.compress(internetid))

               fipedgeid = randomid()
               edges[self.common.compress(fipedgeid)] = properties
               self.properties.updateSequence(self.common.compress(fipedgeid))

         elif icontype.lower() == 'vpngateway':
            icontype = "VPN Gateway" 
            secondarytext = ''
            if self.common.isInputTerraform(): 
               # TBD Add both private and both public but need to increase space.
               secondarytext = iconframe['private_ip_address'] +  '<br>' + iconframe['public_ip_address']
               #secondarytext = iconframe['private_ip_address'] +  '<br>' + iconframe[private_ip_address2']
               #secondarytext = iconname + '<br>' + iconframe['private_ip_address'] +  '<br>' + iconframe['private_ip_address2']
             
               # TBD Include both public IP addresses.
            meta = None
         elif icontype.lower() == 'vpegateway':
            icontype = "Endpoint Gateway"
            # Same endpoint gateway is duplicated across different subnets, so ensure a unique iconid.
            iconid = randomid()
            #secondarytext = ''
            # TBD Test generic name.
            #secondarytext = iconframe['address']
            secondarytext = iconframe['address']
            #secondarytext = iconname + "<br>" + iconframe['address']
            #iconname = "Endpoint Gateway"
            meta = None
         else:
            secondarytext = ''
            meta = None

         #properties = self.properties.getGroupProperties(label=iconname, sublabel=secondarytext, shape="EPNODE", icon=icontype, data=meta, parentid=self.common.compress(subnetid))
         #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon(icontype)
         #properties = self.properties.getItemProperties(label=iconname, sublabel=secondarytext, linecolor=linecolor, fillcolor=fillcolor, icon=icontype, data=meta, parentid=self.common.compress(subnetid))
         properties = self.properties.getItemProperties(label=iconname, sublabel=secondarytext, icon=icontype, data=meta, parentid=self.common.compress(subnetid))

         iconid = self.common.compress(iconid)
         items[iconid] = properties
         self.properties.updateSequence(iconid)

      return groups, items, edges

   def composeLoadBalancers(self, vpcname, vpcid, groups, items, edges, internetid):
      lbs = self.data.getLoadBalancers(vpcid)
      if lbs != None:
         for lbpool in lbs:
            #for lbmembers in lbs:
            for lbkey in lbpool:
               #for lbid, members in lbmembers.items():
               for lbid, members in lbpool[lbkey].items():
                  lb = self.data.getLoadBalancer(lbid)
                  lbid = lb['id']
                  lbname = lb['name']

                  #if lbname[0:4] == 'kube':
                  #   # Kube LB not implemented for now.
                  #   # self.common.printInvalidLoadBalancer(lbname)
                  #   continue

                  if self.common.isInputRIAS():
                     lbispublic = lb['is_public']
                     lbprivateips = lb['private_ips']
                     lbpublicips = lb['public_ips']
                  elif self.common.isInputTerraform():
                     lbispublic = lb['type'] == "public"
                     lbprivateips = lb['private_ips']
                     lbpublicips = lb['public_ips']
                  else:  # yaml
                     lbispublic = lb['isPublic']
                     lbprivateips = lb['privateIPs']
                     lbpublicips = lb['publicIPs']

                  lbiplist = ""
                  if lbispublic == False:
                     for lbprivateip in lbprivateips:
                        if self.common.isInputRIAS():
                           ip = lbprivateip['address']
                        else:
                           ip = lbprivateip
                        if lbiplist == "":
                           lbiplist = ip
                        else:
                           lbiplist = lbiplist + "<br>" + ip
                  else:
                     for lbpublicip in lbpublicips:
                        if self.common.isInputRIAS():
                           ip = lbpublicip['address']
                        else:
                           ip = lbpublicip
                        if lbiplist == "":
                           lbiplist = ip
                        else:
                           lbiplist = lbiplist + "<br>" + ip

                  lbgenerated = False

                  for member in members:
                     if self.common.isInputRIAS():
                        # TODO Get instance id.
                        target = member['target']
                        address = target['address']
                     elif self.common.isInputTerraform():
                        instancename = None
                        memberaddress = member['target_address']
                        nicdata = self.data.getNetworkInterface3(memberaddress)
                        instances = self.data.getInstances()
                        if not instances.empty:
                           for instanceindex, instanceframe in instances.iterrows():
                              nics = instanceframe["networkInterfaces"]
                              for nicframe in nics:
                                 nicaddress = nicframe["primary_ipv4_address"]
                                 if memberaddress == nicaddress:
                                    saveinstanceframe = instanceframe
                                    instancename = saveinstanceframe["name"]
                                    break
                              if instancename != None:
                                 break
                        instanceframe = saveinstanceframe
                        instanceid = instanceframe['id']
                        instancevpcid = instanceframe['vpc']

                        if instancevpcid == vpcid:
                           if not lbgenerated:
                              lbgenerated = True
                              # TODO Handle spacing for > 1 LBs.
                              #iconname, linecolor, fillcolor, staticicon, catalogicon = self.icons.getIcon('Load Balancer')
                              #properties = self.properties.getItemProperties(label=lbname, sublabel=lbiplist, linecolor=linecolor, fillcolor=fillcolor, icon='Load Balancer', parentid=self.common.compress(vpcid))
                              properties = self.properties.getItemProperties(label=lbname, sublabel=lbiplist, icon='Load Balancer', parentid=self.common.compress(vpcid))
                              lbid = randomid()
                              #lbid = self.common.compress(lbid)
                              items[self.common.compress(lbid)] = properties
                              self.properties.updateSequence(self.common.compress(lbid))

                              #routername = vpcname + '-router'
                              properties = self.properties.getDoubleArrowProperties(sourceid=self.common.compress(lbid), targetid=self.common.compress(internetid))

                              edgeid = randomid()
                              edges[self.common.compress(edgeid)] = properties
                              self.properties.updateSequence(self.common.compress(edgeid))

                           # label, source, target
                           #instancelink = self.shapes.buildDoubleArrow('', nicid, lbid, None)
                           properties = self.properties.getDoubleArrowProperties(sourceid=self.common.compress(instanceid), targetid=self.common.compress(lbid))

                           edgeid = randomid()
                           edges[self.common.compress(edgeid)] = properties
                           self.properties.updateSequence(self.common.compress(edgeid))
                     else:
                        instanceid = member['instanceId']
                        instance = self.data.getInstance(instanceid)
                        if len(instance) > 0:
                           nics = instance['networkInterfaces']
                           if nics:
                              for nic in nics:
                                 address = nic['ip']
                                 break
                           else:
                              return groups, items, edges
                        else:
                           return groups, items, edges

                     if not self.common.isInputTerraform():
                        nicdata = self.data.getNetworkInterface(address, instanceid)
                        if len(nicdata) != 0:
                           nicid = nicdata['id']
                           nicinstanceid = nicdata['instance.id']
                           instanceframe = self.data.getInstance(nicinstanceid)
                           instancename = instanceframe['name']
                           instancevpcid = instanceframe['vpc.id']

                           if instancevpcid == vpcid:
                              if not lbgenerated:
                                 lbgenerated = True
                                 # TODO Handle spacing for > 1 LBs.
                                 meta = {}
                                 meta = meta | {'Type': "public" if lbispublic else "private"}
                                 meta = meta | {'IPs': lbiplist}
                                 properties = self.properties.getItemProperties(label=lbname, sublabel=lbiplist, icon='Load Balancer', data=meta, parentid=self.common.compress(vpcid))
                                 lbid = randomid()
                                 #lbid = self.common.compress(lbid)
                                 items[self.common.compress(lbid)] = properties
                                 self.properties.updateSequence(self.common.compress(lbid))

                                 #routername = vpcname + '-router'
                                 properties = self.properties.getDoubleArrowProperties(sourceid=self.common.compress(lbid), targetid=self.common.compress(internetid))

                                 edgeid = randomid()
                                 edges[self.common.compress(edgeid)] = properties
                                 self.properties.updateSequence(self.common.compress(edgeid))

                              # label, source, target
                              #instancelink = self.shapes.buildDoubleArrow('', nicid, lbid, None)
                              properties = self.properties.getDoubleArrowProperties(sourceid=self.common.compress(instanceid), targetid=self.common.compress(lbid))

                              edgeid = randomid()
                              edges[self.common.compress(edgeid)] = properties
                              self.properties.updateSequence(self.common.compress(edgeid))

      return groups, items, edges

   def composeNetworkACLs(self, vpcname, vpcid, groups, items, edges, internetid):
      meta = {}
      acls = self.data.getNetworkACLs(vpcid)

      if acls != None:
          for acl in acls:
              aclname = acl['name']
              aclid = acl['id']
              rules = acl['rules']
              count = 0
              for rule in rules:
                 count = count + 1
                 meta = meta | {'Rule' + str(count): rule}
              properties = self.properties.getItemProperties(label=aclname, icon='ACL Rules', data=meta, parentid=self.common.compress(vpcid))

              items[self.common.compress(aclid)] = properties
              self.properties.updateSequence(self.common.compress(aclid))

      return groups, items, edges

   # Get zone CIDR.
   def getZoneCIDR(self, zone):
      match zone:
         case 'au-syd-1': cidr = ZoneCIDR.AU_SYD_1
         case 'au-syd-2': cidr = ZoneCIDR.AU_SYD_2
         case 'au-syd-3': cidr = ZoneCIDR.AU_SYD_3

         case 'br-sao-1': cidr = ZoneCIDR.BR_SAO_1
         case 'br-sao-2': cidr = ZoneCIDR.BR_SAO_2
         case 'br-sao-3': cidr = ZoneCIDR.BR_SAO_3

         case 'ca-tor-1': cidr = ZoneCIDR.CA_TOR_1
         case 'ca-tor-2': cidr = ZoneCIDR.CA_TOR_2
         case 'ca-tor-3': cidr = ZoneCIDR.CA_TOR_3

         case 'eu-de-1': cidr = ZoneCIDR.EU_DE_1
         case 'eu-de-2': cidr = ZoneCIDR.EU_DE_2
         case 'eu-de-3': cidr = ZoneCIDR.EU_DE_3

         case 'eu-gb-1': cidr = ZoneCIDR.EU_GB_1
         case 'eu-gb-2': cidr = ZoneCIDR.EU_GB_2
         case 'eu-gb-3': cidr = ZoneCIDR.EU_GB_3

         case 'jp-osa-1': cidr = ZoneCIDR.JP_OSA_1
         case 'jp-osa-2': cidr = ZoneCIDR.JP_OSA_2
         case 'jp-osa-3': cidr = ZoneCIDR.JP_OSA_3

         case 'jp-tok-1': cidr = ZoneCIDR.JP_TOK_1
         case 'jp-tok-2': cidr = ZoneCIDR.JP_TOK_2
         case 'jp-tok-3': cidr = ZoneCIDR.JP_TOK_3

         case 'us-east-1': cidr = ZoneCIDR.US_EAST_1
         case 'us-east-2': cidr = ZoneCIDR.US_EAST_2
         case 'us-east-3': cidr = ZoneCIDR.US_EAST_3

         case 'us-south-1': cidr = ZoneCIDR.US_SOUTH_1
         case 'us-south-2': cidr = ZoneCIDR.US_SOUTH_2
         case 'us-south-3': cidr = ZoneCIDR.US_SOUTH_3

         case _: cidr = ZoneCIDR.NONE

      return cidr.value
