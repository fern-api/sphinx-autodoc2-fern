---
layout: overview
slug: nemo-curator-core-client
---

# nemo_curator.core.client



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`RayClient`](#nemo_curatorcoreclientrayclient) | This class is used to setup the Ray cluster and configure metrics integration. |

### API

```python
class nemo_curator.core.client.RayClient
```

This class is used to setup the Ray cluster and configure metrics integration.

If the specified ports are already in use, it will find the next available port and use that.

**Parameters:**

- **ray_port**: The port number of the Ray GCS.
- **ray_dashboard_port**: The port number of the Ray dashboard.
- **ray_temp_dir**: The temporary directory to use for Ray.
- **include_dashboard**: Whether to include dashboard integration. If true, adds Ray metrics service discovery.
- **ray_metrics_port**: The port number of the Ray metrics.
- **ray_dashboard_host**: The host of the Ray dashboard.
- **num_gpus**: The number of GPUs to use.
- **num_cpus**: The number of CPUs to use.
- **enable_object_spilling**: Whether to enable object spilling.
- **Note**: 
  To start monitoring services (Prometheus and Grafana), use the standalone
  start_prometheus_grafana.py script separately.

```python
ray_port: int
```

**Value**: `None`


```python
ray_dashboard_port: int
```

**Value**: `None`


```python
ray_client_server_port: int
```

**Value**: `None`


```python
ray_temp_dir: str
```

**Value**: `None`


```python
include_dashboard: bool
```

**Value**: `True`


```python
ray_metrics_port: int
```

**Value**: `None`


```python
ray_dashboard_host: str
```

**Value**: `None`


```python
num_gpus: int | None
```

**Value**: `None`


```python
num_cpus: int | None
```

**Value**: `None`


```python
enable_object_spilling: bool
```

**Value**: `False`


```python
ray_process: subprocess.Popen | None
```

**Value**: `None`


```python
start() -> None
```


```python
stop() -> None
```


```python
__enter__()
```


```python
__exit__(*exc)
```

