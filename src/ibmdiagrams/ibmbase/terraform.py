# @file terraform.py
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

from json import loads as json_load, dumps as json_dumps
from pandas import concat, DataFrame, json_normalize, read_json
from tabulate import tabulate

from .common import Common
from .icons import Icons
from .resources import Resources

class Terraform:
   activitTrackers = {}
   addresses = {}
   clusters = {}
   floatingIPs = {}
   flowLogs = {}
   instances = {}
   keys = {}
   keyManagements = {}
   loadBalancers = {}
   loadBalancerListeners = {}
   loadBalancerPools = {}
   loadBalancerMembers = {}
   networkACLs = {}
   networkInterfaces = {} # Used to match NICs referenced in LB members.
   objectBuckets = {}
   resourceGroups = {}
   publicGateways = {}
   reservedIPs = {}
   securityGroups = {}
   services = {}
   subnets = {}
   tektonPipelines = {}
   toolchains = {}
   toolchainHostedgits = {}
   toolchainPipelines = {}
   transitGateways = {}
   transitConnections = {}
   volumes = {}
   vpcs = {}
   vpeGateways = {}
   vpeGatewayIPs = {}
   vpnGateways = {}
   vpnConnections = {}

   types = {}
   data = {}
   common = None
   icons = None
   resources = None

   def __init__(self, common):
      self.types = ['vpcs', 'subnets', 'instances', 'clusters', 'public_gateways', 'floating_ips', 'vpn_gateways', 'load_balancers']
      self.common = common
      self.icons = Icons(common)
      return

   def loadTerraform(self):
      stream = open(self.common.getInputFile(), 'r', encoding='utf-8-sig')
      self.data = json_load(stream.read())
      resourcedata = self.data['resources']
      df = json_normalize(resourcedata)

      #tempresourceGroups = {}
      #tempaddresses = {}
      #tempvpcs = {}
      #tempsubnets = {}
      #tempinstances = {}
      #tempfloatingIPs = {}
      #temppublicGateways = {}
      #tempvpnGateways = {}
      #tempvpeGateways = {}
      #tempvpeGatewayIPs = {}
      #temploadBalancers = {}
      #temploadBalancerListeners = {}
      #temploadBalancerPools = {}
      #temploadBalancerMembers = {}
      #tempnetworkACLs = {}
      #tempsecurityGroups = {}
      #tempflowLogs = {}
      #temptransitGateways = {}
      #temptransitConnections = {}
      #tempactivityTrackers = {}
      #tempkeyManagements = {}
      #tempobjectBuckets= {}
      #tempclusters = {}
      #temptoolchains = {}
      #temptoolchainPipelines = {}
      #temptoolchainHostedgits = {}
      #temptektonPipelines = {}

      self.resources = Resources(self.common, df)

      #vpcs = df[df["type"] == "ibm_is_vpc"]
      #subnets = df[df["type"] == "ibm_is_subnet"]

      #if vpcs.empty:
      #   self.common.printMissingVPCs()
      #   exit()
      #elif subnets.empty:
      #   self.common.printMissingSubnets()
      #   exit()

      activityTrackerInstances = self.resources.getResource("ibm_atracker_route")
      addressInstances = self.resources.getResource("ibm_is_vpc_address_prefix")
      clusterInstances = self.resources.getResource("ibm_container_vpc_cluster")
      floatingIPInstances = self.resources.getResource("ibm_is_floating_ip")
      flowLogInstances = self.resources.getResource("ibm_is_flow_log")
      instanceInstances = self.resources.getResource("ibm_is_instance")
      keyManagementInstances = self.resources.getResource("ibm_kms_key")
      loadBalancerInstances = self.resources.getResource("ibm_is_lb")
      loadBalancerListenerInstances = self.resources.getResource("ibm_is_lb_listener")
      loadBalancerPoolInstances = self.resources.getResource("ibm_is_lb_pool")
      loadBalancerMemberInstances = self.resources.getResource("ibm_is_lb_pool_member")
      networkACLInstances = self.resources.getResource("ibm_is_network_acl")
      objectBucketInstances = self.resources.getResource("ibm_cos_bucket")
      publicGatewayInstances = self.resources.getResource("ibm_is_public_gateway")
      resourceGroupInstances = self.resources.getResource("ibm_resource_group")
      securityGroupInstances = self.resources.getResource("ibm_is_security_group")
      subnetInstances = self.resources.getResource("ibm_is_subnet")
      tektonPipelineInstances = self.resources.getResource("ibm_cd_tekton_pipeline")
      toolchainHostedgitsInstances = self.resources.getResource("ibm_cd_toolchain_tool_hostedgit")
      toolchainPipelineInstances = self.resources.getResource("ibm_cd_toolchain_tool_pipeline")
      toolchainInstances = self.resources.getResource("ibm_cd_toolchain")
      transitGatewayInstances = self.resources.getResource("ibm_tg_gateway")
      transitConnectionInstances = self.resources.getResource("ibm_tg_connection")
      vpcInstances = self.resources.getResource("ibm_is_vpc")
      vpeGatewayInstances = self.resources.getResource("ibm_is_virtual_endpoint_gateway")
      vpeGatewayIPInstances = self.resources.getResource("ibm_is_virtual_endpoint_gateway_ip")
      vpnGatewayInstances = self.resources.getResource("ibm_is_vpn_gateway")

      count = 0
      tempresourceGroups = {}
      if len(resourceGroupInstances) > 0:
         for instances in resourceGroupInstances: 
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               tempresourceGroups[count] = instancerow
               count += 1

      if tempresourceGroups != {}:
         self.resourceGroups = DataFrame.from_dict(tempresourceGroups, orient="index")
      else:
         self.resourceGroups = DataFrame()

      count = 0
      tempaddresses = {}
      if len(addressInstances) > 0:
         for instances in addressInstances: 
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               tempaddresses[count] = instancerow
               count += 1

      if tempaddresses != {}:
         self.addresses = DataFrame.from_dict(tempaddresses, orient="index")
      else:
         self.addresses = DataFrame()

      count = 0
      tempvpcs = {}
      if len(vpcInstances) > 0:
         for instances in vpcInstances: 
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               subnets = instanceattributes["subnets"]
               # TBD Duplicate VPCs with slzvsi, one with subnets, other with empty subnets, so skip empty subnets.
               #     No duplication VPCs with slzvpc (no VSIs), so keep empty subnets.
               #if not instanceInstances.empty:
               #   #@TEST if subnets == []:
               #   #@TEST   #instancerow = {}
               #   #@TEST   continue
               instancerow = {"id": instanceid} | instanceattributes
               tempvpcs[count] = instancerow
               count += 1

      if tempvpcs != {}:
         self.vpcs = DataFrame.from_dict(tempvpcs, orient="index")
      else:
         self.vpcs = DataFrame()

      count = 0
      tempsubnets = {}
      if len(subnetInstances) > 0:
         for instances in subnetInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               region = instanceattributes["zone"]
               regionindex = region.rfind('-')
               region = region[0:regionindex]
               instancerow = {"id": instanceid, "region": region} | instanceattributes
               tempsubnets[count] = instancerow
               count += 1

      if tempsubnets != {}:
         self.subnets = DataFrame.from_dict(tempsubnets, orient="index")

         self.subnets.rename(
            columns={'zone': 'zone.name',
                     'vpc': 'vpc.id'}, inplace=True)

         self.subnets['vpc.name'] = self.subnets['vpc.id']
      else:
         self.subnets = DataFrame()

      count = 0
      tempnetworkACLs = {}
      if len(networkACLInstances) > 0:
         for instances in networkACLInstances: 
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               tempnetworkACLs[count] = instancerow
               count += 1

      if tempnetworkACLs != {}:
         self.networkACLs = DataFrame.from_dict(tempvpcs, orient="index")
      else:
         self.networkACLs = DataFrame()

      count = 0
      tempsecurityGroups = {}
      if len(securityGroupInstances) > 0:
         for instances in securityGroupInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               tempsecurityGroups[count] = instancerow
               count += 1

      if tempsecurityGroups != {}:
         self.securityGroups = DataFrame.from_dict(tempsecurityGroups, orient="index")
      else:
         self.securityGroups = DataFrame()

      count = 0
      tempinstances = {}
      if len(instanceInstances) > 0:
         for instances in instanceInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancerow = {"id": instanceid} | instanceattributes
               #tempinstances[instanceid] = instanceattributes
               tempinstances[count] = instancerow
               count += 1

      if tempinstances != {}:
         self.instances = DataFrame.from_dict(tempinstances, orient="index")

         #self.instances.rename(
         #   columns={'network_interfaces': 'networkInterfaces'}, inplace=True)
         self.instances.rename(
            columns={'primary_network_interface': 'networkInterfaces'}, inplace=True)

         self.instances['type'] = 'Instance'
      else:
         self.instances = DataFrame()

      count = 0
      tempfloatingIPs = {}
      if len(floatingIPInstances) > 0:
         for instances in floatingIPInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancerow = {"id": instanceid} | instanceattributes
               #tempfloatingIPs[instanceid] = instanceattributes
               tempfloatingIPs[count] = instancerow
               count += 1

      if tempfloatingIPs != {}:
         self.floatingIPs = DataFrame.from_dict(tempfloatingIPs, orient="index")
      else:
         self.floatingIPs = DataFrame()

      count = 0
      temppublicGateways = {}
      if len(publicGatewayInstances) > 0:
         for instances in publicGatewayInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancerow = {"id": instanceid} | instanceattributes
               #temppublicGateways[instanceid] = instanceattributes
               temppublicGateways[count] = instancerow
               count += 1

      if temppublicGateways != {}:
         self.publicGateways = DataFrame.from_dict(temppublicGateways, orient="index")
      else:
         self.publicGateways = DataFrame()

      count = 0
      tempvpnGateways = {}
      if len(vpnGatewayInstances) > 0:
         for instances in vpnGatewayInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               #tempvpnGateways[instanceid] = instanceattributes
               tempvpnGateways[count] = instancerow
               count += 1

      if tempvpnGateways != {}:
         self.vpnGateways = DataFrame.from_dict(tempvpnGateways, orient="index")
         self.vpnGateways['type'] = 'vpngateway'
      else:
         self.vpnGateways = DataFrame()

      count = 0
      tempvpeGateways = {}
      if len(vpeGatewayInstances) > 0:
         for instances in vpeGatewayInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               #tempvpeGateways[instanceid] = instanceattributes
               tempvpeGateways[count] = instancerow
               count += 1

      if tempvpeGateways != {}:
         self.vpeGateways = DataFrame.from_dict(tempvpeGateways, orient="index")
         self.vpeGateways['type'] = 'vpegateway'
      else:
         self.vpeGateways = DataFrame()

      count = 0
      tempvpeGatewayIPs = {}
      if len(vpeGatewayIPInstances) > 0:
         for instances in vpeGatewayIPInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               #tempvpeGatewayIPs[instanceid] = instanceattributes
               tempvpeGatewayIPs[count] = instancerow
               count += 1

      if tempvpeGatewayIPs != {}:
         self.vpeGatewayIPs = DataFrame.from_dict(tempvpeGatewayIPs, orient="index")
         self.vpeGatewayIPs['type'] = 'vpegatewayip'
      else:
         self.vpeGatewayIPs = DataFrame()

      count = 0
      temploadBalancers = {}
      if len(loadBalancerInstances) > 0:
         for instances in loadBalancerInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancerow = {"id": instanceid} | instanceattributes
               #temploadBalancers[instanceid] = instanceattributes
               temploadBalancers[count] = instancerow
               count += 1

      if temploadBalancers != {}:
         self.loadBalancers = DataFrame.from_dict(temploadBalancers, orient="index")
      else:
         self.loadBalancers = DataFrame()

      count = 0
      temploadBalancerListeners = {}
      if len(loadBalancerListenerInstances) > 0:
         for instances in loadBalancerListenerInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancerow = {"id": instanceid} | instanceattributes
               #temploadBalancerListeners[instanceid] = instanceattributes
               temploadBalancerListeners[count] = instancerow
               count += 1

      if temploadBalancerListeners != {}:
         self.loadBalancerListeners = DataFrame.from_dict(temploadBalancerListeners, orient="index")
      else:
         self.loadBalancerListeners = DataFrame()

      count = 0
      temploadBalancerPools = {}
      if len(loadBalancerPoolInstances) > 0:
         for instances in loadBalancerPoolInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancerow = {"id": instanceid} | instanceattributes
               #temploadBalancerPools[instanceid] = instanceattributes
               temploadBalancerPools[count] = instancerow
               count += 1

      if temploadBalancerPools != {}:
         self.loadBalancerPools = DataFrame.from_dict(temploadBalancerPools, orient="index")
      else:
         self.loadBalancerPools = DataFrame()

      count = 0
      temploadBalancerMembers = {}
      if len(loadBalancerMemberInstances) > 0:
         for instances in loadBalancerMemberInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancerow = {"id": instanceid} | instanceattributes
               #temploadBalancerMembers[instanceid] = instanceattributes
               temploadBalancerMembers[count] = instancerow
               count += 1

      if temploadBalancerMembers != {}:
         self.loadBalancerMembers = DataFrame.from_dict(temploadBalancerMembers, orient="index")
      else:
         self.loadBalancerMembers = DataFrame()

      count = 0
      tempflowLogs = {}
      if len(flowLogInstances) > 0:
         for instances in flowLogInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               tempflowLogs[count] = instancerow
               count += 1

      if tempflowLogs != {}:
         self.flowLogs = DataFrame.from_dict(tempflowLogs, orient="index")
      else:
         self.flowLogs = DataFrame()

      count = 0
      temptransitGateways = {}
      if len(transitGatewayInstances) > 0:
         for instances in transitGatewayInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               temptransitGateways[count] = instancerow
               count += 1

      if temptransitGateways != {}:
         self.transitGateways = DataFrame.from_dict(temptransitGateways, orient="index")
      else:
         self.transitGateways = DataFrame()

      count = 0
      temptransitConnections = {}
      if len(transitConnectionInstances) > 0:
         for instances in transitConnectionInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               temptransitConnections[count] = instancerow
               count += 1

      if temptransitConnections != {}:
         self.transitConnections = DataFrame.from_dict(temptransitConnections, orient="index")
      else:
         self.transitConnections = DataFrame()

      count = 0
      tempactivityTrackers = {}
      if len(activityTrackerInstances) > 0:
         for instances in activityTrackerInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               tempactivityTrackers[count] = instancerow
               count += 1

      if tempactivityTrackers != {}:
         self.activityTrackers = DataFrame.from_dict(tempactivityTrackers, orient="index")
      else:
         self.activityTrackers = DataFrame()

      count = 0
      tempkeyManagements = {}
      if len(keyManagementInstances) > 0:
         for instances in keyManagementInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["key_name"]
               instancerow = {"id": instanceid} | instanceattributes
               tempkeyManagements[count] = instancerow
               count += 1

      if tempkeyManagements != {}:
         self.keyManagements = DataFrame.from_dict(tempkeyManagements, orient="index")
      else:
         self.keyManagements = DataFrame()

      count = 0
      tempobjectBuckets = {}
      if len(objectBucketInstances) > 0:
         for instances in objectBucketInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["bucket_name"]
               instancerow = {"id": instanceid} | instanceattributes
               tempobjectBuckets[count] = instancerow
               count += 1

      if tempobjectBuckets != {}:
         self.objectBuckets = DataFrame.from_dict(tempobjectBuckets, orient="index")
      else:
         self.objectBuckets = DataFrame()

      count = 0
      tempclusters = {}
      if len(clusterInstances) > 0:
         for instances in clusterInstances:
            for instance in instances:
               instanceattributes = instance["attributes"]
               instanceid = instanceattributes["id"]
               instancename = instanceattributes["name"]
               instancerow = {"id": instanceid} | instanceattributes
               tempclusters[count] = instancerow
               count += 1

      if tempclusters != {}:
         self.clusters = DataFrame.from_dict(tempclusters, orient="index")
         self.clusters['type'] = 'cluster'
      else:
         self.clusters = DataFrame()

      self.vpnConnections = DataFrame()
      self.volumes = DataFrame()
      self.services = DataFrame()
      self.keys = DataFrame()

      # TBD: Revisit normalization for Terraform or remove.
      #if self.data != None:
      #   self.normalizeData()

      return

   def normalizeData(self):
      self.vpcs = json_normalize(self.data['vpcs'] if ('vpcs' in self.data) else json_normalize({}))
      self.subnets = json_normalize(self.data['subnets'] if ('subnets' in self.data) else json_normalize({}))
      self.instances = json_normalize(self.data['instances'] if ('instances' in self.data) else json_normalize({}))
      self.clusters = json_normalize(self.data['clusters'] if ('clusters' in self.data) else json_normalize({}))
      self.networkInterfaces = json_normalize(self.data['networkInterfaces'] if ('networkInterfaces' in self.data) else json_normalize({}))
      self.floatingIPs = json_normalize(self.data['floatingIPs'] if ('floatingIPs' in self.data) else json_normalize({}))
      self.publicGateways = json_normalize(self.data['publicGateways'] if ('publicGateways' in self.data) else json_normalize({}))
      self.vpnGateways = json_normalize(self.data['vpnGateways'] if ('vpnGateways' in self.data) else json_normalize({}))
      self.vpnConnections = json_normalize(self.data['vpnConnections'] if ('vpnConnections' in self.data) else json_normalize({}))
      self.vpeGateways = json_normalize(self.data['vpes'] if ('vpes' in self.data) else json_normalize({}))
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

   def getAddresses(self):
      return self.addresses

   def getVPCs(self):
      return self.vpcs

   def setVPCs(self, vpcs):
      self.vpcs = vpcs

   def getVPNGateways(self):
      return self.vpnGateways

   #def getVPNConnections(self):
   #   return self.vpnConnections

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

   def getKeyManagements(self):
      return self.keyManagements

   def getObjectBuckets(self):
      return self.objectBuckets

   def getReservedIPs(self):
      return self.reservedIPs

   def hasServices(self):
      return not self.flowLogs.empty or not self.transitGateways.empty or not self.activityTrackers.empty or not self.keyManagements.empty or not self.objectBuckets.empty

   def hasFlowLogs(self):
      return not self.flowLogs.empty

   def hasTransitGateways(self):
      return not self.transitGateways.empty

   def hasActivityTrackers(self):
      return not self.activityTrackers.empty

   def hasKeyManagement(self):
      return not self.keyManagements.empty

   def hasObjectBuckets(self):
      return not self.objectBuckets.empty

   def hasReservedIPs(self):
      return not self.reservedIPs.empty
