---
layout: overview
slug: nemo-curator-stages-text-download-wikipedia-download
---

# nemo_curator.stages.text.download.wikipedia.download



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`WikipediaDownloader`](#nemo_curatorstagestextdownloadwikipediadownloadwikipediadownloader) | Downloads Wikipedia dump files (.bz2) from wikimedia.org. |

### API

```python
class nemo_curator.stages.text.download.wikipedia.download.WikipediaDownloader(download_dir: str, verbose: bool = False)
```

**Bases**: `nemo_curator.stages.text.download.DocumentDownloader`

Downloads Wikipedia dump files (.bz2) from wikimedia.org.

### Initialization

Creates a Wikipedia downloader.

**Parameters:**

- **download_dir**: Path to store raw compressed .bz2 files
- **verbose**: If True, logs stdout and stderr of the download command


```python
_get_output_filename(url: str) -> str
```

Generate output filename from URL.


```python
_download_to_path(
    url: str, path: str
) -> tuple[bool, str | None]
```

Download a Wikipedia dump file to the specified path.

**Parameters:**

<ParamField path="url" type="str">
  URL to download
</ParamField>

<ParamField path="path" type="str">
  Local path to save file
</ParamField>

**Returns:**

Tuple of (success, error_message). If success is True, error_message is None.
If success is False, error_message contains the error details.


```python
num_workers_per_node() -> int | None
```

