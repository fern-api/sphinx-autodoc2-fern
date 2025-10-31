---
layout: overview
slug: nemo-curator-stages-text-io-reader-jsonl
---

# nemo_curator.stages.text.io.reader.jsonl



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`JsonlReaderStage`](#nemo_curatorstagestextioreaderjsonljsonlreaderstage) | Stage that processes a group of JSONL files into a DocumentBatch. This stage accepts FileGroupTasks created by FilePartitioningStage and reads the actual file contents into DocumentBatches. |
| [`JsonlReader`](#nemo_curatorstagestextioreaderjsonljsonlreader) | Composite stage for reading JSONL files. |

### API

```python
class nemo_curator.stages.text.io.reader.jsonl.JsonlReaderStage
```

**Bases**: `nemo_curator.stages.text.io.reader.base.BaseReader`

Stage that processes a group of JSONL files into a DocumentBatch.
This stage accepts FileGroupTasks created by FilePartitioningStage
and reads the actual file contents into DocumentBatches.

**Parameters:**

- **fields (list[str], optional)**: If specified, only read these fields (columns). Defaults to None.
- **read_kwargs (dict[str, Any], optional)**: Keyword arguments for the reader. Defaults to \{\}.
- **_generate_ids (bool)**: Whether to generate monotonically increasing IDs across all files.
  This uses IdGenerator actor, which needs to be instantiated before using this stage.
  This can be slow, so it is recommended to use AddId stage instead, unless monotonically increasing IDs
  are required.
- **_assign_ids (bool)**: Whether to assign monotonically increasing IDs from an IdGenerator.
  This uses IdGenerator actor, which needs to be instantiated before using this stage.
  This can be slow, so it is recommended to use AddId stage instead, unless monotonically increasing IDs
  are required.

```python
_name: str
```

**Value**: `jsonl_reader`


```python
read_data(
    paths: list[str],
    read_kwargs: dict[str, typing.Any] | None = None,
    fields: list[str] | None = None
) -> pandas.DataFrame | None
```

Read JSONL files using Pandas.


```python
class nemo_curator.stages.text.io.reader.jsonl.JsonlReader
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks._EmptyTask, nemo_curator.tasks.DocumentBatch]`

Composite stage for reading JSONL files.

This high-level stage decomposes into:
1. FilePartitioningStage - partitions files into groups
2. JsonlReaderStage - reads file groups into DocumentBatches

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
task_type: typing.Literal[document, image, video, audio]
```

**Value**: `document`


```python
file_extensions: list[str]
```

**Value**: `field(...)`


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

**Value**: `jsonl_reader`


```python
__post_init__()
```

Initialize parent class after dataclass initialization.


```python
decompose() -> list[nemo_curator.stages.text.io.reader.jsonl.JsonlReaderStage]
```

Decompose into file partitioning and processing stages.


```python
get_description() -> str
```

Get a description of this composite stage.

