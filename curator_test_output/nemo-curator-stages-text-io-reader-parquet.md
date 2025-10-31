---
layout: overview
slug: nemo-curator-stages-text-io-reader-parquet
---

# nemo_curator.stages.text.io.reader.parquet



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ParquetReaderStage`](#nemo_curatorstagestextioreaderparquetparquetreaderstage) | Stage that processes a group of Parquet files into a DocumentBatch. This stage accepts FileGroupTasks created by FilePartitioningStage and reads the actual file contents into DocumentBatches. |
| [`ParquetReader`](#nemo_curatorstagestextioreaderparquetparquetreader) | Composite stage for reading Parquet files. |

### API

```python
class nemo_curator.stages.text.io.reader.parquet.ParquetReaderStage
```

**Bases**: `nemo_curator.stages.text.io.reader.base.BaseReader`

Stage that processes a group of Parquet files into a DocumentBatch.
This stage accepts FileGroupTasks created by FilePartitioningStage
and reads the actual file contents into DocumentBatches.

**Parameters:**

- **fields (list[str], optional)**: If specified, only read these columns. Defaults to None.
- **read_kwargs (dict[str, Any], optional)**: Keyword arguments for the underlying reader. Defaults to \{\}.

```python
_name: str
```

**Value**: `parquet_reader`


```python
read_data(
    paths: list[str],
    read_kwargs: dict[str, typing.Any] | None = None,
    fields: list[str] | None = None
) -> pandas.DataFrame
```

Read Parquet files using Pandas. Raises an exception if reading fails.


```python
class nemo_curator.stages.text.io.reader.parquet.ParquetReader
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks._EmptyTask, nemo_curator.tasks.DocumentBatch]`

Composite stage for reading Parquet files.

This high-level stage decomposes into:
1. FilePartitioningStage - partitions files into groups
2. ParquetReaderStage - reads file groups into DocumentBatches

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
fields: list[str] | None
```

**Value**: `None`


```python
read_kwargs: dict[str, typing.Any] | None
```

**Value**: `None`


```python
file_extensions: list[str]
```

**Value**: `field(...)`


```python
task_type: typing.Literal[document, image, video, audio]
```

**Value**: `document`


```python
_generate_ids: bool
```

**Value**: `False`


```python
_assign_ids: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `parquet_reader`


```python
__post_init__()
```

Initialize parent class after dataclass initialization.


```python
decompose() -> list[nemo_curator.stages.text.io.reader.parquet.ParquetReaderStage]
```

Decompose into file partitioning and processing stages.


```python
get_description() -> str
```

Get a description of this composite stage.

