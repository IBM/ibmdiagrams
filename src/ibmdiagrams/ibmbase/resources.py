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
 
class Resources:
   resourceDictionary = {
      # Activity Tracker API
      'ibm_atracker_route': {},
      'ibm_atracker_settings': {},
      'ibm_atracker_target': {},

      # App Configuration
      'ibm_app_config_collection': {},
      'ibm_app_config_environment': {},
      'ibm_app_config_feature': {},
      'ibm_app_config_property': {},
      'ibm_app_config_segment': {},
      'ibm_app_config_snapshot': {},

      # AppID Management
      'ibm_appid_action_url': {},
      'ibm_appid_apm': {},
      'ibm_appid_application': {},
      'ibm_appid_application_roles': {},
      'ibm_appid_application_scopes': {},
      'ibm_appid_audit_status': {},
      'ibm_appid_cloud_directory_template': {},
      'ibm_appid_cloud_directory_user': {},
      'ibm_appid_idp_cloud_directory': {},
      'ibm_appid_idp_custom': {},
      'ibm_appid_idp_facebook': {},
      'ibm_appid_idp_google': {},
      'ibm_appid_idp_saml': {},
      'ibm_appid_languages': {},
      'ibm_appid_mfa': {},
      'ibm_appid_mfa_channel': {},
      'ibm_appid_password_regex': {},
      'ibm_appid_redirect_urls': {},
      'ibm_appid_role': {},
      'ibm_appid_theme_color': {},
      'ibm_appid_theme_text': {},
      'ibm_appid_token_config': {},
      'ibm_appid_user_roles': {},

      # Catalog Management
      'ibm_cm_catalog': {},
      'ibm_cm_object': {},
      'ibm_cm_offering': {},
      'ibm_cm_offering_instance': {},
      'ibm_cm_version': {},

      # Certificate Manager
      'ibm_certificate_manager_import': {},
      'ibm_certificate_manager_order': {},

      # Classic Infrastructure
      'ibm_cdn': {},
      'ibm_compute_autoscale_group': {},
      'ibm_compute_autoscale_policy': {},
      'ibm_compute_bare_metal': {},
      'ibm_compute_dedicated_host': {},
      'ibm_compute_monitor': {},
      'ibm_compute_placement_group': {},
      'ibm_compute_provisioning_hook': {},
      'ibm_compute_reserved_capacity': {},
      'ibm_compute_ssh_key': {},
      'ibm_compute_ssl_certificate': {},
      'ibm_compute_user': {},
      'ibm_compute_vm_instance': {},
      'ibm_dns_domain': {},
      'ibm_dns_domain_registration_nameservers': {},
      'ibm_dns_record': {},
      'ibm_dns_reverse_record': {},
      'ibm_dns_secondary': {},
      'ibm_firewall': {},
      'ibm_firewall_policy': {},
      'ibm_hardware_firewall_shared': {},
      'ibm_ipsec_vpn': {},
      'ibm_lb': {},
      'ibm_lb_service': {},
      'ibm_lb_service_group': {},
      'ibm_lb_vpx': {},
      'ibm_lb_vpx_ha': {},
      'ibm_lb_vpx_service': {},
      'ibm_lb_vpx_vip': {},
      'ibm_lbaas': {},
      'ibm_lbaas_health_monitor': {},
      'ibm_lbaas_server_instance_attachment': {},
      'ibm_multi_vlan_firewall': {},
      'ibm_network_gateway': {},
      'ibm_network_gateway_vlan_association': {},
      'ibm_network_interface_sg_attachment': {},
      'ibm_network_public_ip': {},
      'ibm_network_vlan': {},
      'ibm_network_vlan_spanning': {},
      'ibm_object_storage_account': {},
      'ibm_security_group': {},
      'ibm_security_group_rule': {},
      'ibm_ssl_certificate': {},
      'ibm_storage_block': {},
      'ibm_storage_evault': {},
      'ibm_storage_file': {},
      'ibm_subnet': {},

      # Cloud Databases
      'ibm_database': {},

      # Cloud Foundry
      'ibm_app': {},
      'ibm_app_domain_private': {},
      'ibm_app_domain_shared': {},
      'ibm_app_route': {},
      'ibm_org': {},
      'ibm_service_instance': {},
      'ibm_service_key': {},
      'ibm_space': {},

      # Cloudant Databases
      'ibm_cloudant': {},
      'ibm_cloudant_database': {},

      # Container Registry
      'ibm_cr_namespace': {},
      'ibm_cr_retention_policy': {},

      # Context Based Restrictions
      'ibm_cbr_rule': {},
      'ibm_cbr_zone': {},

       # Continuous Delivery
      'ibm_cd_tekton_pipeline': {},
      'ibm_cd_tekton_pipeline_definition': {},
      'ibm_cd_tekton_pipeline_property': {},
      'ibm_cd_tekton_pipeline_trigger': {},
      'ibm_cd_toolchain': {},
      'ibm_cd_toolchain_tool_appconfig': {},
      'ibm_cd_toolchain_tool_artifactory': {},
      'ibm_cd_toolchain_tool_bitbucketgit': {},
      'ibm_cd_toolchain_tool_custom': {},
      'ibm_cd_toolchain_tool_devopsinsights': {},
      'ibm_cd_toolchain_tool_githubconsolidated': {},
      'ibm_cd_toolchain_tool_gitlab': {},
      'ibm_cd_toolchain_tool_hashicorpvault': {},
      'ibm_cd_toolchain_tool_hostedgit': {},
      'ibm_cd_toolchain_tool_jenkins': {},
      'ibm_cd_toolchain_tool_jira': {},
      'ibm_cd_toolchain_tool_keyprotect': {},
      'ibm_cd_toolchain_tool_nexus': {},
      'ibm_cd_toolchain_tool_pagerduty': {},
      'ibm_cd_toolchain_tool_pipeline': {},
      'ibm_cd_toolchain_tool_privateworker': {},
      'ibm_cd_toolchain_tool_saucelabs': {},
      'ibm_cd_toolchain_tool_secretsmanager': {},
      'ibm_cd_toolchain_tool_securitycompliance': {},
      'ibm_cd_toolchain_tool_slack': {},
      'ibm_cd_toolchain_tool_sonarqube': {},

      # DNS Services
      'ibm_dns_custom_resolver': {},
      'ibm_dns_custom_resolver_forwarding_rule': {},
      'ibm_dns_custom_resolver_location': {},
      'ibm_dns_custom_resolver_secondary_zone': {},
      'ibm_dns_glb': {},
      'ibm_dns_glb_monitor': {},
      'ibm_dns_glb_pool': {},
      'ibm_dns_glb_permitted_network': {},
      'ibm_dns_resource_record': {},
      'ibm_dns_zone': {},

      # Direct Link
      'ibm_dl_gateway': {},
      'ibm_dl_provider_gateway': {},
      'ibm_dl_route_report': {},
      'ibm_dl_virtual_connection': {},

      # Enterprise Management
      'ibm_enterprise': {},
      'ibm_enterprise_account': {},
      'ibm_enterprise_account_group': {},

      # Event Notifications
      'ibm_en_destination': {},
      'ibm_en_destination_android': {},
      'ibm_en_destination_ce': {},
      'ibm_en_destination_cf': {},
      'ibm_en_destination_chrome': {},
      'ibm_en_integration_cos': {},
      'ibm_en_destination_firefox': {},
      'ibm_en_destination_huawei': {},
      'ibm_en_destination_ios': {},
      'ibm_en_destination_mstreams': {},
      'ibm_en_destination_pagerduty': {},
      'ibm_en_destination_safari': {},
      'ibm_en_destination_slack': {},
      'ibm_en_destination_webhook': {},
      'ibm_en_ibmsource': {},
      'ibm_en_integration': {},
      'ibm_en_source': {},
      'ibm_en_subscription': {},
      'ibm_en_subscription_android': {},
      'ibm_en_subscription_ce': {},
      'ibm_en_subscription_cf': {},
      'ibm_en_subscription_chrome': {},
      'ibm_en_subscription_email': {},
      'ibm_en_subscription_firefox': {},
      'ibm_en_subscription_ios': {},
      'ibm_en_subscription_mstreams': {},
      'ibm_en_subscription_pagerduty': {},
      'ibm_en_subscription_safari': {},
      'ibm_en_subscription_slack': {},
      'ibm_en_subscription_sms': {},
      'ibm_en_subscription_sn': {},
      'ibm_en_subscription_webhook': {},
      'ibm_en_topic': {},

      # Event Streams
      'ibm_event_streams_schema': {},
      'ibm_event_streams_topic': {},

      # functions
      'ibm_function_action': {},
      'ibm_function_namespace': {},
      'ibm_function_package': {},
      'ibm_function_rule': {},
      'ibm_function_trigger': {},

      # Global Tagging
      'ibm_resource_tag': {},

      # Hyper Protect Crypto Services
      'ibm_hpcs': {},
      'ibm_hpcs_key_template': {},
      'ibm_hpcs_keystore': {},
      'ibm_hpcs_managed_key': {},
      'ibm_hpcs_vault': {},

      # Cloud Shell
      'ibm_cloud_shell_account_settings': {},

      # Identity & Access Management (IAM)
      'ibm_api_key': {},
      'ibm_iam_access_group': {},
      'ibm_iam_access_group_account_settings': {},
      'ibm_iam_access_group_dynamic_rule': {},
      'ibm_iam_access_group_members': {},
      'ibm_iam_access_group_policy': {},
      'ibm_iam_account_settings': {},
      'ibm_iam_authorization_policy': {},
      'ibm_iam_authorization_policy_detach': {},
      'ibm_iam_custom_role': {},
      'ibm_iam_service-api-key': {},
      'ibm_iam_service_id': {},
      'ibm_iam_service_policy': {},
      'ibm_iam_trusted_profile': {},
      'ibm_iam_trusted_profile_claim_rule': {},
      'ibm_iam_trusted_profile_link': {},
      'ibm_iam_trusted_profile_policy': {},
      'ibm_iam_user_invite': {},
      'ibm_iam_user_policy': {},
      'ibm_iam_user_settings': {},

      # Internet Services
      'ibm_cis': {},
      'ibm_cis_alert': {},
      'ibm_cis_cache_settings': {},
      'ibm_cis_certificate_order': {},
      'ibm_cis_certificate_upload': {},
      'ibm_cis_custom_page': {},
      'ibm_cis_custom_page': {},
      'ibm_cis_dns_record': {},
      'ibm_cis_dns_records_import': {},
      'ibm_cis_domain': {},
      'ibm_cis_domain_settings': {},
      'ibm_cis_edge_functions_action': {},
      'ibm_cis_edge_functions_trigger': {},
      'ibm_cis_filter': {},
      'ibm_cis_firewall': {},
      'ibm_cis_firewall_rules': {},
      'ibm_cis_global_load_balancer': {},
      'ibm_cis_healthcheck': {},
      'ibm_cis_logpush_jobs': {},
      'ibm_cis_logpush_jobs': {},
      'ibm_cis_mtlss': {},
      'ibm_cis_mtls_apps': {},
      'ibm_cis_origin_auth': {},
      'ibm_cis_origin_pool': {},
      'ibm_cis_page_rule': {},
      'ibm_cis_range_app': {},
      'ibm_cis_rate_limit': {},
      'ibm_cis_routing': {},
      'ibm_cis_tls_settings': {},
      'ibm_cis_waf_group': {},
      'ibm_cis_waf_package': {},
      'ibm_cis_waf_rule': {},
      'ibm_cis_waf_webhook': {},

      # Key Management Service
      'ibm_kms_instance_policies': {},
      'ibm_kms_key': {},
      'ibm_kms_key_alias': {},
      'ibm_kms_key_policies': {},
      'ibm_kms_key_rings': {},
      'ibm_kms_key_with_policy_overrides': {},
      'ibm_kp_key': {},

      # Kubernetes Service
      'ibm_container_addons': {},
      'ibm_container_alb': {},
      'ibm_container_alb_cert': {},
      'ibm_container_alb_create': {},
      'ibm_container_api_key_reset': {},
      'ibm_container_bind_service': {},
      'ibm_container_cluster': {},
      'ibm_container_cluster_feature': {},
      'ibm_container_dedicated_host': {},
      'ibm_container_dedicated_host_pool': {},
      'ibm_container_nlb_dns': {},
      'ibm_container_storage_attachment': {},
      'ibm_container_vpc_alb': {},
      'ibm_container_vpc_alb_create': {},
      'ibm_container_vpc_cluster': {},
      'ibm_container_vpc_worker': {},
      'ibm_container_vpc_worker_pool': {},
      'ibm_container_worker_pool_zone_attachment': {},
      'ibm_ob_logging': {},
      'ibm_ob_monitoring': {},

      # Object Storage
      'ibm_cos_bucket': {},
      'ibm_cos_bucket_object': {},
      'ibm_cos_replication': {},

      # Power Systems
      'ibm_pi_capture': {},
      'ibm_pi_cloud_connection': {},
      'ibm_pi_cloud_connection_network_attach': {},
      'ibm_pi_console_language': {},
      'ibm_pi_dhcp': {},
      'ibm_pi_image': {},
      'ibm_pi_image_export': {},
      'ibm_pi_instance': {},
      'ibm_pi_instance_action': {},
      'ibm_pi_key': {},
      'ibm_pi_network': {},
      'ibm_pi_network_port': {},
      'ibm_pi_network_port_attach': {},
      'ibm_pi_placement_group': {},
      'ibm_pi_shared_processor_pool': {},
      'ibm_pi_snapshot': {},
      'ibm_pi_spp_placement_group': {},
      'ibm_pi_volume': {},
      'ibm_pi_volume_attach': {},
      'ibm_pi_volume_group': {},
      'ibm_pi_volume_group_action': {},
      'ibm_pi_volume_onboarding': {},
      'ibm_pi_vpn_connection': {},
      'ibm_pi_vpn_ike_policy': {},
      'ibm_pi_vpn_ipsec_policy': {},

      # Push Notifications
      'ibm_pn_application_chrome': {},

      # Resource Management
      'ibm_resource_group': {},
      'ibm_resource_instance': {},
      'ibm_resource_key': {},

      # Satellite
      'ibm_satellite_cluster': {},
      'ibm_satellite_cluster_worker_pool': {},
      'ibm_satellite_cluster_worker_pool_zone_attachment': {},
      'ibm_satellite_endpoint': {},
      'ibm_satellite_host': {},
      'ibm_satellite_link': {},
      'ibm_satellite_location': {},
      'ibm_satellite_location_nlb_dns': {},

      # Schematics
      'ibm_schematics_action': {},
      'ibm_schematics_inventory': {},
      'ibm_schematics_job': {},
      'ibm_schematics_resource_query': {},
      'ibm_schematics_workspace': {},

      # Secrets Manager
      'ibm_secrets_manager_secret': {},
      'ibm_sm_arbitrary_secret': {},
      'ibm_sm_en_registration': {},
      'ibm_sm_iam_credentials_configuration': {},
      'ibm_sm_iam_credentials_secret': {},
      'ibm_sm_imported_certificate': {},
      'ibm_sm_kv_secret': {},
      'ibm_sm_private_certificate': {},
      'ibm_sm_private_certificate_configuration_action_set_signed': {},
      'ibm_sm_private_certificate_configuration_action_sign_csr': {},
      'ibm_sm_private_certificate_configuration_intermediate_ca': {},
      'ibm_sm_private_certificate_configuration_root_ca': {},
      'ibm_sm_private_certificate_configuration_template': {},
      'ibm_sm_public_certificate': {},
      'ibm_sm_public_certificate_action_validate_manual_dns': {},
      'ibm_sm_public_certificate_configuration_ca_lets_encrypt': {},
      'ibm_sm_public_certificate_configuration_dns_cis': {},
      'ibm_sm_public_certificate_configuration_dns_classic_infrastructure': {},
      'ibm_sm_secret_group': {},
      'ibm_sm_service_credentials_secret': {},
      'ibm_sm_username_password_secret': {},

      # Security and Compliance Center
      'ibm_scc_account_settings': {},
      'ibm_scc_posture_collector': {},
      'ibm_scc_posture_credential': {},
      'ibm_scc_posture_profile_impact': {},
      'ibm_scc_posture_scan_initiate_validation': {},
      'ibm_scc_posture_scope': {},
      'ibm_scc_rule': {},
      'ibm_scc_rule_attachment': {},
      'ibm_scc_si_note': {},
      'ibm_scc_si_occurrence': {},
      'ibm_scc_template': {},
      'ibm_scc_template_attachment': {},

      # Transit Gateway
      'ibm_connection_prefix_filter': {},
      'ibm_tg_connection': {},
      'ibm_tg_gateway': {},
      'ibm_tg_route_report': {},

      # VPC Infrastructure
      'ibm_is_backup_policy': {},
      'ibm_is_backup_policy_plan': {},
      'ibm_is_bare_metal_server': {},
      'ibm_is_bare_metal_server_action': {},
      'ibm_is_bare_metal_server_disk': {},
      'ibm_is_bare_metal_server_network_interface': {},
      'ibm_is_bare_metal_server_network_interface_allow_float': {},
      'ibm_is_bare_metal_server_network_interface_floating_ip': {},
      'ibm_is_dedicated_host': {},
      'ibm_is_dedicated_host_disk_management': {},
      'ibm_is_dedicated_host_group': {},
      'ibm_is_floating_ip': {},
      'ibm_is_flow_log': {},
      'ibm_is_ike_policy': {},
      'ibm_is_image': {},
      'ibm_is_instance': {},
      'ibm_is_instance_action': {},
      'ibm_is_instance_disk_management': {},
      'ibm_is_instance_group': {},
      'ibm_is_instance_group_manager': {},
      'ibm_is_instance_group_manager_action': {},
      'ibm_is_instance_group_manager_policy': {},
      'ibm_is_instance_group_membership': {},
      'ibm_is_instance_network_interface': {},
      'ibm_is_instance_network_interface_floating_ip': {},
      'ibm_is_instance_template': {},
      'ibm_is_instance_volume_attachment': {},
      'ibm_is_ipsec_policy': {},
      'ibm_is_lb': {},
      'ibm_is_lb_listener': {},
      'ibm_is_lb_listener_policy': {},
      'ibm_is_lb_listener_policy_rule': {},
      'ibm_is_lb_pool': {},
      'ibm_is_lb_pool_member': {},
      'ibm_is_network_acl': {},
      'ibm_is_network_acl_rule': {},
      'ibm_is_placement_group': {},
      'ibm_is_public_gateway': {},
      'ibm_is_security_group': {},
      'ibm_is_security_group_network_interface_attachment': {},
      'ibm_is_security_group_rule': {},
      'ibm_is_security_group_target': {},
      'ibm_is_snapshot': {},
      'ibm_is_ssh_key': {},
      'ibm_is_subnet': {},
      'ibm_is_subnet_network_acl_attachment': {},
      'ibm_is_subnet_public_gateway_attachment': {},
      'ibm_is_subnet_reserved_ip': {},
      'ibm_is_subnet_routing_table_attachment': {},
      'ibm_is_virtual_endpoint_gateway': {},
      'ibm_is_virtual_endpoint_gateway_ip': {},
      'ibm_is_volume': {},
      'ibm_is_vpc': {},
      'ibm_is_vpc_address_prefix': {},
      'ibm_is_vpc_route': {},
      'ibm_is_vpc_routing_table': {},
      'ibm_is_vpc_routing_table_route': {},
      'ibm_is_vpn_gateway': {},
      'ibm_is_vpn_gateway_connection': {},
      'ibm_is_vpn_server': {},
      'ibm_is_vpn_server_client': {},
      'ibm_is_vpn_server_route': {},
      'lastmarker': {}
   }
 
   common = None
 
   def __init__(self, common, df):
      self.common = common
      for resource in self.resourceDictionary:
         if resource != 'finalmarker':
            self.resourceDictionary[resource] = df[df["type"] == resource]["instances"]
 
   def getResourceDictionary(self):
      return self.resourceDictionary
 
   def setResource(self, name, df):
      if name in self.resourceDictionary:
         self.resourceDictionary[name] = df[df["type"] == name]["instances"]
 
   def getResource(self, name):
      if name in self.resourceDictionary:
         resource = self.resourceDictionary[name]
      else:
         resource = None
      return resource
