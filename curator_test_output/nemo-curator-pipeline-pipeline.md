---
layout: overview
slug: nemo-curator-pipeline-pipeline
---

# nemo_curator.pipeline.pipeline



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Pipeline`](#nemo_curatorpipelinepipelinepipeline) | User-facing pipeline definition for composing processing stages. |

### API

```python
class nemo_curator.pipeline.pipeline.Pipeline(name: str, description: str | None = None, stages: list[nemo_curator.stages.base.ProcessingStage] | None = None, config: dict[str, typing.Any] | None = None)
```

User-facing pipeline definition for composing processing stages.

### Initialization

Initialize a new pipeline.

**Parameters:**

- **name (str)**: Name of the pipeline
- **description (str, optional)**: Pipeline Description. Defaults to None.
- **stages (list[ProcessingStage], optional)**: List of stages to add to the pipeline. Defaults to None.
- **config (dict[str, Any], optional)**: Pipeline configuration that is valid across all executors. Defaults to None.


```python
add_stage(stage: nemo_curator.stages.base.ProcessingStage) -> nemo_curator.pipeline.pipeline.Pipeline
```

Add a stage to the pipeline.

**Parameters:**

**Returns:**

Pipeline: Self (Pipeline) for method chaining


```python
build() -> None
```

Build an execution plan from the pipeline.

**Raises:**

ValueError: If the pipeline has no stages


```python
_decompose_stages(stages: list[nemo_curator.stages.base.ProcessingStage | nemo_curator.stages.base.CompositeStage]) -> tuple[list[nemo_curator.stages.base.ProcessingStage], dict[str, list[str]]]
```

Decompose composite stages into execution stages.

**Parameters:**

**Returns:**

tuple[list[ProcessingStage], dict[str, list[str]]]: Tuple of (execution stages, decomposition info dict)

**Raises:**

TypeError: If a composite stage is decomposed into another composite stage


```python
__repr__() -> str
```

String representation of the pipeline.


```python
describe() -> str
```

Get a detailed description of the pipeline stages and their requirements.


```python
run(
    executor: nemo_curator.backends.base.BaseExecutor | None = None,
    initial_tasks: list[nemo_curator.tasks.Task] | None = None
) -> list[nemo_curator.tasks.Task] | None
```

Run the pipeline.

**Parameters:**

**Returns:**

list[Task] | None: List of tasks

