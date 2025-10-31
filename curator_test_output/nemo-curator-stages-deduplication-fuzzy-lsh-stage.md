---
layout: overview
slug: nemo-curator-stages-deduplication-fuzzy-lsh-stage
---

# nemo_curator.stages.deduplication.fuzzy.lsh.stage



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`LSHStage`](#nemo_curatorstagesdeduplicationfuzzylshstagelshstage) | Stage that performs LSH on a FileGroupTask containing minhash data. |

### API

```python
class nemo_curator.stages.deduplication.fuzzy.lsh.stage.LSHStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks.FileGroupTask]`

Stage that performs LSH on a FileGroupTask containing minhash data.

The executor will process this stage in iterations based on bands_per_iteration.

Parameters
----------
num_bands
    Number of LSH bands.
minhashes_per_band
    Number of minhashes per band.
id_field
    Name of the ID field in input data.
minhash_field
    Name of the minhash field in input data.
output_path
    Base path to write output files.
read_kwargs
    Keyword arguments for the read method.
write_kwargs
    Keyword arguments for the write method.
rmm_pool_size
    Size of the RMM GPU memory pool in bytes.
    If "auto", the memory pool is set to 90% of the free GPU memory.
    If None, the memory pool is set to 50% of the free GPU memory that can expand if needed.
spill_memory_limit
    Device memory limit in bytes for spilling to host.
    If "auto", the limit is set to 80% of the RMM pool size.
    If None spilling is disabled.
enable_statistics
    Whether to collect statistics.
bands_per_iteration
    Number of bands to process per shuffle iteration. Between 1 and num_bands.
    Higher values reduce the number of shuffle iterations but increase the memory usage.
total_nparts
    Total number of partitions to write during the shuffle.
    If None, the number of partitions will be decided automatically by the executor as the closest power of 2 <= number of input tasks.

```python
_name
```

**Value**: `LSHStage`


```python
_resources
```

**Value**: `Resources(...)`


```python
actor_class
```

**Value**: `None`


```python
num_bands: int
```

**Value**: `None`


```python
minhashes_per_band: int
```

**Value**: `None`


```python
id_field: str
```

**Value**: `None`


```python
minhash_field: str
```

**Value**: `None`


```python
output_path: str
```

**Value**: `./`


```python
read_kwargs: dict[str, typing.Any] | None
```

**Value**: `None`


```python
write_kwargs: dict[str, typing.Any] | None
```

**Value**: `None`


```python
rmm_pool_size: int | typing.Literal[auto] | None
```

**Value**: `auto`


```python
spill_memory_limit: int | typing.Literal[auto] | None
```

**Value**: `auto`


```python
enable_statistics: bool
```

**Value**: `False`


```python
bands_per_iteration: int
```

**Value**: `5`


```python
total_nparts: int | None
```

**Value**: `None`


```python
__post_init__()
```


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```


```python
ray_stage_spec() -> dict[str, typing.Any]
```

Ray stage specification for this stage.


```python
_check_actor_obj() -> None
```


```python
read_and_insert(
    task: nemo_curator.tasks.FileGroupTask, band_range: tuple[int, int]
) -> nemo_curator.tasks.FileGroupTask
```


```python
insert_finished() -> None
```


```python
extract_and_write() -> list[nemo_curator.tasks.FileGroupTask]
```


```python
teardown() -> None
```


```python
get_band_iterations() -> collections.abc.Iterator[tuple[int, int]]
```

Get all band ranges for iteration.

