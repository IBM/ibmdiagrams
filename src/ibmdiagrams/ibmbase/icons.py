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

import pandas as pd

from .colors import Colors

class Icons:
   iconDictionary = {
      # Core Groups
      'IBM Cloud Group': {'icon': 'ibm-cloud', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'resource': 'none', 'fields': {'label': 'IBM Cloud', 'id': 'IBM Cloud Group'}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'VPC Group': {'icon': 'ibm-cloud--vpc', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'resource': 'ibm_is_vpc', 'fields': {'label': 'name', 'id': 'id', 'Region Group': 'crn[5]'}, 'direction': 'LR', 'deployedOn': 'Region Group', 'deployedTo': 'none'},
      'Subnet Group': {'icon': 'ibm-cloud--subnets', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'resource': 'ibm_is_subnet', 'fields': {'label': 'name', 'sublabel': 'ipv4_cidr_block', 'id': 'id', 'VPC Group': 'vpc', 'Availability Zone Group': 'vpc+zone'}, 'direction': 'LR', 'deployedOn': 'VPC Group', 'deployedTo': 'Availability Zone Group'},
      'Enterprise Network Group': {'icon': 'network--enterprise', 'color': Colors.lines["network"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Public Network Group': {'icon': 'network--public', 'color': Colors.lines["network"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Cloud Services Group': {'icon': 'cloud-services', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'Region Group', 'deployedTo': 'none'},
      #'VPC Services Group': {'icon': 'cloud-services', 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'VPC Group', 'deployedTo': 'none'},
      'Internet Services Group': {'icon': 'ibm-cloud--internet-services', 'color': Colors.lines["network"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Overlay Network Group': {'icon': 'network--overlay', 'color': Colors.lines["network"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Power Workspace Group': {'icon': 'ibm--power-vs', 'color': Colors.lines["network"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Z System Group': {'icon': 'z--systems', 'color': Colors.lines["network"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Internet Group': {'icon': 'wikis', 'color': Colors.lines["network"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'VLAN Group': {'icon': 'vlan', 'color': Colors.lines["network"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Classic VLAN Group': {'icon': 'vlan--ibm', 'color': Colors.lines["network"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Classic Infrastructure Group': {'icon': 'infrastructure--classic', 'color': Colors.lines["network"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'OpenShift Group': {'icon': 'logo--openshift', 'color': Colors.lines["compute"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Kubernetes Service Group': {'icon': 'ibm-cloud--kubernetes-service', 'color': Colors.lines["compute"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Z Containers Group': {'icon': 'ibm-z-os--containers', 'color': Colors.lines["compute"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx Group': {'icon': 'watsonx', 'color': Colors.lines["applications"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx Code Assistant Group': {'icon': 'ibm-watsonx--code-assistant', 'color': Colors.lines["applications"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx Z Code Assistant Group': {'icon': 'ibm-watsonx--code-assistant-for-z', 'color': Colors.lines["applications"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Authorization Boundary Group': {'icon': 'flag', 'color': Colors.lines["security"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Point of Presence Group': {'icon': 'point-of-presence', 'color': Colors.lines["location"], 'fill': Colors.fills["white"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Region Group': {'icon': 'location', 'color': Colors.lines["location"], 'fill': Colors.fills["location"],  'resource': 'local', 'fields': {}, 'direction': 'TB', 'deployedOn': 'IBM Cloud Group', 'deployedTo': 'none'},

      # Zone Groups
      'Access Group': {'icon': 'group--access', 'color': Colors.lines["security"], 'fill': Colors.fills["none"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Account Group': {'icon': 'group--account', 'color': Colors.lines["security"], 'fill': Colors.fills["none"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Instance Group': {'icon': 'autoscaling', 'color': Colors.lines["compute"], 'fill': Colors.fills["none"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Placement Group': {'icon': 'group-objects', 'color': Colors.lines["compute"], 'fill': Colors.fills["none"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Resource Group': {'icon': 'group--resource', 'color': Colors.lines["security"], 'fill': Colors.fills["none"], 'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Security Group': {'icon': 'group--security', 'color': Colors.lines["security"], 'fill': Colors.fills["none"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Availability Zone Group': {'icon': 'data--center', 'color': Colors.lines["location"], 'fill': Colors.fills["location"], 'resource': 'none', 'fields': {}, 'direction': 'TB', 'deployedOn': 'none', 'deployedTo': 'none'},

      # Expanded Groups
      'Expanded Virtual Server Group': {'icon': 'ibm-cloud--virtual-server-vpc', 'color': Colors.lines["compute"], 'fill': Colors.fills["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Expanded Power Virtual Server Group': {'icon': 'ibm--power-vs', 'color': Colors.lines["compute"], 'fill': Colors.fills["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Expanded Classic Virtual Server Group': {'icon': 'ibm-cloud--virtual-server-classic', 'color': Colors.lines["compute"], 'fill': Colors.fills["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Expanded Bare Metal Server Group': {'icon': 'ibm-cloud--bare-metal-servers-vpc', 'color': Colors.lines["compute"], 'fill': Colors.fills["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Expanded Classic Bare Metal Server Group': {'icon': 'ibm-cloud--bare-metal-server', 'color': Colors.lines["compute"], 'fill': Colors.fills["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Expanded Application Group': {'icon': 'application', 'color': Colors.lines["applications"], 'fill': Colors.fills["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Expanded Microservice Group': {'icon': 'microservices--1', 'color': Colors.lines["applications"], 'fill': Colors.fills["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

       # Actors
      'User Icon': {'icon': 'user', 'color': Colors.lines["user"], 'fill': Colors.lines["user"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Users Icon': {'icon': 'group', 'color': Colors.lines["user"], 'fill': Colors.lines["user"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Enterprise Icon': {'icon': 'enterprise', 'color': Colors.lines["user"], 'fill': Colors.lines["user"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Application Icon': {'icon': 'application', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Web Application Icon': {'icon': 'application--web', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Microservice Icon': {'icon': 'microservices--1', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

       # AI
      'watsonx Icon': {'icon': 'watsonx', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx.ai Icon': {'icon': 'watsonx-ai', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx.data Icon': {'icon': 'watsonx-data', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx.governance Icon': {'icon': 'watsonx-governance', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx Orchestrate Icon': {'icon': 'ibm-watsonx--orchestrate', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx Assistant Icon': {'icon': 'ibm-watsonx--assistant', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx Code Assistant Icon': {'icon': 'ibm-watsonx--code-assistant', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx Z Code Assistant Icon': {'icon': 'ibm-watsonx--code-assistant-for-z', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'watsonx Z Refactor Code Assistant Icon': {'icon': 'ibm-watsonx--code-assistant-for-z--refactor', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Watson Discovery Icon': {'icon': 'ibm-watson--discovery', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Watson Machine Learning Icon': {'icon': 'ibm-watson--machine-learning', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Watson Studio Icon': {'icon': 'ibm-watson--studio', 'color': Colors.lines["applications"], 'fill': Colors.lines["applications"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

       # Compute
      'Virtual Server Icon': {'icon': 'ibm-cloud--virtual-server-vpc', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'resource': 'ibm_is_instance', 'fields': 
{'label': 'name', 'sublabel': 'primary_network_interface:primary_ip:address', 'id': 'id', 'Subnet Group': 'primary_network_interface:subnet', 'Availability Zone Group': 'vpc+zone', 'VPC Group': 'vpc'}, 'direction': 'LR', 'deployedOn': 'Subnet Group', 'deployedTo': 'none'},
      'Power Virtual Server Icon': {'icon': 'ibm--power-vs', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Classic Virtual Server Icon': {'icon': 'ibm-cloud--virtual-server-classic', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Bare Metal Server Icon': {'icon': 'ibm-cloud--bare-metal-servers-vpc', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"], 'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Classic Bare Metal Server Icon': {'icon': 'ibm-cloud--bare-metal-server', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Dedicated Host Icon': {'icon': 'ibm-cloud--dedicated-host', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Image Service Icon': {'icon': 'image-service', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Satellite Icon': {'icon': 'cloud-satellite', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

      # Containers
      'OpenShift Icon': {'icon': 'logo--openshift', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Kubernetes Service Icon': {'icon': 'ibm-cloud--kubernetes-service', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Z Containers Icon': {'icon': 'ibm-z-os--containers', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Container Registry Icon': {'icon': 'cloud-registry', 'color': Colors.lines["compute"], 'fill': Colors.lines["compute"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

      # Data
      'Db2 Icon': {'icon': 'ibm--db2', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Db2 Warehouse Icon': {'icon': 'ibm--db2-warehouse', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Cloudant Icon': {'icon': 'ibm--cloudant', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'DataStax Icon': {'icon': 'database--datastax', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Elasticsearch Icon': {'icon': 'database--elastic', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      # Note: EnterpriseEB is fully deprecated as of 10/15/25.
      #'EnterpriseDB Icon': {'icon': 'database--enterprisedb', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      # Note: etcd is fully deprecated as of 10/15/25.
      #'etcd Icon': {'icon': 'database--etcd', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'MongoDB Icon': {'icon': 'database--mongodb', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'MySQL Icon': {'icon': 'database--mysql', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'PostgreSQL Icon': {'icon': 'database--postgresql', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Rabbit Icon': {'icon': 'database--rabbit', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Redis Icon': {'icon': 'database--redis', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Database Icon': {'icon': 'data--base', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Event Streams Icon': {'icon': 'ibm-cloud--event-streams', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Data Pak Icon': {'icon': 'ibm-cloud-pak--data', 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

      # DevOps
      'Continuous Delivery Icon': {'icon': 'ibm-cloud--continuous-delivery', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Continuous Integration Icon': {'icon': 'continuous-integration', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Source Code Repository Icon': {'icon': 'repo--source-code', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Toolchain Icon': {'icon': 'ibm--toolchain', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'MQ Icon': {'icon': 'ibm--mq', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Ansible Icon': {'icon': 'logo--ansible-community', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'GitLab Icon': {'icon': 'logo--gitlab', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Integration Pak Icon': {'icon': 'ibm-cloud-pak--integration', 'color': Colors.lines["devops"], 'fill': Colors.lines["devops"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

      # Network
      'Load Balancer Icon': {'icon': 'load-balancer--vpc', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Application Load Balancer Icon': {'icon': 'load-balancer--application', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Network Load Balancer Icon': {'icon': 'load-balancer--network', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Global Load Balancer Icon': {'icon': 'load-balancer--global', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Classic Load Balancer Icon': {'icon': 'load-balancer--classic', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Floating IP Icon': {'icon': 'floating-ip', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Network Interface Icon': {'icon': 'network-interface', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      #'Endpoint Gateway Icon': {'icon': 'ibm-cloud--vpc-endpoints', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'resource': 'ibm_is_virtual_endpoint_gateway', 'fields': {'label': 'name', 'id': 'id', 'VPC Services Group': '@services+vpc'}, 'direction': 'LR', 'deployedOn': 'VPC Services Group', 'deployedTo': 'none'},
      'Endpoint Gateway Icon': {'icon': 'ibm-cloud--vpc-endpoints', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'resource': 'ibm_is_virtual_endpoint_gateway', 'fields': {'label': 'name', 'sublabel': 'address', 'id': 'id', 'Subnet Group': 'subnet'}, 'direction': 'LR', 'deployedOn': 'Subnet Group', 'deployedTo': 'none'},
      'Public Gateway Icon': {'icon': 'gateway--public', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Transit Gateway Icon': {'icon': 'ibm-cloud--transit-gateway', 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'resource': 'ibm_tg_gateway', 'fields': {'label': 'name', 'id': 'id', 'Cloud Services Group': '@services+location'}, 'direction': 'LR', 'deployedOn': 'Cloud Services Group', 'deployedTo': 'none'},
      'Direct Link Connect Icon': {'icon': 'ibm-cloud--direct-link-2--connect', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Direct Link Dedicated Icon': {'icon': 'ibm-cloud--direct-link-2--dedicated', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'DNS Services Icon': {'icon': 'dns-services', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Internet Services Icon': {'icon': 'ibm-cloud--internet-services', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Internet Icon': {'icon': 'wikis', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      # Note: NTP in process of being added to design center.
      'NTP Icon': {'icon': 'undefined', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Bridge Icon': {'icon': 'arrows--horizontal', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Router Icon': {'icon': 'router', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'VLAN Icon': {'icon': 'vlan', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Classic VLAN Icon': {'icon': 'vlan--ibm', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Proxy Server Icon': {'icon': 'server--proxy', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'L2 Switch Icon': {'icon': 'switch-layer-2', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'L3 Switch Icon': {'icon': 'switch-layer-3', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

      # Observability
      # Note: Activity Tracker is deprecated, replaced with Cloud Logs.
      'Cloud Logs Icon': {'icon': 'ibm-cloud--logging', 'color': Colors.lines["management"], 'fill': Colors.lines["management"], 'resource': 'ibm_atracker_target', 'fields': {'label': 'name', 'id': 'id', 'Cloud Services Group': '@services+crn[5]'}, 'direction': 'LR', 'deployedOn': 'Cloud Services Group', 'deployedTo': 'none'},
      #'Flow Logs Icon': {'icon': 'flow-logs-vpc', 'color': Colors.lines["management"], 'fill': Colors.lines["management"], 'resource': 'ibm_is_flow_log', 'fields': {'label': 'name', 'id': 'id', 'VPC Services Group': '@services+vpc'}, 'direction': 'LR', 'deployedOn': 'VPC Services Group', 'deployedTo': 'none'},
      'Flow Logs Icon': {'icon': 'flow-logs-vpc', 'color': Colors.lines["management"], 'fill': Colors.lines["management"], 'resource': 'ibm_is_flow_log', 'fields': {'label': 'name', 'id': 'id', 'Cloud Services Group': '@services+crn[5]'}, 'direction': 'LR', 'deployedOn': 'Cloud Services Group', 'deployedTo': 'none'},
      'Monitoring Icon': {'icon': 'cloud--monitoring', 'color': Colors.lines["management"], 'fill': Colors.lines["management"], 'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

      # Security
      'App ID Icon': {'icon': 'ibm-cloud--app-id', 'color': Colors.lines["security"], 'fill': Colors.lines["security"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Key Protect Icon': {'icon': 'ibm-cloud--key-protect', 'color': Colors.lines["security"], 'fill': Colors.lines["security"], 'resource': 'ibm_kms_key', 'fields': {'label': 'key_name', 'id': 'id', 'Cloud Services Group': '@services+crn[5]'}, 'direction': 'LR', 'deployedOn': 'Cloud Services Group', 'deployedTo': 'none'},
      'Secrets Manager Icon': {'icon': 'ibm-cloud--secrets-manager', 'color': Colors.lines["security"], 'fill': Colors.lines["security"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Security Complance Center Icon': {'icon': 'ibm-cloud--security-compliance-center', 'color': Colors.lines["security"], 'fill': Colors.lines["security"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'SSH Key Icon': {'icon': 'password', 'color': Colors.lines["network"], 'fill': Colors.lines["security"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'VPN Gateway Icon': {'icon': 'ibm--vpn-for-vpc', 'color': Colors.lines["security"], 'fill': Colors.lines["security"],  'resource': 'ibm_is_vpn_gateway', 'fields': {'label': 'name', 'sublabel': 'public_ip_address', 'id': 'id', 'Subnet Group': 'subnet'}, 'direction': 'LR', 'deployedOn': 'Subnet Group', 'deployedTo': 'none'},
      # TODO Add private_ip_address to sublabel of VPN Connection Icon.
      'VPN Connection Icon': {'icon': 'vpn--connection', 'color': Colors.lines["security"], 'fill': Colors.lines["security"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Bastion Host Icon': {'icon': 'bastion-host', 'color': Colors.lines["security"], 'fill': Colors.lines["security"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'ACL Rules Icon': {'icon': 'subnet-acl-rules', 'color': Colors.lines["security"], 'fill': Colors.lines["security"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Security Pak Icon': {'icon': 'ibm-cloud-pak--security', 'color': Colors.lines["security"], 'fill': Colors.lines["security"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

      # Storage
      'Block Storage Icon': {'icon': 'block-storage', 'color': Colors.lines["storage"], 'fill': Colors.lines["storage"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      # Note: File Storage in process of being added to design center.
      'File Storage Icon': {'icon': 'undefined', 'color': Colors.lines["storage"], 'fill': Colors.lines["storage"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
      'Object Storage Icon': {'icon': 'object-storage', 'color': Colors.lines["storage"], 'fill': Colors.lines["storage"], 'resource': 'ibm_cos_bucket', 'fields': {'label': 'bucket_name', 'id': 'id', 'Cloud Services Group': '@services+region_location'}, 'direction': 'LR', 'deployedOn': 'Cloud Services Group', 'deployedTo': 'none'},
      ' Cloud Backup Icon': {'icon': 'data-backup', 'color': Colors.lines["storage"], 'fill': Colors.lines["storage"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},

      # Other
      'Undefined Icon': {'icon': 'undefined', 'color': Colors.lines["network"], 'fill': Colors.lines["network"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'}
   }

   common = None

   def __init__(self, common):
      self.common = common

   def getIconDictionary(self):
      return self.iconDictionary

   def getIcon(self, iconusage):
      if iconusage in self.iconDictionary:
         icon = self.iconDictionary[iconusage]
         iconname = icon['icon']
         iconcolor = icon['color']
         iconfill = icon['fill']
      else:
         icon = self.iconDictionary['Undefined Icon']
         iconname = icon['icon']
         iconcolor = icon['color']
         iconfill = icon['fill']

      return iconname, iconcolor, iconfill

   def getResourceIcon(self, iconusage):
      if iconusage in self.iconDictionary:
         icon = self.iconDictionary[iconusage]
      else:
         icon = self.iconDictionary['Undefined Icon']

      return icon

   def validIcon(self, iconname):
      if iconname in self.iconDictionary:
         return True
      else:
         return False

   def printIcons(self):
      for entry in self.iconDictionary:
         icon = self.iconDictionary[entry]
         print(icon)

   def mapResources(self, resources):
      for entry in self.iconDictionary:
         icon = self.iconDictionary[entry]

         resource = icon['resource']
         if resource == 'none' or resource == 'local':
            continue

         resource = resources.getResource(resource)
         if resource.empty:
            continue
            
         fields = icon['fields']
         lists = []

         # Field Options:
         #   a. "name1:name2:nameN" to drill down into substructures 
         #   b. "name1+name2+nameN" to concatenate names 
         #   c. "@name" to leave name as is 
         #   d. "name[d]" to retrieve array index d starting at 0 where d is 0 to 9

         for index, row in resource.iterrows():
            list = {}
            for newname, oldname in fields.items():
               if oldname.find(":") > -1:
                  templist = oldname.split(":")
                  tempdata = row[templist[0]]
                  if len(templist) == 1:
                     element = tempdata
                  else:
                     tempindex = 1
                     while tempindex < len(templist): 
                        tempdata = tempdata[0]
                        tempdata = tempdata[templist[tempindex]]
                        tempindex += 1
               else:
                  if oldname.find("+") > -1:
                     templist = oldname.split("+")
                  else:
                     templist = [oldname]

                  tempindex = 0
                  tempstring = ""

                  while tempindex < len(templist): 
                     tempvalue = templist[tempindex]
                     if tempvalue.find("[") > -1:
                        temploc = tempvalue.find("[")
                        tempindex = int(tempvalue[temploc+1])
                        tempname = tempvalue[:temploc]
                        temprow = row[tempname]
                        temparray = temprow.split(':')
                        tempvalue = temparray[tempindex]
                        tempstring = tempstring + tempvalue
                     elif tempvalue[0] == '@':
                        tempname = tempvalue[1:]
                        tempstring = tempstring + tempname
                     else:
                        tempname = row[tempvalue]
                        tempstring = tempstring + tempname
                     tempindex += 1

                  tempdata = tempstring

               list[newname] = tempdata

            lists.append(list)

         df = pd.DataFrame(lists)
         icon['data'] = df 

      self.addClouds()
      self.addRegions()
      self.addZones()
      self.addCloudServices()
      #self.addVPCServices()

      return True

   def addClouds(self):
      data = [{'label': 'IBM Cloud', 'id': 'IBM Cloud Group'}]

      icon = self.iconDictionary['IBM Cloud Group']
      df = pd.DataFrame(data)
      icon['data'] = df 

      return

   def addRegions(self):
      data = [
          {'label': 'Sydney',        'id': 'au-syd',   'IBM Cloud Group': 'IBM Cloud Group'},  
          {'label': 'Sao Paulo',     'id': 'br-sao',   'IBM Cloud Group': 'IBM Cloud Group'},  
          {'label': 'Toronto',       'id': 'ca-tor',   'IBM Cloud Group': 'IBM Cloud Group'},  
          {'label': 'Frankfurt',     'id': 'eu-de',    'IBM Cloud Group': 'IBM Cloud Group'},  
          {'label': 'London',        'id': 'eu-gb',    'IBM Cloud Group': 'IBM Cloud Group'},  
          {'label': 'Osaka',         'id': 'jp-osa',   'IBM Cloud Group': 'IBM Cloud Group'},  
          {'label': 'Tokyo',         'id': 'jp-tok',   'IBM Cloud Group': 'IBM Cloud Group'},  
          {'label': 'Washington DC', 'id': 'us-east',  'IBM Cloud Group': 'IBM Cloud Group'},  
          {'label': 'Dallas',        'id': 'us-south', 'IBM Cloud Group': 'IBM Cloud Group'}  
        ]

      icon = self.iconDictionary['Region Group']
      df = pd.DataFrame(data)
      icon['data'] = df 

      return

   def addZones(self):
      data = [
          {'label': 'Zone 1', 'sublabel': '10.245.0.0/18',   'id': 'au-syd-1'},
          {'label': 'Zone 2', 'sublabel': '10.245.64.0/18',  'id': 'au-syd-2'}, 
          {'label': 'Zone 3', 'sublabel': '10.245.128.0/18', 'id': 'au-syd-3'},

          {'label': 'Zone 1', 'sublabel': '10.250.0.0/18',   'id': 'br-sao-1'},
          {'label': 'Zone 2', 'sublabel': '10.250.64.0/18',  'id': 'br-sao-2'}, 
          {'label': 'Zone 3', 'sublabel': '10.250.128.0/18', 'id': 'br-sao-3'},

          {'label': 'Zone 1', 'sublabel': '10.249.0.0/18',   'id': 'ca-tor-1'},
          {'label': 'Zone 2', 'sublabel': '10.249.64.0/18',  'id': 'ca-tor-2'}, 
          {'label': 'Zone 3', 'sublabel': '10.249.128.0/18', 'id': 'ca-tor-3'},

          {'label': 'Zone 1', 'sublabel': '10.243.0.0/18',   'id': 'eu-de-1'},
          {'label': 'Zone 2', 'sublabel': '10.243.64.0/18',  'id': 'eu-de-2'}, 
          {'label': 'Zone 3', 'sublabel': '10.243.128.0/18', 'id': 'eu-de-3'},

          {'label': 'Zone 1', 'sublabel': '10.242.0.0/18',   'id': 'eu-gb-1'},
          {'label': 'Zone 2', 'sublabel': '10.242.64.0/18',  'id': 'eu-gb-2'}, 
          {'label': 'Zone 3', 'sublabel': '10.242.128.0/18', 'id': 'eu-gb-3'},

          {'label': 'Zone 1', 'sublabel': '10.248.0.0/18',   'id': 'jp-osa-1'},
          {'label': 'Zone 2', 'sublabel': '10.248.64.0/18',  'id': 'jp-osa-2'}, 
          {'label': 'Zone 3', 'sublabel': '10.248.128.0/18', 'id': 'jp-osa-3'},

          {'label': 'Zone 1', 'sublabel': '10.244.0.0/18',   'id': 'jp-tok-1'},
          {'label': 'Zone 2', 'sublabel': '10.244.64.0/18',  'id': 'jp-tok-2'}, 
          {'label': 'Zone 3', 'sublabel': '10.244.128.0/18', 'id': 'jp-tok 3'},

          {'label': 'Zone 1', 'sublabel': '10.241.0.0/18',   'id': 'us-east-1'},
          {'label': 'Zone 2', 'sublabel': '10.241.64.0/18',  'id': 'us-east-2'}, 
          {'label': 'Zone 3', 'sublabel': '10.241.128.0/18', 'id': 'us-east-3'},

          {'label': 'Zone 1', 'sublabel': '10.240.0.0/18',   'id': 'us-south-1'},
          {'label': 'Zone 2', 'sublabel': '10.240.64.0/18',  'id': 'us-south-2'}, 
          {'label': 'Zone 3', 'sublabel': '10.240.128.0/18', 'id': 'us-south-3'}
        ]

      vpcIcon = self.getResourceIcon('VPC Group')
      vpcData = vpcIcon['data']
      zoneData = []

      for vpcKey, vpcRow in vpcData.iterrows():
         vpcID = vpcRow['id']
         for zoneRow in data:
            newRow = zoneRow.copy()
            #newRow["id"] = vpcID + "-" + newRow["id"]
            newRow["id"] = vpcID + newRow["id"]
            zoneData.append(newRow)

      icon = self.iconDictionary['Availability Zone Group']
      df = pd.DataFrame(zoneData)
      icon['data'] = df 

      return

   def addCloudServices(self):
      data = [
          {'label': 'Cloud Services', 'id': 'servicesau-syd',   'Region Group': 'au-syd',   'Cloud Services Group': 'Cloud Services Group'},  
          {'label': 'Cloud Services', 'id': 'servicesbr-sao',   'Region Group': 'br-sao',   'Cloud Services Group': 'Cloud Services Group'},  
          {'label': 'Cloud Services', 'id': 'servicesca-tor',   'Region Group': 'ca-tor',   'Cloud Services Group': 'Cloud Services Group'},  
          {'label': 'Cloud Services', 'id': 'serviceseu-de',    'Region Group': 'eu-de',    'Cloud Services Group': 'Cloud Services Group'},  
          {'label': 'Cloud Services', 'id': 'serviceseu-gb',    'Region Group': 'eu-gb',    'Cloud Services Group': 'Cloud Services Group'},  
          {'label': 'Cloud Services', 'id': 'servicesjp-osa',   'Region Group': 'jp-osa',   'Cloud Services Group': 'Cloud Services Group'},  
          {'label': 'Cloud Services', 'id': 'servicesjp-tok',   'Region Group': 'jp-tok',   'Cloud Services Group': 'Cloud Services Group'},  
          {'label': 'Cloud Services', 'id': 'servicesus-east',  'Region Group': 'us-east',  'Cloud Services Group': 'Cloud Services Group'},  
          {'label': 'Cloud Services', 'id': 'servicesus-south', 'Region Group': 'us-south', 'Cloud Services Group': 'Cloud Services Group'}  
        ]

      icon = self.iconDictionary['Cloud Services Group']
      df = pd.DataFrame(data)
      icon['data'] = df 

      return

   '''
   def addVPCServices(self):
      vpcIcon = self.getResourceIcon('VPC Group')
      vpcData = vpcIcon['data']
      data = []

      for vpcKey, vpcRow in vpcData.iterrows():
         vpcID = vpcRow['id']
         data.append({'label': 'VPC Services', 'id': 'services' + '-' + vpcID, 'VPC Group': vpcID, 'VPC Services Group': 'VPC Services Group'})

      icon = self.iconDictionary['VPC Services Group']
      df = pd.DataFrame(data)
      icon['data'] = df 

      return
   '''
