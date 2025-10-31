---
layout: overview
slug: nemo-curator-stages-text-download-common-crawl-download
---

# nemo_curator.stages.text.download.common_crawl.download



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CommonCrawlWARCDownloader`](#nemo_curatorstagestextdownloadcommon_crawldownloadcommoncrawlwarcdownloader) | Downloads WARC files from the Common Crawl to a local directory |

### API

```python
class nemo_curator.stages.text.download.common_crawl.download.CommonCrawlWARCDownloader(download_dir: str, use_aws_to_download: bool = False, verbose: bool = False)
```

**Bases**: `nemo_curator.stages.text.download.DocumentDownloader`

Downloads WARC files from the Common Crawl to a local directory

### Initialization

Creates a downloader

**Parameters:**

- **download_dir**: Path to store raw compressed WARC files
- **use_aws_to_download**: If True, uses the s5cmd command to download from the Common Crawl's S3 bucket.
  If False, uses wget.
- **verbose**: If True, logs stdout and stderr of the download command (s5cmd/wget)


```python
_get_output_filename(url: str) -> str
```

Generate output filename from URL.


```python
_download_to_path(
    url: str, path: str
) -> tuple[bool, str | None]
```

Download a file to a temporary file.

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

