---
layout: overview
slug: nemo-curator-tasks-document
---

# nemo_curator.tasks.document



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`DocumentBatch`](#nemo_curatortasksdocumentdocumentbatch) | Task for processing batches of text documents. Documents are stored as a dataframe (PyArrow Table or Pandas DataFrame). |

### API

```python
class nemo_curator.tasks.document.DocumentBatch
```

**Bases**: `nemo_curator.tasks.tasks.Task[pyarrow.Table | pandas.DataFrame]`

Task for processing batches of text documents.
Documents are stored as a dataframe (PyArrow Table or Pandas DataFrame).

```python
data: pyarrow.Table | pandas.DataFrame
```

**Value**: `field(...)`


```python
to_pyarrow() -> pyarrow.Table
```

Convert data to PyArrow table.


```python
to_pandas() -> pandas.DataFrame
```

Convert data to Pandas DataFrame.


```python
num_items: int
```

Get the number of documents in this batch.


```python
get_columns() -> list[str]
```

Get column names from the data.


```python
validate() -> bool
```

Validate the task data.

