---
layout: overview
slug: nemo-curator-tasks-utils
---

# nemo_curator.tasks.utils



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`TaskPerfUtils`](#nemo_curatortasksutilstaskperfutils) | Utilities for aggregating stage performance metrics from tasks. |

### API

```python
class nemo_curator.tasks.utils.TaskPerfUtils
```

Utilities for aggregating stage performance metrics from tasks.

Example output format:
\{
    "StageA": \{"process_time": np.array([...]), "actor_idle_time": np.array([...]), "read_time_s": np.array([...]), ...\},
    "StageB": \{"process_time": np.array([...]), ...\}
\}

```python
collect_stage_metrics(tasks: list[nemo_curator.tasks.tasks.Task]) -> dict[str, dict[str, numpy.ndarray[float]]]
```

Collect per-stage metric lists from a list of tasks.

The returned mapping aggregates both built-in StagePerfStats metrics and any
custom_stats recorded by stages.

**Parameters:**

<ParamField path="tasks" type="list[nemo_curator.tasks.tasks.Task]">
  Iterable of tasks, each having a `_stage_perf: list[StagePerfStats]` attribute.
</ParamField>

**Returns:**

Dict mapping stage_name -> metric_name -> list of numeric values.

