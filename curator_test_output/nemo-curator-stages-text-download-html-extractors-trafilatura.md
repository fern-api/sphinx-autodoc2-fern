---
layout: overview
slug: nemo-curator-stages-text-download-html-extractors-trafilatura
---

# nemo_curator.stages.text.download.html_extractors.trafilatura



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`TrafilaturaExtractor`](#nemo_curatorstagestextdownloadhtml_extractorstrafilaturatrafilaturaextractor) | None |

### API

```python
class nemo_curator.stages.text.download.html_extractors.trafilatura.TrafilaturaExtractor(required_stopword_density: float = 0.32, min_extracted_size: int = 250, min_extracted_comm_size: int = 1, min_output_size: int = 1, min_output_comm_size: int = 1, max_tree_size: int | None = None, min_duplcheck_size: int = 100, max_repetitions: int = 2, **extract_kwargs)
```

**Bases**: `nemo_curator.stages.text.download.html_extractors.base.HTMLExtractorAlgorithm`

### Initialization

Initialize the Trafilatura text extraction algorithm with specified parameters.

The Trafilatura extraction process combines readability-lxml and jusText as fallbacks to ensure robustness.
Trafilatura's own algorithm follows a cascade of rule-based filters and content heuristics:
    • Content Delimitation: Uses XPath expressions to exclude unwanted HTML elements (e.g., navigation bars) and focus on relevant content (e.g., article body).
        Extracted HTML nodes are analyzed for relevance based on element type, text length, and link density.
    • Fallback Mechanism: If extraction seems faulty, alternative algorithms are run as backups.
        These use heuristics like line length, text-to-markup ratio, and HTML depth to improve extraction.
        Outputs are compared, prioritizing longer extractions with fewer impurities.
    • Baseline Extraction: If all else fails, it searches for text elements that might have been missed, discarding irrelevant content.

The system balances precision and recall, extracting main text, comments, and metadata (title, site name, author, date, categories, tags).

Please refer to the Trafilatura documentation for more details:
    https://trafilatura.readthedocs.io/en/latest/ and https://aclanthology.org/2021.acl-demo.15/

NeMo Curator has added a stopword density filter to the Trafilatura extraction process, which requires that a paragraph contains a certain proportion of stopwords.

**Parameters:**

- **required_stopword_density**: Proportion of stopwords required preserve an extracted paragraph.
  Studies on stopword lists and their distribution in various text corpora often
  suggest that around 30-40% of a typical English text consists of stopwords.
- **min_extracted_size**: Acceptable size in characters (used to trigger fallbacks).
- **Defaults to 250. See Trafilatura documentation**: https://trafilatura.readthedocs.io/en/latest/settings.html.
- **min_extracted_comm_size**: Works the same as min_output_comm_size for comment extraction.
- **Defaults to 1. See Trafilatura documentation**: https://trafilatura.readthedocs.io/en/latest/settings.html.
- **min_output_size**: Absolute acceptable minimum for main text output.
- **Defaults to 1. See Trafilatura documentation**: https://trafilatura.readthedocs.io/en/latest/settings.html.
- **min_output_comm_size**: Works the same as min_output_comm_size for comment extraction.
- **Defaults to 1. See Trafilatura documentation**: https://trafilatura.readthedocs.io/en/latest/settings.html.
- **max_tree_size**: Used to discard documents with too many elements. Defaults to None.
- **min_duplcheck_size**: Minimum size in characters to run deduplication on.
- **Defaults to 100. See Trafilatura documentation**: https://trafilatura.readthedocs.io/en/latest/settings.html.
- **max_repetitions**: Maximum number of duplicates allowed.
- **Defaults to 2. See Trafilatura documentation**: https://trafilatura.readthedocs.io/en/latest/settings.html.
- **extract_kwargs**: Additional keyword arguments for the Trafilatura extract function.
- **See API documentation https**: //trafilatura.readthedocs.io/en/latest/corefunctions.html#extract
  for list of possible parameters.
  All arguments are set to their default values, except for deduplicate (bool) which is set to True.


```python
extract_text(
    html: str,
    stop_words: frozenset[str],
    language: str
) -> list[str] | None
```

