---
layout: overview
slug: nemo-curator-stages-text-filters-fasttext-filter
---

# nemo_curator.stages.text.filters.fasttext_filter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`FastTextQualityFilter`](#nemo_curatorstagestextfiltersfasttext_filterfasttextqualityfilter) | None |
| [`FastTextLangId`](#nemo_curatorstagestextfiltersfasttext_filterfasttextlangid) | None |

### API

```python
class nemo_curator.stages.text.filters.fasttext_filter.FastTextQualityFilter(model_path: str | None = None, label: str = '__label__hq', alpha: float = 3, seed: int = 42)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

```python
model_check_or_download() -> None
```


```python
load_model() -> None
```


```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.fasttext_filter.FastTextLangId(model_path: str | None = None, min_langid_score: float = 0.3)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

```python
model_check_or_download() -> None
```


```python
load_model() -> None
```


```python
score_document(text: str) -> list[float | str]
```


```python
keep_document(score: float | str) -> bool
```

