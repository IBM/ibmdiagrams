# @file load.py
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

import ipaddress
from math import isnan
from pandas import concat, DataFrame

from .common import Common
from .opsjson import OpsJson
from .terraform import Terraform
from .rias import RIAS

class Load:
   #instanceTable = {}   # Table of instances ordered by subnet that shows instances within each subnet.
   nicTable = {}         # Table of nics ordered by subnet+instance that shows nics for same instance in different subnets.
   subnetIconTable = {}  # Table of subnet icons ordered by subnet that shows subnet icons within each subnet.
   serviceIconTable = {} # Table of service icons ordered by region that shows service icons within each region.
   regionTable = {}      # Table of vpcs ordered by region that shows vpcs within each region.
   vpcTable = {}         # Table of zones ordered by vpc that shows zones with each vpc.
   zoneTable = {}        # Table of subnets ordered by vpc+zone that shows subnets within each zone.
   lbTable = {}          # Table of load balancerbs ordered by vpc+lb that shows load balancers within each vpc.
   aclTable = {}         # Table of network ACLs ordered by vpc that shows network ACLs within each vpc.

   data = None
   common = None

   def __init__(self, common):
      self.common = common
      if common.isInputRIAS():
         self.data = RIAS(common)
      elif common.isInputJSON():
         self.data = OpsJson(common)
      elif common.isInputYAML():
         self.data = OpsJson(common)
      elif common.isInputTerraform():
         self.data = Terraform(common)
      return

   def loadData(self):
      normalizeddata = None
      if self.common.isInputRIAS():
         self.data.loadRIAS()
      elif self.common.isInputJSON():
         self.data.loadJSON()
      elif self.common.isInputYAML():
         self.data.loadYAML()
      elif self.common.isInputTerraform():
         self.data.loadTerraform()

      #if not self.common.isInputTerraform():
      if self.analyzeData():
         self.analyzeContainers()
         #self.analyzeInstances()
         if not self.common.isInputRIAS():
            # TODO: Fix Subnet Icons for RIAS.
            self.analyzeSubnetIcons()
         #self.analyzeServiceIcons()
         if self.common.isInputTerraform():
            self.analyzeTerraformLoadBalancers()
            #self.analyzeiTerraformNetworkACLs()
            return True
         else:
            self.analyzeLoadBalancers()
            self.analyzeNetworkACLs()
         return True

      return False

   def analyzeData(self):
      # If no VPCs then print error and exit.
      vpcs = self.data.getVPCs()
      if vpcs.empty:
         self.common.printMissingVPCs() 
         return False

      for vpcindex, vpcframe in vpcs.iterrows():
         vpcname = vpcframe['name']
         if vpcname == '':
            vpcname = None

         vpcid = vpcframe['id']
         if vpcid == '':
            vpcid = None

         # If invalid vpc name/id then print error and drop vpc.
         if vpcname == None or vpcid == None:
            # Skip references to dangling vpc references from deleting a VPC.
            #self.common.printInvalidVPC("(unknown)")
            vpcs.drop(index=vpcindex, inplace=True)
            continue

      self.data.setVPCs(vpcs)

      # Recheck if no vpcs then print error and exit.
      if vpcs.empty:
         self.common.printMissingVPCs() 
         return False

      # If no subnets then print error and exit.
      subnets = self.data.getSubnets()
      if subnets.empty:
         self.common.printMissingSubnets() 
         return False

      for subnetindex, subnetframe in subnets.iterrows():
         subnetname = subnetframe['name']
         if subnetname == '':
            subnetname = None

         subnetid = subnetframe['id']
         if subnetid == '':
            subnetid = None

         # If invalid subnet name/id then print error and drop subnet.
         if subnetname == None or subnetid == None:
            self.common.printInvalidSubnet("(unknown)")
            subnets.drop(index=subnetindex, inplace=True)
            continue

         #self.instanceTable[subnetid] = []
         self.subnetIconTable[subnetid] = []

         # If invalid zone then print error and drop subnet.
         # TODO Add check for valid zone.
         subnetzonename = subnetframe['zone.name']
         if subnetzonename == '':
            subnetzonename = None

         if subnetzonename == None:
            self.common.printMissingZone(subnetname)
            subnets.drop(index=subnetindex, inplace=True)
            continue

         subnetvpcid = subnetframe['vpc.id']
         #subnetvpcname = subnetframe['vpc.name']

         # If invalid vpc then print error and drop subnet.
         vpcframe = self.findRow(vpcs, 'id', subnetvpcid)
         if len(vpcframe) == 0:
            # Skip references to dangling vpc references from deleting a VPC.
            #self.common.printInvalidVPC(subnetvpcid)
            subnets.drop(index=subnetindex, inplace=True)
            continue

      self.data.setSubnets(subnets)

      # Recheck if no subnets then print error and exit.
      if subnets.empty:
         self.common.printMissingSubnets() 
         return False

      return True

   def analyzeContainers(self):
      subnets = self.data.getSubnets()

      # Add subnets to zoneTable, zones to vpcTable, and vpcs to regionTable.
      for subnetindex, subnetframe in subnets.iterrows():
         subnetname = subnetframe['name']
         subnetid = subnetframe['id']

         subnetzonename = subnetframe['zone.name']
         if subnetzonename == None:
            self.common.printMissingZone(subnetname)
            continue

         if self.common.isInputRIAS():
            lastindex = subnetzonename.rfind('-')
            subnetregion = subnetzonename[0:lastindex]
         else:
            subnetregion = subnetframe['region']
         subnetvpcid = subnetframe['vpc.id']
         #subnetvpcname = subnetframe['vpc.name']

         # Add subnets to zoneTable ordered by vpcid+zonename.
         zonekey = subnetvpcid + ':' + subnetzonename
         if zonekey in self.zoneTable:
            if subnetid not in self.zoneTable[zonekey]:
               self.zoneTable[zonekey].append(subnetid)
         else:
            self.zoneTable[zonekey] = [subnetid]

         # Add zones to vpcTable ordered by vpcid.
         #zonekey = subnetvpcid +  subnetzonename
         if subnetvpcid in self.vpcTable:
            if zonekey not in self.vpcTable[subnetvpcid]:
               self.vpcTable[subnetvpcid].append(zonekey)
         else:
            self.vpcTable[subnetvpcid] = [zonekey]

         # Add vpcs to regionTable ordered by region.
         if subnetregion in self.regionTable:
            if subnetvpcid not in self.regionTable[subnetregion]:
               self.regionTable[subnetregion].append(subnetvpcid)
         else:
            self.regionTable[subnetregion] = [subnetvpcid]

      services = self.data.getServices()

      # Add services to regionTable ordered by region.
      #for serviceindex, serviceframe in services.iterrows():
      #   servicename = serviceframe['name']
      #   serviceid = serviceframe['id']
      #   serviceregion = serviceframe['region']

      #   if serviceregion in self.regionTable:
      #      if serviceid not in self.regionTable[serviceregion]:
      #         self.regionTable[serviceregion].append(serviceid)
      #   else:
      #      self.regionTable[serviceregion] = [serviceid]

      return

   def analyzeInstances(self):
      #subnets = self.data.getSubnets()

      # Create empty instanceTable.
      #if not subnets.empty:
      #   for subnetindex, subnetframe in subnets.iterrows():
      #      subnetid = subnetframe['id']
      #      self.instanceTable[subnetid] = []

      # Add instances to instanceTable ordered by subnetid, nics to nicTable ordered by subnetid+instanceid.
      instances = self.data.getInstances()
      if not instances.empty:
         for instanceindex, instanceframe in instances.iterrows():
            instanceid = instanceframe['id']
            #instancename = instanceframe['name']
            #vpcname = instanceframe['vpc.name'] if self.common.isInputRIAS() else instanceframe['vpcName']
            #vpcid = instanceframe['vpc.id'] if self.common.isInputRIAS() else instanceframe['vpcId']
            #zonename = instanceframe['zone.name'] if self.common.isInputRIAS() else instanceframe['availabilityZone']
            #regionname = zonename[:len(zonename) - 2] if self.common.isInputRIAS() else instanceframe['availabilityZone']

            addedInstance = False
            nics = instanceframe['network_interfaces'] if self.common.isInputRIAS() else instanceframe['networkInterfaces']
            if nics:
               for nicframe in nics:
                  #nicname = nicframe['name']
                  #nicid = nicframe['id']
                  if self.common.isInputTerraform():
                     nicsubnetid = nicframe['subnet']
                  else:
                     nicsubnetid = nicframe['subnet']['id'] if self.common.isInputRIAS() else nicframe['networkId']

                  if nicsubnetid in self.subnetIconTable:
                     if addedInstance == False:
                        self.subnetIconTable[nicsubnetid].append(instanceframe)
                        addedInstance = True
                  else:
                     self.common.printInvalidSubnet(nicsubnetid)
                     continue

                  dualid = nicsubnetid + ':' + instanceid
                  if dualid in self.nicTable:
                     self.nicTable[dualid].append(nicframe)
                  else:
                     self.nicTable[dualid] = [nicframe]

      return

   def analyzeSubnetIcons(self):
      subnets = self.data.getSubnets()

      # Create empty subnetIconTable.
      if not subnets.empty:
         for subnetindex, subnetframe in subnets.iterrows():
            subnetid = subnetframe['id']
            self.subnetIconTable[subnetid] = []

      # Add vpns to subnetIconTable ordered by subnetid.
      vpns = self.data.getVPNGateways()
      if not vpns.empty:
         for vpnindex, vpnframe in vpns.iterrows():
            vpnid = vpnframe['id']
            if self.common.isInputTerraform():
               vpnsubnetid = vpnframe['subnet']
            else:
               vpnsubnetid = vpnframe['networkId']

            if vpnsubnetid in self.subnetIconTable:
               self.subnetIconTable[vpnsubnetid].append(vpnframe)
            else:
               self.common.printInvalidSubnet(vpnsubnetid)

      # Add vpes to subnetIconTable ordered by subnetid.
      if self.common.isInputTerraform():
         vpes = self.data.getVPEGateways()
         vpeips = self.data.getVPEGatewayIPs()
         if not vpes.empty:
            for vpeindex, vpeframe in vpes.iterrows():
               vpeid = vpeframe['id']
               vpename = vpeframe['name']

               for vpeipindex, vpeipframe in vpeips.iterrows():
                  vpeipgateway = vpeipframe['gateway']
                  vpeipaddress = vpeipframe['address']

                  if vpeid != vpeipgateway:
                     continue

                  vpesubnetid = {}
                  vpesubnetframe = {}
                  subnets = self.data.getSubnets()

                  for subnetindex, subnetframe in subnets.iterrows():
                     subnetid = subnetframe['id']
                     subnetname = subnetframe['name']
                     subnetcidr = subnetframe['ipv4_cidr_block']

                     if ipaddress.ip_address(vpeipaddress) in ipaddress.ip_network(subnetcidr):
                        vpesubnetid = subnetid
                        vpesubnetframe = subnetframe 
                        break

                  addedVPE = False

                  if vpesubnetid in self.subnetIconTable:
                     if addedVPE == False:
                        vpeframecopy = vpeframe.copy()
                        vpeframecopy['id'] = vpeid + str(vpeindex)
                        vpeframecopy['subnet'] = vpesubnetid
                        vpeframecopy['address'] = vpeipaddress
                        self.subnetIconTable[vpesubnetid].append(vpeframecopy)
                        addedVPE = True
                     else:
                       if self.common.printInvalidSubnet(vpesubnetid):
                          continue

      else:
         vpes = self.data.getVPEGateways()
         reservedIPs = self.data.getReservedIPs()
         if not vpes.empty:
            for vpeindex, vpeframe in vpes.iterrows():
               vpeid = vpeframe['id']
               vpename = vpeframe['name']
               vpeips = vpeframe['ips']

               for vpeip in vpeips:

                  for ipindex, ipframe in reservedIPs.iterrows():
                     ipid = ipframe['id']
                     if vpeip != ipid:
                        continue

                     vpeipaddress = ipframe['address']

                     vpesubnetid = {}
                     vpesubnetframe = {}
                     subnets = self.data.getSubnets()

                     for subnetindex, subnetframe in subnets.iterrows():
                        subnetid = subnetframe['id']
                        subnetname = subnetframe['name']
                        subnetcidr = subnetframe['ipv4_cidr_block']

                        if ipaddress.ip_address(vpeipaddress) in ipaddress.ip_network(subnetcidr):
                           vpesubnetid = subnetid
                           vpesubnetframe = subnetframe 
                           break

                     addedVPE = False

                     if vpesubnetid in self.subnetIconTable:
                        if addedVPE == False:
                           vpeframecopy = vpeframe.copy()
                           vpeframecopy['id'] = vpeid + str(vpeindex)
                           vpeframecopy['subnet'] = vpesubnetid
                           vpeframecopy['address'] = vpeipaddress
                           self.subnetIconTable[vpesubnetid].append(vpeframecopy)
                           addedVPE = True
                        else:
                           if self.common.printInvalidSubnet(vpesubnetid):
                              continue

      # TBD Add clusters to subnetIconTable ordered by subnetid.
      #if self.common.isInputTerraform():
      #   clusters = self.data.getContainerClusters()
      #   if not clusters.empty:
      #      for clusterindex, clusterframe in clusters.iterrows():
      #         clusterid = clusterframe['id']
      #         clustername = clusterframe['name']
      #         clustersubnet = clusterframe['service_subnet']
      #if self.common.isInputTerraform():
      #   clusters = self.data.getClusters()
      #   if not clusters.empty:
      #      for clusterindex, clusterframe in clusters.iterrows():
      #         clusterid = clusterframe['id']
      #         #clustersubnetid = clusterframe['networkId']
      #         #clustersubnetid = clusterframe['subnet_id']
    
      #        #if clustersubnetid in self.subnetIconTable:
      #        #   self.subnetIconTable[clustersubnetid].append(clusterframe)
      #        #else:
      #        #   self.common.printInvalidSubnet(clustersubnetid)

      self.analyzeInstances()

      return

   def analyzeServiceIcons(self):
      services = self.data.getServices()

      # Add services to serviceIconTable ordered by serviceid.
      if not services.empty:
         for serviceindex, serviceframe in services.iterrows():
            servicename = serviceframe['name']
            serviceid = serviceframe['id']
            serviceregion = serviceframe['region']

            self.serviceIconTable[serviceid] = []

            if serviceid in self.serviceIconTable:
               self.serviceIconTable[serviceid].append(serviceframe)
            else:
               self.serviceIconTable[serviceid] = [serviceframe]

      return

   def analyzeLoadBalancers(self):
      listenerdata = []
      pooldata = []
      memberdata = []

      lbdata = self.data.getLoadBalancers()
      if not lbdata.empty:
         for lbindex, lb in lbdata.iterrows():
            lbid = lb['id']

            lbname = lb['name']
            if lbname[0:4] == 'kube':
               continue

            #lblisteners = lb['listeners']

            if not 'pools.region' in lb:
               continue

            lbpools = lb['pools.region']
            if not hasattr(lbpools, '__iter__'):
               self.common.printMissingPool(lbname)
               continue

            vpcid = None

            if lbpools:
               for lbpool in lbpools:
                  lbpoolid = lbpool['id']
                  lbpoolname = lbpool['name']

                  extended = lbpool
                  extended['lbid'] = lbid
                  pooldata.append(extended)

                  lbpoolid = extended['lbid']

                  poolmemberdata = []

                  if not 'members' in lbpool:
                     #self.common.printMissingMember(lbname, lbpoolname)
                     continue

                  lbmembers = lbpool['members']
                  if lbmembers:
                     for lbmember in lbmembers:
                        if lbmember:
                           #if lbmember['health'] == 'ok':
                           if lbmember['health'] == 'faulted':
                              poolmemberdata.append(lbmember)

                              if vpcid == None:
                                 instanceId = lbmember['instanceId']
                                 if instanceId != None:
                                    instance = self.getInstance(instanceId)

                                    if len(instance) == 0:
                                       vpcid = None
                                       # TBD Getting invalid member from incomplete cleanup - disable for now.
                                       # self.common.printInvalidInstanceMember(lbname, lbpoolname, instanceId)
                                       continue

                                    vpcid = instance['vpcId']

                  if poolmemberdata and vpcid != None:
                     #extended = {vpcid: {lbid: [ poolmemberdata ] }}
                     extended = {lbid: { lbpoolid: poolmemberdata }}
                     #memberdata.append(extended)
                     if vpcid in self.lbTable:
                        self.lbTable[vpcid].append(extended)
                     else:
                        self.lbTable[vpcid] = [extended]

      return

   def analyzeTerraformLoadBalancers(self):
      listenerdata = []
      pooldata = []
      memberdata = []

      lbdata = self.data.getLoadBalancers()
      if not lbdata.empty:
         for lbindex, lb in lbdata.iterrows():
            lbpools = []
            lbmembers = []

            lbid = lb['id']

            lbname = lb['name']
            if lbname[0:4] == 'kube':
               continue

            #lblisteners = lb['listeners']

            pooldatatemp = self.data.getLoadBalancerPools() 
            if not pooldatatemp.empty:
                for poolindex, lbpool in pooldatatemp.iterrows():
                   poolid = lbpool['pool_id']
                   poollb = lbpool['lb']
                   if poollb != lbid:
                      continue
                   #lbpools.append(dict(lbpool))

                   memberdata = self.data.getLoadBalancerMembers()
                   if not memberdata.empty:
                      for memberindex, lbmember in memberdata.iterrows():
                         memberpool = lbmember['pool']
                         memberlb = lbmember['lb']
                         if memberlb != lbid:
                            continue
                         lbmembers.append(dict(lbmember))

                      if lbmembers:
                         lbpool['members'] = lbmembers

                   lbpools.append(dict(lbpool))

                if lbpools:
                   lb['pools'] = lbpools

            lbpools = lb['pools']
            if not hasattr(lbpools, '__iter__'):
               self.common.printMissingPool(lbname)
               continue

            vpcid = None

            if lbpools:
               for lbpool in lbpools:
                  lbpoolid = lbpool['id']
                  lbpoolname = lbpool['name']

                  extended = lbpool
                  extended['lbid'] = lbid
                  pooldata.append(extended)

                  lbpoolid = extended['lbid']

                  poolmemberdata = []

                  if not 'members' in lbpool:
                     #self.common.printMissingMember(lbname, lbpoolname)
                     continue

                  lbmembers = lbpool['members']
                  if lbmembers:
                     for lbmember in lbmembers:
                        if lbmember:
                           #if lbmember['health'] == 'ok':
                           poolmemberdata.append(lbmember)

                           if vpcid == None:
                              instancedata = self.data.getInstances()
                              instanceIP = lbmember['target_address']
                              if instanceIP != None:
                                 instance = self.getInstanceByIP(instanceIP)

                                 if len(instance) == 0:
                                    vpcid = None
                                    self.common.printInvalidInstanceMember(lbname, lbpoolname, instanceId)
                                    continue

                                 vpcid = instance['vpc']

                  if poolmemberdata and vpcid != None:
                     #extended = {vpcid: {lbid: [ poolmemberdata ] }}
                     extended = {lbid: { lbpoolid: poolmemberdata }}
                     #memberdata.append(extended)
                     if vpcid in self.lbTable:
                        self.lbTable[vpcid].append(extended)
                     else:
                        self.lbTable[vpcid] = [extended]

      return

   def analyzeNetworkACLs(self):
      acldata = self.data.getNetworkACLs()
      if not acldata.empty:
         for aclindex, acl in acldata.iterrows():
            aclid = acl['id']
            vpcid = acl['vpcId']

            #extended = {aclid: {acl}}
            if vpcid in self.aclTable:
               #self.aclTable[vpcid].append(extended)
               self.aclTable[vpcid].append(acl)
            else:
              #self.aclTable[vpcid] = [extended]
              self.aclTable[vpcid] = [acl]

      return


   def findRow(self, dictionarylist, columnname, columnvalue):
      if len(dictionarylist) > 0:
         for dictionaryindex, dictionary in dictionarylist.iterrows():
            if dictionary[columnname] == columnvalue:
               return dictionary
      return {}

   def findRow2(self, dictionarylist, columnname1, columnvalue1, columnname2, columnvalue2):
      if len(dictionarylist) > 0:
         for dictionaryindex, dictionary in dictionarylist.iterrows():
            if dictionary[columnname1] == columnvalue1 and dictionary[columnname2] == columnvalue2:
               return dictionary
      return {}

   def findRow3(self, dictionarylist, columnname1, columnvalue1):
      if len(dictionarylist) > 0:
         for dictionaryindex, dictionary in dictionarylist.iterrows():
             if dictionary[columnname1] == columnvalue1:
               return dictionary
      return {}

   def getInstanceTable(self, subnetid):
      return self.instanceTable[subnetid]

   def getSubnetIconTable(self, subnetid):
      return self.subnetIconTable[subnetid]

   def getServiceIconTable(self, serviceid):
      return self.serviceIconTable[serviceid]

   def getLoadBalancerTable(self):
      return self.lbTable

   def getNICTable(self, subnetid, instanceid):
      return self.nicTable[subnetid + ':' + instanceid]

   def getRegionTable(self):
      return self.regionTable

   def getVPCTable(self):
      return self.vpcTable

   def getZoneTable(self):
      return self.zoneTable

   def getFloatingIPs(self):
      return self.data.getFloatingIPs()

   def getInstances(self):
      return self.data.getInstances()

   def getClusters(self):
      return self.data.getClusters()

   def getKeys(self):
      return self.data.getKeys()

   def getNetworkInterfaces(self):
      return self.data.getNetworkInterfaces()

   def getLoadBalancers(self):
      return self.data.getLoadBalancers()

   def getLoadBalancers(self, vpcid):
      if vpcid in self.lbTable:
         return self.lbTable[vpcid]
      else:
         return None

   def getLoadBalancerListeners(self):
      return self.data.getLoadBalancerListeners()

   def getLoadBalancerPools(self):
      return self.data.getLoadBalancerPools()

   def getLoadBalancerMembers(self):
      return self.data.getLoadBalancerMembers()

   def getNetworkACLs(self):
      return self.data.getNetworkACLs()

   def getNetworkACLs(self, vpcid):
      if vpcid in self.aclTable:
         return self.aclTable[vpcid]
      else:
         return None

   def getPublicGateways(self):
      return self.data.getPublicGateways()

   def getSecurityGroups(self):
      return self.data.getSecurityGroups()

   def getSubnets(self):
      return self.data.getSubnets()

   def getVolumes(self):
      return self.data.getVolumes()

   def getResourceGroups(self):
      return self.data.getResourceGroups()

   def getAddresses(self):
      return self.data.getAddresses()

   def getVPCs(self):
      return self.data.getVPCs()

   def getVPNGateways(self):
      return self.data.getVPNGateways()

   def getVPNConnections(self):
      return self.data.getVPNConnections()

   def getVPEGateways(self):
      return self.data.getVPEGateways()

   def getVPEGatewayIPs(self):
      return self.data.getVPEGatewayIPs()

   def getFlowLogs(self):
      return self.data.getFlowLogs()

   def getTransitGateways(self):
      return self.data.getTransitGateways()

   def getTransitConnections(self):
      return self.data.getTransitConnections()

   def getActivityTrackers(self):
      return self.data.getActivityTrackers()

   def getKeyManagements(self):
      return self.data.getKeyManagements()

   def getObjectBuckets(self):
      return self.data.getObjectBuckets()

   def getReservedIPs(self):
      return self.data.getReservedIPs()

   def getContainerClusters(self):
      return self.data.getContainerClusters()

   def hasServices(self):
      return self.data.hasServices()

   def hasFlowLogs(self):
      return self.data.hasFlowLogs()

   def hasTransitGateways(self):
      return self.data.hasTransitGateways()

   def hasActivityTrackers(self):
      return self.data.hasActivityTrackers()

   def hasKeyManagement(self):
      return self.data.hasKeyManagement()

   def hasObjectBuckets(self):
      return self.data.hasObjectBuckets()

   def hasReservedIPs(self):
      return self.hasReservedIPs()

   def getInstance(self, id):
      return self.findRow(self.data.getInstances(), 'id', id)

   def getInstanceByIP(self, ip):
      instances = self.data.getInstances()
      if not instances.empty:
         for instanceindex, instance in instances.iterrows():
            nics = instance['networkInterfaces']
            for nic in nics:
               nicip = nic['primary_ipv4_address']
               if ip == nicip:
                  return instance
      return None

   def getNetworkInterface(self, id1, id2):
      return self.findRow2( self.data.getNetworkInterfaces(), 'primary_ip.address', id1, 'instance.id', id2)

   def getNetworkInterface3(self, id1):
      return self.findRow3( self.data.getNetworkInterfaces(), 'primary_ip.address', id1)

   def getLoadBalancer(self, id):
      return self.findRow(self.data.getLoadBalancers(), 'id', id)

   def getLoadBalancerMember(self, id):
      return self.findRow(self.data.getLoadBalancerMembers(), 'id', id)

   def getSubnet(self, id):
      return self.findRow(self.data.getSubnets(), 'id', id)

   def getVPC(self, id):
      return self.findRow(self.data.getVPCs(), 'id', id)

   def getFloatingIP(self, id):
      if self.common.isInputTerraform():
         return self.findRow(self.data.getFloatingIPs(), 'target', id)
      else:
         return self.findRow(self.data.getFloatingIPs(), 'target.id', id)

   def getPublicGateway(self, id):
      return self.findRow(self.data.getPublicGateways(), 'id', id)

   def getVPNGateway(self, id):
      if self.common.isInputRIAS():
         return self.findRow(self.data.getVPNGateways(), 'subnet.id', id)
      else:
         return self.findRow(self.data.getVPNGateways(), 'networkId', id)

   def getVPEGateway(self, id):
      return self.findRow(self.data.getVPEGateways(), 'id', id)

   def getVPEGatewayIP(self, id):
      return self.findRow(self.data.getVPEGatewayIPs(), 'id', id)

   def getFlowLog(self, id):
      return self.findRow(self.data.getFlowLog(), 'id', id)

   def getTransitGateway(self, id):
      return self.findRow(self.data.getTransitGateway(), 'id', id)

   def getActivityTracker(self, id):
      return self.findRow(self.data.getActivityTracker(), 'id', id)

   def getKeyManagement(self, id):
      return self.findRow(self.data.getKeyManagement(), 'id', id)

   def getObjectBucket(self, id):
      return self.findRow(self.data.getObjectBucket(), 'id', id)

   def getReservedIP(self, id):
      return self.findRow(self.data.getReservedIP(), 'id', id)
