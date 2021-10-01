# Ansible Role mafalb.apache.httpd

## Basic Usage

```yaml
- name: install httpd
  hosts: localhost
  roles:
  - role: mafalb.apache.httpd
```

```yaml
- name: install httpd as Software Collection
  hosts: localhost
  roles:
  - role: mafalb.apache.httpd
    scl_prefix: httpd24
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


## Variables

```yaml
httpd_service_enabled: true
```

```yaml
scl_prefix: httpd24
```

## License

GPL-3.0-or-later
