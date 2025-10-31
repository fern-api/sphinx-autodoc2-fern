---
layout: overview
slug: nemo-curator-stages-file-partitioning
---

# nemo_curator.stages.file_partitioning



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`FilePartitioningStage`](#nemo_curatorstagesfile_partitioningfilepartitioningstage) | Stage that partitions input file paths into FileGroupTasks. |

### API

```python
class nemo_curator.stages.file_partitioning.FilePartitioningStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks._EmptyTask, nemo_curator.tasks.FileGroupTask]`

Stage that partitions input file paths into FileGroupTasks.

This stage runs as a dedicated processing stage (not on the driver)
and creates file groups based on the partitioning strategy.

Parameters
----------
file_paths: str | list[str]
    Path to the input files.
files_per_partition: int | None = None
    Number of files per partition. If provided, the blocksize is ignored.
    Defaults to 1 if both files_per_partition and blocksize are not provided.
blocksize: int | str | None = None
    Target size of the partitions.
    Note: For compressed files, the compressed size is used for blocksize estimation.
file_extensions: list[str] | None = None
    File extensions to filter.
storage_options: dict[str, Any] | None = None
    Storage options to pass to the file system.
limit: int | None = None
    Maximum number of partitions to create.

```python
file_paths: str | list[str]
```

**Value**: `None`


```python
files_per_partition: int | None
```

**Value**: `None`


```python
blocksize: int | str | None
```

**Value**: `None`


```python
file_extensions: list[str] | None
```

**Value**: `None`


```python
storage_options: dict[str, typing.Any] | None
```

**Value**: `None`


```python
limit: int | None
```

**Value**: `None`


```python
_name: str
```

**Value**: `file_partitioning`


```python
__post_init__()
```

Initialize default values.


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
ray_stage_spec() -> dict[str, typing.Any]
```

Ray stage specification for this stage.


```python
process(_: nemo_curator.tasks._EmptyTask) -> list[nemo_curator.tasks.FileGroupTask]
```

Process the initial task to create file group tasks.

This stage expects a simple Task with file paths information
and outputs multiple FileGroupTasks for parallel processing.


```python
_get_file_list_with_sizes() -> list[tuple[str, int]]
```

Get the list of files to process.


```python
_get_file_list() -> list[str]
```

Get the list of files to process.


```python
_get_dataset_name(files: list[str]) -> str
```

Extract dataset name from file paths (fsspec-compatible).


```python
_partition_by_count(
    files: list[str], count: int
) -> list[list[str]]
```

Partition files by count.


```python
_partition_by_size(
    files: list[tuple[str, int]], blocksize: int | str
) -> list[list[str]]
```

Partition files by target size.

**Parameters:**

<ParamField path="files" type="list[tuple[str, int]]">
  A list of tuples (file_path, file_size)
</ParamField>

<ParamField path="blocksize" type="int | str">
  The target size of the partitions
</ParamField>

**Returns:**

A list of lists, where each inner list contains the file paths of the files in the partitionN


```python
_parse_size(s: float | str) -> int
```

Taken from dask.utils.parse_bytes
https://github.com/dask/dask/blob/3801bedc7c71c83f37e836af71f740974c0434b3/dask/utils.py#L1585
Parse byte string to numbers.

>>> parse_bytes('100')
100
>>> parse_bytes('100 MB')
100000000
>>> parse_bytes('100M')
100000000
>>> parse_bytes('5kB')
5000
>>> parse_bytes('5.4 kB')
5400
>>> parse_bytes('1kiB')
1024
>>> parse_bytes('1e6')
1000000
>>> parse_bytes('1e6 kB')
1000000000
>>> parse_bytes('MB')
1000000
>>> parse_bytes(123)
123
>>> parse_bytes('5 foos')
Traceback (most recent call last):
    ...
ValueError: Could not interpret 'foos' as a byte unit

