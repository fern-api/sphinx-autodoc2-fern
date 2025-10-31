---
layout: overview
slug: nemo-curator-stages-text-download-base-download
---

# nemo_curator.stages.text.download.base.download



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`DocumentDownloader`](#nemo_curatorstagestextdownloadbasedownloaddocumentdownloader) | Abstract base class for document downloaders. |
| [`DocumentDownloadStage`](#nemo_curatorstagestextdownloadbasedownloaddocumentdownloadstage) | Stage that downloads files from URLs to local storage. |

### API

```python
class nemo_curator.stages.text.download.base.download.DocumentDownloader(download_dir: str, verbose: bool = False)
```

**Bases**: `abc.ABC`

Abstract base class for document downloaders.

### Initialization

Initialize the downloader.

**Parameters:**

- **download_dir**: Directory to store downloaded files
- **verbose**: If True, logs detailed download information


```python
_check_s5cmd_installed() -> bool
```

Check if s5cmd is installed.


```python
_get_output_filename(url: str) -> str
```

Generate output filename from URL.

**Parameters:**

<ParamField path="url" type="str">
  URL to download
</ParamField>

**Returns:**

Output filename (without directory path)


```python
_download_to_path(
    url: str, path: str
) -> tuple[bool, str | None]
```

Download URL to specified path.

**Parameters:**

<ParamField path="url" type="str">
  URL to download
</ParamField>

<ParamField path="path" type="str">
  Local path to save file
</ParamField>

**Returns:**

Tuple of (success, error_message). If success is True, error_message should be None.
If success is False, error_message should contain the error details.


```python
download(url: str) -> str | None
```

Download a document from URL with temporary file handling.

Downloads file to temporary location then atomically moves to final path.
Checks for existing file to avoid re-downloading. Supports resumable downloads.

**Parameters:**

<ParamField path="url" type="str">
  URL to download
</ParamField>

**Returns:**

Path to downloaded file, or None if download failed


```python
num_workers_per_node() -> int | None
```

Number of workers per node for Downloading. This is sometimes needed to ensure we are not overloading the network.

**Returns:**

Number of workers per node, or None if there is no limit and we can download as fast as possible


```python
class nemo_curator.stages.text.download.base.download.DocumentDownloadStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks.FileGroupTask]`

Stage that downloads files from URLs to local storage.

Takes a FileGroupTask with URLs and returns a FileGroupTask with local file paths.
This allows the download step to scale independently from iteration/extraction.

```python
_resources
```

**Value**: `Resources(...)`


```python
downloader: nemo_curator.stages.text.download.base.download.DocumentDownloader
```

**Value**: `None`


```python
_batch_size
```

**Value**: `None`


```python
__post_init__()
```


```python
inputs() -> tuple[list[str], list[str]]
```

Define input requirements - expects FileGroupTask with URLs.


```python
outputs() -> tuple[list[str], list[str]]
```

Define output - produces FileGroupTask with local paths.


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```

Download URLs to local files.

**Parameters:**

**Returns:**

FileGroupTask: Task containing local file paths


```python
xenna_stage_spec() -> dict[str, typing.Any]
```

