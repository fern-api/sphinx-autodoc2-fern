---
layout: overview
slug: nemo-curator-metrics-constants
---

# nemo_curator.metrics.constants



## Module Contents

### Data

`DEFAULT_NEMO_CURATOR_METRICS_PATH`
`GRAFANA_VERSION`
`PROMETHEUS_YAML_TEMPLATE`
`GRAFANA_INI_TEMPLATE`
`GRAFANA_DASHBOARD_YAML_TEMPLATE`
`GRAFANA_DATASOURCE_YAML_TEMPLATE`
`DEFAULT_PROMETHEUS_WEB_PORT`
`DEFAULT_GRAFANA_WEB_PORT`

### API

```python
nemo_curator.metrics.constants.DEFAULT_NEMO_CURATOR_METRICS_PATH
```

**Value**: `/tmp/nemo_curator_metrics`


```python
nemo_curator.metrics.constants.GRAFANA_VERSION
```

**Value**: `12.0.2`


```python
nemo_curator.metrics.constants.PROMETHEUS_YAML_TEMPLATE
```

**Value**: `
global:
  scrape_interval: 10s # Set the scrape interval to every 10 seconds. Default is every 1 minute.
  evaluation_interval: 10s # Evaluate rules every 10 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

scrape_configs:
# Scrape from each Ray node as defined in the service_discovery.json provided by Ray.
- job_name: 'ray'
  file_sd_configs:
  - files:
    - /tmp/ray/prom_metrics_service_discovery.json
`


```python
nemo_curator.metrics.constants.GRAFANA_INI_TEMPLATE
```

**Value**: `
[security]
allow_embedding = true

[auth.anonymous]
enabled = true
org_name = Main Org.
org_role = Viewer

[paths]
provisioning = \{provisioning_path\}

[server]
http_port = \{grafana_web_port\}
`


```python
nemo_curator.metrics.constants.GRAFANA_DASHBOARD_YAML_TEMPLATE
```

**Value**: `

apiVersion: 1

providers:
  - name: Ray    # Default dashboards provided by OSS Ray
    folder: Ray
    type: file
    options:
      path: \{dashboards_path\}
`


```python
nemo_curator.metrics.constants.GRAFANA_DATASOURCE_YAML_TEMPLATE
```

**Value**: `<Multiline-String>`


```python
nemo_curator.metrics.constants.DEFAULT_PROMETHEUS_WEB_PORT
```

**Value**: `9090`


```python
nemo_curator.metrics.constants.DEFAULT_GRAFANA_WEB_PORT
```

**Value**: `3000`

