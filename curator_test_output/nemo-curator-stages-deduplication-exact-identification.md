---
layout: overview
slug: nemo-curator-stages-deduplication-exact-identification
---

# nemo_curator.stages.deduplication.exact.identification



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ExactDuplicateIdentification`](#nemo_curatorstagesdeduplicationexactidentificationexactduplicateidentification) | Stage that finds exact duplicates in a given column. |

### Data

`EXACT_DUPLICATE_GROUP_FIELD`

### API

```python
nemo_curator.stages.deduplication.exact.identification.EXACT_DUPLICATE_GROUP_FIELD
```

**Value**: `_exact_duplicate_group`


```python
class nemo_curator.stages.deduplication.exact.identification.ExactDuplicateIdentification(text_field: str, output_path: str, input_filetype: typing.Literal[jsonl, parquet] = 'parquet', read_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None, assign_id: bool = True, id_field: str | None = None, total_nparts: int | None = None, rmm_pool_size: int | typing.Literal[auto] | None = 'auto', spill_memory_limit: int | typing.Literal[auto] | None = 'auto', enable_statistics: bool = False)
```

**Bases**: `nemo_curator.stages.deduplication.io_utils.DeduplicationIO`, `nemo_curator.stages.deduplication.shuffle_utils.stage.ShuffleStage`

Stage that finds exact duplicates in a given column.

Parameters
----------
text_field
    Field name representing the field to find duplicates in.
output_path
    Path to write output files.
input_filetype
    Type of the input files.
    Must be one of "jsonl" or "parquet". Default is "parquet".
read_kwargs
    Keyword arguments for cudf.read_parquet method.
write_kwargs
    Keyword arguments for cudf.to_parquet method.
assign_id
    Whether to assign a unique id to each document.
id_field
    Existing id field name if not assigning a new id.
total_nparts
    Total number of output partitions. If None, will be set automatically by the executor.
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

**Value**: `ExactDuplicateIds`


```python
_get_removal_ids(df: cudf.DataFrame) -> cudf.DataFrame
```

Get the removal ids for the given dataframe.


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```


```python
ray_stage_spec() -> dict[str, typing.Any]
```


```python
setup(_worker_metadata: WorkerMetadata | None = None) -> None
```


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
read_and_insert(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```


```python
insert_finished() -> None
```


```python
extract_and_write() -> list[nemo_curator.tasks.FileGroupTask]
```

