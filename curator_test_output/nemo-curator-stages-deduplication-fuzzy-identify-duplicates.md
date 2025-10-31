---
layout: overview
slug: nemo-curator-stages-deduplication-fuzzy-identify-duplicates
---

# nemo_curator.stages.deduplication.fuzzy.identify_duplicates



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`IdentifyDuplicatesStage`](#nemo_curatorstagesdeduplicationfuzzyidentify_duplicatesidentifyduplicatesstage) | Stage that generates removal IDs for fuzzy deduplication. The approach involves shuffling the data based on the duplicate group field similar to grouping by the group field. followed by selecting one document per group. Currently the removal strategy is to randomly keep one document per group. |

### Data

`DUPLICATE_IDS_SUBDIR`

### API

```python
nemo_curator.stages.deduplication.fuzzy.identify_duplicates.DUPLICATE_IDS_SUBDIR
```

**Value**: `FuzzyDuplicateIds`


```python
class nemo_curator.stages.deduplication.fuzzy.identify_duplicates.IdentifyDuplicatesStage(duplicate_group_field: str = CURATOR_FUZZY_DUPLICATE_GROUP_FIELD, document_id_field: str = CURATOR_DEDUP_ID_STR, total_nparts: int | None = None, output_path: str = './', read_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None, rmm_pool_size: int | typing.Literal[auto] | None = 'auto', spill_memory_limit: int | typing.Literal[auto] | None = 'auto', enable_statistics: bool = False)
```

**Bases**: `nemo_curator.stages.deduplication.shuffle_utils.stage.ShuffleStage`

Stage that generates removal IDs for fuzzy deduplication.
The approach involves shuffling the data based on the duplicate group field similar to grouping by the group field.
followed by selecting one document per group.
Currently the removal strategy is to randomly keep one document per group.

Parameters
----------
duplicate_group_field
    Column name representing the group id for a document.
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

**Value**: `IdentifyDuplicates`


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
read_and_insert(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```


```python
insert_finished() -> None
```


```python
extract_and_write() -> list[nemo_curator.tasks.FileGroupTask]
```

