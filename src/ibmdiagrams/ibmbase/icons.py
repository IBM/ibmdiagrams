# @file icons.py
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

from .colors import Colors
from .staticicons import StaticIcons
from .catalogicons import CatalogIcons

# There are three sets of icons: 
# 1. Builtin Icons - icon is name from design center containing product icons and non-product icons.
# 2. Static Icons - staticicon is name from static stencils in staticicons.py containing product icons and non-product icons.
# 3. Catalog Icons - catalogicon is name from cloud catalog in catalogicons.py containing only product icons.
#
# For catalog icons, the non-product icons are reused from the static icons.
# A single asterisk represents using a static icon.
# A double asterisk represents using a static icon for a group.

class Icons:
   iconDictionary = {
      # Core Groups
      # Note: App icons has an IBM Cloud icon but too light so using UI icon. 
      'IBM Cloud': {'icon': 'ibm-cloud', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'IBM Cloud', 'catalogicon': '**IBM Cloud'},
      'VPC': {'icon': 'ibm-cloud--vpc', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'VPC', 'catalogicon': '**VPC'},
      'Subnet': {'icon': 'ibm-cloud--subnets', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'Subnet', 'catalogicon': '**Subnet'},
      'Enterprise Network': {'icon': 'network--enterprise', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'Enterprise Network', 'catalogicon': '**Undefined Group'},
      'Public Network': {'icon': 'network--public', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'Public Network', 'catalogicon': '**Public Network'},
      'Cloud Services': {'icon': 'cloud-services', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'Cloud Services', 'catalogicon': '**Cloud Services'},
      'Internet Services': {'icon': 'ibm-cloud--internet-services', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'Internet Services', 'catalogicon': 'Undefined Group'},
      'Overlay Network': {'icon': 'network--overlay', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'Network Overlay', 'catalogicon': 'Undefined Group'},
      'Power Workspace': {'icon': 'ibm--power-vs', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'Power Workspace', 'catalogicon': 'Workspace for Power Virtual Server'},
      'Z System': {'icon': 'z--systems', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'Undefined Group', 'catalogicon': 'Undefined Group'},
      'Internet': {'icon': 'wikis', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'Internet', 'catalogicon': 'Undefined Group'},
      'VLAN': {'icon': 'vlan', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'VLAN', 'catalogicon': 'Undefined Group'},
      'Classic VLAN': {'icon': 'vlan--ibm', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'IBM Classic VLAN', 'catalogicon': 'VLAN'},
      'Classic Infrastructure': {'icon': 'infrastructure--classic', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'staticicon': 'Undefined Group', 'catalogicon': 'Undefined Group'},
      'OpenShift': {'icon': 'logo--openshift', 'color': Colors.lines["compute"], 'fill': Colors.fills["white"], 'staticicon': 'OpenShift', 'catalogicon': 'Red Hat OpenShift on IBM Cloud'},
      'Kubernetes Service': {'icon': 'ibm-cloud--kubernetes-service', 'color': Colors.lines["compute"], 'fill': Colors.fills["white"], 'staticicon': 'Kubernetes', 'catalogicon': 'Kubernetes Service'},
      'Z Containers': {'icon': 'ibm-z-os--containers', 'color': Colors.lines["compute"], 'fill': Colors.fills["white"], 'staticicon': 'Z Containers', 'catalogicon': 'Undefined Group'},
      'watsonx': {'icon': 'watsonx', 'color': Colors.lines["applications"], 'fill': Colors.fills["white"], 'staticicon': 'Watsonx', 'catalogicon': 'watsonx'},
      'watsonx Code Assistant': {'icon': 'ibm-watsonx--code-assistant', 'color': Colors.lines["applications"], 'fill': Colors.fills["white"], 'staticicon': 'Undefined Group', 'catalogicon': 'watsonx'},
      'watsonx Z Code Assistant': {'icon': 'ibm-watsonx--code-assistant-for-z', 'color': Colors.lines["applications"], 'fill': Colors.fills["white"], 'staticicon': 'Undefined Group', 'catalogicon': 'watsonx'},
      'Authorization Boundary': {'icon': 'flag', 'color': Colors.lines["security"], 'fill': Colors.fills["white"], 'staticicon': 'Authorization Boundary', 'catalogicon': 'Undefined Group'},
      'Point of Presence': {'icon': 'point-of-presence', 'color': Colors.lines["location"], 'fill': Colors.fills["white"], 'staticicon': 'Point of Presence', 'catalogicon': 'Undefined Group'},
      'Region': {'icon': 'location', 'color': Colors.lines["location"], 'fill': Colors.fills["location"], 'staticicon': 'Region', 'catalogicon': '**Region'},

      # Zone Groups
      'Access Group': {'icon': 'group--access', 'color': Colors.lines["security"], 'fill': Colors.fills["none"], 'staticicon': 'Access Group', 'catalogicon': 'Undefined Group'},
      'Account Group': {'icon': 'group--account', 'color': Colors.lines["security"], 'fill': Colors.fills["none"], 'staticicon': 'Account Group', 'catalogicon': 'Undefined Group'},
      'Instance Group': {'icon': 'autoscaling', 'color': Colors.lines["compute"], 'fill': Colors.fills["none"], 'staticicon': 'Instance Group', 'catalogicon': 'Undefined Group'},
      # Note: App icons has a Placement Groups for VPC icon but too light so using UI icon. 
      'Placement Group': {'icon': 'group-objects', 'color': Colors.lines["compute"], 'fill': Colors.fills["none"], 'staticicon': 'Undefined Group', 'catalogicon': '**Placement Group'},
      'Resource Group': {'icon': 'group--resource', 'color': Colors.lines["security"], 'fill': Colors.fills["none"], 'staticicon': 'Resource Group', 'catalogicon': '**Resource Group'},
      # Note: App has icon Security Group for VPC but not in App icons in design center so using UI icon.
      'Security Group': {'icon': 'group--security', 'color': Colors.lines["security"], 'fill': Colors.fills["none"], 'staticicon': 'Security Group', 'catalogicon': '**Security Group'},
      'Availability Zone': {'icon': 'data--center', 'color': Colors.lines["location"], 'fill': Colors.fills["location"], 'staticicon': 'Zone', 'catalogicon': '**Zone'},

      # Expanded Groups
      'Expanded Virtual Server': {'icon': 'ibm-cloud--virtual-server-vpc', 'color': Colors.lines["compute"], 'fill': Colors.fills["compute"], 'staticicon': 'Virtual Server for VPC', 'catalogicon': '**Virtual Server for VPC'},
      'Expanded Power Virtual Server': {'icon': 'ibm--power-vs', 'color': Colors.lines["compute"], 'fill': Colors.fills["compute"], 'staticicon': 'Power Virtual Server', 'catalogicon': 'Power Virtual Server Virtual Machine'},
      'Expanded Classic Virtual Server': {'icon': 'ibm-cloud--virtual-server-classic', 'color': Colors.lines["compute"], 'fill': Colors.fills["compute"], 'staticicon': 'Virtual Server Classic', 'catalogicon': 'Virtual Server for Classic'},
      'Expanded Bare Metal Server': {'icon': 'ibm-cloud--bare-metal-servers-vpc', 'color': Colors.lines["compute"], 'fill': Colors.fills["compute"], 'staticicon': 'Bare Metal for VPC', 'catalogicon': 'Bare Metal Server for VPC'},
      'Expanded Classic Bare Metal Server': {'icon': 'ibm-cloud--bare-metal-server', 'color': Colors.lines["compute"], 'fill': Colors.fills["compute"], 'staticicon': 'Bare Metal Server', 'catalogicon': 'Bare Metal Server for Classic'},
      'Expanded Application': {'icon': 'application', 'color': Colors.lines["applications"], 'fill': Colors.fills["applications"], 'staticicon': 'Application', 'catalogicon': 'Undefined Node'},
      'Expanded Microservice': {'icon': 'microservices--1', 'color': Colors.lines["applications"], 'fill': Colors.fills["compute"], 'staticicon': 'Undefined Node', 'catalogicon': 'Undefined Node'},

       # Actors
      'User': {'icon': 'user', 'color': Colors.lines["user"], 'fill': Colors.lines["user"], 'staticicon': 'User', 'catalogicon': '*User'},
      'Users': {'icon': 'group', 'color': Colors.lines["user"], 'fill': Colors.lines["user"], 'staticicon': 'Group', 'catalogicon': '*Group'},
      'Enterprise': {'icon': 'enterprise', 'color': Colors.lines["user"], 'fill': Colors.lines["user"], 'fill': Colors.lines["compute"], 'staticicon': 'Enterprise', 'catalogicon': '*Enterprise'},
      'Application': {'icon': 'application', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Application', 'catalogicon': '*Application'},
      'Web Application': {'icon': 'application--web', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Web Application', 'catalogicon': '*Web Application'},
      'Microservice': {'icon': 'microservices--1', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Microservices', 'catalogicon': '*Undefined Actor'},

       # AI
      'watsonx': {'icon': 'watsonx', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watsonx', 'catalogicon': 'Undefined Node'},
      'watsonx.ai': {'icon': 'watsonx-ai', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watsonx AI', 'catalogicon': 'Undefined Node'},
      'watsonx.data': {'icon': 'watsonx-data', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watsonx Data', 'catalogicon': 'watsonx.data'},
      'watsonx.governance': {'icon': 'watsonx-governance', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watsonx Governance', 'catalogicon': 'watsonx.governance'},
      'watsonx Orchestrate': {'icon': 'ibm-watsonx--orchestrate', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watsonx Orchestrate', 'catalogicon': 'Undefined Node'},
      'watsonx Assistant': {'icon': 'ibm-watsonx--assistant', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watsonx  Assistant', 'catalogicon': 'watsonx Assistant'},
      'watsonx Code Assistant': {'icon': 'ibm-watsonx--code-assistant', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watsonx Code  Assistant', 'catalogicon': 'watsonx Code Assistant'},
      'watsonx Z Code Assistant': {'icon': 'ibm-watsonx--code-assistant-for-z', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watsonx  Code  Assistant for Z', 'catalogicon': 'Undefined Node'},
      'watsonx Z Refactor Code Assistant': {'icon': 'ibm-watsonx--code-assistant-for-z--refactor', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watsonx Code Assistant for Z Refactor', 'catalogicon': 'Undefined Node'},
      'Watson Discovery': {'icon': 'ibm-watson--discovery', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watson Discovery', 'catalogicon': 'Watson Discovery'},
      'Watson Machine Learning': {'icon': 'ibm-watson--machine-learning', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watsonx Machine Learning', 'catalogicon': 'Watson Machine Learning'},
      'Watson Studio': {'icon': 'ibm-watson--studio', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"], 'staticicon': 'Watson Studio', 'catalogicon': 'Watson Studio'},

       # Compute
      'Virtual Server': {'icon': 'ibm-cloud--virtual-server-vpc', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Virtual Server for VPC', 'catalogicon': 'Virtual Server for VPC'},
      # Note: Need to correct static icon name.
      'Power Virtual Server': {'icon': 'ibm--power-vs', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Power Virtual Server', 'catalogicon': 'Power Virtual Server Virtual Machine'},
      'Classic Virtual Server': {'icon': 'ibm-cloud--virtual-server-classic', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Virtual Server Classic', 'catalogicon': 'Virtual Server for Classic'},
      'Bare Metal Server': {'icon': 'ibm-cloud--bare-metal-servers-vpc', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Bare Metal for VPC', 'catalogicon': 'Bare Metal Server for VPC'},
      'Classic Bare Metal Server': {'icon': 'ibm-cloud--bare-metal-server', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Bare Metal Server', 'catalogicon': 'Bare Metal Server for Classic'},
      'Dedicated Host': {'icon': 'ibm-cloud--dedicated-host', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Dedicated Host', 'catalogicon': 'Dedicated Host for VPC'},
      'Image Service': {'icon': 'image-service', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Image Service', 'catalogicon': 'Undefined Node'},
      'Satellite': {'icon': 'cloud-satellite', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Satellite', 'catalogicon': 'Undefined Node'},

      # Containers
      'OpenShift': {'icon': 'logo--openshift', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'OpenShift', 'catalogicon': 'Undefined Node'},
      'Kubernetes Service': {'icon': 'ibm-cloud--kubernetes-service', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Kubernetes', 'catalogicon': 'Undefined Node'},
      'Z Containers': {'icon': 'ibm-z-os--containers', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Undefined Node', 'catalogicon': 'Undefined Node'},
      'Container Registry': {'icon': 'cloud-registry', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'staticicon': 'Container Registry', 'catalogicon': 'Undefined Node'},

      # Data
      'Db2': {'icon': 'ibm--db2', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'DB2 Database', 'catalogicon': 'Db2'},
      'Db2 Warehouse': {'icon': 'ibm--db2-warehouse', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'DB2 Warehouse', 'catalogicon': 'Db2 Warehouse'},
      'Cloudant': {'icon': 'ibm--cloudant', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'Cloudant Database', 'catalogicon': 'Cloudant'},
      'DataStax': {'icon': 'database--datastax', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'DataStax Database', 'catalogicon': 'Undefined Node'},
      'Elasticsearch': {'icon': 'database--elastic', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'Elasticsearch Database', 'catalogicon': 'Undefined Node'},
      'EnterpriseDB': {'icon': 'database--enterprisedb', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'EDB Database', 'catalogicon': 'Undefined Node'},
      'etcd': {'icon': 'database--etcd', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'etcd Database', 'catalogicon': 'Undefined Node'},
      'MongoDB': {'icon': 'database--mongodb', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'Mongo Database', 'catalogicon': 'Undefined Node'},
      'MySQL': {'icon': 'database--mysql', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'MySQL Database', 'catalogicon': 'Databases for MySQL'},
      'PostgreSQL': {'icon': 'database--postgresql', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'PostgreSQL Database', 'catalogicon': 'Undefined Node'},
      'Rabbit': {'icon': 'database--rabbit', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'Rabbit Database', 'catalogicon': 'Undefined Node'},
      'Redis': {'icon': 'database--redis', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'Redis Database', 'catalogicon': 'Undefined Node'},
      'Database': {'icon': 'data--base', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'Database', 'catalogicon': 'Undefined Node'},
      'Event Streams': {'icon': 'ibm-cloud--event-streams', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'Undefined Node', 'catalogicon': 'Undefined Node'},
      'Data Pak': {'icon': 'ibm-cloud-pak--data', 'color': Colors.lines["data"], 'fill': Colors.lines["data"], 'staticicon': 'Cloud Pak for Data', 'catalogicon': 'Undefined Node'},

      # DevOps
      'Continuous Delivery': {'icon': 'ibm-cloud--continuous-delivery', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"], 'staticicon': 'Continuous Delivery', 'catalogicon': 'Undefined Node'},
      'Continuous Integration': {'icon': 'continuous-integration', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"], 'staticicon': 'Continuous Integration', 'catalogicon': 'Undefined Node'},
      'Source Code Repository': {'icon': 'repo--source-code', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"], 'staticicon': 'Source Code Repo', 'catalogicon': 'Undefined Node'},
      'Toolchain': {'icon': 'ibm--toolchain', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"], 'staticicon': 'Toolchain', 'catalogicon': 'Undefined Node'},
      'MQ': {'icon': 'ibm--mq', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"], 'staticicon': 'Toolchain', 'catalogicon': 'MQ'},
      'Ansible': {'icon': 'logo--ansible-community', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"], 'staticicon': 'Ansible', 'catalogicon': 'Undefined Node'},
      'GitLab': {'icon': 'logo--gitlab', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"], 'staticicon': 'GitLabe', 'catalogicon': 'Undefined Node'},
      'Integration Pak': {'icon': 'ibm-cloud-pak--integration', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"], 'staticicon': 'Cloud Pak for Integration', 'catalogicon': 'Undefined Node'},

      # Network
      'Load Balancer': {'icon': 'load-balancer--vpc', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'VPC Load Balancer', 'catalogicon': 'Load Balancer for VPC'},
      'Application Load Balancer': {'icon': 'load-balancer--application', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Application Load Balancer', 'catalogicon': '*Application Load Balancer'},
      'Network Load Balancer': {'icon': 'load-balancer--network', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Network Load Balancer', 'catalogicon': '*Network Load Balancer'},
      'Global Load Balancer': {'icon': 'load-balancer--global', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Global Load Balancer', 'catalogicon': '*Global Load Balancer'},
      'Classic Load Balancer': {'icon': 'load-balancer--classic', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Classic Load Balancer', 'catalogicon': '*Cloud Load Balancer'},
      'Floating IP': {'icon': 'floating-ip', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Floating IP', 'catalogicon': '**Floating IP'},
      'Network Interface': {'icon': 'network-interface', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Network Interface', 'catalogicon': 'Undefined Node'},
      'Endpoint Gateway': {'icon': 'ibm-cloud--vpc-endpoints', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'VPC Endpoints', 'catalogicon': 'Virtual Private Endpoint for VPC'},
      'Public Gateway': {'icon': 'gateway--public', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Public Gateway', 'catalogicon': 'Public Gateway'},
      'Transit Gateway': {'icon': 'ibm-cloud--transit-gateway', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Transit Gateway', 'catalogicon': 'Transit Gateway'},
      'Direct Link Connect': {'icon': 'ibm-cloud--direct-link-2--connect', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Direct Link Connect', 'catalogicon': 'Direct Link Connect'},
      'Direct Link Dedicated': {'icon': 'ibm-cloud--direct-link-2--dedicated', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Direct Link Dedicated', 'catalogicon': 'Direct Link Dedicated'},
      'DNS Services': {'icon': 'dns-services', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'DNS', 'catalogicon': 'Undefined Node'},
      'Internet Services': {'icon': 'ibm-cloud--internet-services', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Internet Services', 'catalogicon': 'Undefined Node'},
      'Internet': {'icon': 'wikis', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Internet', 'catalogicon': 'Undefined Node'},
      # Note: NTP in process of being added to design center.
      'NTP': {'icon': 'undefined', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Undefined Node', 'catalogicon': 'Undefined Node'},
      'Bridge': {'icon': 'arrows--horizontal', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Undefined Node', 'catalogicon': 'Undefined Node'},
      'Router': {'icon': 'router', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Router', 'catalogicon': 'Undefined Node'},
      'VLAN': {'icon': 'vlan', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'VLAN', 'catalogicon': 'Undefined Node'},
      'Classic VLAN': {'icon': 'vlan--ibm', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'IBM Classic VLAN', 'catalogicon': 'Undefined Node'},
      'Proxy Server': {'icon': 'server--proxy', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Proxy Server', 'catalogicon': 'Undefined Node'},
      'L2 Switch': {'icon': 'switch-layer-2', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'L2 Switch', 'catalogicon': 'Undefined Node'},
      'L3 Switch': {'icon': 'switch-layer-3', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'L3 Switch', 'catalogicon': 'Undefined Node'},

      # Observability
      'Cloud Logs': {'icon': 'ibm-cloud--logging', 'color': Colors.lines["management"], 'fill': Colors.lines["management"], 'staticicon': 'Cloud logs', 'catalogicon': 'Cloud Activity Tracker'},
      'Flow Logs': {'icon': 'flow-logs-vpc', 'color': Colors.lines["management"], 'fill': Colors.lines["management"], 'staticicon': 'Flow Logs', 'catalogicon': 'Flow Logs for VPC'},
      'Monitoring': {'icon': 'cloud--monitoring', 'color': Colors.lines["management"], 'fill': Colors.lines["management"], 'staticicon': 'Monitoring', 'catalogicon': 'Cloud Monitoring'},

      # Security
      'App ID': {'icon': 'ibm-cloud--app-id', 'color': Colors.lines["security"], 'fill': Colors.lines["security"], 'staticicon': 'Undefined Node', 'catalogicon': 'Undefined Node'},
      'Key Protect': {'icon': 'ibm-cloud--key-protect', 'color': Colors.lines["security"], 'fill': Colors.lines["security"], 'staticicon': 'Key Protect', 'catalogicon': 'Key Protect'},
      'Secrets Manager': {'icon': 'ibm-cloud--secrets-manager', 'color': Colors.lines["security"], 'fill': Colors.lines["security"], 'staticicon': 'Secrets Manager', 'catalogicon': 'Undefined Node'},
      'Security Complance Center': {'icon': 'ibm-cloud--security-compliance-center', 'color': Colors.lines["security"], 'fill': Colors.lines["security"], 'staticicon': 'Undefined Node', 'catalogicon': 'Undefined Node'},
      'SSH Key': {'icon': 'password', 'color': Colors.lines["network"], 'fill': Colors.lines["security"], 'staticicon': 'Key', 'catalogicon': 'SSH Key for VPC'},
      'VPN Gateway': {'icon': 'ibm--vpn-for-vpc', 'color': Colors.lines["security"], 'fill': Colors.lines["security"], 'staticicon': 'VPN Gateway', 'catalogicon': 'VPN for VPC'},
      'VPN Connection': {'icon': 'vpn--connection', 'color': Colors.lines["security"], 'fill': Colors.lines["security"], 'staticicon': 'VPN Connection', 'catalogicon': 'Undefined Node'},
      'Bastion Host': {'icon': 'bastion-host', 'color': Colors.lines["security"], 'fill': Colors.lines["security"], 'staticicon': 'Bastion Host', 'catalogicon': '**Bastion Host'},
      'ACL Rules': {'icon': 'subnet-acl-rules', 'color': Colors.lines["security"], 'fill': Colors.lines["security"], 'staticicon': 'Network ACL Rules', 'catalogicon': 'Undefined Node'},
      'Security Pak': {'icon': 'ibm-cloud-pak--security', 'color': Colors.lines["security"], 'fill': Colors.lines["security"], 'staticicon': 'Cloud Pak for Security', 'catalogicon': 'Undefined Node'},

      # Storage
      'Block Storage': {'icon': 'block-storage', 'color': Colors.lines["storage"], 'fill': Colors.lines["storage"], 'staticicon': 'Block  Storage Application', 'catalogicon': 'Block Storage for VPC'},
      # Note: File Storage in process of being added to design center.
      'File Storage': {'icon': 'undefined', 'color': Colors.lines["storage"], 'fill': Colors.lines["storage"], 'staticicon': 'Undefined Node', 'catalogicon': 'Undefined Node'},
      'Object Storage': {'icon': 'object-storage', 'color': Colors.lines["storage"], 'fill': Colors.lines["storage"], 'staticicon': 'Object Storage Application', 'catalogicon': 'Cloud Object Storage'},
      'Cloud Backup': {'icon': 'data-backup', 'color': Colors.lines["storage"], 'fill': Colors.lines["storage"], 'staticicon': 'Undefined Node', 'catalogicon': 'Cloud Backup for VPC'},

      # Other
      'Undefined': {'icon': 'undefined', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'staticicon': 'Undefined Node', 'catalogicon': 'Undefined Node'}
   }

   common = None
   staticicons = None
   catalogicons = None

   def __init__(self, common):
      self.common = common
      self.staticicons = StaticIcons(self.staticicons)
      self.catalogicons = CatalogIcons(self.catalogicons)

   def getIconDictionary(self):
      return self.iconDictionary

   def getIcon(self, iconusage):
      if iconusage in self.iconDictionary:
         icon = self.iconDictionary[iconusage]
         iconname = icon['icon']
         iconcolor = icon['color']
         iconfill = icon['fill']
         iconstatic = icon['staticicon']
         iconcatalog = icon['catalogicon']
      else:
         icon = self.iconDictionary['Undefined']
         iconname = icon['icon']
         iconcolor = icon['color']
         iconfill = icon['fill']
         iconstatic = icon['staticicon']
         iconcatalog = icon['catalogicon']

      return iconname, iconcolor, iconfill, iconstatic, iconcatalog

   def getStaticIcon(self, staticname):
      staticimage = self.staticicons.getIcon(staticname)
      return staticimage

   def getCatalogIcon(self, staticname):
      if staticname[0] == '*':
         if staticname[1] == '*':
            staticimage = self.staticicons.getIcon("(Group) " + staticname[2:])
         else:
            staticimage = self.staticicons.getIcon(staticname[1:])
      else:
        staticimage = self.catalogicons.getIcon(staticname)
      return staticimage

   '''
   def getIcon(self, iconusage):
      if self.common.isProviderAny():
         if iconusage in self.iconDictionary:
            icon = self.iconDictionary[iconusage]
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         elif iconusage + '-any' in selfs.iconDictionary:
            icon = selfs.iconDictionary[iconusage + '-any']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         elif iconusage + '-ibm' in self.iconDictionary:
            icon = self.iconDictionary[iconusage + '-ibm']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         else:
            icon = self.iconDictionary['Undefined']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
      else: # check prescribed
         if iconusage in self.iconDictionary:
            icon = self.iconDictionary[iconusage]
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         elif iconusage + '-ibm' in self.iconDictionary:
            icon = self.iconDictionary[iconusage + '-ibm']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         elif iconusage + '-any' in self.iconDictionary:
            icon = self.iconDictionary[iconusage + '-any']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         else:
            icon = self.iconDictionary['Undefined']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""

      #return iconname, iconcolor, iconshape, hideicon
      return iconname, iconcolor
   '''

   def validIcon(self, iconname):
      if iconname in self.iconDictionary:
         return True
      if iconname + '-any' in self.iconDictionary:
         return True
      if iconname + '-ibm' in self.iconDictionary:
         return True
      return False

