# @file opsjson.py
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

from sys import exit

from json import loads as json_load
from yaml import load as yaml_load
from yaml import FullLoader as yaml_FullLoader
from pandas import concat, DataFrame, json_normalize

from .common import Common
from .icons import Icons

class OpsJson:
   resourceGroups = {}
   addresses = {}
   floatingIPs = {}
   instances = {}
   clusters = {}
   keys = {}
   networkInterfaces = {} # Used to match NICs referenced in LB members.
   loadBalancers = {}
   loadBalancerListeners = {}
   loadBalancerPools = {}
   loadBalancerMembers = {}
   networkACLs = {}
   publicGateways = {}
   securityGroups = {}
   subnets = {}
   volumes = {}
   vpcs = {}
   vpnGateways = {}
   vpnConnections = {}
   vpeGateways = {}
   vpeGatewayIPs = {}
   flowLogs = {}
   transitGateways = {}
   activityTrackers = {}
   keyManagement = {}
   objectBuckets = {}
   reservedIPs = {}
   services = {}
   types = []
   data = {}
   common = None
   icons = None

   def __init__(self, common):
      self.types = ['vpcs', 'subnets', 'instances', 'clusters', 'public_gateways', 'floating_ips', 'vpn_gateways', 'load_balancers']
      self.common = common
      self.icons = Icons(common)
      return

   def loadJSON(self):
      stream = open(self.common.getInputFile(), 'r', encoding='utf-8-sig')
      self.data = json_load(stream.read())
      if not 'vpcs' in self.data:
         #self.common.printMissingVPCs(self.common.getInputFile())
         self.common.printMissingVPCs()
         exit()
      elif not 'subnets' in self.data:
         #self.common.printMissingSubnets(self.common.getInputFile())
         self.common.printMissingSubnets()
         exit()

      if self.data != None:
         self.normalizeData()

      return

   def loadYAML(self):
      stream = open(self.common.getInputFile(), 'r')
      self.data = yaml_load(stream, Loader=yaml_FullLoader)
      if not 'vpcs' in self.data:
         #self.common.printMissingVPCs(self.common.getInputFile())
         self.common.printMissingVPCs()
         exit()
      elif not 'subnets' in self.data:
         #self.common.printMissingSubnets(self.common.getInputFile())
         self.common.printMissingSubnets()
         exit()

      if self.data != None:
         self.normalizeData()

      return

   def normalizeData(self):
      self.vpcs = json_normalize(self.data['vpcs'] if ('vpcs' in self.data) else json_normalize({}))
      self.subnets = json_normalize(self.data['subnets'] if ('subnets' in self.data) else json_normalize({}))
      self.instances = json_normalize(self.data['instances'] if ('instances' in self.data) else json_normalize({}))
      self.clusters = json_normalize(self.data['clusters'] if ('clusters' in self.data) else json_normalize({}))
      self.networkInterfaces = json_normalize(self.data['networkInterfaces'] if ('networkInterfaces' in self.data) else json_normalize({}))
      self.publicGateways = json_normalize(self.data['publicGateways'] if ('publicGateways' in self.data) else json_normalize({}))
      self.floatingIPs = json_normalize(self.data['floatingIPs'] if ('floatingIPs' in self.data) else json_normalize({}))
      self.vpnGateways = json_normalize(self.data['vpnGateways'] if ('vpnGateways' in self.data) else json_normalize({}))
      self.vpnConnections = json_normalize(self.data['vpnConnections'] if ('vpnConnections' in self.data) else json_normalize({}))
      self.vpeGateways = json_normalize(self.data['vpes'] if ('vpes' in self.data) else json_normalize({}))
      self.flowLogs = json_normalize(self.data['flowLogCollectors'] if ('flowLogCollectors' in self.data) else json_normalize({}))
      self.transitGateways = json_normalize({})
      self.activityTrackers = json_normalize({})
      self.keyManagement = json_normalize({})
      self.objectBuckets = json_normalize({})
      self.reservedIPs = json_normalize(self.data['reservedIPs'] if ('reservedIPs' in self.data) else json_normalize({}))
      self.loadBalancers = json_normalize(self.data['loadBalancers'] if ('loadBalancers' in self.data) else json_normalize({}))
      self.loadBalancerListeners = json_normalize(self.data['loadBalancerListeners'] if ('loadBalancerListeners' in self.data) else json_normalize({}))
      self.loadBalancerPools = json_normalize(self.data['loadBalancerPools'] if ('loadBalancerPools' in self.data) else json_normalize({}))
      self.loadBalancerMembers = json_normalize(self.data['loadBalancerMembers'] if ('loadBalancerMembers' in self.data) else json_normalize({}))
      self.volumes = json_normalize(self.data['volumes'] if ('volumes' in self.data) else json_normalize({}))
      self.networkACLs = json_normalize(self.data['networkACLs'] if ('networkACLs' in self.data) else json_normalize({}))
      self.securityGroups = json_normalize(self.data['securityGroups'] if ('securityGroups' in self.data) else json_normalize({}))
      self.services = json_normalize(self.data['services'] if ('services' in self.data) else json_normalize({}))
      self.keys = json_normalize(self.data['keys'] if ('keys' in self.data) else json_normalize({}))

      if not self.vpcs.empty:
         self.vpcs.rename(
            columns={'availabilityZone': 'zone.name'}, inplace=True)

      if not self.subnets.empty:
         self.subnets.rename(
            columns={'availabilityZone': 'zone.name',
                     'subnet': 'ipv4_cidr_block',
                     'publicGateway.id': 'public_gateway.id',
                     'vpcId': 'vpc.id'}, inplace=True)

         self.subnets['vpc.name'] = self.subnets['vpc.id'] 

      if not self.instances.empty:
         self.instances.rename(
            columns={'memoryGb': 'memory',
                     'bandwidthMb': 'bandwidth',
                     'cpuCount': 'vcpu.count',
                     'profile': 'profile.name',
                     'osVersion': 'image.name'}, inplace=True)
         if len(self.instances) == 1:
            for instanceindex, instanceframe in self.instances.iterrows():
               if instanceframe['name'] == '*':
                  self.addAllIcons()
                  self.common.setAllIcons()
                  break

      if not self.networkInterfaces.empty:
         self.networkInterfaces.rename(
            columns={'ip': 'primary_ip.address',
                     'networkId': 'subnet.id',
                     'instanceId': 'instance.id'}, inplace=True)

      if not self.vpnGateways.empty:
         self.vpnGateways.rename(
            columns={'floatingIP': 'floating_ip.address'}, inplace=True)

      if not self.vpeGateways.empty:
         self.vpeGateways['type'] = 'vpegateway'

      if not self.flowLogs.empty:
         self.flowLogs['type'] = 'flowlogs'

      return

   def addAllIcons(self):
      iconDictionary = self.icons.getIconDictionary()
      iconCount = len(iconDictionary)
      newinstances = concat([self.instances]*iconCount, ignore_index=True)
      iconIndex = 0

      for iconkey, iconvalue in iconDictionary.items():
         icon = iconvalue['icon']
         newinstances.at[iconIndex, 'name'] =  icon
         newinstances.at[iconIndex, 'id'] = icon + '-id'
         newinstances.at[iconIndex, 'networkInterfaces.id'] = icon + '-eth0-id'
         iconIndex += 1

      self.instances = newinstances

      for instanceindex, instanceframe in self.instances.iterrows():
         instanceid = instanceframe['id']
         niclist = instanceframe['networkInterfaces']
         nic = niclist[0]
         nic['id'] = instanceid + '-eth0'

      return

   def getFloatingIPs(self):
      return self.floatingIPs

   def getInstances(self):
      return self.instances

   def getClusters(self):
      return self.clusters

   def getKeys(self):
      return self.keys

   def getNetworkInterfaces(self):
      return self.networkInterfaces

   def getLoadBalancers(self):
      return self.loadBalancers

   def getLoadBalancerListeners(self):
      return self.loadBalancerListeners

   def getLoadBalancerPools(self):
      return self.loadBalancerPools

   def getLoadBalancerMembers(self):
      return self.loadBalancerMembers

   def getNetworkACLs(self):
      return self.networkACLs

   def getPublicGateways(self):
      return self.publicGateways

   def getSecurityGroups(self):
      return self.securityGroups

   def getSubnets(self):
      return self.subnets

   def setSubnets(self, subnets):
      self.subnets = subnets

   def getServices(self):
      return self.services

   def setServices(self, services):
      self.services = services

   def getVolumes(self):
      return self.volumes

   def getResourceGroups(self):
      return self.resourceGroups

   def getResourceGroups(self):
      return self.resourceGroups

   def getAddresses(self):
      return self.addresses

   def getVPCs(self):
      return self.vpcs

   def setVPCs(self, vpcs):
      self.vpcs = vpcs

   def getVPNGateways(self):
      return self.vpnGateways

   #def getVPNConnections(self):
   #  return self.vpnConnections

   def getVPEGateways(self):
      return self.vpeGateways

   def getVPEGatewayIPs(self):
      return self.vpeGatewayIPs

   def getFlowLogs(self):
      return self.flowLogs

   def getTransitGateways(self):
      return self.transitGateways

   def getTransitConnections(self):
      return self.transitConnections

   def getActivityTrackers(self):
      return self.activityTrackers

   def getKeyManagement(self):
      return self.keyManagement

   def getObjectBuckets(self):
      return self.objectBuckets

   def getReservedIPs(self):
      return self.reservedIPs

   def hasServices(self):
      return not self.flowLogs.empty or not self.transitGateways.empty or not self.activitytrackers.empty or not self.keyManagement.empty or not self.objectBuckets.empty

   def hasFlowLogs(self):
      return not self.flowLogs.empty

   def hasTransitGateways(self):
      return not self.transitGateways.empty

   def hasActivityTrackers(self):
      return not self.activityTrackers.empty

   def hasKeyManagement(self):
      return not self.keyManagement.empty

   def hasObjectBuckets(self):
      return not self.objectBuckets.empty

   def hasReservedIPs(self):
      return not self.reservedIPs.empty
