---
layout: overview
slug: nemo-curator-stages-text-download-common-crawl-stage
---

# nemo_curator.stages.text.download.common_crawl.stage



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CommonCrawlDownloadExtractStage`](#nemo_curatorstagestextdownloadcommon_crawlstagecommoncrawldownloadextractstage) | Composite stage for downloading and processing Common Crawl data. |

### API

```python
class nemo_curator.stages.text.download.common_crawl.stage.CommonCrawlDownloadExtractStage(start_snapshot: str, end_snapshot: str, download_dir: str, crawl_type: typing.Literal[main, news] = 'main', html_extraction: nemo_curator.stages.text.download.html_extractors.HTMLExtractorAlgorithm | str | None = None, html_extraction_kwargs: dict | None = None, stop_lists: dict[str, frozenset[str]] | None = None, use_aws_to_download: bool = False, verbose: bool = False, url_limit: int | None = None, record_limit: int | None = None, add_filename_column: bool | str = True)
```

**Bases**: `nemo_curator.stages.text.download.DocumentDownloadExtractStage`

Composite stage for downloading and processing Common Crawl data.

This pipeline:
1. Generates WARC URLs (either from main or news crawls)
2. Downloads WARC files
3. Extracts content from WARC files
4. Extracts text from HTML content

```python
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

Decompose this composite stage into its constituent stages.


```python
get_description() -> str
```

Get a description of this composite stage.

