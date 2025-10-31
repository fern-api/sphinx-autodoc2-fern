---
layout: overview
slug: nemo-curator-stages-text-download-arxiv-download
---

# nemo_curator.stages.text.download.arxiv.download



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ArxivDownloader`](#nemo_curatorstagestextdownloadarxivdownloadarxivdownloader) | Downloads Arxiv data from s3://arxiv/src/ |

### API

```python
class nemo_curator.stages.text.download.arxiv.download.ArxivDownloader(download_dir: str, verbose: bool = False)
```

**Bases**: `nemo_curator.stages.text.download.DocumentDownloader`

Downloads Arxiv data from s3://arxiv/src/

```python
_get_output_filename(url: str) -> str
```


```python
_download_to_path(
    url: str, path: str
) -> tuple[bool, str | None]
```

