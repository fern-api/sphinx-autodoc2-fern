---
layout: overview
slug: nemo-curator-stages-text-filters-code
---

# nemo_curator.stages.text.filters.code



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`PythonCommentToCodeFilter`](#nemo_curatorstagestextfilterscodepythoncommenttocodefilter) | None |
| [`GeneralCommentToCodeFilter`](#nemo_curatorstagestextfilterscodegeneralcommenttocodefilter) | None |
| [`NumberOfLinesOfCodeFilter`](#nemo_curatorstagestextfilterscodenumberoflinesofcodefilter) | None |
| [`TokenizerFertilityFilter`](#nemo_curatorstagestextfilterscodetokenizerfertilityfilter) | None |
| [`XMLHeaderFilter`](#nemo_curatorstagestextfilterscodexmlheaderfilter) | This filter tries to identify files that have incorrect file extensions. In many cases, these end up being XML files and we try to identify them based on the header. (Source: Starcoder https://arxiv.org/abs/2305.06161) |
| [`AlphaFilter`](#nemo_curatorstagestextfilterscodealphafilter) | This filter tries to identify files that have large tensors, or tables stored as raw text within code files. (Source: Starcoder https://arxiv.org/abs/2305.06161) |
| [`HTMLBoilerplateFilter`](#nemo_curatorstagestextfilterscodehtmlboilerplatefilter) | This filter tries to identify HTML that is largely boilerplate. |
| [`PerExtensionFilter`](#nemo_curatorstagestextfilterscodeperextensionfilter) | This filter that has specific conditions depending on the file extension. |

### API

```python
class nemo_curator.stages.text.filters.code.PythonCommentToCodeFilter(min_comment_to_code_ratio: float = 0.01, max_comment_to_code_ratio: float = 0.85)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

```python
score_document(source: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.code.GeneralCommentToCodeFilter(language: str, min_comment_to_code_ratio: float = 0.01, max_comment_to_code_ratio: float = 0.85)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

### Initialization

Does not include the comment characters (// or /**/) towards the length of the comment.

**Parameters:**

- **language**: Mime string of language


```python
score_document(source: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.code.NumberOfLinesOfCodeFilter(min_lines: int = 10, max_lines: int = 20000)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

```python
score_document(source: str) -> int
```


```python
keep_document(score: int) -> bool
```


```python
class nemo_curator.stages.text.filters.code.TokenizerFertilityFilter(path_to_tokenizer: str | None = None, min_char_to_token_ratio: float = 2.5)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

```python
score_document(source: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.code.XMLHeaderFilter(char_prefix_search_length: int = 100)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

This filter tries to identify files that have incorrect file extensions.
In many cases, these end up being XML files and we try to identify them
based on the header.
(Source: Starcoder https://arxiv.org/abs/2305.06161)

```python
score_document(source: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.code.AlphaFilter(min_alpha_ratio: float = 0.25)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

This filter tries to identify files that have large tensors, or tables stored
as raw text within code files.
(Source: Starcoder https://arxiv.org/abs/2305.06161)

```python
score_document(source: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.code.HTMLBoilerplateFilter(min_lang_content_ratio: float = 0.2, min_lang_content_num_chars: int = 100)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

This filter tries to identify HTML that is largely boilerplate.

```python
score_document(source: str) -> float | None
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.code.PerExtensionFilter(lang: str, extension: str, metadata_file: str = 'code_meta.csv')
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

This filter that has specific conditions depending on the file extension.

```python
_load_filter_csv(
    path: str, language: str | None = None
) -> dict
```

Load csv file that specifies the filter to apply for each (lang, extension).


```python
_get_filter_params(row: dict) -> tuple[bool, int | None, float | None, float | None, float | None]
```

Extract filter parameters from csv row


```python
_language_format_from_dataset(lang: str) -> str
```

Convert: Language field in dataset -> language field in csv file that defines the filters.


```python
_line_statistics(source: str) -> tuple[int, float]
```


```python
_alphanum_fraction(source: str) -> float
```


```python
score_document(source: str) -> float
```

Filter files based on line length and % alphanumeric characters.
The filtering parameters depend on the file extension, given by `ext_to_filter`


```python
keep_document(score: float | None) -> bool
```

