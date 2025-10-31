---
layout: overview
slug: nemo-curator-stages-client-partitioning
---

# nemo_curator.stages.client_partitioning



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ClientPartitioningStage`](#nemo_curatorstagesclient_partitioningclientpartitioningstage) | Stage that partitions input file paths from a client into FileGroupTasks. |

### Functions

| Name | Description |
|------|-------------|
| [`_read_list_json_rel`](#nemo_curatorstagesclient_partitioning_read_list_json_rel) | Read JSON list (via fsspec) and return entries relative to `root`. Validates each entry is under `root`. |

### API

```python
class nemo_curator.stages.client_partitioning.ClientPartitioningStage
```

**Bases**: `nemo_curator.stages.file_partitioning.FilePartitioningStage`

Stage that partitions input file paths from a client into FileGroupTasks.

This stage runs as a dedicated processing stage (not on the driver)
and creates file groups based on the partitioning strategy.

```python
input_list_json_path: str | None
```

**Value**: `None`


```python
_name: str
```

**Value**: `client_partitioning`


```python
_fs: fsspec.AbstractFileSystem | None
```

**Value**: `field(...)`


```python
_root: str | None
```

**Value**: `field(...)`


```python
setup(worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
process(_: nemo_curator.tasks._EmptyTask) -> list[nemo_curator.tasks.FileGroupTask]
```


```python
_list_relative() -> list[str]
```

Return sorted, de-duplicated list of paths relative to root.


```python
nemo_curator.stages.client_partitioning._read_list_json_rel(
    root: str,
    json_url: str,
    storage_options: dict[str, typing.Any]
) -> list[str]
```

Read JSON list (via fsspec) and return entries relative to `root`.
Validates each entry is under `root`.

