#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021 Markus Falb <markus.falb@mafalb.at>
# GNU General Public License v3.0+
# see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt

from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleError
from ansible.parsing.yaml.objects import AnsibleMapping


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect
        result['changed'] = False
        result['failed'] = False
        result['template_options'] = []

        templates = task_vars['httpd_templates']
        if not isinstance(templates, list):
            raise AnsibleError("httpd_templates is not a list")
        if templates == []:
            return result
        for t in templates:
            if not isinstance(t, AnsibleMapping):
                raise AnsibleError("t is not an AnsibleMapping: {}".format(t))
            # mangle destination
            if t['dest'] == '_main_config':
                t['dest'] = self._templar.template(task_vars['httpd_main_cfg'])
            elif not t['dest'].startswith('/'):
                t['dest'] = self._templar.template(task_vars['httpd_conf_d']) +
                            '/' + self._templar.template(t['dest'])
            # mangle src
            if 'src' not in t:
                t['src'] = 'mafalb.apache.httpd.conf.j2'
            # mangle mode
            if 'mode' not in t:
                t['mode'] = self._templar.template(task_vars['httpd_cfg_mode'])
            # remove yaml
            if 'yaml' in t:
                del t['yaml']
            # add backup option
            t['backup'] = True
        result['template_options'] = templates
        return result
