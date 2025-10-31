---
layout: overview
slug: nemo-curator-stages-text-download-wikipedia-iterator
---

# nemo_curator.stages.text.download.wikipedia.iterator



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`WikipediaIterator`](#nemo_curatorstagestextdownloadwikipediaiteratorwikipediaiterator) | Processes downloaded Wikipedia dump files and extracts article content. |

### API

```python
class nemo_curator.stages.text.download.wikipedia.iterator.WikipediaIterator(language: str = 'en', log_frequency: int = 1000)
```

**Bases**: `nemo_curator.stages.text.download.DocumentIterator`

Processes downloaded Wikipedia dump files and extracts article content.

### Initialization

Initialize the Wikipedia iterator.

**Parameters:**

- **language**: Language code for the Wikipedia dump
- **log_frequency**: How often to log progress (every N articles)


```python
_should_log_progress(_: str) -> bool
```

Check if progress should be logged based on counter.


```python
_extract_element_text(
    elem: xml.etree.ElementTree.Element,
    namespace: str,
    tag: str
) -> str | None
```

Extract text from an XML element.


```python
_get_article_metadata(
    elem: xml.etree.ElementTree.Element, namespace: str
) -> dict[str, typing.Any] | None
```

Extract metadata from a Wikipedia article element.


```python
_get_article_content(
    elem: xml.etree.ElementTree.Element, namespace: str
) -> str | None
```

Extract raw content from Wikipedia article element.


```python
_should_skip_article(
    metadata: dict[str, typing.Any], raw_content: str | None
) -> bool
```

Check if article should be skipped based on metadata and content.


```python
iterate(file_path: str) -> collections.abc.Iterator[dict[str, typing.Any]]
```

Process a Wikipedia dump file and extract article content.

**Parameters:**

<ParamField path="file_path" type="str">
  Path to the downloaded .bz2 file
</ParamField>

**Returns:**

Dict containing article metadata and raw content


```python
output_columns() -> list[str]
```

Define the output columns produced by this iterator.

