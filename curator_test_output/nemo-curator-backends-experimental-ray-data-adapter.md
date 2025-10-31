---
layout: overview
slug: nemo-curator-backends-experimental-ray-data-adapter
---

# nemo_curator.backends.experimental.ray_data.adapter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`RayDataStageAdapter`](#nemo_curatorbackendsexperimentalray_dataadapterraydatastageadapter) | Adapts ProcessingStage to Ray Data operations. |

### Functions

| Name | Description |
|------|-------------|
| [`create_actor_from_stage`](#nemo_curatorbackendsexperimentalray_dataadaptercreate_actor_from_stage) | Create a StageProcessor class with the proper stage name for display. |
| [`create_task_from_stage`](#nemo_curatorbackendsexperimentalray_dataadaptercreate_task_from_stage) | Create a named Ray Data stage adapter function. |

### API

```python
class nemo_curator.backends.experimental.ray_data.adapter.RayDataStageAdapter(stage: nemo_curator.stages.base.ProcessingStage)
```

**Bases**: `nemo_curator.backends.base.BaseStageAdapter`

Adapts ProcessingStage to Ray Data operations.

This adapter converts stages to work with Ray Data datasets by:
1. Working directly with Task objects (no dictionary conversion)
2. Using Ray Data's map_batches for parallel processing
    a. If stage has both gpus and cpus specified, then we use actors
    b. If stage.setup is overridden, then we use actors
    c. Else we use tasks

```python
batch_size: int | None
```

Get the batch size for this stage.


```python
_process_batch_internal(batch: dict[str, typing.Any]) -> dict[str, typing.Any]
```

Internal method that handles the actual batch processing logic.

**Parameters:**

<ParamField path="batch" type="dict[str, typing.Any]">
  Dictionary with arrays/lists representing a batch of Task objects
</ParamField>

**Returns:**

Dictionary with arrays/lists representing processed Task objects


```python
process_dataset(dataset: ray.data.Dataset) -> ray.data.Dataset
```

Process a Ray Data dataset through this stage.

**Parameters:**

**Returns:**

Dataset: Processed Ray Data dataset


```python
nemo_curator.backends.experimental.ray_data.adapter.create_actor_from_stage(stage: nemo_curator.stages.base.ProcessingStage) -> type[nemo_curator.backends.experimental.ray_data.adapter.RayDataStageAdapter]
```

Create a StageProcessor class with the proper stage name for display.


```python
nemo_curator.backends.experimental.ray_data.adapter.create_task_from_stage(stage: nemo_curator.stages.base.ProcessingStage) -> collections.abc.Callable[[dict[str, typing.Any]], dict[str, typing.Any]]
```

Create a named Ray Data stage adapter function.

This creates a standalone function that wraps the stage processing logic
with a clean name that doesn't include the class qualification.

**Parameters:**

**Returns:**

Callable: A function that can be used directly with Ray Data's map_batches

