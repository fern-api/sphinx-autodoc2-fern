---
layout: overview
slug: nemo-curator-stages-deduplication-fuzzy-buckets-to-edges
---

# nemo_curator.stages.deduplication.fuzzy.buckets_to_edges



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`BucketsToEdgesStage`](#nemo_curatorstagesdeduplicationfuzzybuckets_to_edgesbucketstoedgesstage) | Stage that takes in a file consiting of LSH bucket ids and document ids belonging to the bucket and outputs a file consisting of edges between documents with the same bucket id. |

### API

```python
class nemo_curator.stages.deduplication.fuzzy.buckets_to_edges.BucketsToEdgesStage(output_path: str, doc_id_field: str = CURATOR_DEDUP_ID_STR, read_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None)
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks.FileGroupTask]`

Stage that takes in a file consiting of LSH bucket ids and document ids belonging to the bucket
and outputs a file consisting of edges between documents with the same bucket id.

**Parameters:**

- **doc_id_field**: The field name containing the document ids for each bucket.
- **output_path**: The directory to write the output file to.
- **read_kwargs**: Keyword arguments to pass for reading the input files.
  Only the storage_options key is supported for now.
- **write_kwargs**: Keyword arguments to pass for writing the output files.
  Only the storage_options key is supported for now.

```python
_name
```

**Value**: `BucketsToEdgesStage`


```python
_resources
```

**Value**: `Resources(...)`


```python
_check_io_kwargs(kwargs: dict[str, typing.Any] | None) -> None
```


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```

