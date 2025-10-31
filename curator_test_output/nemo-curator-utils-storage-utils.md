---
layout: overview
slug: nemo-curator-utils-storage-utils
---

# nemo_curator.utils.storage_utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`_get_local_path`](#nemo_curatorutilsstorage_utils_get_local_path) | Construct a full local path from a base path and additional components. Args: localpath: The base local path. *args: Additional path components. Returns: The full local path as a Path object. |
| [`get_full_path`](#nemo_curatorutilsstorage_utilsget_full_path) | Construct a full path from a base path and additional components. Args: path: The base path. *args: Additional path components. Returns: The full path as a StoragePrefix or Path object. |

### API

```python
nemo_curator.utils.storage_utils._get_local_path(
    localpath: pathlib.Path, *args: str
) -> pathlib.Path
```

Construct a full local path from a base path and additional components.

**Parameters:**

<ParamField path="localpath" type="pathlib.Path">
  The base local path.
</ParamField>

**Returns:**

The full local path as a Path object.


```python
nemo_curator.utils.storage_utils.get_full_path(
    path: str | pathlib.Path, *args: str
) -> pathlib.Path
```

Construct a full path from a base path and additional components.

**Parameters:**

<ParamField path="path" type="str | pathlib.Path">
  The base path.
</ParamField>

**Returns:**

The full path as a StoragePrefix or Path object.

