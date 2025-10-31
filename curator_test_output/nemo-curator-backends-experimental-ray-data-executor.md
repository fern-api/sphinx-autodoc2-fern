---
layout: overview
slug: nemo-curator-backends-experimental-ray-data-executor
---

# nemo_curator.backends.experimental.ray_data.executor



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`RayDataExecutor`](#nemo_curatorbackendsexperimentalray_dataexecutorraydataexecutor) | Ray Data-based executor for pipeline execution. |

### API

```python
class nemo_curator.backends.experimental.ray_data.executor.RayDataExecutor(config: dict[str, typing.Any] | None = None)
```

**Bases**: `nemo_curator.backends.base.BaseExecutor`

Ray Data-based executor for pipeline execution.

This executor:
1. Executes setup on all nodes for all stages
2. Converts initial tasks to Ray Data dataset
3. Applies each stage as a Ray Data transformation (as a task or actor in map_batches)
4. Returns final results as a list of tasks

```python
execute(
    stages: list[nemo_curator.stages.base.ProcessingStage],
    initial_tasks: list[nemo_curator.tasks.Task] | None = None
) -> list[nemo_curator.tasks.Task]
```

Execute the pipeline stages using Ray Data.

**Parameters:**

**Returns:**

list[Task]: List of final processed tasks


```python
_tasks_to_dataset(tasks: list[nemo_curator.tasks.Task]) -> ray.data.Dataset
```

Convert list of tasks to Ray Data dataset.

**Parameters:**

<ParamField path="tasks" type="list[nemo_curator.tasks.Task]">
  List of Task objects
</ParamField>

**Returns:**

Ray Data dataset containing Task objects directly


```python
_dataset_to_tasks(dataset: ray.data.Dataset) -> list[nemo_curator.tasks.Task]
```

Convert Ray Data dataset back to list of tasks.

**Parameters:**

<ParamField path="dataset" type="ray.data.Dataset">
  Ray Data dataset containing Task objects
</ParamField>

**Returns:**

List of Task objects

