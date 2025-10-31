---
layout: overview
slug: nemo-curator-backends-xenna-executor
---

# nemo_curator.backends.xenna.executor



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`XennaExecutor`](#nemo_curatorbackendsxennaexecutorxennaexecutor) | Executor that runs pipelines using Cosmos-Xenna. This executor provides integration between the nemo-curator pipeline framework and the Cosmos-Xenna execution engine for distributed processing. |

### API

```python
class nemo_curator.backends.xenna.executor.XennaExecutor(config: dict[str, typing.Any] | None = None)
```

**Bases**: `nemo_curator.backends.base.BaseExecutor`

Executor that runs pipelines using Cosmos-Xenna.
This executor provides integration between the nemo-curator pipeline framework
and the Cosmos-Xenna execution engine for distributed processing.

### Initialization

Initialize the executor.

**Parameters:**

- **config (dict[str, Any], optional)**: Configuration dictionary with options like:
- **- logging_interval**: Seconds between status logs (default: 60)
- **- ignore_failures**: Whether to continue on failures (default: False)
- **- max_workers_per_stage**: Max workers per stage (default: None)
- **- execution_mode**: 'streaming' or 'batch' (default: 'streaming')
- **- cpu_allocation_percentage**: CPU allocation ratio (default: 0.95)
- **- autoscale_interval_s**: Auto-scaling interval (default: 180)


```python
execute(
    stages: list[nemo_curator.stages.base.ProcessingStage],
    initial_tasks: list[nemo_curator.tasks.Task] | None = None
) -> list[nemo_curator.tasks.Task]
```

Execute the pipeline using Cosmos-Xenna.

**Parameters:**

**Returns:**

list[Task]: List of output tasks from the pipeline


```python
_get_pipeline_config(key: str) -> typing.Any
```

Get configuration value with fallback to defaults.

