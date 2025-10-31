---
layout: overview
slug: nemo-curator-utils-file-utils
---

# nemo_curator.utils.file_utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`get_fs`](#nemo_curatorutilsfile_utilsget_fs) | None |
| [`is_not_empty`](#nemo_curatorutilsfile_utilsis_not_empty) | None |
| [`delete_dir`](#nemo_curatorutilsfile_utilsdelete_dir) | None |
| [`create_or_overwrite_dir`](#nemo_curatorutilsfile_utilscreate_or_overwrite_dir) | Creates a directory if it does not exist and overwrites it if it does. Warning: This function will delete all files in the directory if it exists. |
| [`filter_files_by_extension`](#nemo_curatorutilsfile_utilsfilter_files_by_extension) | None |
| [`_split_files_as_per_blocksize`](#nemo_curatorutilsfile_utils_split_files_as_per_blocksize) | None |
| [`_gather_extention`](#nemo_curatorutilsfile_utils_gather_extention) | Gather the extension of a given path. Args: path: The path to get the extension from. Returns: The extension of the path. |
| [`_gather_file_records`](#nemo_curatorutilsfile_utils_gather_file_records) | Gather file records from a given path. Args: path: The path to get the file paths from. recurse_subdirectories: Whether to recurse subdirectories. keep_extensions: The extensions to keep. storage_options: The storage options to use. fs: The filesystem to use. include_size: Whether to include the size of the files. Returns: A list of tuples (file_path, file_size). |
| [`get_all_file_paths_under`](#nemo_curatorutilsfile_utilsget_all_file_paths_under) | Get all file paths under a given path. Args: path: The path to get the file paths from. recurse_subdirectories: Whether to recurse subdirectories. keep_extensions: The extensions to keep. storage_options: The storage options to use. fs: The filesystem to use. Returns: A list of file paths. |
| [`get_all_file_paths_and_size_under`](#nemo_curatorutilsfile_utilsget_all_file_paths_and_size_under) | Get all file paths and their sizes under a given path. Args: path: The path to get the file paths from. recurse_subdirectories: Whether to recurse subdirectories. keep_extensions: The extensions to keep. storage_options: The storage options to use. fs: The filesystem to use. Returns: A list of tuples (file_path, file_size). |
| [`infer_protocol_from_paths`](#nemo_curatorutilsfile_utilsinfer_protocol_from_paths) | Infer a protocol from a list of paths, if any. |
| [`pandas_select_columns`](#nemo_curatorutilsfile_utilspandas_select_columns) | Project a Pandas DataFrame onto existing columns, logging warnings for missing ones. |
| [`check_output_mode`](#nemo_curatorutilsfile_utilscheck_output_mode) | Validate and act on the write mode for an output directory. |
| [`infer_dataset_name_from_path`](#nemo_curatorutilsfile_utilsinfer_dataset_name_from_path) | Infer a dataset name from a path, handling both local and cloud storage paths. Args: path: Local path or cloud storage URL (e.g. s3://, abfs://) Returns: Inferred dataset name from the path |
| [`check_disallowed_kwargs`](#nemo_curatorutilsfile_utilscheck_disallowed_kwargs) | Check if any of the disallowed keys are in provided kwargs Used for read/write kwargs in stages. Args: kwargs: The dictionary to check disallowed_keys: The keys that are not allowed. raise_error: Whether to raise an error if any of the disallowed keys are in the kwargs. Raises: ValueError: If any of the disallowed keys are in the kwargs and raise_error is True. Warning: If any of the disallowed keys are in the kwargs and raise_error is False. Returns: None |
| [`_is_safe_path`](#nemo_curatorutilsfile_utils_is_safe_path) | Check if a path is safe for extraction (no path traversal). |
| [`tar_safe_extract`](#nemo_curatorutilsfile_utilstar_safe_extract) | Safely extract a tar file, preventing path traversal attacks. |

### Data

`FILETYPE_TO_DEFAULT_EXTENSIONS`

### API

```python
nemo_curator.utils.file_utils.FILETYPE_TO_DEFAULT_EXTENSIONS
```

**Value**: `None`


```python
nemo_curator.utils.file_utils.get_fs(
    path: str, storage_options: dict[str, str] | None = None
) -> fsspec.AbstractFileSystem
```


```python
nemo_curator.utils.file_utils.is_not_empty(
    path: str,
    fs: fsspec.AbstractFileSystem | None = None,
    storage_options: dict[str, str] | None = None
) -> bool
```


```python
nemo_curator.utils.file_utils.delete_dir(
    path: str,
    fs: fsspec.AbstractFileSystem | None = None,
    storage_options: dict[str, str] | None = None
) -> None
```


```python
nemo_curator.utils.file_utils.create_or_overwrite_dir(
    path: str,
    fs: fsspec.AbstractFileSystem | None = None,
    storage_options: dict[str, str] | None = None
) -> None
```

Creates a directory if it does not exist and overwrites it if it does.
Warning: This function will delete all files in the directory if it exists.


```python
nemo_curator.utils.file_utils.filter_files_by_extension(
    files_list: list[str], keep_extensions: str | list[str]
) -> list[str]
```


```python
nemo_curator.utils.file_utils._split_files_as_per_blocksize(
    sorted_file_sizes: list[tuple[str, int]], max_byte_per_chunk: int
) -> list[list[str]]
```


```python
nemo_curator.utils.file_utils._gather_extention(path: str) -> str
```

Gather the extension of a given path.

**Parameters:**

<ParamField path="path" type="str">
  The path to get the extension from.
</ParamField>

**Returns:**

The extension of the path.


```python
nemo_curator.utils.file_utils._gather_file_records(
    path: str,
    recurse_subdirectories: bool,
    keep_extensions: str | list[str] | None,
    storage_options: dict[str, str] | None,
    fs: fsspec.AbstractFileSystem | None,
    include_size: bool
) -> list[tuple[str, int]]
```

Gather file records from a given path.

**Parameters:**

<ParamField path="path" type="str">
  The path to get the file paths from.
</ParamField>

<ParamField path="recurse_subdirectories" type="bool">
  Whether to recurse subdirectories.
</ParamField>

<ParamField path="keep_extensions" type="str | list[str] | None">
  The extensions to keep.
</ParamField>

<ParamField path="storage_options" type="dict[str, str] | None">
  The storage options to use.
</ParamField>

<ParamField path="fs" type="fsspec.AbstractFileSystem | None">
  The filesystem to use.
</ParamField>

<ParamField path="include_size" type="bool">
  Whether to include the size of the files.
</ParamField>

**Returns:**

A list of tuples (file_path, file_size).


```python
nemo_curator.utils.file_utils.get_all_file_paths_under(
    path: str,
    recurse_subdirectories: bool = False,
    keep_extensions: str | list[str] | None = None,
    storage_options: dict[str, str] | None = None,
    fs: fsspec.AbstractFileSystem | None = None
) -> list[str]
```

Get all file paths under a given path.

**Parameters:**

<ParamField path="path" type="str">
  The path to get the file paths from.
</ParamField>

<ParamField path="recurse_subdirectories" type="bool" default="False">
  Whether to recurse subdirectories.
</ParamField>

<ParamField path="keep_extensions" type="str | list[str] | None">
  The extensions to keep.
</ParamField>

<ParamField path="storage_options" type="dict[str, str] | None">
  The storage options to use.
</ParamField>

<ParamField path="fs" type="fsspec.AbstractFileSystem | None">
  The filesystem to use.
</ParamField>

**Returns:**

A list of file paths.


```python
nemo_curator.utils.file_utils.get_all_file_paths_and_size_under(
    path: str,
    recurse_subdirectories: bool = False,
    keep_extensions: str | list[str] | None = None,
    storage_options: dict[str, str] | None = None,
    fs: fsspec.AbstractFileSystem | None = None
) -> list[tuple[str, int]]
```

Get all file paths and their sizes under a given path.

**Parameters:**

<ParamField path="path" type="str">
  The path to get the file paths from.
</ParamField>

<ParamField path="recurse_subdirectories" type="bool" default="False">
  Whether to recurse subdirectories.
</ParamField>

<ParamField path="keep_extensions" type="str | list[str] | None">
  The extensions to keep.
</ParamField>

<ParamField path="storage_options" type="dict[str, str] | None">
  The storage options to use.
</ParamField>

<ParamField path="fs" type="fsspec.AbstractFileSystem | None">
  The filesystem to use.
</ParamField>

**Returns:**

A list of tuples (file_path, file_size).


```python
nemo_curator.utils.file_utils.infer_protocol_from_paths(paths: collections.abc.Iterable[str]) -> str | None
```

Infer a protocol from a list of paths, if any.

Returns the first detected protocol scheme (e.g., "s3", "gcs", "gs", "abfs")
or None for local paths.


```python
nemo_curator.utils.file_utils.pandas_select_columns(
    df: pandas.DataFrame,
    columns: list[str] | None,
    file_path: str
) -> pandas.DataFrame | None
```

Project a Pandas DataFrame onto existing columns, logging warnings for missing ones.

Returns the projected DataFrame. If no requested columns exist, returns None.


```python
nemo_curator.utils.file_utils.check_output_mode(
    mode: typing.Literal[overwrite, append, error, ignore],
    fs: fsspec.AbstractFileSystem,
    path: str,
    append_mode_implemented: bool = False
) -> None
```

Validate and act on the write mode for an output directory.

Modes:
- "overwrite": delete existing `output_dir` recursively if it exists.
- "append": no-op here; raises if append is not implemented.
- "error": raise FileExistsError if `output_dir` already exists.
- "ignore": no-op.


```python
nemo_curator.utils.file_utils.infer_dataset_name_from_path(path: str) -> str
```

Infer a dataset name from a path, handling both local and cloud storage paths.

**Parameters:**

<ParamField path="path" type="str">
  Local path or cloud storage URL (e.g. s3://, abfs://)
</ParamField>

**Returns:**

Inferred dataset name from the path


```python
nemo_curator.utils.file_utils.check_disallowed_kwargs(
    kwargs: dict,
    disallowed_keys: list[str],
    raise_error: bool = True
) -> None
```

Check if any of the disallowed keys are in provided kwargs
Used for read/write kwargs in stages.

**Parameters:**

<ParamField path="kwargs" type="dict">
  The dictionary to check
</ParamField>

<ParamField path="disallowed_keys" type="list[str]">
  The keys that are not allowed.
</ParamField>

<ParamField path="raise_error" type="bool" default="True">
  Whether to raise an error if any of the disallowed keys are in the kwargs.
</ParamField>

**Returns:**

None

**Raises:**

ValueError: If any of the disallowed keys are in the kwargs and raise_error is True.
<Warning> If any of the disallowed keys are in the kwargs and raise_error is False. </Warning>


```python
nemo_curator.utils.file_utils._is_safe_path(
    path: str, base_path: str
) -> bool
```

Check if a path is safe for extraction (no path traversal).

**Parameters:**

<ParamField path="path" type="str">
  The path to check
</ParamField>

<ParamField path="base_path" type="str">
  The base directory for extraction
</ParamField>

**Returns:**

True if the path is safe, False otherwise


```python
nemo_curator.utils.file_utils.tar_safe_extract(
    tar: tarfile.TarFile, path: str
) -> None
```

Safely extract a tar file, preventing path traversal attacks.

**Parameters:**

<ParamField path="tar" type="tarfile.TarFile">
  The TarFile object to extract
</ParamField>

<ParamField path="path" type="str">
  The destination path for extraction
</ParamField>

**Raises:**

ValueError: If any member has an unsafe path

