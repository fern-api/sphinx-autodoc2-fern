---
layout: overview
slug: nemo-curator-stages-image-deduplication-removal
---

# nemo_curator.stages.image.deduplication.removal



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ImageDuplicatesRemovalStage`](#nemo_curatorstagesimagededuplicationremovalimageduplicatesremovalstage) | Filter stage that removes images whose IDs appear in a Parquet file. |

### API

```python
class nemo_curator.stages.image.deduplication.removal.ImageDuplicatesRemovalStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.ImageBatch, nemo_curator.tasks.ImageBatch]`

Filter stage that removes images whose IDs appear in a Parquet file.

The Parquet file must contain a column with image identifiers; by default this
column is assumed to be ``id`` to match writer metadata. You can change
the column name via ``duplicate_id_field``.

**Parameters:**

- **removal_parquets_dir**: Directory containing Parquet files with image IDs to remove
- **duplicate_id_field**: Name of the column containing image IDs to remove
- **verbose**: Whether to log verbose output
- **num_workers_per_node**: Number of workers per node for the stage. This is sometimes needed
  to avoid OOM when concurrently running actors on one node loading the same removal
  parquet files into memory.

```python
removal_parquets_dir: str
```

**Value**: `None`


```python
duplicate_id_field: str
```

**Value**: `id`


```python
verbose: bool
```

**Value**: `False`


```python
num_workers_per_node: int | None
```

**Value**: `None`


```python
_name: str
```

**Value**: `image_dedup_filter`


```python
_ids_to_remove: set[str]
```

**Value**: `field(...)`


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
setup(_worker_metadata=None) -> None
```


```python
process(task: nemo_curator.tasks.ImageBatch) -> nemo_curator.tasks.ImageBatch
```


```python
xenna_stage_spec() -> dict[str, typing.Any]
```

