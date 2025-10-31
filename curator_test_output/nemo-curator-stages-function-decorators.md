---
layout: overview
slug: nemo-curator-stages-function-decorators
---

# nemo_curator.stages.function_decorators

Utility decorators for creating ProcessingStage instances from simple functions.

This module provides a :func:`processing_stage` decorator that turns a plain
Python function into a concrete :class:`nemo_curator.stages.base.ProcessingStage`.

Example
-------

```python
from nemo_curator.stages.resources import Resources
from nemo_curator.stages.function_decorators import processing_stage


@processing_stage(name="WordCountStage", resources=Resources(cpus=1.0), batch_size=1)
def word_count(task: SampleTask) -> SampleTask:
    # Add a *word_count* column to the task's DataFrame
    task.data["word_count"] = task.data["sentence"].str.split().str.len()
    return task
```

The variable ``word_count`` now holds an *instance* of a concrete
``ProcessingStage`` subclass that can be added directly to a
:class:`nemo_curator.pipeline.Pipeline` like so:

```python
from nemo_curator.pipeline import Pipeline


pipeline = Pipeline(...)
# Add read stage, etc.
pipeline.add_stage(...)

# Add ``WordCountStage``
pipeline.add_stage(word_count)

result = pipeline.run(...)
```


## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`processing_stage`](#nemo_curatorstagesfunction_decoratorsprocessing_stage) | Decorator that converts a function into a :class:`ProcessingStage`. |

### Data

`TIn`
`TOut`

### API

```python
nemo_curator.stages.function_decorators.TIn
```

**Value**: `TypeVar(...)`


```python
nemo_curator.stages.function_decorators.TOut
```

**Value**: `TypeVar(...)`


```python
nemo_curator.stages.function_decorators.processing_stage(
    *,
    name: str,
    resources: nemo_curator.stages.resources.Resources | dict[str, float] | None = None,
    batch_size: int | None = None
) -> collections.abc.Callable[[collections.abc.Callable[[nemo_curator.stages.function_decorators.TIn], nemo_curator.stages.function_decorators.TOut | list[nemo_curator.stages.function_decorators.TOut]]], nemo_curator.stages.base.ProcessingStage]
```

Decorator that converts a function into a :class:`ProcessingStage`.

Parameters
----------
name:
    The *name* assigned to the resulting stage (``ProcessingStage.name``).
resources:
    Optional :class:`nemo_curator.stages.resources.Resources`
    or dict[str, float] describing the required compute resources.
    If *None* a default of ``Resources()`` is used.
batch_size:
    Optional *batch size* for the stage. ``None`` means *no explicit batch
    size* (executor decides).

The decorated function **must**:
1. Accept exactly one positional argument: a :class:`Task` instance (or
   subclass).
2. Return either a single :class:`Task` instance or a ``list`` of tasks.

