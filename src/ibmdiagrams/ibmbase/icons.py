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

import logging

import pandas as pd

from .colors import Colors

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class Icons:
    iconDictionary = {
        # Core Groups
        "IBM Cloud Group": {
            "icon": "ibm-cloud",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {"label": "IBM Cloud", "id": "IBM Cloud Group"},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "VPC Group": {
            "icon": "ibm-cloud--vpc",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "ibm_is_vpc",
            "fields": {"label": "name", "id": "id", "Region Group": "crn[5]"},
            "direction": "LR",
            "deployedOn": "Region Group",
            "deployedTo": "none",
        },
        "Subnet Group": {
            "icon": "ibm-cloud--subnets",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "ibm_is_subnet",
            "fields": {
                "label": "name",
                "sublabel": "ipv4_cidr_block",
                "id": "id",
                "VPC Group": "vpc",
                "Availability Zone Group": "vpc+zone",
            },
            "direction": "LR",
            "deployedOn": "VPC Group",
            "deployedTo": "Availability Zone Group",
        },
        "Enterprise Network Group": {
            "icon": "network--enterprise",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Public Network Group": {
            "icon": "network--public",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Cloud Services Group": {
            "icon": "cloud-services",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "Region Group",
            "deployedTo": "none",
        },
        #'VPC Services Group': {'icon': 'cloud-services', 'custom_icon': None, 'color': Colors.lines["network"], 'fill': Colors.fills["white"], 'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'VPC Group', 'deployedTo': 'none'},
        "Internet Services Group": {
            "icon": "ibm-cloud--internet-services",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Overlay Network Group": {
            "icon": "network--overlay",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Power Workspace Group": {
            "icon": "ibm--power-vs",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Z System Group": {
            "icon": "z--systems",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Internet Group": {
            "icon": "wikis",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "VLAN Group": {
            "icon": "vlan",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Classic VLAN Group": {
            "icon": "vlan--ibm",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Classic Infrastructure Group": {
            "icon": "infrastructure--classic",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "OpenShift Group": {
            "icon": "logo--openshift",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Kubernetes Service Group": {
            "icon": "ibm-cloud--kubernetes-service",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Z Containers Group": {
            "icon": "ibm-z-os--containers",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx Group": {
            "icon": "watsonx",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx Code Assistant Group": {
            "icon": "ibm-watsonx--code-assistant",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx Z Code Assistant Group": {
            "icon": "ibm-watsonx--code-assistant-for-z",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Authorization Boundary Group": {
            "icon": "flag",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Point of Presence Group": {
            "icon": "point-of-presence",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["white"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Region Group": {
            "icon": "location",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["location"],
            "resource": "local",
            "fields": {},
            "direction": "TB",
            "deployedOn": "IBM Cloud Group",
            "deployedTo": "none",
        },
        # Zone Groups
        "Access Group": {
            "icon": "group--access",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["none"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Account Group": {
            "icon": "group--account",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["none"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Instance Group": {
            "icon": "autoscaling",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["none"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Placement Group": {
            "icon": "group-objects",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["none"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Resource Group": {
            "icon": "group--resource",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["none"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Security Group": {
            "icon": "group--security",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["none"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Availability Zone Group": {
            "icon": "data--center",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.fills["location"],
            "resource": "none",
            "fields": {},
            "direction": "TB",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Expanded Groups
        "Expanded Virtual Server Group": {
            "icon": "ibm-cloud--virtual-server-vpc",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.fills["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Expanded Power Virtual Server Group": {
            "icon": "ibm--power-vs",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.fills["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Expanded Classic Virtual Server Group": {
            "icon": "ibm-cloud--virtual-server-classic",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.fills["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Expanded Bare Metal Server Group": {
            "icon": "ibm-cloud--bare-metal-servers-vpc",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.fills["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Expanded Classic Bare Metal Server Group": {
            "icon": "ibm-cloud--bare-metal-server",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.fills["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Expanded Application Group": {
            "icon": "application",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.fills["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Expanded Microservice Group": {
            "icon": "microservices--1",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.fills["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Actors
        "User Icon": {
            "icon": "user",
            "custom_icon": None,
            "color": Colors.lines["user"],
            "fill": Colors.lines["user"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Users Icon": {
            "icon": "group",
            "custom_icon": None,
            "color": Colors.lines["user"],
            "fill": Colors.lines["user"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Enterprise Icon": {
            "icon": "enterprise",
            "custom_icon": None,
            "color": Colors.lines["user"],
            "fill": Colors.lines["user"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Application Icon": {
            "icon": "application",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Web Application Icon": {
            "icon": "application--web",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Microservice Icon": {
            "icon": "microservices--1",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # AI
        "watsonx Icon": {
            "icon": "watsonx",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx.ai Icon": {
            "icon": "watsonx-ai",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx.data Icon": {
            "icon": "watsonx-data",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx.governance Icon": {
            "icon": "watsonx-governance",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx Orchestrate Icon": {
            "icon": "ibm-watsonx--orchestrate",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx Assistant Icon": {
            "icon": "ibm-watsonx--assistant",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx Code Assistant Icon": {
            "icon": "ibm-watsonx--code-assistant",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx Z Code Assistant Icon": {
            "icon": "ibm-watsonx--code-assistant-for-z",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "watsonx Z Refactor Code Assistant Icon": {
            "icon": "ibm-watsonx--code-assistant-for-z--refactor",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Watson Discovery Icon": {
            "icon": "ibm-watson--discovery",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Watson Machine Learning Icon": {
            "icon": "ibm-watson--machine-learning",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Watson Studio Icon": {
            "icon": "ibm-watson--studio",
            "custom_icon": None,
            "color": Colors.lines["applications"],
            "fill": Colors.lines["applications"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Compute
        "Virtual Server Icon": {
            "icon": "ibm-cloud--virtual-server-vpc",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "ibm_is_instance",
            "fields": {
                "label": "name",
                "sublabel": "primary_network_interface:primary_ip:address",
                "id": "id",
                "Subnet Group": "primary_network_interface:subnet",
                "Availability Zone Group": "vpc+zone",
                "VPC Group": "vpc",
            },
            "direction": "LR",
            "deployedOn": "Subnet Group",
            "deployedTo": "none",
        },
        "Power Virtual Server Icon": {
            "icon": "ibm--power-vs",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Classic Virtual Server Icon": {
            "icon": "ibm-cloud--virtual-server-classic",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Bare Metal Server Icon": {
            "icon": "ibm-cloud--bare-metal-servers-vpc",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Classic Bare Metal Server Icon": {
            "icon": "ibm-cloud--bare-metal-server",
            "custom_icon": None,
            "color": Colors.lines["black"],
            "fill": Colors.lines["black"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Dedicated Host Icon": {
            "icon": "ibm-cloud--dedicated-host",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Image Service Icon": {
            "icon": "image-service",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Satellite Icon": {
            "icon": "cloud-satellite",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Containers
        "OpenShift Icon": {
            "icon": "logo--openshift",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "ibm_container_vpc_cluster",
            "fields": {
                "label": "name",
                "id": "id",
                "Subnet Group": "zones:subnet_id",
                "Availability Zone Group": "zones:name",
                "VPC Group": "vpc_id",
            },
            "direction": "LR",
            "deployedOn": "Subnet Group",
            "deployedTo": "none",
        },
        "Kubernetes Service Icon": {
            "icon": "ibm-cloud--kubernetes-service",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Z Containers Icon": {
            "icon": "ibm-z-os--containers",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Container Registry Icon": {
            "icon": "cloud-registry",
            "custom_icon": None,
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Code Engine Icon": {
            "icon": None,
            "custom_icon": "data:image/svg+xml,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iNDlweCIgaGVpZ2h0PSI0OXB4IiB2aWV3Qm94PSIwIDAgNDkgNDkiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8dGl0bGU+Q29kZSBFbmdpbmUgdjIgSWNvbjwvdGl0bGU+CiAgICA8ZyBpZD0iUGFnZS0xIiBzdHJva2U9Im5vbmUiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj4KICAgICAgICA8ZyBpZD0idjItNDh4NDgiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0yNjE4LCAtOTM5KSI+CiAgICAgICAgICAgIDxnIGlkPSJDb2RlLUVuZ2luZS12Mi1JY29uIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyNjE4LjUsIDkzOS41MzA0KSI+CiAgICAgICAgICAgICAgICA8ZyBpZD0iS3ViZXJuZXRlcyIgZmlsbD0iIzE5ODAzOCI+CiAgICAgICAgICAgICAgICAgICAgPHBvbHlnb24gaWQ9IkZpbGwtNCIgcG9pbnRzPSIwIDQ4IDQ4IDQ4IDQ4IDAgMCAwIj48L3BvbHlnb24+CiAgICAgICAgICAgICAgICA8L2c+CiAgICAgICAgICAgICAgICA8ZyBpZD0iaWJtLWNsb3VkLS1jb2RlLWVuZ2luZSgxKSIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTEuNSwgMTIuNDY5NikiPgogICAgICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0xNi41LDE1IEwxNi41LDIwLjk0MjI1IEMxNi41LDIxLjM4ODUgMTYuMTM4NSwyMS43NSAxNS42OTIyNSwyMS43NSBMNi44MDc3NSwyMS43NSBDNi4zNjE1LDIxLjc1IDYsMjEuMzg4NSA2LDIwLjk0MjI1IEw2LDE3LjI1IEwxLjUsMTcuMjUgTDEuNSwxNS43NSBMNiwxNS43NSBMNiwxMi4wNTc3NSBDNiwxMS42MTE1IDYuMzYxNSwxMS4yNSA2LjgwNzc1LDExLjI1IEw5Ljc1LDExLjI1IEw5Ljc1LDEyLjc1IEw3LjUsMTIuNzUgTDcuNSwyMC4yNSBMMTUsMjAuMjUgTDE1LDE1IEwxNi41LDE1IFogTTkuNzUsNiBMMS41LDYgTDEuNSw3LjUgTDkuNzUsNy41IEw5Ljc1LDYgWiBNMjEuNzUsMTIuNzUgQzIyLjE2NDc1LDEyLjc1IDIyLjUsMTIuNDE0NzUgMjIuNSwxMiBMMjIuNSwzIEMyMi41LDIuNTg2IDIyLjE2NDc1LDIuMjUgMjEuNzUsMi4yNSBMMTIuNzUsMi4yNSBDMTIuMzM1MjUsMi4yNSAxMiwyLjU4NiAxMiwzIEwxMiwxMiBDMTIsMTIuNDE0NzUgMTIuMzM1MjUsMTIuNzUgMTIuNzUsMTIuNzUgTDIxLjc1LDEyLjc1IE0xMy41LDMuNzUgTDIxLDMuNzUgTDIxLDExLjI1IEwxMy41LDExLjI1IEwxMy41LDMuNzUgWiIgaWQ9IlNoYXBlIiBmaWxsPSIjRkZGRkZGIiBmaWxsLXJ1bGU9Im5vbnplcm8iPjwvcGF0aD4KICAgICAgICAgICAgICAgICAgICA8cmVjdCBpZD0iX3gzQ19UcmFuc3BhcmVudF9SZWN0YW5nbGVfeDNFXyIgeD0iMCIgeT0iMCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48L3JlY3Q+CiAgICAgICAgICAgICAgICA8L2c+CiAgICAgICAgICAgIDwvZz4KICAgICAgICA8L2c+CiAgICA8L2c+Cjwvc3ZnPg==",
            "color": Colors.lines["compute"],
            "fill": Colors.lines["compute"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Data
        "Db2 Icon": {
            "icon": "ibm--db2",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Db2 Warehouse Icon": {
            "icon": "ibm--db2-warehouse",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Cloudant Icon": {
            "icon": "ibm--cloudant",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "DataStax Icon": {
            "icon": "database--datastax",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Elasticsearch Icon": {
            "icon": "database--elastic",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Note: EnterpriseEB is fully deprecated as of 10/15/25.
        #'EnterpriseDB Icon': {'icon': 'database--enterprisedb', 'custom_icon': None, 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
        # Note: etcd is fully deprecated as of 10/15/25.
        #'etcd Icon': {'icon': 'database--etcd', 'custom_icon': None, 'color': Colors.lines["data"], 'fill': Colors.lines["data"],  'resource': 'none', 'fields': {}, 'direction': 'LR', 'deployedOn': 'none', 'deployedTo': 'none'},
        "MongoDB Icon": {
            "icon": "database--mongodb",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "MySQL Icon": {
            "icon": "database--mysql",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "PostgreSQL Icon": {
            "icon": "database--postgresql",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Rabbit Icon": {
            "icon": "database--rabbit",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Redis Icon": {
            "icon": "database--redis",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Database Icon": {
            "icon": "data--base",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Event Streams Icon": {
            "icon": "ibm-cloud--event-streams",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Data Pak Icon": {
            "icon": "ibm-cloud-pak--data",
            "custom_icon": None,
            "color": Colors.lines["data"],
            "fill": Colors.lines["data"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # DevOps
        "Continuous Delivery Icon": {
            "icon": "ibm-cloud--continuous-delivery",
            "custom_icon": None,
            "color": Colors.lines["devops"],
            "fill": Colors.lines["devops"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Continuous Integration Icon": {
            "icon": "continuous-integration",
            "custom_icon": None,
            "color": Colors.lines["devops"],
            "fill": Colors.lines["devops"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Source Code Repository Icon": {
            "icon": "repo--source-code",
            "custom_icon": None,
            "color": Colors.lines["devops"],
            "fill": Colors.lines["devops"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Toolchain Icon": {
            "icon": "ibm--toolchain",
            "custom_icon": None,
            "color": Colors.lines["devops"],
            "fill": Colors.lines["devops"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "MQ Icon": {
            "icon": "ibm--mq",
            "custom_icon": None,
            "color": Colors.lines["devops"],
            "fill": Colors.lines["devops"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Ansible Icon": {
            "icon": "logo--ansible-community",
            "custom_icon": None,
            "color": Colors.lines["devops"],
            "fill": Colors.lines["devops"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "GitLab Icon": {
            "icon": "logo--gitlab",
            "custom_icon": None,
            "color": Colors.lines["devops"],
            "fill": Colors.lines["devops"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Integration Pak Icon": {
            "icon": "ibm-cloud-pak--integration",
            "custom_icon": None,
            "color": Colors.lines["devops"],
            "fill": Colors.lines["devops"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Network
        "Load Balancer Icon": {
            "icon": "load-balancer--vpc",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Application Load Balancer Icon": {
            "icon": "load-balancer--application",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Network Load Balancer Icon": {
            "icon": "load-balancer--network",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Global Load Balancer Icon": {
            "icon": "load-balancer--global",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Classic Load Balancer Icon": {
            "icon": "load-balancer--classic",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Floating IP Icon": {
            "icon": "floating-ip",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Network Interface Icon": {
            "icon": "network-interface",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        #'Endpoint Gateway Icon': {'icon': 'ibm-cloud--vpc-endpoints', 'custom_icon': None, 'color': Colors.lines["network"], 'fill': Colors.lines["network"], 'resource': 'ibm_is_virtual_endpoint_gateway', 'fields': {'label': 'name', 'id': 'id', 'VPC Services Group': '@services+vpc'}, 'direction': 'LR', 'deployedOn': 'VPC Services Group', 'deployedTo': 'none'},
        "Endpoint Gateway Icon": {
            "icon": "ibm-cloud--vpc-endpoints",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "ibm_is_virtual_endpoint_gateway",
            "fields": {
                "label": "name",
                "sublabel": "address",
                "id": "id",
                "Subnet Group": "subnet",
            },
            "direction": "LR",
            "deployedOn": "Subnet Group",
            "deployedTo": "none",
        },
        "Public Gateway Icon": {
            "icon": "gateway--public",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Transit Gateway Icon": {
            "icon": "ibm-cloud--transit-gateway",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "ibm_tg_gateway",
            "fields": {
                "label": "name",
                "id": "id",
                "Cloud Services Group": "@services+location",
            },
            "direction": "LR",
            "deployedOn": "Cloud Services Group",
            "deployedTo": "none",
        },
        "Direct Link Connect Icon": {
            "icon": "ibm-cloud--direct-link-2--connect",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Direct Link Dedicated Icon": {
            "icon": "ibm-cloud--direct-link-2--dedicated",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "DNS Services Icon": {
            "icon": "dns-services",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Internet Services Icon": {
            "icon": "ibm-cloud--internet-services",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Internet Icon": {
            "icon": "wikis",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Note: NTP in process of being added to design center.
        "NTP Icon": {
            "icon": "undefined",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Bridge Icon": {
            "icon": "arrows--horizontal",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Router Icon": {
            "icon": "router",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "VLAN Icon": {
            "icon": "vlan",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Classic VLAN Icon": {
            "icon": "vlan--ibm",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Proxy Server Icon": {
            "icon": "server--proxy",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "L2 Switch Icon": {
            "icon": "switch-layer-2",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "L3 Switch Icon": {
            "icon": "switch-layer-3",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Observability
        # Note: Activity Tracker is deprecated, replaced with Cloud Logs.
        "Cloud Logs Icon": {
            "icon": "ibm-cloud--logging",
            "custom_icon": None,
            "color": Colors.lines["management"],
            "fill": Colors.lines["management"],
            "resource": "ibm_atracker_target",
            "fields": {
                "label": "name",
                "id": "id",
                "Cloud Services Group": "@services+crn[5]",
            },
            "direction": "LR",
            "deployedOn": "Cloud Services Group",
            "deployedTo": "none",
        },
        #'Flow Logs Icon': {'icon': 'flow-logs-vpc', 'custom_icon': None, 'color': Colors.lines["management"], 'fill': Colors.lines["management"], 'resource': 'ibm_is_flow_log', 'fields': {'label': 'name', 'id': 'id', 'VPC Services Group': '@services+vpc'}, 'direction': 'LR', 'deployedOn': 'VPC Services Group', 'deployedTo': 'none'},
        "Flow Logs Icon": {
            "icon": "flow-logs-vpc",
            "custom_icon": None,
            "color": Colors.lines["management"],
            "fill": Colors.lines["management"],
            "resource": "ibm_is_flow_log",
            "fields": {
                "label": "name",
                "id": "id",
                "Cloud Services Group": "@services+crn[5]",
            },
            "direction": "LR",
            "deployedOn": "Cloud Services Group",
            "deployedTo": "none",
        },
        "Monitoring Icon": {
            "icon": "cloud--monitoring",
            "custom_icon": None,
            "color": Colors.lines["management"],
            "fill": Colors.lines["management"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Security
        "App ID Icon": {
            "icon": "ibm-cloud--app-id",
            "custom_icon": None,
            "color": Colors.lines["security"],
            "fill": Colors.lines["security"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Key Protect Icon": {
            "icon": "ibm-cloud--key-protect",
            "custom_icon": None,
            "color": Colors.lines["security"],
            "fill": Colors.lines["security"],
            "resource": "ibm_kms_key",
            "fields": {
                "label": "key_name",
                "id": "id",
                "Cloud Services Group": "@services+crn[5]",
            },
            "direction": "LR",
            "deployedOn": "Cloud Services Group",
            "deployedTo": "none",
        },
        "Secrets Manager Icon": {
            "icon": "ibm-cloud--secrets-manager",
            "custom_icon": None,
            "color": Colors.lines["security"],
            "fill": Colors.lines["security"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Security Compliance Center Icon": {
            "icon": "ibm-cloud--security-compliance-center",
            "custom_icon": None,
            "color": Colors.lines["security"],
            "fill": Colors.lines["security"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "SSH Key Icon": {
            "icon": "password",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["security"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "VPN Gateway Icon": {
            "icon": "ibm--vpn-for-vpc",
            "custom_icon": None,
            "color": Colors.lines["security"],
            "fill": Colors.lines["security"],
            "resource": "ibm_is_vpn_gateway",
            "fields": {
                "label": "name",
                "sublabel": "public_ip_address",
                "id": "id",
                "Subnet Group": "subnet",
            },
            "direction": "LR",
            "deployedOn": "Subnet Group",
            "deployedTo": "none",
        },
        # TODO Add private_ip_address to sublabel of VPN Connection Icon.
        "VPN Connection Icon": {
            "icon": "vpn--connection",
            "custom_icon": None,
            "color": Colors.lines["security"],
            "fill": Colors.lines["security"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Bastion Host Icon": {
            "icon": "bastion-host",
            "custom_icon": None,
            "color": Colors.lines["security"],
            "fill": Colors.lines["security"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "ACL Rules Icon": {
            "icon": "subnet-acl-rules",
            "custom_icon": None,
            "color": Colors.lines["security"],
            "fill": Colors.lines["security"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Security Pak Icon": {
            "icon": "ibm-cloud-pak--security",
            "custom_icon": None,
            "color": Colors.lines["security"],
            "fill": Colors.lines["security"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Storage
        "Block Storage Icon": {
            "icon": "block-storage",
            "custom_icon": None,
            "color": Colors.lines["storage"],
            "fill": Colors.lines["storage"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Block Storage Snapshots Icon": {
            "icon": None,
            "custom_icon": "data:image/svg+xml,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iNDlweCIgaGVpZ2h0PSI0OXB4IiB2aWV3Qm94PSIwIDAgNDkgNDkiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8dGl0bGU+QmxvY2sgU3RvcmFnZSBTbmFwc2hvdHM8L3RpdGxlPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTEuNSwgMTEuNSkgc2NhbGUoMC44KSI+CiAgICAgICAgPHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTI4LDMwSDRjLTEuMSwwLTItLjktMi0ydi0xMmgydjEyaDI0VjRoLTEydi0yaDEyYzEuMSwwLDIsLjksMiwydjI0YzAsMS4xLS45LDItMiwyWk0yMi41LDEyLjFsLTYtM2MtLjMtLjEtLjYtLjEtLjksMGwtNiwzYy0uMy4yLS41LjUtLjYuOXY3YzAsLjQuMi43LjYuOWw2LDNjLjMuMS42LjEuOSwwbDYtM2MuMy0uMi41LS41LjYtLjl2LTdjMC0uNC0uMi0uNy0uNS0uOWgtLjFaTTE2LDExLjFsMy44LDEuOS0zLjgsMS45LTMuOC0xLjlzMy44LTEuOSwzLjgtMS45Wk0xMSwxNC42bDQsMnY0LjhsLTQtMnYtNC44Wk0xNywyMS40di00LjhsNC0ydjQuOHMtNCwyLTQsMlpNMCwxMGg1djJIMHYtMlpNMTIsMHY1aC0yVjBoMlpNMy40LDJsMy41LDMuNS0xLjQsMS40LTMuNS0zLjUsMS40LTEuNFoiLz4KICAgIDwvZz4KPC9zdmc+Cg==",
            "color": Colors.lines["storage"],
            "fill": Colors.lines["storage"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Note: File Storage in process of being added to design center.
        "File Storage Icon": {
            "icon": "undefined",
            "custom_icon": None,
            "color": Colors.lines["storage"],
            "fill": Colors.lines["storage"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        "Object Storage Icon": {
            "icon": "object-storage",
            "custom_icon": None,
            "color": Colors.lines["storage"],
            "fill": Colors.lines["storage"],
            "resource": "ibm_cos_bucket",
            "fields": {
                "label": "bucket_name",
                "id": "id",
                "Cloud Services Group": "@services+region_location",
            },
            "direction": "LR",
            "deployedOn": "Cloud Services Group",
            "deployedTo": "none",
        },
        "Cloud Backup Icon": {
            "icon": None,
            "custom_icon": "data:image/svg+xml,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iNDlweCIgaGVpZ2h0PSI0OXB4IiB2aWV3Qm94PSIwIDAgNDkgNDkiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8dGl0bGU+SUJNIENsb3Vkwq4gQmFja3VwIFNlcnZpY2UgZm9yIFZQQzwvdGl0bGU+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMS41LCAxMy41KSBzY2FsZSgwLjgpIj4KICAgICAgICA8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNNiwyMGg4di0ySDZ2LTZoMThWNGMwLTEuMTA0NS0uODk1NS0yLTItMkg2Yy0xLjEwNDUsMC0yLC44OTU1LTIsMnYyMmMwLDEuMTA0Ny44OTU1LDIsMiwyaDh2LTJINnYtNlpNNiw0aDE2djZINnYtNlpNOCwyMi45OTk5YzAtLjU1MjMuNDQ3Ny0xLDEtMXMxLC40NDc3LDEsMS0uNDQ3NywxLTEsMS0xLS40NDc3LTEtMVpNOCwxNWMwLS41NTIzLjQ0NzctMSwxLTFzMSwuNDQ3NywxLDEtLjQ0NzcsMS0xLDEtMS0uNDQ3Ny0xLTFaTTgsN2MwLS41NTIzLjQ0NzctMSwxLTFzMSwuNDQ3NywxLDEtLjQ0NzcsMS0xLDEtMS0uNDQ3Ny0xLTFaTTMwLDE3aC0zLjQxMzFjMi4wNDA1LDEuMjI0NiwzLjQxMzEsMy40NTIxLDMuNDEzMSw2LDAsMy44NTk5LTMuMTQwMSw3LTcsN3MtNy0zLjE0MDEtNy03YzAtMS44Njk2LjcyOC0zLjYyNzQsMi4wNTAzLTQuOTQ5N2wxLjQxNDEsMS40MTQxYy0uOTQ0My45NDQzLTEuNDY0NCwyLjIwMDItMS40NjQ0LDMuNTM1NiwwLDIuNzU2OCwyLjI0MzIsNSw1LDVzNS0yLjI0MzIsNS01YzAtMi4wNDQ5LTEuMjM3My0zLjgwMjUtMy00LjU3NjJ2My41NzYyaC0ydi03aDd2MlpNOCwyM2MwLS41NTIzLjQ0NzctMSwxLTFzMSwuNDQ3NywxLDEtLjQ0NzcsMS0xLDEtMS0uNDQ3Ny0xLTFaTTgsMTVjMC0uNTUyMy40NDc3LTEsMS0xczEsLjQ0NzcsMSwxLS40NDc3LDEtMSwxLTEtLjQ0NzctMS0xWk04LDdjMC0uNTUyMy40NDc3LTEsMS0xczEsLjQ0NzcsMSwxLS40NDc3LDEtMSwxLTEtLjQ0NzctMS0xWk0zMCwxN2gtMy40MTMxYzIuMDQwNSwxLjIyNDYsMy40MTMxLDMuNDUyMSwzLjQxMzEsNiwwLDMuODU5OS0zLjE0MDEsNy03LDdzLTctMy4xNDAxLTctN2MwLTEuODY5Ni43MjgtMy42Mjc0LDIuMDUwMy00Ljk0OTdsMS40MTQxLDEuNDE0MWMtLjk0NDMuOTQ0My0xLjQ2NDQsMi4yMDAyLTEuNDY0NCwzLjUzNTYsMCwyLjc1NjgsMi4yNDMyLDUsNSw1czUtMi4yNDMyLDUtNWMwLTIuMDQ0OS0xLjIzNzMtMy44MDI1LTMtNC41NzYydjMuNTc2MmgtMnYtN2g3djJaIi8+CiAgICA8L2c+Cjwvc3ZnPgo=",
            "color": Colors.lines["storage"],
            "fill": Colors.lines["storage"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
        # Other
        "Undefined Icon": {
            "icon": "undefined",
            "custom_icon": None,
            "color": Colors.lines["network"],
            "fill": Colors.lines["network"],
            "resource": "none",
            "fields": {},
            "direction": "LR",
            "deployedOn": "none",
            "deployedTo": "none",
        },
    }

    common = None

    def __init__(self, common):
        self.common = common

    def getIconDictionary(self):
        return self.iconDictionary

    def getIcon(self, iconusage):
        if iconusage in self.iconDictionary:
            icon = self.iconDictionary[iconusage]
            iconname = icon["icon"]
            iconcolor = icon["color"]
            iconfill = icon["fill"]
        else:
            icon = self.iconDictionary["Undefined Icon"]
            iconname = icon["icon"]
            iconcolor = icon["color"]
            iconfill = icon["fill"]

        return iconname, iconcolor, iconfill

    def getResourceIcon(self, iconusage):
        if iconusage in self.iconDictionary:
            icon = self.iconDictionary[iconusage]
        else:
            icon = self.iconDictionary["Undefined Icon"]

        return icon

    def validIcon(self, iconname):
        return iconname in self.iconDictionary

    def printIcons(self):
        for entry in self.iconDictionary:
            icon = self.iconDictionary[entry]
            logger.debug(icon)

    def mapResources(self, resources):
        for entry in self.iconDictionary:
            icon = self.iconDictionary[entry]

            resource = icon["resource"]
            if resource == "none" or resource == "local":
                continue

            resource = resources.getResource(resource)
            if resource.empty:
                continue

            fields = icon["fields"]
            lists = []

            # Field Options:
            #   a. "name1:name2:nameN" to drill down into substructures
            #   b. "name1+name2+nameN" to concatenate names
            #   c. "@name" to leave name as is
            #   d. "name[d]" to retrieve array index d starting at 0 where d is 0 to 9

            for _index, row in resource.iterrows():
                list = {}
                for newname, oldname in fields.items():
                    if oldname.find(":") > -1:
                        templist = oldname.split(":")
                        tempdata = row[templist[0]]
                        if len(templist) == 1:
                            element = tempdata  # noqa: F841
                        else:
                            tempindex = 1
                            while tempindex < len(templist):
                                tempdata = tempdata[0]
                                tempdata = tempdata[templist[tempindex]]
                                tempindex += 1
                    else:
                        templist = oldname.split("+") if oldname.find("+") > -1 else [oldname]

                        tempindex = 0
                        tempstring = ""

                        while tempindex < len(templist):
                            tempvalue = templist[tempindex]
                            if tempvalue.find("[") > -1:
                                temploc = tempvalue.find("[")
                                tempindex = int(tempvalue[temploc + 1])
                                tempname = tempvalue[:temploc]
                                temprow = row[tempname]
                                temparray = temprow.split(":")
                                tempvalue = temparray[tempindex]
                                tempstring = tempstring + tempvalue
                            elif tempvalue[0] == "@":
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
            icon["data"] = df

        self.addClouds()
        self.addRegions()
        self.addZones()
        self.addCloudServices()
        # self.addVPCServices()

        return True

    def addClouds(self):
        data = [{"label": "IBM Cloud", "id": "IBM Cloud Group"}]

        icon = self.iconDictionary["IBM Cloud Group"]
        df = pd.DataFrame(data)
        icon["data"] = df

        return

    def addRegions(self):
        data = [
            {"label": "Sydney", "id": "au-syd", "IBM Cloud Group": "IBM Cloud Group"},
            {
                "label": "Sao Paulo",
                "id": "br-sao",
                "IBM Cloud Group": "IBM Cloud Group",
            },
            {"label": "Toronto", "id": "ca-tor", "IBM Cloud Group": "IBM Cloud Group"},
            {"label": "Frankfurt", "id": "eu-de", "IBM Cloud Group": "IBM Cloud Group"},
            {"label": "London", "id": "eu-gb", "IBM Cloud Group": "IBM Cloud Group"},
            {"label": "Osaka", "id": "jp-osa", "IBM Cloud Group": "IBM Cloud Group"},
            {"label": "Tokyo", "id": "jp-tok", "IBM Cloud Group": "IBM Cloud Group"},
            {
                "label": "Washington DC",
                "id": "us-east",
                "IBM Cloud Group": "IBM Cloud Group",
            },
            {"label": "Dallas", "id": "us-south", "IBM Cloud Group": "IBM Cloud Group"},
        ]

        icon = self.iconDictionary["Region Group"]
        df = pd.DataFrame(data)
        icon["data"] = df

        return

    def addZones(self):
        data = [
            {"label": "Zone 1", "sublabel": "10.245.0.0/18", "id": "au-syd-1"},
            {"label": "Zone 2", "sublabel": "10.245.64.0/18", "id": "au-syd-2"},
            {"label": "Zone 3", "sublabel": "10.245.128.0/18", "id": "au-syd-3"},
            {"label": "Zone 1", "sublabel": "10.250.0.0/18", "id": "br-sao-1"},
            {"label": "Zone 2", "sublabel": "10.250.64.0/18", "id": "br-sao-2"},
            {"label": "Zone 3", "sublabel": "10.250.128.0/18", "id": "br-sao-3"},
            {"label": "Zone 1", "sublabel": "10.249.0.0/18", "id": "ca-tor-1"},
            {"label": "Zone 2", "sublabel": "10.249.64.0/18", "id": "ca-tor-2"},
            {"label": "Zone 3", "sublabel": "10.249.128.0/18", "id": "ca-tor-3"},
            {"label": "Zone 1", "sublabel": "10.243.0.0/18", "id": "eu-de-1"},
            {"label": "Zone 2", "sublabel": "10.243.64.0/18", "id": "eu-de-2"},
            {"label": "Zone 3", "sublabel": "10.243.128.0/18", "id": "eu-de-3"},
            {"label": "Zone 1", "sublabel": "10.242.0.0/18", "id": "eu-gb-1"},
            {"label": "Zone 2", "sublabel": "10.242.64.0/18", "id": "eu-gb-2"},
            {"label": "Zone 3", "sublabel": "10.242.128.0/18", "id": "eu-gb-3"},
            {"label": "Zone 1", "sublabel": "10.248.0.0/18", "id": "jp-osa-1"},
            {"label": "Zone 2", "sublabel": "10.248.64.0/18", "id": "jp-osa-2"},
            {"label": "Zone 3", "sublabel": "10.248.128.0/18", "id": "jp-osa-3"},
            {"label": "Zone 1", "sublabel": "10.244.0.0/18", "id": "jp-tok-1"},
            {"label": "Zone 2", "sublabel": "10.244.64.0/18", "id": "jp-tok-2"},
            {"label": "Zone 3", "sublabel": "10.244.128.0/18", "id": "jp-tok 3"},
            {"label": "Zone 1", "sublabel": "10.241.0.0/18", "id": "us-east-1"},
            {"label": "Zone 2", "sublabel": "10.241.64.0/18", "id": "us-east-2"},
            {"label": "Zone 3", "sublabel": "10.241.128.0/18", "id": "us-east-3"},
            {"label": "Zone 1", "sublabel": "10.240.0.0/18", "id": "us-south-1"},
            {"label": "Zone 2", "sublabel": "10.240.64.0/18", "id": "us-south-2"},
            {"label": "Zone 3", "sublabel": "10.240.128.0/18", "id": "us-south-3"},
        ]

        vpcIcon = self.getResourceIcon("VPC Group")
        vpcData = vpcIcon["data"]
        zoneData = []

        for _vpcKey, vpcRow in vpcData.iterrows():
            vpcID = vpcRow["id"]
            for zoneRow in data:
                newRow = zoneRow.copy()
                # newRow["id"] = vpcID + "-" + newRow["id"]
                newRow["id"] = vpcID + newRow["id"]
                zoneData.append(newRow)

        icon = self.iconDictionary["Availability Zone Group"]
        df = pd.DataFrame(zoneData)
        icon["data"] = df

        return

    def addCloudServices(self):
        data = [
            {
                "label": "Cloud Services",
                "id": "servicesau-syd",
                "Region Group": "au-syd",
                "Cloud Services Group": "Cloud Services Group",
            },
            {
                "label": "Cloud Services",
                "id": "servicesbr-sao",
                "Region Group": "br-sao",
                "Cloud Services Group": "Cloud Services Group",
            },
            {
                "label": "Cloud Services",
                "id": "servicesca-tor",
                "Region Group": "ca-tor",
                "Cloud Services Group": "Cloud Services Group",
            },
            {
                "label": "Cloud Services",
                "id": "serviceseu-de",
                "Region Group": "eu-de",
                "Cloud Services Group": "Cloud Services Group",
            },
            {
                "label": "Cloud Services",
                "id": "serviceseu-gb",
                "Region Group": "eu-gb",
                "Cloud Services Group": "Cloud Services Group",
            },
            {
                "label": "Cloud Services",
                "id": "servicesjp-osa",
                "Region Group": "jp-osa",
                "Cloud Services Group": "Cloud Services Group",
            },
            {
                "label": "Cloud Services",
                "id": "servicesjp-tok",
                "Region Group": "jp-tok",
                "Cloud Services Group": "Cloud Services Group",
            },
            {
                "label": "Cloud Services",
                "id": "servicesus-east",
                "Region Group": "us-east",
                "Cloud Services Group": "Cloud Services Group",
            },
            {
                "label": "Cloud Services",
                "id": "servicesus-south",
                "Region Group": "us-south",
                "Cloud Services Group": "Cloud Services Group",
            },
        ]

        icon = self.iconDictionary["Cloud Services Group"]
        df = pd.DataFrame(data)
        icon["data"] = df

        return

    """
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
   """
