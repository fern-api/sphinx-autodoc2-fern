---
layout: overview
slug: nemo-curator-stages-base
---

# nemo_curator.stages.base



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`StageMeta`](#nemo_curatorstagesbasestagemeta) | Metaclass that automatically registers concrete Stage subclasses. A class is considered *concrete* if it directly inherits from :class:`ProcessingStage` **and** implements a ``name`` property.  Abstract helper classes (e.g. *ProcessingStage* itself) will not be added to the registry because they have the ``_is_abstract`` attribute set. |
| [`ProcessingStage`](#nemo_curatorstagesbaseprocessingstage) | Base class for all processing stages. Processing stages operate on Task objects (or subclasses like DocumentBatch). Each stage type can declare what type of Task it processes as input (X) and what type it produces as output (Y). Stages can return either: - A single task (typical for transformations) - A list of tasks (for stages that split work, like readers) - None (for filtered out tasks) |
| [`CompositeStage`](#nemo_curatorstagesbasecompositestage) | Base class for high-level composite stages. |

### Functions

| Name | Description |
|------|-------------|
| [`get_stage_class`](#nemo_curatorstagesbaseget_stage_class) | Retrieve a registered stage class by its *class name*. Raises ------ KeyError If no stage with that name is registered. |

### Data

`X`
`Y`
`_STAGE_REGISTRY`

### API

```python
nemo_curator.stages.base.X
```

**Value**: `TypeVar(...)`


```python
nemo_curator.stages.base.Y
```

**Value**: `TypeVar(...)`


```python
nemo_curator.stages.base._STAGE_REGISTRY: dict[str, type[nemo_curator.stages.base.ProcessingStage]]
```

**Value**: `None`


```python
class nemo_curator.stages.base.StageMeta
```

**Bases**: `abc.ABCMeta`

Metaclass that automatically registers concrete Stage subclasses.
A class is considered *concrete* if it directly inherits from
:class:`ProcessingStage` **and** implements a ``name`` property.  Abstract
helper classes (e.g. *ProcessingStage* itself) will not be added to the
registry because they have the ``_is_abstract`` attribute set.

```python
__new__(
    name,
    bases,
    namespace,
    **kwargs
)
```


```python
nemo_curator.stages.base.get_stage_class(name: str) -> type[ProcessingStage]
```

Retrieve a registered stage class by its *class name*.
Raises
------
KeyError
    If no stage with that name is registered.


```python
class nemo_curator.stages.base.ProcessingStage
```

**Bases**: `abc.ABC`, `typing.Generic[nemo_curator.stages.base.X, nemo_curator.stages.base.Y]`

Base class for all processing stages.
Processing stages operate on Task objects (or subclasses like DocumentBatch).
Each stage type can declare what type of Task it processes as input (X)
and what type it produces as output (Y).
Stages can return either:
- A single task (typical for transformations)
- A list of tasks (for stages that split work, like readers)
- None (for filtered out tasks)

```python
_is_abstract_root
```

**Value**: `True`


```python
_name
```

**Value**: `ProcessingStage`


```python
_resources
```

**Value**: `Resources(...)`


```python
_batch_size
```

**Value**: `1`


```python
name: str
```


```python
resources: nemo_curator.stages.resources.Resources
```


```python
batch_size: int | None
```

Number of tasks to process in a batch.


```python
num_workers() -> int | None
```

Number of workers required. If None, then executor will determine the number of workers.


```python
validate_input(task: nemo_curator.tasks.Task) -> bool
```

Validate input task meets requirements.

**Parameters:**

<ParamField path="task" type="nemo_curator.tasks.Task">
  Task to validate
</ParamField>

**Returns:**

True if valid, False otherwise


```python
process(task: nemo_curator.stages.base.X) -> nemo_curator.stages.base.Y | list[nemo_curator.stages.base.Y]
```

Process a task and return the result.

**Parameters:**


```python
process_batch(tasks: list[nemo_curator.stages.base.X]) -> list[nemo_curator.stages.base.Y]
```

Process a batch of tasks and return results.
Override this method to enable batch processing for your stage.
If not overridden, the stage will only support single-task processing.

**Parameters:**


```python
setup_on_node(
    node_info: nemo_curator.backends.base.NodeInfo | None = None,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None
) -> None
```

Setup method called once per node in distributed settings.
Override this method to perform node-level initialization.

**Parameters:**


```python
setup(worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```

Setup method called once before processing begins.
Override this method to perform any initialization that should
happen once per worker.

**Parameters:**


```python
teardown() -> None
```

Teardown method called once after processing ends.
Override this method to perform any cleanup.


```python
supports_batch_processing() -> bool
```

Whether this stage supports vectorized batch processing.
This is automatically determined by checking if the stage has
overridden the process_batch method from the base class.


```python
__repr__() -> str
```

String representation of the stage.


```python
inputs() -> tuple[list[str], list[str]]
```

Define stage input requirements.

Returns (tuple[list[str], list[str]]):
    Tuple of (required_attributes, required_columns) where:
    - required_top_level_attributes: List of task attributes that must be present
    - required_data_attributes: List of attributes within the data that must be present


```python
outputs() -> tuple[list[str], list[str]]
```

Define stage output specification.

Returns (tuple[list[str], list[str]]):
    Tuple of (output_attributes, output_columns) where:
    - output_top_level_attributes: List of task attributes this stage adds/modifies
    - output_data_attributes: List of attributes within the data that this stage adds/modifies


```python
xenna_stage_spec() -> dict[str, typing.Any]
```

Get Xenna configuration for this stage.

Returns (dict[str, Any]):
    Dictionary containing Xenna-specific configuration


```python
with_(
    name: str | None = None,
    resources: nemo_curator.stages.resources.Resources | None = None,
    batch_size: int | None = None
) -> nemo_curator.stages.base.ProcessingStage
```

Apply configuration changes to this stage with overridden properties.

Note: This method uses class-level attributes and instance attributes interchangeably which can sometimes
lead to unexpected behavior. Please see https://github.com/NVIDIA-NeMo/Curator/pull/764 for more details.

**Parameters:**

<ParamField path="name" type="str | None">
  Override the name property
</ParamField>

<ParamField path="resources" type="nemo_curator.stages.resources.Resources | None">
  Override the resources property
</ParamField>

<ParamField path="batch_size" type="int | None">
  Override the batch_size property
</ParamField>


```python
get_config() -> dict[str, typing.Any]
```

Get configuration for this stage.
Returns (dict[str, Any]):
    Dictionary containing configuration for this stage


```python
ray_stage_spec() -> dict[str, typing.Any]
```

Get Ray configuration for this stage.
Note : This is only used for Ray Data which is an experimental backend.
The keys are defined in RayStageSpecKeys in backends/experimental/ray_data/utils.py

Returns (dict[str, Any]):
    Dictionary containing Ray-specific configuration


```python
_log_metrics(metrics: dict[str, float]) -> None
```

Record custom metrics for this stage (e.g., sub-stage timings).


```python
_log_metric(
    name: str, value: float
) -> None
```


```python
_consume_custom_metrics() -> dict[str, float]
```

Return and clear metrics recorded during the last process call.


```python
class nemo_curator.stages.base.CompositeStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.stages.base.X, nemo_curator.stages.base.Y]`, `abc.ABC`

Base class for high-level composite stages.

Composite stages are user-facing stages that decompose into multiple
low-level execution stages during pipeline planning. They provide a
simplified API while maintaining fine-grained control at execution time.

Composite stages never actually execute - they only exist to be decomposed
into their constituent execution stages.

```python
inputs() -> tuple[list[str], list[str]]
```

Get the inputs for this stage.


```python
outputs() -> tuple[list[str], list[str]]
```

Get the outputs for this stage.


```python
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

Decompose into execution stages.

This method must be implemented by composite stages to define
what low-level stages they represent.

Returns (list[ProcessingStage]):
    List of execution stages that will actually run


```python
with_(stage_with_dict: dict[str, typing.Any]) -> nemo_curator.stages.base.CompositeStage
```

Apply configuration changes to this stage.


```python
decompose_and_apply_with() -> list[nemo_curator.stages.base.ProcessingStage]
```

Decompose and apply configuration changes to this stage.


```python
_apply_with_(stages: list[nemo_curator.stages.base.ProcessingStage]) -> list[nemo_curator.stages.base.ProcessingStage]
```

Apply configuration changes to this stage.


```python
process(task: nemo_curator.stages.base.X) -> nemo_curator.stages.base.Y | list[nemo_curator.stages.base.Y]
```

Composite stages should never be executed directly.


```python
get_description() -> str
```

Get a description of what this composite stage does.

Override this to provide user-friendly documentation.

