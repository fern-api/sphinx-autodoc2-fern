---
layout: overview
slug: nemo-curator-stages-text-modules-score-filter
---

# nemo_curator.stages.text.modules.score_filter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Score`](#nemo_curatorstagestextmodulesscore_filterscore) | The module responsible for adding metadata to records based on statistics about the text. It accepts an arbitrary scoring function that accepts a text field and returns a score. It also accepts a DocumentFilter object, in which case the score_fn will be the score_document method of the DocumentFilter. |
| [`Filter`](#nemo_curatorstagestextmodulesscore_filterfilter) | The module responsible for filtering records based on a metadata field. It accepts an arbitrary filter function that accepts a metadata field and returns True if the field should be kept. It also accepts a DocumentFilter object, in which case the filter_fn will be the keep_document method of the DocumentFilter. Unlike ScoreFilter, it does not compute the metadata based on a document. It only filters using existing metadata. |
| [`ScoreFilter`](#nemo_curatorstagestextmodulesscore_filterscorefilter) | The module responsible for applying a filter (or chain of filters) to all documents in a dataset. It accepts an arbitrary DocumentFilter and first computes the score for a document. Then, determines whether to keep the document based on the criteria in the DocumentFilter. |

### Functions

| Name | Description |
|------|-------------|
| [`_filter_name`](#nemo_curatorstagestextmodulesscore_filter_filter_name) | None |
| [`_get_filter_stage_name`](#nemo_curatorstagestextmodulesscore_filter_get_filter_stage_name) | Derive the stage name from the provided score/filter functions. |
| [`_format_single_field_list`](#nemo_curatorstagestextmodulesscore_filter_format_single_field_list) | In the case of a single DocumentFilter or Callable, format the relevant field (filter_field, score_field, text_field, invert) to a list of length 1. |
| [`_format_field_list`](#nemo_curatorstagestextmodulesscore_filter_format_field_list) | In the case of a list of DocumentFilters or Callables, format the relevant field (filter_field, score_field, text_field, invert) to a list of length equal to the number of filters. |
| [`_validate_and_normalize_filters`](#nemo_curatorstagestextmodulesscore_filter_validate_and_normalize_filters) | Validate and normalize all parameters needed for the Score, Filter, and ScoreFilter modules. "Normalize" means to reformat all parameters to a list of length equal to the number of filters. |

### API

```python
class nemo_curator.stages.text.modules.score_filter.Score
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

The module responsible for adding metadata to records based on statistics about the text.
It accepts an arbitrary scoring function that accepts a text field and returns a score.
It also accepts a DocumentFilter object, in which case the score_fn will be the score_document method of the DocumentFilter.

Unlike ScoreFilter, it does not filter based on the computed score.
It only adds metadata to the record.

If a list of DocumentFilters is provided, the filters are applied in order.
In this case, the score_field parameter should be a list of strings corresponding to the filters.
If different filters should be applied to different text fields, then text_field should be a list of strings corresponding to the filters.

**Parameters:**

- **score_fn (Callable | DocumentFilter | list[DocumentFilter])**: The score function or the DocumentFilter object (or list of DocumentFilters). If it is a DocumentFilter object, the score_fn will be the score_document method of the DocumentFilter.
- **score_field (str | list[str])**: The field (or list of fields) the score will be stored in.
- **text_field (str | list[str])**: The field (or list of fields) the documents will be read from.

```python
score_fn: collections.abc.Callable[[str], float | str] | nemo_curator.stages.text.filters.doc_filter.DocumentFilter | list[nemo_curator.stages.text.filters.doc_filter.DocumentFilter]
```

**Value**: `None`


```python
score_field: str | list[str]
```

**Value**: `None`


```python
text_field: str | list[str]
```

**Value**: `text`


```python
_name: str
```

**Value**: `score_fn`


```python
__post_init__()
```


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
ray_stage_spec() -> dict[str, typing.Any]
```


```python
setup_on_node(
    _node_info: nemo_curator.backends.base.NodeInfo | None = None,
    _worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None
) -> None
```


```python
setup(_: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
process(batch: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.DocumentBatch | None
```

Applies the scoring to a dataset

**Parameters:**

**Returns:**

DocumentBatch: A batch with the new score


```python
class nemo_curator.stages.text.modules.score_filter.Filter
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

The module responsible for filtering records based on a metadata field.
It accepts an arbitrary filter function that accepts a metadata field and returns True if the field should be kept.
It also accepts a DocumentFilter object, in which case the filter_fn will be the keep_document method of the DocumentFilter.
Unlike ScoreFilter, it does not compute the metadata based on a document.
It only filters using existing metadata.

If a list of DocumentFilters is provided, the filters are applied in order.
In this case, the filter_field parameter should be a list of strings corresponding to the filters.
If some filters should be inverted and others not, then invert should be a list of booleans corresponding to the filters.

**Parameters:**

- **filter_fn (Callable | DocumentFilter | list[DocumentFilter])**: A function (or list of functions) that returns True if the document is to be kept or a DocumentFilter object,
  in which case the filter_fn will be the keep_document method of the DocumentFilter.
- **filter_field (str | list[str])**: The field (or list of fields) to be passed into the filter function.
- **invert (bool | list[bool])**: Whether to invert the filter condition.

```python
filter_fn: collections.abc.Callable | nemo_curator.stages.text.filters.doc_filter.DocumentFilter | list[nemo_curator.stages.text.filters.doc_filter.DocumentFilter]
```

**Value**: `None`


```python
filter_field: str | list[str]
```

**Value**: `None`


```python
invert: bool | list[bool]
```

**Value**: `False`


```python
_name: str
```

**Value**: `filter_fn`


```python
__post_init__()
```


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
compute_filter_mask(
    df: pandas.DataFrame,
    filter_fn: collections.abc.Callable | nemo_curator.stages.text.filters.doc_filter.DocumentFilter,
    filter_field: str,
    invert: bool
) -> pandas.Series
```

Compute the bool mask to filter the dataset.

**Parameters:**

**Returns:**

Series: A mask corresponding to each data instance indicating whether it will be retained.


```python
process(batch: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.DocumentBatch | None
```

Applies the filtering to a dataset

**Parameters:**

**Returns:**

DocumentBatch: A batch with entries removed according to the filter


```python
class nemo_curator.stages.text.modules.score_filter.ScoreFilter
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

The module responsible for applying a filter (or chain of filters) to all documents in a dataset.
It accepts an arbitrary DocumentFilter and first computes the score for a document.
Then, determines whether to keep the document based on the criteria in the DocumentFilter.

The filter can be applied to any field in the dataset, and the score can be logged for later.
Also, the filter can be inverted such that "rejected" documents are kept.

If a list of DocumentFilters is provided, the filters are applied in order.
If different filters should be applied to different text fields, then text_field should be a list of strings corresponding to the filters.
If different score fields should be created for each filter, then score_field should be a list of strings corresponding to the filters.
If some filters should be inverted and others not, then invert should be a list of booleans corresponding to the filters.

**Parameters:**

- **filter_obj (DocumentFilter | list[DocumentFilter])**: The score function (or list of score functions) that takes in a document string and outputs a score for the document.
- **text_field (str | list[str])**: The field (or list of fields) the documents will be read from.
- **score_field (str | list[str] | None)**: The field (or list of fields) to which the scores will be written. If None, scores will be immediately discarded after use.
- **invert (bool | list[bool])**: If True, will keep all documents that are normally discarded.

```python
filter_obj: nemo_curator.stages.text.filters.doc_filter.DocumentFilter | list[nemo_curator.stages.text.filters.doc_filter.DocumentFilter]
```

**Value**: `None`


```python
text_field: str | list[str]
```

**Value**: `text`


```python
score_field: str | list[str] | None
```

**Value**: `None`


```python
invert: bool | list[bool]
```

**Value**: `False`


```python
_name: str
```

**Value**: `score_filter`


```python
__post_init__()
```


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
ray_stage_spec() -> dict[str, typing.Any]
```


```python
setup_on_node(
    _node_info: nemo_curator.backends.base.NodeInfo | None = None,
    _worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None
) -> None
```


```python
setup(_: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
compute_filter_mask(
    df: pandas.DataFrame,
    filter_obj: nemo_curator.stages.text.filters.doc_filter.DocumentFilter,
    text_field: str,
    score_field: str | None,
    invert: bool
) -> pandas.Series
```

Compute the bool mask to filter the dataset.

**Parameters:**

**Returns:**

Series: A mask corresponding to each data instance indicating whether it will be retained.


```python
process(batch: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.DocumentBatch | None
```

Scores and filters all records in the dataset

**Parameters:**

**Returns:**

DocumentBatch: A batch with the score and filter applied


```python
nemo_curator.stages.text.modules.score_filter._filter_name(x: nemo_curator.stages.text.filters.doc_filter.DocumentFilter | collections.abc.Callable) -> str
```


```python
nemo_curator.stages.text.modules.score_filter._get_filter_stage_name(
    filters: list[nemo_curator.stages.text.filters.doc_filter.DocumentFilter | collections.abc.Callable],
    prefix: str
) -> str
```

Derive the stage name from the provided score/filter functions.


```python
nemo_curator.stages.text.modules.score_filter._format_single_field_list(
    _field: str | list[str] | None,
    field_name: str,
    field_type: type = str
) -> list[str] | list[bool]
```

In the case of a single DocumentFilter or Callable, format the relevant field
(filter_field, score_field, text_field, invert) to a list of length 1.

**Parameters:**

**Returns:**

list[str] | list[bool]: The reformatted field.


```python
nemo_curator.stages.text.modules.score_filter._format_field_list(
    _field: str | list[str] | None,
    filter_count: int,
    field_name: str,
    field_type: type = str
) -> list[str] | list[bool]
```

In the case of a list of DocumentFilters or Callables, format the relevant field
(filter_field, score_field, text_field, invert) to a list of length equal to the number of filters.

**Parameters:**

**Returns:**

list[str] | list[bool]: The reformatted field.


```python
nemo_curator.stages.text.modules.score_filter._validate_and_normalize_filters(
    _filter: nemo_curator.stages.text.filters.doc_filter.DocumentFilter | collections.abc.Callable | list[nemo_curator.stages.text.filters.doc_filter.DocumentFilter | collections.abc.Callable],
    input_field: str | list[str] | None,
    invert: bool | list[bool] | None,
    output_field: str | list[str] | None,
    fn_type: typing.Literal[score, filter, score_filter]
) -> tuple[str, list[nemo_curator.stages.text.filters.doc_filter.DocumentFilter | collections.abc.Callable], list[str] | None, list[bool] | None, list[str] | None]
```

Validate and normalize all parameters needed for the Score, Filter, and ScoreFilter modules.
"Normalize" means to reformat all parameters to a list of length equal to the number of filters.

**Parameters:**

**Returns:**

tuple[str, list[DocumentFilter | Callable], list[str] | None, list[bool] | None, list[str] | None]:
The first string returned corresponds to the name given to the DocumentFilter or Callable.
The normalized filters, input fields, invert flags, and output fields make up the rest of the tuple.

