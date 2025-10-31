---
layout: overview
slug: nemo-curator-stages-text-download-common-crawl-url-generation
---

# nemo_curator.stages.text.download.common_crawl.url_generation



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`BaseCommonCrawlUrlGenerator`](#nemo_curatorstagestextdownloadcommon_crawlurl_generationbasecommoncrawlurlgenerator) | Get URLs for Common Crawl data Each concrete implementation must implement `_parse_datetime_from_snapshot_string` and `generate_path_urls` |
| [`MainCommonCrawlUrlGenerator`](#nemo_curatorstagestextdownloadcommon_crawlurl_generationmaincommoncrawlurlgenerator) | Get URLs for Common Crawl data Each concrete implementation must implement `_parse_datetime_from_snapshot_string` and `generate_path_urls` |
| [`NewsCommonCrawlUrlGenerator`](#nemo_curatorstagestextdownloadcommon_crawlurl_generationnewscommoncrawlurlgenerator) | Get URLs for Common Crawl data Each concrete implementation must implement `_parse_datetime_from_snapshot_string` and `generate_path_urls` |

### API

```python
class nemo_curator.stages.text.download.common_crawl.url_generation.BaseCommonCrawlUrlGenerator
```

**Bases**: `nemo_curator.stages.text.download.URLGenerator`, `abc.ABC`

Get URLs for Common Crawl data
Each concrete implementation must implement `_parse_datetime_from_snapshot_string` and `generate_path_urls`

```python
start_snapshot_str: str
```

**Value**: `None`


```python
end_snapshot_str: str
```

**Value**: `None`


```python
data_prefix: str
```

**Value**: `https://data.commoncrawl.org`


```python
limit: int | None
```

**Value**: `None`


```python
_parse_datetime_from_snapshot_string(
    snapshot_str: str, for_start: bool
) -> datetime.datetime
```

Parses a snapshot string (YYYY-WW or YYYY-MM) into a datetime object.


```python
generate_path_urls() -> list[str]
```

Generates the list of URLs pointing to warc.paths.gz files.


```python
__post_init__()
```


```python
_start_end_dates() -> tuple[datetime.date, datetime.date]
```

Parses the start and end snapshot strings into date objects.
For 'news' (YYYY-MM), the day is set to 1 for start_date, and the last day of the month for end_date
to ensure the full month is covered.


```python
generate_data_urls(path_urls: str | list[str] | None = None) -> list[str]
```

Fetches all relevant warc.paths.gz files, decompresses them,
and returns a list of all individual WARC file URLs.


```python
generate_urls() -> list[str]
```

Process the task and return a list of WARC URLs


```python
class nemo_curator.stages.text.download.common_crawl.url_generation.MainCommonCrawlUrlGenerator
```

**Bases**: `nemo_curator.stages.text.download.common_crawl.url_generation.BaseCommonCrawlUrlGenerator`

```python
index_prefix: str
```

**Value**: `https://index.commoncrawl.org`


```python
_parse_datetime_from_snapshot_string(
    snapshot_str: str, for_start: bool
) -> datetime.datetime
```


```python
_snapshot_index() -> list[dict]
```


```python
generate_path_urls() -> list[str]
```


```python
class nemo_curator.stages.text.download.common_crawl.url_generation.NewsCommonCrawlUrlGenerator
```

**Bases**: `nemo_curator.stages.text.download.common_crawl.url_generation.BaseCommonCrawlUrlGenerator`

```python
_parse_datetime_from_snapshot_string(
    snapshot_str: str, for_start: bool
) -> datetime.datetime
```


```python
generate_path_urls() -> list[str]
```

