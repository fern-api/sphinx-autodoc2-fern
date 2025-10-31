---
layout: overview
slug: nemo-curator-stages-text-download-common-crawl-extract
---

# nemo_curator.stages.text.download.common_crawl.extract



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CommonCrawlHTMLExtractor`](#nemo_curatorstagestextdownloadcommon_crawlextractcommoncrawlhtmlextractor) | None |

### API

```python
class nemo_curator.stages.text.download.common_crawl.extract.CommonCrawlHTMLExtractor(algorithm: nemo_curator.stages.text.download.html_extractors.HTMLExtractorAlgorithm | str | None = None, algorithm_kwargs: dict | None = None, stop_lists: dict[str, frozenset[str]] | None = None)
```

**Bases**: `nemo_curator.stages.text.download.DocumentExtractor`

```python
extract(record: dict[str, typing.Any]) -> dict[str, typing.Any] | None
```

Extract text from HTML content in the record.

Takes a record dict containing "content" field with HTML and returns
a new dict with only the output columns: url, warc_id, source_id, language, text.


```python
input_columns() -> list[str]
```


```python
output_columns() -> list[str]
```

