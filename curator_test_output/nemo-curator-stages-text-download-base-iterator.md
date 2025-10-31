---
layout: overview
slug: nemo-curator-stages-text-download-base-iterator
---

# nemo_curator.stages.text.download.base.iterator



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`DocumentIterator`](#nemo_curatorstagestextdownloadbaseiteratordocumentiterator) | Abstract base class for document iterators. |
| [`DocumentIterateStage`](#nemo_curatorstagestextdownloadbaseiteratordocumentiteratestage) | Stage that iterates through downloaded files and extracts records. |

### API

```python
class nemo_curator.stages.text.download.base.iterator.DocumentIterator
```

**Bases**: `abc.ABC`

Abstract base class for document iterators.

Always yields dict[str, str] records. For raw content that needs extraction,
the iterator can put it in any field (e.g., "raw_content", "html", "content", etc.)

```python
iterate(file_path: str) -> collections.abc.Iterator[dict[str, typing.Any]]
```

Iterate over records in a file, yielding dict records.


```python
output_columns() -> list[str]
```

Define output columns - produces DocumentBatch with records.


```python
class nemo_curator.stages.text.download.base.iterator.DocumentIterateStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks.DocumentBatch]`

Stage that iterates through downloaded files and extracts records.

Takes local file paths and produces a DocumentBatch with records.
All iterators yield dict[str, str] records uniformly.

```python
iterator: nemo_curator.stages.text.download.base.iterator.DocumentIterator
```

**Value**: `None`


```python
record_limit: int | None
```

**Value**: `None`


```python
add_filename_column: bool | str
```

**Value**: `True`


```python
__post_init__()
```

Initialize the stage.


```python
inputs() -> tuple[list[str], list[str]]
```

Define input requirements - expects FileGroupTask with local file paths.


```python
outputs() -> tuple[list[str], list[str]]
```

Define output - produces DocumentBatch with records.


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.DocumentBatch
```

Iterate through files and extract records.

**Parameters:**

**Returns:**

DocumentBatch: Batch containing records

