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

## Variables

```yaml
httpd_service_enabled: true
```

```yaml
scl_prefix: httpd24
```

## License

GPL-3.0-or-later
