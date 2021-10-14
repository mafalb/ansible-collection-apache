#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021 Markus Falb <markus.falb@mafalb.at>
# GNU General Public License v3.0+
# see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt

# This is a virtual module that is entirely implemented as an action plugin
# and runs on the controller

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: normalize_parameter
short_description: ...
version_added: "0.0.1"
description: ...
options:
  var:
    description:
    - The name of the variable that should act as the input of processing
    - This is used by mafalb.apache.httpd, I dont know if it's useful
    - outside of that.
    type: str
    required: true
author:
- Markus Falb <markus.falb@mafalb.at>
'''

EXAMPLES = r'''
- name: create modified cfgs list
  mafalb.apache.normalize_parameter:
    name: "{{ 'cfgs' if cfgs is defined else 'httpd_cfgs' }}"
  when: cfgs is defined or httpd_cfgs is defined
  register: _cfgs
'''

RETURN = r'''
original_cfgs:
  - dest: _main_config
  - src: bla.conf.j2
    dest: bla.conf
  - dest: bla1.conf
    yaml:
        LogFormat: '"%h gugu" justforCI'
cfgs:
  - src: 'mafalb.apache.httpd.conf.j2'
    dest: /etc/httpd/conf/httpd.conf
  - src: bla.conf.j2
    dest: bla.conf
  - src: 'mafalb.apache.httpd.conf.j2'
    dest: bla1.conf
    yaml:
        LogFormat: '"%h gugu" justforCI'
'''
