---
layout: overview
slug: nemo-curator-stages-text-deduplication-removal
---

# nemo_curator.stages.text.deduplication.removal

Removal stage for distributed deduplication pipeline.

This stage implements the removal phase of the distributed deduplication approach:
1. Takes a DocumentBatch and determines the min/max ID range
2. Filters the parquet files for IDs to remove within this range
3. Filters out documents based on the removal list
4. Returns the filtered DocumentBatch

## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`TextDuplicatesRemovalStage`](#nemo_curatorstagestextdeduplicationremovaltextduplicatesremovalstage) | Stage for removing duplicate documents based on pre-computed removal lists. |

### API

```python
class nemo_curator.stages.text.deduplication.removal.TextDuplicatesRemovalStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

Stage for removing duplicate documents based on pre-computed removal lists.

**Parameters:**

- **ids_to_remove_path**: Path to parquet files containing IDs to remove
- **id_field**: Field to use for deduplication within the input dataframe. Defaults to CURATOR_DEDUP_ID_STR.
- **duplicate_id_field**: Field to use for deduplication within the removal dataframe. Defaults to "id".
- **read_kwargs**: Additional arguments for reading parquet files

```python
ids_to_remove_path: str
```

**Value**: `None`


```python
id_field: str
```

**Value**: `None`


```python
duplicate_id_field: str
```

**Value**: `id`


```python
read_kwargs: dict[str, typing.Any] | None
```

**Value**: `None`


```python
__post_init__()
```

Initialize parent class after dataclass initialization.


```python
process(task: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.DocumentBatch
```

Our deduplicator should've written out a parquet file with the IDs to remove.
We read that file, filter the input dataframe to only include the IDs to remove,
and return the filtered dataframe.
We optimize by not loading the whole ids to remove into memory, but only loading the ids that are in the range of the input dataframe.


```python
inputs() -> tuple[list[str], list[str]]
```

