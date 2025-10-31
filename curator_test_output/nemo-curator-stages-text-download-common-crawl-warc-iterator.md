---
layout: overview
slug: nemo-curator-stages-text-download-common-crawl-warc-iterator
---

# nemo_curator.stages.text.download.common_crawl.warc_iterator



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CommonCrawlWarcIterator`](#nemo_curatorstagestextdownloadcommon_crawlwarc_iteratorcommoncrawlwarciterator) | Processes downloaded WARC files. |

### API

```python
class nemo_curator.stages.text.download.common_crawl.warc_iterator.CommonCrawlWarcIterator
```

**Bases**: `nemo_curator.stages.text.download.DocumentIterator`

Processes downloaded WARC files.

```python
iterate(file_path: str) -> collections.abc.Iterator[dict[str, typing.Any]]
```

Process a task containing WARC files and extract their contents.


```python
output_columns() -> list[str]
```

