---
layout: overview
slug: nemo-curator-backends-xenna-adapter
---

# nemo_curator.backends.xenna.adapter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`XennaStageAdapter`](#nemo_curatorbackendsxennaadapterxennastageadapter) | Adapts ProcessingStage to Xenna. Args: stage: ProcessingStage to adapt |

### Functions

| Name | Description |
|------|-------------|
| [`create_named_xenna_stage_adapter`](#nemo_curatorbackendsxennaadaptercreate_named_xenna_stage_adapter) | When we run a pipeline in Xenna, since we wrap using XennaStageAdapter, the stage name is shown as XennaStageAdapter. This is not what we want. So we create a dynamic subclass with the original stage's name. This ensures that when Xenna calls type(adapter).__name__, it returns the original stage's class name rather than 'XennaStageAdapter'. Args: stage (ProcessingStage): ProcessingStage to adapt |

### API

```python
class nemo_curator.backends.xenna.adapter.XennaStageAdapter(processing_stage: nemo_curator.stages.base.ProcessingStage)
```

**Bases**: `nemo_curator.backends.base.BaseStageAdapter`, `cosmos_xenna.pipelines.v1.Stage`

Adapts ProcessingStage to Xenna.

**Parameters:**

- **stage**: ProcessingStage to adapt

```python
required_resources: cosmos_xenna.ray_utils.resources.Resources
```

Get the resources required for this stage.


```python
stage_batch_size: int
```

Get the batch size for this stage.


```python
env_info: cosmos_xenna.pipelines.v1.RuntimeEnv | None
```

Runtime environment for this stage.


```python
process_data(tasks: list[nemo_curator.tasks.Task]) -> list[nemo_curator.tasks.Task] | None
```

Process batch of tasks with automatic performance tracking.

**Parameters:**

<ParamField path="tasks" type="list[nemo_curator.tasks.Task]">
  List of tasks to process
</ParamField>

**Returns:**

List of processed tasks or None


```python
setup_on_node(
    node_info: cosmos_xenna.ray_utils.resources.NodeInfo,
    worker_metadata: cosmos_xenna.ray_utils.resources.WorkerMetadata
) -> None
```

Setup the stage on a node - Xenna-specific signature.
This method is called by Xenna with its specific types. We convert them
to our generic types and delegate to the base adapter.

**Parameters:**

<ParamField path="node_info" type="cosmos_xenna.ray_utils.resources.NodeInfo">
  Xenna's NodeInfo object
</ParamField>

<ParamField path="worker_metadata" type="cosmos_xenna.ray_utils.resources.WorkerMetadata">
  Xenna's WorkerMetadata object
</ParamField>


```python
setup(worker_metadata: cosmos_xenna.ray_utils.resources.WorkerMetadata) -> None
```

Setup the stage per worker - Xenna-specific signature.
This method is called by Xenna with its specific types. We convert them
to our generic types and delegate to the base adapter.

**Parameters:**

<ParamField path="worker_metadata" type="cosmos_xenna.ray_utils.resources.WorkerMetadata">
  Xenna's WorkerMetadata object
</ParamField>


```python
nemo_curator.backends.xenna.adapter.create_named_xenna_stage_adapter(stage: nemo_curator.stages.base.ProcessingStage) -> nemo_curator.backends.xenna.adapter.XennaStageAdapter
```

When we run a pipeline in Xenna, since we wrap using XennaStageAdapter,
the stage name is shown as XennaStageAdapter. This is not what we want.
So we create a dynamic subclass with the original stage's name.
This ensures that when Xenna calls type(adapter).__name__, it returns the
original stage's class name rather than 'XennaStageAdapter'.

**Parameters:**

**Returns:**

XennaStageAdapter: XennaStageAdapter instance with the wrapped stage's class name

