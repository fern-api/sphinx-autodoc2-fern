---
layout: overview
slug: nemo-curator-metrics-utils
---

# nemo_curator.metrics.utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`download_and_extract_prometheus`](#nemo_curatormetricsutilsdownload_and_extract_prometheus) | Download the prometheus tarball and extract it to the default nemo curator metrics path. |
| [`is_prometheus_running`](#nemo_curatormetricsutilsis_prometheus_running) | Check if Prometheus is currently running. |
| [`is_grafana_running`](#nemo_curatormetricsutilsis_grafana_running) | Check if Grafana is currently running. |
| [`get_prometheus_port`](#nemo_curatormetricsutilsget_prometheus_port) | Get the port number that Prometheus is running on. |
| [`run_prometheus`](#nemo_curatormetricsutilsrun_prometheus) | Run the prometheus server. |
| [`download_grafana`](#nemo_curatormetricsutilsdownload_grafana) | Download the grafana tarball and extract it to the default nemo curator metrics path. |
| [`launch_grafana`](#nemo_curatormetricsutilslaunch_grafana) | Launch the grafana server. |
| [`write_grafana_configs`](#nemo_curatormetricsutilswrite_grafana_configs) | Write the grafana configs to the grafana directory. |
| [`add_ray_prometheus_metrics_service_discovery`](#nemo_curatormetricsutilsadd_ray_prometheus_metrics_service_discovery) | Add the ray prometheus metrics service discovery to the prometheus config. |

### API

```python
nemo_curator.metrics.utils.download_and_extract_prometheus(
    os_type = None,
    architecture = None,
    prometheus_version = None
) -> str
```

Download the prometheus tarball and extract it to the default nemo curator metrics path.


```python
nemo_curator.metrics.utils.is_prometheus_running() -> bool
```

Check if Prometheus is currently running.


```python
nemo_curator.metrics.utils.is_grafana_running() -> bool
```

Check if Grafana is currently running.


```python
nemo_curator.metrics.utils.get_prometheus_port() -> int
```

Get the port number that Prometheus is running on.


```python
nemo_curator.metrics.utils.run_prometheus(
    prometheus_dir: str, prometheus_web_port: int
) -> None
```

Run the prometheus server.


```python
nemo_curator.metrics.utils.download_grafana() -> str
```

Download the grafana tarball and extract it to the default nemo curator metrics path.


```python
nemo_curator.metrics.utils.launch_grafana(
    grafana_dir: str, grafana_ini_path: str
) -> None
```

Launch the grafana server.


```python
nemo_curator.metrics.utils.write_grafana_configs(
    grafana_web_port: int, prometheus_web_port: int
) -> str
```

Write the grafana configs to the grafana directory.


```python
nemo_curator.metrics.utils.add_ray_prometheus_metrics_service_discovery(ray_temp_dir: str) -> None
```

Add the ray prometheus metrics service discovery to the prometheus config.

