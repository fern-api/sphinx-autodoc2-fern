---
layout: overview
slug: nemo-curator-core-utils
---

# nemo_curator.core.utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`get_free_port`](#nemo_curatorcoreutilsget_free_port) | Checks if start_port is free. If not, it will get the next free port starting from start_port if get_next_free_port is True. Else, it will raise an error if the free port is not equal to start_port. |
| [`_logger_custom_serializer`](#nemo_curatorcoreutils_logger_custom_serializer) | None |
| [`_logger_custom_deserializer`](#nemo_curatorcoreutils_logger_custom_deserializer) | None |
| [`init_cluster`](#nemo_curatorcoreutilsinit_cluster) | Initialize a new local Ray cluster or connects to an existing one. |

### API

```python
nemo_curator.core.utils.get_free_port(
    start_port: int, get_next_free_port: bool = True
) -> int
```

Checks if start_port is free.
If not, it will get the next free port starting from start_port if get_next_free_port is True.
Else, it will raise an error if the free port is not equal to start_port.


```python
nemo_curator.core.utils._logger_custom_serializer(_: loguru.Logger) -> None
```


```python
nemo_curator.core.utils._logger_custom_deserializer(_: None) -> loguru.Logger
```


```python
nemo_curator.core.utils.init_cluster(
    ray_port: int,
    ray_temp_dir: str,
    ray_dashboard_port: int,
    ray_metrics_port: int,
    ray_client_server_port: int,
    ray_dashboard_host: str,
    num_gpus: int | None = None,
    num_cpus: int | None = None,
    enable_object_spilling: bool = False,
    block: bool = True,
    ip_address: str | None = None
) -> subprocess.Popen
```

Initialize a new local Ray cluster or connects to an existing one.

