---
layout: overview
slug: nemo-curator-stages-text-download-wikipedia-extract
---

# nemo_curator.stages.text.download.wikipedia.extract



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`WikipediaExtractor`](#nemo_curatorstagestextdownloadwikipediaextractwikipediaextractor) | Extractor for Wikipedia articles from MediaWiki XML dumps. |

### Data

`MEDIA_ALIASES`
`CAT_ALIASES`

### API

```python
nemo_curator.stages.text.download.wikipedia.extract.MEDIA_ALIASES
```

**Value**: `None`


```python
nemo_curator.stages.text.download.wikipedia.extract.CAT_ALIASES
```

**Value**: `None`


```python
class nemo_curator.stages.text.download.wikipedia.extract.WikipediaExtractor(language: str = 'en')
```

**Bases**: `nemo_curator.stages.text.download.DocumentExtractor`

Extractor for Wikipedia articles from MediaWiki XML dumps.

### Initialization

Initialize the Wikipedia extractor.

**Parameters:**

- **language**: Language code for the Wikipedia articles


```python
_create_filters() -> tuple[re.Pattern[str], re.Pattern[str], re.Pattern[str]]
```

Create regex patterns for filtering Wikipedia content.


```python
_create_filter_functions(
    re_rm_wikilink: re.Pattern[str], re_clean_wikilink: re.Pattern[str]
) -> tuple
```

Create filter functions for Wikipedia content processing.


```python
_process_sections(
    wikicode: typing.Any,
    re_rm_magic: re.Pattern[str],
    rm_wikilink: typing.Any,
    rm_tag: typing.Any,
    is_category: typing.Any,
    try_replace_obj: typing.Any,
    try_remove_obj: typing.Any
) -> str
```

Process sections of the Wikipedia article.


```python
extract(record: dict[str, typing.Any]) -> dict[str, typing.Any] | None
```

Extract and clean Wikipedia article content.

**Parameters:**

<ParamField path="record" type="dict[str, typing.Any]">
  Record containing raw_content field with Wikipedia markup
</ParamField>

**Returns:**

Dict with cleaned text and metadata, or None if extraction fails


```python
input_columns() -> list[str]
```

Define the input columns expected by this extractor.


```python
output_columns() -> list[str]
```

Define the output columns produced by this extractor.

