---
layout: overview
slug: nemo-curator-utils-operation-utils
---

# nemo_curator.utils.operation_utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`get_tmp_dir`](#nemo_curatorutilsoperation_utilsget_tmp_dir) | Retrieve the appropriate temporary directory based on the runtime environment. |
| [`make_temporary_dir`](#nemo_curatorutilsoperation_utilsmake_temporary_dir) | Context manager to create a temporary directory. |
| [`make_named_temporary_file`](#nemo_curatorutilsoperation_utilsmake_named_temporary_file) | Context manager to create a named temporary file. |
| [`make_pipeline_temporary_dir`](#nemo_curatorutilsoperation_utilsmake_pipeline_temporary_dir) | Context manager to create a temporary directory for pipelines. |
| [`make_pipeline_named_temporary_file`](#nemo_curatorutilsoperation_utilsmake_pipeline_named_temporary_file) | Context manager to create a named temporary file for pipelines. |

### API

```python
nemo_curator.utils.operation_utils.get_tmp_dir() -> pathlib.Path
```

Retrieve the appropriate temporary directory based on the runtime environment.

**Returns:**

pathlib.Path: Path to the temporary directory.


```python
nemo_curator.utils.operation_utils.make_temporary_dir(
    *,
    prefix: str | None = None,
    target_dir: pathlib.Path | None = None,
    delete: bool = True
) -> collections.abc.Generator[pathlib.Path, None, None]
```

Context manager to create a temporary directory.

**Parameters:**

**Returns:**

Generator[pathlib.Path, None, None]: Path of the created temporary directory.


```python
nemo_curator.utils.operation_utils.make_named_temporary_file(
    *,
    prefix: str | None = None,
    suffix: str | None = None,
    delete: bool = True,
    target_dir: pathlib.Path | None = None
) -> collections.abc.Generator[pathlib.Path, None, None]
```

Context manager to create a named temporary file.

**Parameters:**

**Returns:**

Generator[pathlib.Path, None, None]: Path of the created temporary file.


```python
nemo_curator.utils.operation_utils.make_pipeline_temporary_dir(sub_dir: str | None = None) -> collections.abc.Generator[pathlib.Path, None, None]
```

Context manager to create a temporary directory for pipelines.


```python
nemo_curator.utils.operation_utils.make_pipeline_named_temporary_file(
    sub_dir: str | None = None, suffix: str | None = None
) -> collections.abc.Generator[pathlib.Path, None, None]
```

Context manager to create a named temporary file for pipelines.

