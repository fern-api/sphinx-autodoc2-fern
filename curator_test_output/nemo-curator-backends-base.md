---
layout: overview
slug: nemo-curator-backends-base
---

# nemo_curator.backends.base



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`NodeInfo`](#nemo_curatorbackendsbasenodeinfo) | Generic node information for setup_on_node calls across backends. Simplified to match Xenna's structure. |
| [`WorkerMetadata`](#nemo_curatorbackendsbaseworkermetadata) | Generic worker metadata for setup_on_node calls across backends. Simplified to match Xenna's structure. The allocation field can contain backend-specific allocation information. |
| [`BaseExecutor`](#nemo_curatorbackendsbasebaseexecutor) | Executor for a pipeline. |
| [`BaseStageAdapter`](#nemo_curatorbackendsbasebasestageadapter) | Adapts ProcessingStage to an execution backend, if needed. |

### API

```python
class nemo_curator.backends.base.NodeInfo
```

Generic node information for setup_on_node calls across backends.
Simplified to match Xenna's structure.

```python
node_id: str
```

**Value**: ``


```python
class nemo_curator.backends.base.WorkerMetadata
```

Generic worker metadata for setup_on_node calls across backends.
Simplified to match Xenna's structure. The allocation field can contain
backend-specific allocation information.

```python
worker_id: str
```

**Value**: ``


```python
allocation: typing.Any
```

**Value**: `None`


```python
class nemo_curator.backends.base.BaseExecutor(config: dict[str, typing.Any] | None = None)
```

**Bases**: `abc.ABC`

Executor for a pipeline.

```python
execute(
    stages: list[nemo_curator.stages.base.ProcessingStage],
    initial_tasks: list[nemo_curator.tasks.Task] | None = None
) -> None
```

Execute the pipeline.


```python
class nemo_curator.backends.base.BaseStageAdapter(stage: nemo_curator.stages.base.ProcessingStage)
```

Adapts ProcessingStage to an execution backend, if needed.

```python
process_batch(tasks: list[nemo_curator.tasks.Task]) -> list[nemo_curator.tasks.Task]
```

Process a batch of tasks.

**Parameters:**

**Returns:**

list[Task]: List of processed tasks


```python
setup_on_node(
    node_info: nemo_curator.backends.base.NodeInfo | None = None,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None
) -> None
```

Setup the stage on a node.

**Parameters:**


```python
setup(worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```

Setup the stage once per actor.

**Parameters:**


```python
teardown() -> None
```

Teardown the stage once per actor.

