---
layout: overview
slug: nemo-curator-stages-deduplication-io-utils
---

# nemo_curator.stages.deduplication.io_utils



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`DeduplicationIO`](#nemo_curatorstagesdeduplicationio_utilsdeduplicationio) | None |

### API

```python
class nemo_curator.stages.deduplication.io_utils.DeduplicationIO(id_generator: IdGenerator | None, **kwargs)
```

```python
read_jsonl(
    filepath: str | list[str],
    columns: list[str] | None = None,
    assign_id: bool = False,
    **kwargs
) -> cudf.DataFrame
```


```python
read_parquet(
    filepath: str | list[str],
    assign_id: bool = False,
    **kwargs
) -> cudf.DataFrame
```


```python
write_parquet(
    df: cudf.DataFrame,
    filepath: str,
    **kwargs
) -> None
```


```python
custom_read(
    filepath: str | list[str],
    read_func: collections.abc.Callable,
    assign_id: bool = False,
    **kwargs
) -> cudf.DataFrame
```


```python
assign_id(
    filepath: str | list[str], df: cudf.DataFrame
) -> cudf.DataFrame
```

