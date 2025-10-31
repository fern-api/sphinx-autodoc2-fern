---
layout: overview
slug: nemo-curator-utils-performance-utils
---

# nemo_curator.utils.performance_utils



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`StagePerfStats`](#nemo_curatorutilsperformance_utilsstageperfstats) | Statistics for tracking stage performance metrics. Attributes: stage_name: Name of the processing stage. process_time: Total processing time in seconds. actor_idle_time: Time the actor spent idle in seconds. input_data_size_mb: Size of input data in megabytes. num_items_processed: Number of items processed in this stage. custom_metrics: Custom metrics to track. |
| [`StageTimer`](#nemo_curatorutilsperformance_utilsstagetimer) | Tracker for stage performance stats. Tracks processing time and other metrics at a per process_data call level. |

### API

```python
class nemo_curator.utils.performance_utils.StagePerfStats
```

Statistics for tracking stage performance metrics.
Attributes:
    stage_name: Name of the processing stage.
    process_time: Total processing time in seconds.
    actor_idle_time: Time the actor spent idle in seconds.
    input_data_size_mb: Size of input data in megabytes.
    num_items_processed: Number of items processed in this stage.
    custom_metrics: Custom metrics to track.

```python
stage_name: str
```

**Value**: `None`


```python
process_time: float
```

**Value**: `0.0`


```python
actor_idle_time: float
```

**Value**: `0.0`


```python
input_data_size_mb: float
```

**Value**: `0.0`


```python
num_items_processed: int
```

**Value**: `0`


```python
custom_metrics: dict[str, float]
```

**Value**: `field(...)`


```python
__add__(other: nemo_curator.utils.performance_utils.StagePerfStats) -> nemo_curator.utils.performance_utils.StagePerfStats
```

Add two StagePerfStats.


```python
__radd__(other: int | nemo_curator.utils.performance_utils.StagePerfStats) -> nemo_curator.utils.performance_utils.StagePerfStats
```

Add two StagePerfStats together, if right is 0, returns itself.


```python
reset() -> None
```

Reset the stats.


```python
to_dict() -> dict[str, float | int]
```

Convert the stats to a dictionary.


```python
items() -> list[tuple[str, float | int]]
```

Returns (metric_name, metric_value) pairs
custom_metrics are flattened into the format (custom.`<metric_name>`, metric_value)


```python
class nemo_curator.utils.performance_utils.StageTimer(stage: nemo_curator.stages.base.ProcessingStage)
```

Tracker for stage performance stats.
Tracks processing time and other metrics at a per process_data call level.

### Initialization

Initialize the stage timer.

**Parameters:**

- **stage**: The stage to track.


```python
_reset() -> None
```

Reset internal counters.


```python
reinit(stage_input_size: int = 1) -> None
```

Reinitialize the stage timer.

**Parameters:**

<ParamField path="stage_input_size" type="int" default="1">
  The size of the stage input.
</ParamField>


```python
time_process(num_items: int = 1) -> collections.abc.Generator[None, None, None]
```

Time the processing of the stage.

**Parameters:**

<ParamField path="num_items" type="int" default="1">
  The number of items being processed.
</ParamField>


```python
log_stats(
    *, verbose: bool = False
) -> tuple[str, nemo_curator.utils.performance_utils.StagePerfStats]
```

Log the stats of the stage.

**Parameters:**

<ParamField path="verbose" type="bool" default="False">
  Whether to log the stats verbosely.
</ParamField>

**Returns:**

A tuple of the stage name and the stage performance stats.

