# Ansible Role mafalb.apache.httpd

## Basic Usage

```yaml
- name: install httpd with vendor config
  hosts: localhost
  roles:
  - role: mafalb.apache.httpd
```

```yaml
- name: install httpd as Software Collection
  hosts: localhost
  roles:
  - role: mafalb.apache.httpd
    httpd_scl_prefix: httpd24
```

```yaml
- name: install httpd
  hosts: localhost
  roles:
  - role: mafalb.apache.httpd
    templates:
    - dest: __main_config  # special name for main config
      yaml: { ... }  # config as yaml
    - src: myowntemplate.j2  # config as template
      dest: myowntemplate.conf
    - dest: test.conf
      yaml:  # config as yaml
        EnableSendfile: 'on'
      dest: test.conf
```

The above config snippet shows that there are multiple ways to specify the configuration.
If you specify src, then the template will be used.
If you specify yaml, then the provided default template will be used which translates the provided yaml dict into apache config.

## Variables

```yaml
state: present  # apache httpd is installed
```

```yaml
state: absent  # apache httpd is not installed
```

```yaml
state: cfg  # apache httpd variables are set
```

```yaml
httpd_service_enabled: true
```

```yaml
httpd_cfg_mode: '644'  # the mode of the cfg files
httpd_cfg_owner: 'root'  # the owner of the cfg files
httpd_cfg_group: 'root'  # the group of the cfg files
```

```yaml
httpd_scl_prefix: httpd24
```

```yaml
httpd_templates: [ ... ]  # list of config files
```

## License

GPL-3.0-or-later
