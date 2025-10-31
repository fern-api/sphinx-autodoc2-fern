---
layout: overview
slug: nemo-curator-utils-client-utils
---

# nemo_curator.utils.client_utils



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`FSPath`](#nemo_curatorutilsclient_utilsfspath) | Wrapper that combines filesystem and path for convenient file operations. |

### Functions

| Name | Description |
|------|-------------|
| [`is_remote_url`](#nemo_curatorutilsclient_utilsis_remote_url) | None |

### API

```python
class nemo_curator.utils.client_utils.FSPath(fs: fsspec.AbstractFileSystem, path: str)
```

Wrapper that combines filesystem and path for convenient file operations.

```python
open(
    mode: str = 'rb', **kwargs
) -> fsspec.spec.AbstractBufferedFile
```


```python
__str__()
```


```python
__repr__()
```


```python
as_posix() -> str
```


```python
get_bytes_cat_ranges(
    *, part_size: int = 10 * 1024**2
) -> bytes
```

Read object into memory using fsspec's cat_ranges.
Modified from https://github.com/rapidsai/cudf/blob/ba64909422016ba389ab06ed01d7578336c19e8e/python/dask_cudf/dask_cudf/io/json.py#L26-L34


```python
nemo_curator.utils.client_utils.is_remote_url(url: str) -> bool
```

