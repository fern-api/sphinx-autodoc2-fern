---
layout: overview
slug: nemo-curator-stages-text-io-reader-base
---

# nemo_curator.stages.text.io.reader.base



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`BaseReader`](#nemo_curatorstagestextioreaderbasebasereader) | Common base for tabular file readers. |

### API

```python
class nemo_curator.stages.text.io.reader.base.BaseReader
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks.DocumentBatch]`

Common base for tabular file readers.

Subclasses must implement the read_data method.

```python
fields: list[str] | None
```

**Value**: `None`


```python
read_kwargs: dict[str, typing.Any]
```

**Value**: `field(...)`


```python
_name: str
```

**Value**: ``


```python
_generate_ids: bool
```

**Value**: `False`


```python
_assign_ids: bool
```

**Value**: `False`


```python
__post_init__() -> None
```


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
setup(_: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.DocumentBatch
```


```python
read_data(
    file_paths: list[str],
    read_kwargs: dict[str, typing.Any] | None,
    fields: list[str] | None
) -> pandas.DataFrame | None
```


```python
_assign_ids_func(
    filepath: str | list[str], df: pandas.DataFrame
) -> pandas.DataFrame
```


```python
_generate_ids_func(
    filepath: str | list[str], df: pandas.DataFrame
) -> pandas.DataFrame
```


```python
ray_stage_spec() -> dict[str, typing.Any]
```

