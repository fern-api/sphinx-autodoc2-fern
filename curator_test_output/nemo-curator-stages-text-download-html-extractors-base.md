---
layout: overview
slug: nemo-curator-stages-text-download-html-extractors-base
---

# nemo_curator.stages.text.download.html_extractors.base



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`HTMLExtractorAlgorithm`](#nemo_curatorstagestextdownloadhtml_extractorsbasehtmlextractoralgorithm) | Helper class that provides a standard way to create an ABC using inheritance. |

### API

```python
class nemo_curator.stages.text.download.html_extractors.base.HTMLExtractorAlgorithm
```

**Bases**: `abc.ABC`

```python
NON_SPACED_LANGUAGES
```

**Value**: `frozenset(...)`


```python
extract_text(
    html: str,
    stop_words: frozenset[str],
    language: str
) -> list[str] | None
```

