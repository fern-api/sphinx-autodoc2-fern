---
layout: overview
slug: nemo-curator-stages-text-download-html-extractors-justext
---

# nemo_curator.stages.text.download.html_extractors.justext



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`JusTextExtractor`](#nemo_curatorstagestextdownloadhtml_extractorsjustextjustextextractor) | None |

### API

```python
class nemo_curator.stages.text.download.html_extractors.justext.JusTextExtractor(length_low: int = 70, length_high: int = 200, stopwords_low: float = 0.3, stopwords_high: float = 0.32, max_link_density: float = 0.2, max_heading_distance: int = 200, no_headings: bool = False, is_boilerplate: bool | None = None)
```

**Bases**: `nemo_curator.stages.text.download.html_extractors.base.HTMLExtractorAlgorithm`

### Initialization

Initialize the jusText text extraction algorithm with specified parameters.

jusText is a tool for removing boilerplate content, such as navigation links, headers, and footers from HTML pages.
It is designed to preserve mainly text containing full sentences and it is therefore well suited for creating linguistic resources such as Web corpora.
The key idea is that long blocks can often be classified with high confidence, while shorter blocks require context-based adjustments.

Here is an overview of the jusText algorithm:
    • Segmentation: The document is split into textual blocks based on HTML tags that typically define separate sections (e.g., `<div>`, `<p>`, `<table>`).
    • Preprocessing: Contents of `<header>`, `<style>`, and `<script>` tags are removed.
        Certain elements (e.g., `<select>`, copyright symbols) are immediately classified as boilerplate.
    • Context-Free Classification: Each block is classified as:
        - Bad (boilerplate) if it has high link density.
        - Short if it is too small to be classified reliably.
        - Near-Good if it has a moderate density of stopwords.
        - Good (main content) if it is long and contains many stopwords.
    • Context-Sensitive Classification: Blocks that were classified as short or near-good are reclassified based on surrounding blocks.
        The assumption is that main content clusters together, as does boilerplate.
    • Headings Processing: Header elements (e.g., `<h1>`, `<h2>`) are treated separately to ensure useful headings are preserved.
        Short headers near good content may be reclassified as near-good or good.

Please refer to the jusText documentation for more details: https://corpus.tools/wiki/Justext/Algorithm

**Parameters:**

- **length_low**: Minimum length of text to be considered for extraction.
- **length_high**: Maximum length of text to be considered for extraction.
- **stopwords_low**: Minimum proportion of stopwords in the text to be considered for extraction.
- **stopwords_high**: Maximum proportion of stopwords in the text to be considered for extraction.
- **max_link_density**: Maximum allowed link density in the text.
- **max_heading_distance**: Maximum distance from a heading to consider text for extraction.
- **no_headings**: If True, text extraction will ignore headings.
- **is_boilerplate**: If True, text extraction will ignore boilerplate content.
  Default is True for space-separated languages and False for non-space-separated languages
  (Thai, Chinese, Japanese, and Korean).
- **logger**: Optional logger instance for logging messages.


```python
_logged_languages: typing.ClassVar[set[str]]
```

**Value**: `set(...)`


```python
extract_text(
    html: str,
    stop_words: frozenset[str],
    language: str
) -> list[str] | None
```

