---
layout: overview
slug: nemo-curator-stages-deduplication-shuffle-utils-stage
---

# nemo_curator.stages.deduplication.shuffle_utils.stage



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ShuffleStage`](#nemo_curatorstagesdeduplicationshuffle_utilsstageshufflestage) | Stage that performs generic shuffling on specified columns from a FileGroupTask. This stage uses the BulkRapidsMPFShuffler with cuDF I/O for efficient GPU-based shuffling. |

### API

```python
class nemo_curator.stages.deduplication.shuffle_utils.stage.ShuffleStage(shuffle_on: list[str], total_nparts: int | None = None, output_path: str = './', read_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None, rmm_pool_size: int | typing.Literal[auto] | None = 'auto', spill_memory_limit: int | typing.Literal[auto] | None = 'auto', enable_statistics: bool = False)
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks.FileGroupTask]`

Stage that performs generic shuffling on specified columns from a FileGroupTask.
This stage uses the BulkRapidsMPFShuffler with cuDF I/O for efficient GPU-based shuffling.

Parameters
----------
shuffle_on
    List of column names to shuffle on.
total_nparts
    Total number of output partitions. If None, will be set automatically by the executor.
output_path
    Path to write output files.
read_kwargs
    Keyword arguments for cudf.read_parquet method.
write_kwargs
    Keyword arguments for cudf.to_parquet method.
rmm_pool_size
    Size of the RMM GPU memory pool in bytes.
    If "auto", the memory pool is set to 90% of the free GPU memory.
    If None, the memory pool is set to 50% of the free GPU memory that can expand if needed.
spill_memory_limit
    Device memory limit in bytes for spilling to host.
    If "auto", the limit is set to 80% of the RMM pool size.
    If None spilling is disabled.
enable_statistics
    Whether the underlying rapidsmpf shuffler should collect shuffle statistics.

```python
_name
```

**Value**: `ShuffleStage`


```python
_resources
```

**Value**: `Resources(...)`


```python
actor_class
```

**Value**: `None`


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```

Not implemented for actor-based stages.


```python
ray_stage_spec() -> dict[str, typing.Any]
```

Ray stage specification for this stage.


```python
_check_actor_obj() -> None
```

Verify the actor object is properly initialized.


```python
read_and_insert(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```

Read files and insert into shuffler.


```python
insert_finished() -> None
```


```python
extract_and_write() -> list[nemo_curator.tasks.FileGroupTask]
```


```python
teardown() -> None
```

