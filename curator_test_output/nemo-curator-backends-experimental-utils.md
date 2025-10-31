---
layout: overview
slug: nemo-curator-backends-experimental-utils
---

# nemo_curator.backends.experimental.utils



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`RayStageSpecKeys`](#nemo_curatorbackendsexperimentalutilsraystagespeckeys) | String enum of different flags that define keys inside ray_stage_spec. |

### Functions

| Name | Description |
|------|-------------|
| [`get_worker_metadata_and_node_id`](#nemo_curatorbackendsexperimentalutilsget_worker_metadata_and_node_id) | Get the worker metadata and node id from the runtime context. |
| [`get_available_cpu_gpu_resources`](#nemo_curatorbackendsexperimentalutilsget_available_cpu_gpu_resources) | Get available CPU and GPU resources from Ray. |
| [`_setup_stage_on_node`](#nemo_curatorbackendsexperimentalutils_setup_stage_on_node) | Ray remote function to execute setup_on_node for a stage. |
| [`execute_setup_on_node`](#nemo_curatorbackendsexperimentalutilsexecute_setup_on_node) | Execute setup on node for a stage. |

### API

```python
class nemo_curator.backends.experimental.utils.RayStageSpecKeys
```

**Bases**: `str`, `enum.Enum`

String enum of different flags that define keys inside ray_stage_spec.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.


```python
IS_ACTOR_STAGE
```

**Value**: `is_actor_stage`


```python
IS_FANOUT_STAGE
```

**Value**: `is_fanout_stage`


```python
IS_RAFT_ACTOR
```

**Value**: `is_raft_actor`


```python
IS_LSH_STAGE
```

**Value**: `is_lsh_stage`


```python
IS_SHUFFLE_STAGE
```

**Value**: `is_shuffle_stage`


```python
nemo_curator.backends.experimental.utils.get_worker_metadata_and_node_id() -> tuple[nemo_curator.backends.base.NodeInfo, nemo_curator.backends.base.WorkerMetadata]
```

Get the worker metadata and node id from the runtime context.


```python
nemo_curator.backends.experimental.utils.get_available_cpu_gpu_resources(init_and_shudown: bool = False) -> tuple[int, int]
```

Get available CPU and GPU resources from Ray.


```python
nemo_curator.backends.experimental.utils._setup_stage_on_node(
    stage: nemo_curator.stages.base.ProcessingStage,
    node_info: nemo_curator.backends.base.NodeInfo,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata
) -> None
```

Ray remote function to execute setup_on_node for a stage.


```python
nemo_curator.backends.experimental.utils.execute_setup_on_node(stages: list[nemo_curator.stages.base.ProcessingStage]) -> None
```

Execute setup on node for a stage.

