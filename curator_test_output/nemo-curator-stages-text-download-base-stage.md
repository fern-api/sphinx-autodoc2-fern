---
layout: overview
slug: nemo-curator-stages-text-download-base-stage
---

# nemo_curator.stages.text.download.base.stage



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`DocumentDownloadExtractStage`](#nemo_curatorstagestextdownloadbasestagedocumentdownloadextractstage) | Composite stage that combines URL generation, download, iterate, and extract stages. |

### API

```python
class nemo_curator.stages.text.download.base.stage.DocumentDownloadExtractStage
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks._EmptyTask, nemo_curator.tasks.DocumentBatch]`

Composite stage that combines URL generation, download, iterate, and extract stages.

This supports the full 4-step pipeline pattern like Common Crawl:
1. Generate URLs from minimal input
2. Download files from URLs
3. Iterate through files to extract raw records
4. Extract structured content from raw records

```python
url_generator: nemo_curator.stages.text.download.base.url_generation.URLGenerator
```

**Value**: `None`


```python
downloader: nemo_curator.stages.text.download.base.download.DocumentDownloader
```

**Value**: `None`


```python
iterator: nemo_curator.stages.text.download.base.iterator.DocumentIterator
```

**Value**: `None`


```python
extractor: nemo_curator.stages.text.download.base.extract.DocumentExtractor | None
```

**Value**: `None`


```python
url_limit: int | None
```

**Value**: `None`


```python
record_limit: int | None
```

**Value**: `None`


```python
add_filename_column: bool | str
```

**Value**: `True`


```python
__post_init__()
```

Initialize the constituent stages.


```python
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

Decompose into constituent stages.


```python
get_description() -> str
```

Get description of this composite stage.

