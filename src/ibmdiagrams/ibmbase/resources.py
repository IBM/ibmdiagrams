# @file resources.py
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

import os.path
import pandas as pd
from json import loads as json_load, dumps as json_dumps
from tabulate import tabulate

import pandas as pd

class Resources:
   resourceDictionary = {
      # Activity Tracker API
      'ibm_atracker_route': pd.DataFrame(),
      'ibm_atracker_settings': pd.DataFrame(),
      'ibm_atracker_target': pd.DataFrame(),

      # App Configuration
      'ibm_app_config_collection': pd.DataFrame(),
      'ibm_app_config_environment': pd.DataFrame(),
      'ibm_app_config_feature': pd.DataFrame(),
      'ibm_app_config_property': pd.DataFrame(),
      'ibm_app_config_segment': pd.DataFrame(),
      'ibm_app_config_snapshot': pd.DataFrame(),

      # AppID Management
      'ibm_appid_action_url': pd.DataFrame(),
      'ibm_appid_apm': pd.DataFrame(),
      'ibm_appid_application': pd.DataFrame(),
      'ibm_appid_application_roles': pd.DataFrame(),
      'ibm_appid_application_scopes': pd.DataFrame(),
      'ibm_appid_audit_status': pd.DataFrame(),
      'ibm_appid_cloud_directory_template': pd.DataFrame(),
      'ibm_appid_cloud_directory_user': pd.DataFrame(),
      'ibm_appid_idp_cloud_directory': pd.DataFrame(),
      'ibm_appid_idp_custom': pd.DataFrame(),
      'ibm_appid_idp_facebook': pd.DataFrame(),
      'ibm_appid_idp_google': pd.DataFrame(),
      'ibm_appid_idp_saml': pd.DataFrame(),
      'ibm_appid_languages': pd.DataFrame(),
      'ibm_appid_mfa': pd.DataFrame(),
      'ibm_appid_mfa_channel': pd.DataFrame(),
      'ibm_appid_password_regex': pd.DataFrame(),
      'ibm_appid_redirect_urls': pd.DataFrame(),
      'ibm_appid_role': pd.DataFrame(),
      'ibm_appid_theme_color': pd.DataFrame(),
      'ibm_appid_theme_text': pd.DataFrame(),
      'ibm_appid_token_config': pd.DataFrame(),
      'ibm_appid_user_roles': pd.DataFrame(),

      # Catalog Management
      'ibm_cm_catalog': pd.DataFrame(),
      'ibm_cm_object': pd.DataFrame(),
      'ibm_cm_offering': pd.DataFrame(),
      'ibm_cm_offering_instance': pd.DataFrame(),
      'ibm_cm_version': pd.DataFrame(),

      # Certificate Manager
      'ibm_certificate_manager_import': pd.DataFrame(),
      'ibm_certificate_manager_order': pd.DataFrame(),

      # Classic Infrastructure
      'ibm_cdn': pd.DataFrame(),
      'ibm_compute_autoscale_group': pd.DataFrame(),
      'ibm_compute_autoscale_policy': pd.DataFrame(),
      'ibm_compute_bare_metal': pd.DataFrame(),
      'ibm_compute_dedicated_host': pd.DataFrame(),
      'ibm_compute_monitor': pd.DataFrame(),
      'ibm_compute_placement_group': pd.DataFrame(),
      'ibm_compute_provisioning_hook': pd.DataFrame(),
      'ibm_compute_reserved_capacity': pd.DataFrame(),
      'ibm_compute_ssh_key': pd.DataFrame(),
      'ibm_compute_ssl_certificate': pd.DataFrame(),
      'ibm_compute_user': pd.DataFrame(),
      'ibm_compute_vm_instance': pd.DataFrame(),
      'ibm_dns_domain': pd.DataFrame(),
      'ibm_dns_domain_registration_nameservers': pd.DataFrame(),
      'ibm_dns_record': pd.DataFrame(),
      'ibm_dns_reverse_record': pd.DataFrame(),
      'ibm_dns_secondary': pd.DataFrame(),
      'ibm_firewall': pd.DataFrame(),
      'ibm_firewall_policy': pd.DataFrame(),
      'ibm_hardware_firewall_shared': pd.DataFrame(),
      'ibm_ipsec_vpn': pd.DataFrame(),
      'ibm_lb': pd.DataFrame(),
      'ibm_lb_service': pd.DataFrame(),
      'ibm_lb_service_group': pd.DataFrame(),
      'ibm_lb_vpx': pd.DataFrame(),
      'ibm_lb_vpx_ha': pd.DataFrame(),
      'ibm_lb_vpx_service': pd.DataFrame(),
      'ibm_lb_vpx_vip': pd.DataFrame(),
      'ibm_lbaas': pd.DataFrame(),
      'ibm_lbaas_health_monitor': pd.DataFrame(),
      'ibm_lbaas_server_instance_attachment': pd.DataFrame(),
      'ibm_multi_vlan_firewall': pd.DataFrame(),
      'ibm_network_gateway': pd.DataFrame(),
      'ibm_network_gateway_vlan_association': pd.DataFrame(),
      'ibm_network_interface_sg_attachment': pd.DataFrame(),
      'ibm_network_public_ip': pd.DataFrame(),
      'ibm_network_vlan': pd.DataFrame(),
      'ibm_network_vlan_spanning': pd.DataFrame(),
      'ibm_object_storage_account': pd.DataFrame(),
      'ibm_security_group': pd.DataFrame(),
      'ibm_security_group_rule': pd.DataFrame(),
      'ibm_ssl_certificate': pd.DataFrame(),
      'ibm_storage_block': pd.DataFrame(),
      'ibm_storage_evault': pd.DataFrame(),
      'ibm_storage_file': pd.DataFrame(),
      'ibm_subnet': pd.DataFrame(),

      # Cloud Databases
      'ibm_database': pd.DataFrame(),

      # Cloud Foundry
      'ibm_app': pd.DataFrame(),
      'ibm_app_domain_private': pd.DataFrame(),
      'ibm_app_domain_shared': pd.DataFrame(),
      'ibm_app_route': pd.DataFrame(),
      'ibm_org': pd.DataFrame(),
      'ibm_service_instance': pd.DataFrame(),
      'ibm_service_key': pd.DataFrame(),
      'ibm_space': pd.DataFrame(),

      # Cloudant Databases
      'ibm_cloudant': pd.DataFrame(),
      'ibm_cloudant_database': pd.DataFrame(),

      # Container Registry
      'ibm_cr_namespace': pd.DataFrame(),
      'ibm_cr_retention_policy': pd.DataFrame(),

      # Context Based Restrictions
      'ibm_cbr_rule': pd.DataFrame(),
      'ibm_cbr_zone': pd.DataFrame(),

       # Continuous Delivery
      'ibm_cd_tekton_pipeline': pd.DataFrame(),
      'ibm_cd_tekton_pipeline_definition': pd.DataFrame(),
      'ibm_cd_tekton_pipeline_property': pd.DataFrame(),
      'ibm_cd_tekton_pipeline_trigger': pd.DataFrame(),
      'ibm_cd_toolchain': pd.DataFrame(),
      'ibm_cd_toolchain_tool_appconfig': pd.DataFrame(),
      'ibm_cd_toolchain_tool_artifactory': pd.DataFrame(),
      'ibm_cd_toolchain_tool_bitbucketgit': pd.DataFrame(),
      'ibm_cd_toolchain_tool_custom': pd.DataFrame(),
      'ibm_cd_toolchain_tool_devopsinsights': pd.DataFrame(),
      'ibm_cd_toolchain_tool_githubconsolidated': pd.DataFrame(),
      'ibm_cd_toolchain_tool_gitlab': pd.DataFrame(),
      'ibm_cd_toolchain_tool_hashicorpvault': pd.DataFrame(),
      'ibm_cd_toolchain_tool_hostedgit': pd.DataFrame(),
      'ibm_cd_toolchain_tool_jenkins': pd.DataFrame(),
      'ibm_cd_toolchain_tool_jira': pd.DataFrame(),
      'ibm_cd_toolchain_tool_keyprotect': pd.DataFrame(),
      'ibm_cd_toolchain_tool_nexus': pd.DataFrame(),
      'ibm_cd_toolchain_tool_pagerduty': pd.DataFrame(),
      'ibm_cd_toolchain_tool_pipeline': pd.DataFrame(),
      'ibm_cd_toolchain_tool_privateworker': pd.DataFrame(),
      'ibm_cd_toolchain_tool_saucelabs': pd.DataFrame(),
      'ibm_cd_toolchain_tool_secretsmanager': pd.DataFrame(),
      'ibm_cd_toolchain_tool_securitycompliance': pd.DataFrame(),
      'ibm_cd_toolchain_tool_slack': pd.DataFrame(),
      'ibm_cd_toolchain_tool_sonarqube': pd.DataFrame(),

      # DNS Services
      'ibm_dns_custom_resolver': pd.DataFrame(),
      'ibm_dns_custom_resolver_forwarding_rule': pd.DataFrame(),
      'ibm_dns_custom_resolver_location': pd.DataFrame(),
      'ibm_dns_custom_resolver_secondary_zone': pd.DataFrame(),
      'ibm_dns_glb': pd.DataFrame(),
      'ibm_dns_glb_monitor': pd.DataFrame(),
      'ibm_dns_glb_pool': pd.DataFrame(),
      'ibm_dns_glb_permitted_network': pd.DataFrame(),
      'ibm_dns_resource_record': pd.DataFrame(),
      'ibm_dns_zone': pd.DataFrame(),

      # Direct Link
      'ibm_dl_gateway': pd.DataFrame(),
      'ibm_dl_provider_gateway': pd.DataFrame(),
      'ibm_dl_route_report': pd.DataFrame(),
      'ibm_dl_virtual_connection': pd.DataFrame(),

      # Enterprise Management
      'ibm_enterprise': pd.DataFrame(),
      'ibm_enterprise_account': pd.DataFrame(),
      'ibm_enterprise_account_group': pd.DataFrame(),

      # Event Notifications
      'ibm_en_destination': pd.DataFrame(),
      'ibm_en_destination_android': pd.DataFrame(),
      'ibm_en_destination_ce': pd.DataFrame(),
      'ibm_en_destination_cf': pd.DataFrame(),
      'ibm_en_destination_chrome': pd.DataFrame(),
      'ibm_en_integration_cos': pd.DataFrame(),
      'ibm_en_destination_firefox': pd.DataFrame(),
      'ibm_en_destination_huawei': pd.DataFrame(),
      'ibm_en_destination_ios': pd.DataFrame(),
      'ibm_en_destination_mstreams': pd.DataFrame(),
      'ibm_en_destination_pagerduty': pd.DataFrame(),
      'ibm_en_destination_safari': pd.DataFrame(),
      'ibm_en_destination_slack': pd.DataFrame(),
      'ibm_en_destination_webhook': pd.DataFrame(),
      'ibm_en_ibmsource': pd.DataFrame(),
      'ibm_en_integration': pd.DataFrame(),
      'ibm_en_source': pd.DataFrame(),
      'ibm_en_subscription': pd.DataFrame(),
      'ibm_en_subscription_android': pd.DataFrame(),
      'ibm_en_subscription_ce': pd.DataFrame(),
      'ibm_en_subscription_cf': pd.DataFrame(),
      'ibm_en_subscription_chrome': pd.DataFrame(),
      'ibm_en_subscription_email': pd.DataFrame(),
      'ibm_en_subscription_firefox': pd.DataFrame(),
      'ibm_en_subscription_ios': pd.DataFrame(),
      'ibm_en_subscription_mstreams': pd.DataFrame(),
      'ibm_en_subscription_pagerduty': pd.DataFrame(),
      'ibm_en_subscription_safari': pd.DataFrame(),
      'ibm_en_subscription_slack': pd.DataFrame(),
      'ibm_en_subscription_sms': pd.DataFrame(),
      'ibm_en_subscription_sn': pd.DataFrame(),
      'ibm_en_subscription_webhook': pd.DataFrame(),
      'ibm_en_topic': pd.DataFrame(),

      # Event Streams
      'ibm_event_streams_schema': pd.DataFrame(),
      'ibm_event_streams_topic': pd.DataFrame(),

      # functions
      'ibm_function_action': pd.DataFrame(),
      'ibm_function_namespace': pd.DataFrame(),
      'ibm_function_package': pd.DataFrame(),
      'ibm_function_rule': pd.DataFrame(),
      'ibm_function_trigger': pd.DataFrame(),

      # Global Tagging
      'ibm_resource_tag': pd.DataFrame(),

      # Hyper Protect Crypto Services
      'ibm_hpcs': pd.DataFrame(),
      'ibm_hpcs_key_template': pd.DataFrame(),
      'ibm_hpcs_keystore': pd.DataFrame(),
      'ibm_hpcs_managed_key': pd.DataFrame(),
      'ibm_hpcs_vault': pd.DataFrame(),

      # Cloud Shell
      'ibm_cloud_shell_account_settings': pd.DataFrame(),

      # Identity & Access Management (IAM)
      'ibm_api_key': pd.DataFrame(),
      'ibm_iam_access_group': pd.DataFrame(),
      'ibm_iam_access_group_account_settings': pd.DataFrame(),
      'ibm_iam_access_group_dynamic_rule': pd.DataFrame(),
      'ibm_iam_access_group_members': pd.DataFrame(),
      'ibm_iam_access_group_policy': pd.DataFrame(),
      'ibm_iam_account_settings': pd.DataFrame(),
      'ibm_iam_authorization_policy': pd.DataFrame(),
      'ibm_iam_authorization_policy_detach': pd.DataFrame(),
      'ibm_iam_custom_role': pd.DataFrame(),
      'ibm_iam_service-api-key': pd.DataFrame(),
      'ibm_iam_service_id': pd.DataFrame(),
      'ibm_iam_service_policy': pd.DataFrame(),
      'ibm_iam_trusted_profile': pd.DataFrame(),
      'ibm_iam_trusted_profile_claim_rule': pd.DataFrame(),
      'ibm_iam_trusted_profile_link': pd.DataFrame(),
      'ibm_iam_trusted_profile_policy': pd.DataFrame(),
      'ibm_iam_user_invite': pd.DataFrame(),
      'ibm_iam_user_policy': pd.DataFrame(),
      'ibm_iam_user_settings': pd.DataFrame(),

      # Internet Services
      'ibm_cis': pd.DataFrame(),
      'ibm_cis_alert': pd.DataFrame(),
      'ibm_cis_cache_settings': pd.DataFrame(),
      'ibm_cis_certificate_order': pd.DataFrame(),
      'ibm_cis_certificate_upload': pd.DataFrame(),
      'ibm_cis_custom_page': pd.DataFrame(),
      'ibm_cis_custom_page': pd.DataFrame(),
      'ibm_cis_dns_record': pd.DataFrame(),
      'ibm_cis_dns_records_import': pd.DataFrame(),
      'ibm_cis_domain': pd.DataFrame(),
      'ibm_cis_domain_settings': pd.DataFrame(),
      'ibm_cis_edge_functions_action': pd.DataFrame(),
      'ibm_cis_edge_functions_trigger': pd.DataFrame(),
      'ibm_cis_filter': pd.DataFrame(),
      'ibm_cis_firewall': pd.DataFrame(),
      'ibm_cis_firewall_rules': pd.DataFrame(),
      'ibm_cis_global_load_balancer': pd.DataFrame(),
      'ibm_cis_healthcheck': pd.DataFrame(),
      'ibm_cis_logpush_jobs': pd.DataFrame(),
      'ibm_cis_logpush_jobs': pd.DataFrame(),
      'ibm_cis_mtlss': pd.DataFrame(),
      'ibm_cis_mtls_apps': pd.DataFrame(),
      'ibm_cis_origin_auth': pd.DataFrame(),
      'ibm_cis_origin_pool': pd.DataFrame(),
      'ibm_cis_page_rule': pd.DataFrame(),
      'ibm_cis_range_app': pd.DataFrame(),
      'ibm_cis_rate_limit': pd.DataFrame(),
      'ibm_cis_routing': pd.DataFrame(),
      'ibm_cis_tls_settings': pd.DataFrame(),
      'ibm_cis_waf_group': pd.DataFrame(),
      'ibm_cis_waf_package': pd.DataFrame(),
      'ibm_cis_waf_rule': pd.DataFrame(),
      'ibm_cis_waf_webhook': pd.DataFrame(),

      # Key Management Service
      'ibm_kms_instance_policies': pd.DataFrame(),
      'ibm_kms_key': pd.DataFrame(),
      'ibm_kms_key_alias': pd.DataFrame(),
      'ibm_kms_key_policies': pd.DataFrame(),
      'ibm_kms_key_rings': pd.DataFrame(),
      'ibm_kms_key_with_policy_overrides': pd.DataFrame(),
      'ibm_kp_key': pd.DataFrame(),

      # Kubernetes Service
      'ibm_container_addons': pd.DataFrame(),
      'ibm_container_alb': pd.DataFrame(),
      'ibm_container_alb_cert': pd.DataFrame(),
      'ibm_container_alb_create': pd.DataFrame(),
      'ibm_container_api_key_reset': pd.DataFrame(),
      'ibm_container_bind_service': pd.DataFrame(),
      'ibm_container_cluster': pd.DataFrame(),
      'ibm_container_cluster_feature': pd.DataFrame(),
      'ibm_container_dedicated_host': pd.DataFrame(),
      'ibm_container_dedicated_host_pool': pd.DataFrame(),
      'ibm_container_nlb_dns': pd.DataFrame(),
      'ibm_container_storage_attachment': pd.DataFrame(),
      'ibm_container_vpc_alb': pd.DataFrame(),
      'ibm_container_vpc_alb_create': pd.DataFrame(),
      'ibm_container_vpc_cluster': pd.DataFrame(),
      'ibm_container_vpc_worker': pd.DataFrame(),
      'ibm_container_vpc_worker_pool': pd.DataFrame(),
      'ibm_container_worker_pool_zone_attachment': pd.DataFrame(),
      'ibm_ob_logging': pd.DataFrame(),
      'ibm_ob_monitoring': pd.DataFrame(),

      # Object Storage
      'ibm_cos_bucket': pd.DataFrame(),
      'ibm_cos_bucket_object': pd.DataFrame(),
      'ibm_cos_replication': pd.DataFrame(),

      # Power Systems
      'ibm_pi_capture': pd.DataFrame(),
      'ibm_pi_cloud_connection': pd.DataFrame(),
      'ibm_pi_cloud_connection_network_attach': pd.DataFrame(),
      'ibm_pi_console_language': pd.DataFrame(),
      'ibm_pi_dhcp': pd.DataFrame(),
      'ibm_pi_image': pd.DataFrame(),
      'ibm_pi_image_export': pd.DataFrame(),
      'ibm_pi_instance': pd.DataFrame(),
      'ibm_pi_instance_action': pd.DataFrame(),
      'ibm_pi_key': pd.DataFrame(),
      'ibm_pi_network': pd.DataFrame(),
      'ibm_pi_network_port': pd.DataFrame(),
      'ibm_pi_network_port_attach': pd.DataFrame(),
      'ibm_pi_placement_group': pd.DataFrame(),
      'ibm_pi_shared_processor_pool': pd.DataFrame(),
      'ibm_pi_snapshot': pd.DataFrame(),
      'ibm_pi_spp_placement_group': pd.DataFrame(),
      'ibm_pi_volume': pd.DataFrame(),
      'ibm_pi_volume_attach': pd.DataFrame(),
      'ibm_pi_volume_group': pd.DataFrame(),
      'ibm_pi_volume_group_action': pd.DataFrame(),
      'ibm_pi_volume_onboarding': pd.DataFrame(),
      'ibm_pi_vpn_connection': pd.DataFrame(),
      'ibm_pi_vpn_ike_policy': pd.DataFrame(),
      'ibm_pi_vpn_ipsec_policy': pd.DataFrame(),

      # Push Notifications
      'ibm_pn_application_chrome': pd.DataFrame(),

      # Resource Management
      'ibm_resource_group': pd.DataFrame(),
      'ibm_resource_instance': pd.DataFrame(),
      'ibm_resource_key': pd.DataFrame(),

      # Satellite
      'ibm_satellite_cluster': pd.DataFrame(),
      'ibm_satellite_cluster_worker_pool': pd.DataFrame(),
      'ibm_satellite_cluster_worker_pool_zone_attachment': pd.DataFrame(),
      'ibm_satellite_endpoint': pd.DataFrame(),
      'ibm_satellite_host': pd.DataFrame(),
      'ibm_satellite_link': pd.DataFrame(),
      'ibm_satellite_location': pd.DataFrame(),
      'ibm_satellite_location_nlb_dns': pd.DataFrame(),

      # Schematics
      'ibm_schematics_action': pd.DataFrame(),
      'ibm_schematics_inventory': pd.DataFrame(),
      'ibm_schematics_job': pd.DataFrame(),
      'ibm_schematics_resource_query': pd.DataFrame(),
      'ibm_schematics_workspace': pd.DataFrame(),

      # Secrets Manager
      'ibm_secrets_manager_secret': pd.DataFrame(),
      'ibm_sm_arbitrary_secret': pd.DataFrame(),
      'ibm_sm_en_registration': pd.DataFrame(),
      'ibm_sm_iam_credentials_configuration': pd.DataFrame(),
      'ibm_sm_iam_credentials_secret': pd.DataFrame(),
      'ibm_sm_imported_certificate': pd.DataFrame(),
      'ibm_sm_kv_secret': pd.DataFrame(),
      'ibm_sm_private_certificate': pd.DataFrame(),
      'ibm_sm_private_certificate_configuration_action_set_signed': pd.DataFrame(),
      'ibm_sm_private_certificate_configuration_action_sign_csr': pd.DataFrame(),
      'ibm_sm_private_certificate_configuration_intermediate_ca': pd.DataFrame(),
      'ibm_sm_private_certificate_configuration_root_ca': pd.DataFrame(),
      'ibm_sm_private_certificate_configuration_template': pd.DataFrame(),
      'ibm_sm_public_certificate': pd.DataFrame(),
      'ibm_sm_public_certificate_action_validate_manual_dns': pd.DataFrame(),
      'ibm_sm_public_certificate_configuration_ca_lets_encrypt': pd.DataFrame(),
      'ibm_sm_public_certificate_configuration_dns_cis': pd.DataFrame(),
      'ibm_sm_public_certificate_configuration_dns_classic_infrastructure': pd.DataFrame(),
      'ibm_sm_secret_group': pd.DataFrame(),
      'ibm_sm_service_credentials_secret': pd.DataFrame(),
      'ibm_sm_username_password_secret': pd.DataFrame(),

      # Security and Compliance Center
      'ibm_scc_account_settings': pd.DataFrame(),
      'ibm_scc_posture_collector': pd.DataFrame(),
      'ibm_scc_posture_credential': pd.DataFrame(),
      'ibm_scc_posture_profile_impact': pd.DataFrame(),
      'ibm_scc_posture_scan_initiate_validation': pd.DataFrame(),
      'ibm_scc_posture_scope': pd.DataFrame(),
      'ibm_scc_rule': pd.DataFrame(),
      'ibm_scc_rule_attachment': pd.DataFrame(),
      'ibm_scc_si_note': pd.DataFrame(),
      'ibm_scc_si_occurrence': pd.DataFrame(),
      'ibm_scc_template': pd.DataFrame(),
      'ibm_scc_template_attachment': pd.DataFrame(),

      # Transit Gateway
      'ibm_connection_prefix_filter': pd.DataFrame(),
      'ibm_tg_connection': pd.DataFrame(),
      'ibm_tg_gateway': pd.DataFrame(),
      'ibm_tg_route_report': pd.DataFrame(),

      # VPC Infrastructure
      'ibm_is_backup_policy': pd.DataFrame(),
      'ibm_is_backup_policy_plan': pd.DataFrame(),
      'ibm_is_bare_metal_server': pd.DataFrame(),
      'ibm_is_bare_metal_server_action': pd.DataFrame(),
      'ibm_is_bare_metal_server_disk': pd.DataFrame(),
      'ibm_is_bare_metal_server_network_interface': pd.DataFrame(),
      'ibm_is_bare_metal_server_network_interface_allow_float': pd.DataFrame(),
      'ibm_is_bare_metal_server_network_interface_floating_ip': pd.DataFrame(),
      'ibm_is_dedicated_host': pd.DataFrame(),
      'ibm_is_dedicated_host_disk_management': pd.DataFrame(),
      'ibm_is_dedicated_host_group': pd.DataFrame(),
      'ibm_is_floating_ip': pd.DataFrame(),
      'ibm_is_flow_log': pd.DataFrame(),
      'ibm_is_ike_policy': pd.DataFrame(),
      'ibm_is_image': pd.DataFrame(),
      'ibm_is_instance': pd.DataFrame(),
      'ibm_is_instance_action': pd.DataFrame(),
      'ibm_is_instance_disk_management': pd.DataFrame(),
      'ibm_is_instance_group': pd.DataFrame(),
      'ibm_is_instance_group_manager': pd.DataFrame(),
      'ibm_is_instance_group_manager_action': pd.DataFrame(),
      'ibm_is_instance_group_manager_policy': pd.DataFrame(),
      'ibm_is_instance_group_membership': pd.DataFrame(),
      'ibm_is_instance_network_interface': pd.DataFrame(),
      'ibm_is_instance_network_interface_floating_ip': pd.DataFrame(),
      'ibm_is_instance_template': pd.DataFrame(),
      'ibm_is_instance_volume_attachment': pd.DataFrame(),
      'ibm_is_ipsec_policy': pd.DataFrame(),
      'ibm_is_lb': pd.DataFrame(),
      'ibm_is_lb_listener': pd.DataFrame(),
      'ibm_is_lb_listener_policy': pd.DataFrame(),
      'ibm_is_lb_listener_policy_rule': pd.DataFrame(),
      'ibm_is_lb_pool': pd.DataFrame(),
      'ibm_is_lb_pool_member': pd.DataFrame(),
      'ibm_is_network_acl': pd.DataFrame(),
      'ibm_is_network_acl_rule': pd.DataFrame(),
      'ibm_is_placement_group': pd.DataFrame(),
      'ibm_is_public_gateway': pd.DataFrame(),
      'ibm_is_security_group': pd.DataFrame(),
      'ibm_is_security_group_network_interface_attachment': pd.DataFrame(),
      'ibm_is_security_group_rule': pd.DataFrame(),
      'ibm_is_security_group_target': pd.DataFrame(),
      'ibm_is_snapshot': pd.DataFrame(),
      'ibm_is_ssh_key': pd.DataFrame(),
      'ibm_is_subnet': pd.DataFrame(),
      'ibm_is_subnet_network_acl_attachment': pd.DataFrame(),
      'ibm_is_subnet_public_gateway_attachment': pd.DataFrame(),
      'ibm_is_subnet_reserved_ip': pd.DataFrame(),
      'ibm_is_subnet_routing_table_attachment': pd.DataFrame(),
      'ibm_is_virtual_endpoint_gateway': pd.DataFrame(),
      'ibm_is_virtual_endpoint_gateway_ip': pd.DataFrame(),
      'ibm_is_volume': pd.DataFrame(),
      'ibm_is_vpc': pd.DataFrame(),
      'ibm_is_vpc_address_prefix': pd.DataFrame(),
      'ibm_is_vpc_route': pd.DataFrame(),
      'ibm_is_vpc_routing_table': pd.DataFrame(),
      'ibm_is_vpc_routing_table_route': pd.DataFrame(),
      'ibm_is_vpn_gateway': pd.DataFrame(),
      'ibm_is_vpn_gateway_connection': pd.DataFrame(),
      'ibm_is_vpn_server': pd.DataFrame(),
      'ibm_is_vpn_server_client': pd.DataFrame(),
      'ibm_is_vpn_server_route': pd.DataFrame()
   }
 
   common = None
 
   def __init__(self, common):
      self.common = common
 
   def getResourceDictionary(self):
      return self.resourceDictionary
 
   def getResource(self, name):
      if name in self.resourceDictionary:
         resource = self.resourceDictionary[name]
      else:
         resource = pd.DataFrame()
      return resource

   def loadResources(self):
      if not os.path.isfile(self.common.getInputFile()):
         return False
      
      stream = open(self.common.getInputFile(), 'r', encoding='utf-8-sig')
      data = json_load(stream.read())
      resourcedata = data['resources']
      df = pd.json_normalize(resourcedata)

      for resource in self.resourceDictionary:
         count = 0
         table = {}

         for instances in df[df["type"] == resource]["instances"]:
            for instance in instances:
               attributes = instance["attributes"]
               id = attributes["id"]
               row = {"id": id} | attributes
               #print(row)
               table[count] = row
               count += 1

         if table != {}:
            frame = pd.DataFrame.from_dict(table, orient="index")
         else:
            frame = pd.DataFrame()

         self.resourceDictionary[resource] = frame

      return True

   def loadJSON(self):
      if not os.path.isfile(self.common.getInputFile()):
         return False
      
      instances = pd.DataFrame()
      subnets = pd.DataFrame()
      vpcs = pd.DataFrame()

      stream = open(self.common.getInputFile(), 'r', encoding='utf-8-sig')
      data = json_load(stream.read())

      # Map instances to name, primary_network_interface primary_ip address, id, primary_network_interface subnet, vpc+zone, vpc  
      if 'instances' in data:
         count = 0
         table = {}
         instances = data['instances']

         for instance in instances: 
            name = instance['name']
            id = instance['id']
            vpc = instance['vpcId']
            zone = instance['availabilityZone']
            nics = instance['networkInterfaces']
            nic = nics[0]
            subnet = nic['networkId']
            ip = nic['ip']
            attributes = {'name': name, 'id': id, 'vpc': vpc, 'zone': zone, 'primary_network_interface': [{'primary_ip': [{'address': ip}], 'subnet': subnet}]}
            row = {"id": id} | attributes
            table[count] = row
            count += 1

         if table != {}:
            frame = pd.DataFrame.from_dict(table, orient="index")
         else:
            frame = pd.DataFrame()

         self.resourceDictionary['ibm_is_instance'] = frame

      # Map subnets to name, ipv4_cidr_block, id, vpc, vpc+zone
      if 'subnets' in data:
         count = 0
         table = {}
         subnets = data['subnets']

         for subnet in subnets: 
            name = subnet['name']
            id = subnet['id']
            cidr = subnet['subnet']
            vpc = subnet['vpcId']
            zone = subnet['availabilityZone']
            attributes = {'name': name, 'id': id, 'vpc': vpc, 'zone': zone, 'ipv4_cidr_block': cidr}
            row = {"id": id} | attributes
            table[count] = row
            count += 1

         if table != {}:
            frame = pd.DataFrame.from_dict(table, orient="index")
         else:
            frame = pd.DataFrame()

         self.resourceDictionary['ibm_is_subnet'] = frame

      # Map vpcs to name, id, crn
      if 'vpcs' in data:
         count = 0
         table = {}
         vpcs = data['vpcs']

         for vpc in vpcs: 
            name = vpc['name']
            id = vpc['id']
            region = subnet['region']
            attributes = {'name': name, 'id': id, 'crn': 'crn:v1:bluemix:public:vpc:' + region}
            row = {"id": id} | attributes
            table[count] = row
            count += 1

         if table != {}:
            frame = pd.DataFrame.from_dict(table, orient="index")
         else:
            frame = pd.DataFrame()

         self.resourceDictionary['ibm_is_vpc'] = frame

      return True

