---
layout: overview
slug: nemo-curator-stages-deduplication-semantic-utils
---

# nemo_curator.stages.deduplication.semantic.utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`get_array_from_df`](#nemo_curatorstagesdeduplicationsemanticutilsget_array_from_df) | Convert a column of lists to a 2D array. |
| [`break_parquet_partition_into_groups`](#nemo_curatorstagesdeduplicationsemanticutilsbreak_parquet_partition_into_groups) | Break parquet files into groups to avoid cudf 2bn row limit. |

### API

```python
nemo_curator.stages.deduplication.semantic.utils.get_array_from_df(
    df: cudf.DataFrame, embedding_col: str
) -> cupy.ndarray
```

Convert a column of lists to a 2D array.


```python
nemo_curator.stages.deduplication.semantic.utils.break_parquet_partition_into_groups(
    files: list[str],
    embedding_dim: int | None = None,
    storage_options: dict[str, typing.Any] | None = None
) -> list[list[str]]
```

Break parquet files into groups to avoid cudf 2bn row limit.

