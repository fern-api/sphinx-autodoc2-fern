---
layout: overview
slug: nemo-curator-tasks-tasks
---

# nemo_curator.tasks.tasks



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Task`](#nemo_curatortaskstaskstask) | Abstract base class for tasks in the pipeline. A task represents a batch of data to be processed. Different modalities (text, audio, video) can implement their own task types. Attributes: task_id: Unique identifier for this task dataset_name: Name of the dataset this task belongs to dataframe_attribute: Name of the attribute that contains the dataframe data. We use this for input/output validations. _stage_perf: List of stages perfs this task has passed through |
| [`_EmptyTask`](#nemo_curatortaskstasks_emptytask) | Dummy task for testing. |

### Data

`T`
`EmptyTask`

### API

```python
nemo_curator.tasks.tasks.T
```

**Value**: `TypeVar(...)`


```python
class nemo_curator.tasks.tasks.Task
```

**Bases**: `abc.ABC`, `typing.Generic[nemo_curator.tasks.tasks.T]`

Abstract base class for tasks in the pipeline.
A task represents a batch of data to be processed. Different modalities
(text, audio, video) can implement their own task types.
Attributes:
    task_id: Unique identifier for this task
    dataset_name: Name of the dataset this task belongs to
    dataframe_attribute: Name of the attribute that contains the dataframe data. We use this for input/output validations.
    _stage_perf: List of stages perfs this task has passed through

```python
task_id: str
```

**Value**: `None`


```python
dataset_name: str
```

**Value**: `None`


```python
data: nemo_curator.tasks.tasks.T
```

**Value**: `None`


```python
_stage_perf: list[nemo_curator.utils.performance_utils.StagePerfStats]
```

**Value**: `field(...)`


```python
_metadata: dict[str, typing.Any]
```

**Value**: `field(...)`


```python
_uuid: str
```

**Value**: `field(...)`


```python
__post_init__() -> None
```

Post-initialization hook.


```python
num_items: int
```

**Decorators**: `@abstractmethod`

Get the number of items in this task.


```python
add_stage_perf(perf_stats: nemo_curator.utils.performance_utils.StagePerfStats) -> None
```

Add performance stats for a stage.


```python
__repr__() -> str
```


```python
validate() -> bool
```

Validate the task data.


```python
class nemo_curator.tasks.tasks._EmptyTask
```

**Bases**: `nemo_curator.tasks.tasks.Task[None]`

Dummy task for testing.

```python
num_items: int
```


```python
validate() -> bool
```

Validate the task data.


```python
nemo_curator.tasks.tasks.EmptyTask
```

**Value**: `_EmptyTask(...)`

