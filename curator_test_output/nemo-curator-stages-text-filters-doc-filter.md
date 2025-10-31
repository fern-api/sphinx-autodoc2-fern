---
layout: overview
slug: nemo-curator-stages-text-filters-doc-filter
---

# nemo_curator.stages.text.filters.doc_filter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`DocumentFilter`](#nemo_curatorstagestextfiltersdoc_filterdocumentfilter) | An abstract base class for text-based document filters. |

### API

```python
class nemo_curator.stages.text.filters.doc_filter.DocumentFilter
```

**Bases**: `abc.ABC`

An abstract base class for text-based document filters.

This class serves as a template for creating specific document filters
in the library. Subclasses should implement the abstract methods to
define custom filtering behavior.

```python
score_document(text: str) -> float | list[int | float]
```

Calculate a score for the given document text.

This method should be implemented by subclasses to define how
a document's text is evaluated and scored.

**Parameters:**

**Returns:**

Any: A score or set of scores representing the document's
relevance or quality. The type and structure of the
return value should be consistent for each subclass.

**Raises:**

NotImplementedError: If the method is not implemented in a subclass.


```python
keep_document(scores: float | list[int | float]) -> bool
```

Determine whether to keep a document based on its scores.

This method should be implemented by subclasses to define the
criteria for keeping or discarding a document based on the
scores calculated by score_document().

**Parameters:**

**Returns:**

bool: True if the document should be kept, False otherwise.

**Raises:**

NotImplementedError: If the method is not implemented in a subclass.


```python
name: str
```


```python
sentences: list
```


```python
paragraphs: list
```


```python
ngrams: dict
```

