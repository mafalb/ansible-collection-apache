#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021 Markus Falb <markus.falb@mafalb.at>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: httpd_config
author:
  - "Markus Falb (@mafalb)"
version_added: '1.0.0'
notes:
- Supports check_mode
short_description: Manage apache httpd configuration
description:
  - Manage apache httpd configuration
requirements:
  - apache httpd daemon and utilities
options:
  templates:
    description:
    - A list of configuration templates.
    required: True
    type: elements
  scl_prefix:
    description:
    - The prefix of the SCL.
    - Only applicable if apache httpd is packaged as an Software Collection
    required: False
    type: str
"""

EXAMPLES = r"""
- name: httpd configuration as a custom template
  mafalb.apache.httpd_config:
    templates:
    - src: my_custom_template.j2
      dest: /etc/httpd/conf/httpd.conf
    - src: another_template.j2
      dest: /etc/httpd/conf.d/custom.conf

- name: httpd configuration file as a yaml dictionary
  mafalb.apache.httpd_config:
  templates:
  - dest: /etc/httpd/conf.d/custom.conf
    yaml:
      Listen: 8080
"""

RETURN = r"""
container:
    description:
      - Facts representing the current state of the container. Matches the
        buildah inspect output.
      - Note that facts are part of the registered vars since Ansible 2.8. For
        compatibility reasons, the facts
        are also accessible directly as C(buildah_container). Note that the
        returned fact will be removed in Ansible 2.12.
      - Empty if C(state) is I(absent).
    returned: always
    type: dict
"""

from ansible.module_utils.basic import AnsibleModule  # noqa: E402
from ansible_collections.mafalb.containers.plugins.module_utils.buildah.buildah_container_lib import BuildahManager  # noqa: E402
from ansible_collections.mafalb.containers.plugins.module_utils.buildah.buildah_container_lib import ARGUMENTS_SPEC_CONTAINER  # noqa: E402


def main():
    module = AnsibleModule(
        argument_spec=ARGUMENTS_SPEC_CONTAINER,
        supports_check_mode=True,
    )

    results = {}
    module.exit_json(**results)


if __name__ == '__main__':
    main()
