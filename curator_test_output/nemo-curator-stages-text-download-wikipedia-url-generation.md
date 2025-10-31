---
layout: overview
slug: nemo-curator-stages-text-download-wikipedia-url-generation
---

# nemo_curator.stages.text.download.wikipedia.url_generation



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`WikipediaUrlGenerator`](#nemo_curatorstagestextdownloadwikipediaurl_generationwikipediaurlgenerator) | Generates URLs for Wikipedia dump files. |

### Data

`REQUEST_TIMEOUT`

### API

```python
nemo_curator.stages.text.download.wikipedia.url_generation.REQUEST_TIMEOUT
```

**Value**: `30`


```python
class nemo_curator.stages.text.download.wikipedia.url_generation.WikipediaUrlGenerator
```

**Bases**: `nemo_curator.stages.text.download.URLGenerator`

Generates URLs for Wikipedia dump files.

```python
language: str
```

**Value**: `en`


```python
dump_date: str | None
```

**Value**: `None`


```python
wikidumps_index_prefix: str
```

**Value**: `https://dumps.wikimedia.org`


```python
generate_urls() -> list[str]
```

Generate Wikipedia dump URLs.

**Returns:**

List of URLs pointing to Wikipedia dump files


```python
_get_data_for_dump(
    dump_date: str, wiki_index_url: str
) -> dict | None
```

Get the JSON dump data for a given dump date. Returns None if the dump is not found.


```python
_get_wikipedia_urls() -> list[str]
```

Retrieves all URLs pointing to Wikipedia dumps for the specified language and date.

**Returns:**

List of URLs for Wikipedia dump files

