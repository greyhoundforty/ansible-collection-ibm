#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_dns_record
short_description: Configure IBM Cloud 'ibm_cis_dns_record' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_dns_record' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    cis_id:
        description:
            - (Required for new resource) CIS object id
        required: False
        type: str
    domain_id:
        description:
            - (Required for new resource) Associated CIS domain
        required: False
        type: str
    content:
        description:
            - None
        required: False
        type: str
    proxied:
        description:
            - None
        required: False
        type: bool
        default: False
    created_on:
        description:
            - None
        required: False
        type: str
    name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    type:
        description:
            - (Required for new resource) 
        required: False
        type: str
    data:
        description:
            - None
        required: False
        type: dict
        elements: dict
    priority:
        description:
            - None
        required: False
        type: int
    modified_on:
        description:
            - None
        required: False
        type: str
    proxiable:
        description:
            - None
        required: False
        type: bool
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be provided
              via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('cis_id', 'str'),
    ('domain_id', 'str'),
    ('name', 'str'),
    ('type', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'cis_id',
    'domain_id',
    'content',
    'proxied',
    'created_on',
    'name',
    'type',
    'data',
    'priority',
    'modified_on',
    'proxiable',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    cis_id=dict(
        required=False,
        type='str'),
    domain_id=dict(
        required=False,
        type='str'),
    content=dict(
        required=False,
        type='str'),
    proxied=dict(
        default=False,
        type='bool'),
    created_on=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    data=dict(
        required=False,
        elements='',
        type='dict'),
    priority=dict(
        required=False,
        type='int'),
    modified_on=dict(
        required=False,
        type='str'),
    proxiable=dict(
        required=False,
        type='bool'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south')
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_cis_dns_record',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.3',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
