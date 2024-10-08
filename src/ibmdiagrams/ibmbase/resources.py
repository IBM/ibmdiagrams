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
      'ibm_resource_group': {},
      'ibm_pi_volume': {},
      'ibm_pi_volume_attach': {},
      'ibm_pi_instance_console_language': {},
      'ibm_pi_instance_action': {},
      'ibm_pi_snapshot': {},
      'ibm_pi_host': {},
      'ibm_pi_ike_policy': {},
      'ibm_pi_host_group': {},
      'ibm_pi_workspace': {},
      'ibm_pi_vpn_connection': {},
      'ibm_pi_capture': {},
      'ibm_pi_volume_group_action': {},
      'ibm_pi_spp_placement_group': {},
      'ibm_pi_volume_onboarding': {},
      'ibm_pi_image_export': {},
      'ibm_pi_network': {},
      'ibm_pi_image': {},
      'ibm_pi_ipsec_policy': {},
      'ibm_pi_volume_clone': {},
      'ibm_pi_shared_processor_pool': {},
      'ibm_pi_instance': {},
      'ibm_pi_cloud_connection': {},
      'ibm_pi_cloud_connection_network_attach': {},
      'ibm_pi_key': {},
      'ibm_pi_placement_group': {},
      'ibm_pi_network_port_attach': {},
      'ibm_pi_dhcp': {},
      'ibm_pi_volume_group': {},
      'ibm_code_engine_build': {},
      'ibm_code_engine_app': {},
      'ibm_code_engine_config_map': {},
      'ibm_code_engine_project': {},
      'ibm_code_engine_job': {},
      'ibm_code_engine_binding': {},
      'ibm_code_engine_secret': {},
      'ibm_code_engine_domain_mapping': {},
      'ibm_database': {},
      'ibm_sm_secret_group': {},
      'ibm_sm_en_registration': {},
      'ibm_sm_public_certificate_configuration_dns_classic_infrastructure': {},
      'ibm_sm_public_certificate_configuration_dns_cis': {},
      'ibm_sm_private_certificate_configuration_action_sign_csr': {},
      'ibm_sm_iam_credentials_secret': {},
      'ibm_sm_arbitrary_secret': {},
      'ibm_sm_service_credentials_secret': {},
      'ibm_sm_private_certificate_configuration_action_set_signed': {},
      'ibm_sm_kv_secret': {},
      'ibm_sm_public_certificate_configuration_ca_lets_encrypt': {},
      'ibm_sm_private_certificate_configuration_intermediate_ca': {},
      'ibm_sm_iam_credentials_configuration': {},
      'ibm_sm_public_certificate_action_validate_manual_dns': {},
      'ibm_sm_imported_certificate': {},
      'ibm_sm_public_certificate': {},
      'ibm_sm_private_certificate_configuration_template': {},
      'ibm_sm_username_password_secret': {},
      'ibm_sm_private_certificate': {},
      'ibm_sm_private_certificate_configuration_root_ca': {},
      'ibm_billing_report_snapshot': {},
      'ibm_onboarding_resource_broker': {},
      'ibm_onboarding_catalog_product': {},
      'ibm_onboarding_product': {},
      'ibm_onboarding_catalog_deployment': {},
      'ibm_onboarding_registration': {},
      'ibm_onboarding_catalog_plan': {},
      'ibm_onboarding_iam_registration': {},
      'ibm_kms_key_with_policy_overrides': {},
      'ibm_kms_key_rings': {},
      'ibm_kms_instance_policies': {},
      'ibm_kms_kmip_client_cert': {},
      'ibm_kms_kmip_adapter': {},
      'ibm_kms_key_policies': {},
      'ibm_kms_key': {},
      'ibm_kp_key': {},
      'ibm_kms_key_alias': {},
      'ibm_en_integration_cos': {},
      'ibm_en_smtp_setting': {},
      'ibm_en_subscription_custom_sms': {},
      'ibm_en_destination_custom_email': {},
      'ibm_en_destination_msteams': {},
      'ibm_en_email_template': {},
      'ibm_en_destination_cf': {},
      'ibm_en_slack_template': {},
      'ibm_en_destination_apns': {},
      'ibm_en_destination_slack': {},
      'ibm_en_subscription_sms': {},
      'ibm_en_destination_fcm': {},
      'ibm_en_FCM_subscription': {},
      'ibm_en_destination_servicenow': {},
      'ibm_en_destination_custom_sms': {},
      'ibm_en_smtp_user': {},
      'ibm_en_destination_safari': {},
      'ibm_en_destination_huawei': {},
      'ibm_en_topic': {},
      'ibm_en_integration': {},
      'ibm_en_subscription_slack': {},
      'ibm_en_destination_pagerduty': {},
      'ibm_en_destination_chrome': {},
      'ibm_en_subscription_webhook': {},
      'ibm_en_destination_ce': {},
      'ibm_en_subscription_email': {},
      'ibm_en_destination_firefox': {},
      'ibm_en_source': {},
      'ibm_en_ibmsource': {},
      'ibm_en_smtp_configuration': {},
      'ibm_en_subscription_custom_email': {},
      'ibm_en_destination_webhook': {},
      'ibm_en_destination_cos': {},
      'ibm_cd_tekton_pipeline_definition': {},
      'ibm_cd_tekton_pipeline_trigger_property': {},
      'ibm_cd_tekton_pipeline_trigger': {},
      'ibm_cd_tekton_pipeline_property': {},
      'ibm_cd_tekton_pipeline': {},
      'ibm_dl_gateway_virtual_connection': {},
      'ibm_dl_gateway_action': {},
      'ibm_dl_provider_gateway': {},
      'ibm_dl_route_report': {},
      'ibm_dl_gateway': {},
      'ibm_enterprise': {},
      'ibm_enterprise_account': {},
      'ibm_enterprise_account_group': {},
      'ibm_metrics_router_settings': {},
      'ibm_metrics_router_target': {},
      'ibm_metrics_router_route': {},
      'ibm_app_route': {},
      'ibm_service_instance': {},
      'ibm_org': {},
      'ibm_app_domain_private': {},
      'ibm_app': {},
      'ibm_space': {},
      'ibm_service_key': {},
      'ibm_app_domain_shared': {},
      'ibm_cloudant_database': {},
      'ibm_cloudant': {},
      'ibm_storage_evault': {},
      'ibm_ipsec_vpn': {},
      'ibm_network_public_ip': {},
      'ibm_dns_domain_registration_nameservers': {},
      'ibm_securitygroup': {},
      'ibm_firewall_policy': {},
      'ibm_compute_vm_instance': {},
      'ibm_lb': {},
      'ibm_dns_reverse_record': {},
      'ibm_securitygroup_rule': {},
      'ibm_firewall': {},
      'ibm_dns_secondary': {},
      'ibm_compute_reserved_capacity': {},
      'ibm_dns_record': {},
      'ibm_network_gateway': {},
      'ibm_network_gateway_vlan_attachment': {},
      'ibm_object_storage_account': {},
      'ibm_compute_dedicated_host': {},
      'ibm_storage_block': {},
      'ibm_lb_service_group': {},
      'ibm_cdn': {},
      'ibm_compute_autoscale_policy': {},
      'ibm_compute_bare_metal': {},
      'ibm_lb_vpx': {},
      'ibm_lb_vpx_vip': {},
      'ibm_network_interface_sg_attachment': {},
      'ibm_storage_file': {},
      'ibm_compute_ssl_certificate': {},
      'ibm_lb_vpx_ha': {},
      'ibm_ssl_certificate': {},
      'ibm_compute_user': {},
      'ibm_lb_service': {},
      'ibm_lbaas_health_monitor': {},
      'ibm_lbaas_server_instance_attachment': {},
      'ibm_lbaas': {},
      'ibm_compute_placement_group': {},
      'ibm_compute_ssh_key': {},
      'ibm_compute_provisioning_hook': {},
      'ibm_compute_autoscale_group': {},
      'ibm_firewall_shared': {},
      'ibm_network_vlan_spanning': {},
      'ibm_network_vlan': {},
      'ibm_multi_vlan_firewall': {},
      'ibm_subnet': {},
      'ibm_compute_monitor': {},
      'ibm_lb_vpx_service': {},
      'ibm_dns_domain': {},
      'ibm_app_config_environment': {},
      'ibm_app_config_feature': {},
      'ibm_app_config_snapshot': {},
      'ibm_app_config_collection': {},
      'ibm_app_config_property': {},
      'ibm_app_config_segment': {},
      'ibm_tg_gateway': {},
      'ibm_tg_connection': {},
      'ibm_resource_key': {},
      'ibm_resource_instance': {},
      'ibm_cos_bucket_object': {},
      'ibm_cos_replication_configuration': {},
      'ibm_cos_bucket': {},
      'ibm_cos_bucket_objectlock_configuration': {},
      'ibm_cos_bucket_website_configuration': {},
      'ibm_project_config': {},
      'ibm_project': {},
      'ibm_project_environment': {},
      'ibm_hpcs_keystore': {},
      'ibm_hpcs_key_template': {},
      'ibm_hpcs': {},
      'ibm_hpcs_vault': {},
      'ibm_hpcs_managed_key': {},
      'ibm_event_streams_topic': {},
      'ibm_event_streams_schema': {},
      'ibm_appid_cloud_directory_template': {},
      'ibm_appid_theme_text': {},
      'ibm_appid_languages': {},
      'ibm_appid_mfa': {},
      'ibm_appid_idp_facebook': {},
      'ibm_appid_idp_custom': {},
      'ibm_appid_application': {},
      'ibm_appid_theme_color': {},
      'ibm_appid_idp_cloud_directory': {},
      'ibm_appid_application_roles': {},
      'ibm_appid_redirect_urls': {},
      'ibm_appid_role': {},
      'ibm_appid_idp_google': {},
      'ibm_appid_user_roles': {},
      'ibm_appid_apm': {},
      'ibm_appid_mfa_channel': {},
      'ibm_appid_cloud_directory_user': {},
      'ibm_appid_application_scopes': {},
      'ibm_appid_token_config': {},
      'ibm_appid_idp_saml': {},
      'ibm_appid_audit_status': {},
      'ibm_appid_action_url': {},
      'ibm_appid_password_regex': {},
      'ibm_logs_data_access_rule': {},
      'ibm_logs_data_usage_metrics': {},
      'ibm_logs_alert': {},
      'ibm_logs_dashboard_folder': {},
      'ibm_logs_rule_group': {},
      'ibm_logs_enrichment': {},
      'ibm_logs_policy': {},
      'ibm_logs_dashboard': {},
      'ibm_logs_outgoing_webhook': {},
      'ibm_logs_view': {},
      'ibm_logs_view_folder': {},
      'ibm_logs_e2m': {},
      'ibm_atracker_route': {},
      'ibm_atracker_target': {},
      'ibm_atracker_settings': {},
      'ibm_resource_access_tag': {},
      'ibm_resource_tag': {},
      'ibm_satellite_link': {},
      'ibm_satellite_storage_assignment': {},
      'ibm_satellite_host': {},
      'ibm_satellite_cluster_worker_pool': {},
      'ibm_satellite_cluster_worker_pool_zone_attachment': {},
      'ibm_satellite_storage_configuration': {},
      'ibm_satellite_location_nlb_dns': {},
      'ibm_satellite_cluster': {},
      'ibm_satellite_location': {},
      'ibm_satellite_endpoint': {},
      'ibm_cr_retention_policy': {},
      'ibm_cr_namespace': {},
      'ibm_iam_user_invite': {},
      'ibm_iam_authorization_policy': {},
      'ibm_iam_user_policy': {},
      'ibm_iam_trusted_profile_policy': {},
      'ibm_iam_access_group_policy': {},
      'ibm_iam_service_policy': {},
      'ibm_iam_authorization_policy_detach': {},
      'ibm_iam_policy_template_version': {},
      'ibm_iam_custom_role': {},
      'ibm_iam_policy_template': {},
      'ibm_iam_policy_assignment': {},
      'ibm_function_namespace': {},
      'ibm_function_action': {},
      'ibm_function_trigger': {},
      'ibm_function_package': {},
      'ibm_function_rule': {},
      'ibm_mqcloud_keystore_certificate': {},
      'ibm_mqcloud_queue_manager': {},
      'ibm_mqcloud_application': {},
      'ibm_mqcloud_truststore_certificate': {},
      'ibm_mqcloud_user': {},
      'ibm_logs-router_tenant': {},
      'ibm_iam_account_settings_template_assignment': {},
      'ibm_iam_trusted_profile_link': {},
      'ibm_iam_user_settings': {},
      'ibm_iam_service_id': {},
      'ibm_iam_api_key': {},
      'ibm_iam_trusted_profile_claim_rule': {},
      'ibm_iam_account_settings_template': {},
      'ibm_iam_trusted_profile_template': {},
      'ibm_iam_trusted_profile': {},
      'ibm_iam_service_api_key': {},
      'ibm_iam_trusted_profile_template_assignment': {},
      'ibm_iam_trusted_profile_identity': {},
      'ibm_iam_account_settings': {},
      'ibm_is_instance_network_interface_floating_ip': {},
      'ibm_is_networkacls': {},
      'ibm_is_ipsec_policy': {},
      'ibm_is_subnet_public_gateway_attachment': {},
      'ibm_is_image': {},
      'ibm_is_share_replica_operations': {},
      'ibm_is_security_group_target': {},
      'ibm_is_image_obsolete': {},
      'ibm_is_lb_listener': {},
      'ibm_is_image_export_job': {},
      'ibm_is_instance_group_membership': {},
      'ibm_is_instance_volume_attachment': {},
      'ibm_is_instance_network_attachment': {},
      'ibm_is_lb': {},
      'ibm_is_vpn_server': {},
      'ibm_is_lb_listener_policy_rule': {},
      'ibm_is_floating_ip': {},
      'ibm_is_snapshot': {},
      'ibm_is_virtual_endpoint_gateway_ip': {},
      'ibm_is_reservation': {},
      'ibm_is_public_gateway': {},
      'ibm_is_instance_template': {},
      'ibm_is_ike_policy': {},
      'ibm_is_virtual_endpoint_gateway': {},
      'ibm_is_share': {},
      'ibm_is_bare_metal_server_action': {},
      'ibm_is_subnet': {},
      'ibm_is_instance_group': {},
      'ibm_is_lb_listener_policy': {},
      'ibm_is_vpc_routing_table': {},
      'ibm_is_backup_policy': {},
      'ibm_is_subnet_routing_table_attachment': {},
      'ibm_is_vpn_server_route': {},
      'ibm_is_instance_action': {},
      'ibm_is_network_acl': {},
      'ibm_is_network_acl_rule': {},
      'ibm_is_subnet_reserved_ip': {},
      'ibm_is_bare_metal_server_network_attachment': {},
      'ibm_is_instance_group_manager': {},
      'ibm_is_bare_metal_server_initialization': {},
      'ibm_is_vpc': {},
      'ibm_is_security_group': {},
      'ibm_is_dedicated_host': {},
      'ibm_is_share_delete_accessor_binding': {},
      'ibm_is_reservation_activate': {},
      'ibm_is_vpn_server_client': {},
      'ibm_is_virtual_network_interface': {},
      'ibm_is_instance_network_interface': {},
      'ibm_is_vpn_gateway_connections': {},
      'ibm_is_bare_metal_server_network_interface_floating_ip': {},
      'ibm_is_bare_metal_server_network_interface': {},
      'ibm_is_bare_metal_server': {},
      'ibm_is_placement_group': {},
      'ibm_is_image_deprecate': {},
      'ibm_is_lb_pool_member': {},
      'ibm_is_snapshot_consistency_group': {},
      'ibm_is_vpc_dns_resolution_binding': {},
      'ibm_is_vpn_gateway': {},
      'ibm_is_lb_pool': {},
      'ibm_is_flow_log': {},
      'ibm_is_vpc_routing_table_route': {},
      'ibm_is_instance': {},
      'ibm_is_bare_metal_server_network_interface_allow_float': {},
      'ibm_is_backup_policy_plan': {},
      'ibm_is_volume': {},
      'ibm_is_ssh_key': {},
      'ibm_is_bare_metal_server_disk': {},
      'ibm_is_subnet_network_acl_attachment': {},
      'ibm_is_share_mount_target': {},
      'ibm_is_dedicated_host_disk_management': {},
      'ibm_is_security_group_rule': {},
      'ibm_is_virtual_network_interface_floating_ip': {},
      'ibm_is_instance_group_manager_policy': {},
      'ibm_is_vpc_address_prefix': {},
      'ibm_is_dedicated_host_group': {},
      'ibm_is_instance_disk_management': {},
      'ibm_is_virtual_network_interface_ip': {},
      'ibm_is_instance_group_manager_action': {},
      'ibm_cbr_zone': {},
      'ibm_cbr_rule': {},
      'ibm_cbr_zone_addresses': {},
      'ibm_cm_object': {},
      'ibm_cm_validation': {},
      'ibm_cm_offering': {},
      'ibm_cm_version': {},
      'ibm_cm_catalog': {},
      'ibm_cm_offering_instance': {},
      'ibm_cd_toolchain_tool_gitlab': {},
      'ibm_cd_toolchain_tool_hostedgit': {},
      'ibm_cd_toolchain_tool_privateworker': {},
      'ibm_cd_toolchain_tool_bitbucketgit': {},
      'ibm_cd_toolchain_tool_slack': {},
      'ibm_cd_toolchain_tool_nexus': {},
      'ibm_cd_toolchain_tool_saucelabs': {},
      'ibm_cd_toolchain_tool_artifactory': {},
      'ibm_cd_toolchain_tool_pagerduty': {},
      'ibm_cd_toolchain_tool_securitycompliance': {},
      'ibm_cd_toolchain_tool_custom': {},
      'ibm_cd_toolchain_tool_keyprotect': {},
      'ibm_cd_toolchain_tool_secretsmanager': {},
      'ibm_cd_toolchain': {},
      'ibm_cd_toolchain_tool_jenkins': {},
      'ibm_cd_toolchain_tool_githubconsolidated': {},
      'ibm_cd_toolchain_tool_eventnotifications': {},
      'ibm_cd_toolchain_tool_pipeline': {},
      'ibm_cd_toolchain_tool_jira': {},
      'ibm_cd_toolchain_tool_hashicorpvault': {},
      'ibm_cd_toolchain_tool_devopsinsights': {},
      'ibm_cd_toolchain_tool_appconfig': {},
      'ibm_cd_toolchain_tool_sonarqube': {},
      'ibm_scc_profile_attachment': {},
      'ibm_scc_rule': {},
      'ibm_scc_instance_settings': {},
      'ibm_scc_profile': {},
      'ibm_scc_template_attachment': {},
      'ibm_scc_rule_attachment': {},
      'ibm_scc_template': {},
      'ibm_scc_account_settings': {},
      'ibm_scc_provider_type_instance': {},
      'ibm_scc_control_library': {},
      'ibm_ob_monitoring': {},
      'ibm_container_ingress_secret_tls': {},
      'ibm_container_worker_pool_zone_attachment': {},
      'ibm_container_api_key_reset': {},
      'ibm_container_ingress_instance': {},
      'ibm_container_alb_cert': {},
      'ibm_container_vpc_worker': {},
      'ibm_container_vpc_worker_pool': {},
      'ibm_container_vpc_alb': {},
      'ibm_container_dedicated_host': {},
      'ibm_container_addons': {},
      'ibm_container_vpc_cluster': {},
      'ibm_container_alb': {},
      'ibm_container_bind_service': {},
      'ibm_container_vpc_alb_create': {},
      'ibm_container_dedicated_host_pool': {},
      'ibm_container_nlb_dns': {},
      'ibm_container_ingress_secret_opaque': {},
      'ibm_container_cluster': {},
      'ibm_container_alb_create': {},
      'ibm_container_cluster_feature': {},
      'ibm_ob_logging': {},
      'ibm_container_worker_pool': {},
      'ibm_container_storage_attachment': {},
      'ibm_private_dns_custom_resolver': {},
      'ibm_private_dns_custom_resolver_forwarding_rule': {},
      'ibm_dns_linked_zone': {},
      'ibm_private_dns_custom_resolver_location': {},
      'ibm_private_dns_custom_resolver_secondary_zone': {},
      'ibm_private_dns_permitted_network': {},
      'ibm_private_dns_resource_record': {},
      'ibm_private_dns_zones': {},
      'ibm_private_dns_glb_monitor': {},
      'ibm_private_dns_glb_pool': {},
      'ibm_private_dns_glb': {},
      'ibm_push_notification_chrome': {},
      'ibm_schematics_inventory': {},
      'ibm_schematics_agent_prs': {},
      'ibm_schematics_resource_query': {},
      'ibm_schematics_workspace': {},
      'ibm_schematics_agent': {},
      'ibm_schematics_action': {},
      'ibm_schematics_policy': {},
      'ibm_schematics_agent_deploy': {},
      'ibm_schematics_job': {},
      'ibm_schematics_agent_health': {},
      'ibm_iam_access_group_dynamic_rule': {},
      'ibm_iam_access_group_template_version': {},
      'ibm_iam_access_group': {},
      'ibm_iam_access_group_template': {},
      'ibm_iam_access_group_template_assignment': {},
      'ibm_iam_access_group_members': {},
      'ibm_iam_access_group_account_settings': {},
      'ibm_cloud_shell_account_settings': {},
      'ibm_cis_waf_package': {},
      'ibm_cis_ruleset_rule': {},
      'ibm_cis_alert': {},
      'ibm_cis_ruleset': {},
      'ibm_cis_dns_records_import': {},
      'ibm_cis_mtls_app': {},
      'ibm_cis_origin_auth': {},
      'ibm_cis_page_rule': {},
      'ibm_cis_mtls': {},
      'ibm_cis_ruleset_entrypoint_version': {},
      'ibm_cis_waf_rule': {},
      'ibm_cis': {},
      'ibm_cis_firewall_rules': {},
      'ibm_cis_healthcheck': {},
      'ibm_cis_origin_certificate_order': {},
      'ibm_cis_advanced_certificate_pack_order': {},
      'ibm_cis_certificate_order': {},
      'ibm_cis_domain_settings': {},
      'ibm_cis_range_app': {},
      'ibm_cis_domain': {},
      'ibm_cis_custom_page': {},
      'ibm_cis_ruleset_version_detach': {},
      'ibm_cis_alert_webhook': {},
      'ibm_cis_cache_settings': {},
      'ibm_cis_certificate_upload': {},
      'ibm_cis_routing': {},
      'ibm_cis_waf_group': {},
      'ibm_cis_logpush_job': {},
      'ibm_cis_global_load_balancer': {},
      'ibm_cis_tls_settings': {},
      'ibm_cis_dns_record': {},
      'ibm_cis_firewall': {},
      'ibm_cis_edge_functions_trigger': {},
      'ibm_cis_edge_functions_action': {},
      'ibm_cis_origin_pool': {},
      'ibm_cis_rate_limit': {},
      'ibm_cis_bot_management': {},
      'ibm_cis_filter': {},
      'ibm_api_gateway_endpoint_subscription': {},
      'ibm_api_gateway_endpoint': {},
      'ibm_pag_instance': {},
      'ibm_vmaas_vdc': {},
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
