
ibm_lbaas_info -- Retrieve IBM Cloud 'ibm_lbaas' resource
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_lbaas' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.3
- Terraform v0.12.20



Parameters
----------

  datacenter (False, str, None)
    None


  vip (False, str, None)
    None


  use_system_public_ip_pool (False, bool, None)
    None


  server_instances (False, list, None)
    None


  name (True, str, None)
    None


  protocols (False, list, None)
    None


  description (False, str, None)
    None


  health_monitors (False, list, None)
    None


  server_instances_up (False, int, None)
    None


  status (False, str, None)
    None


  server_instances_down (False, int, None)
    None


  active_connections (False, int, None)
    None


  ssl_ciphers (False, list, None)
    None


  type (False, str, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

