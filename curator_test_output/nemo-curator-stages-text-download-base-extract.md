---
layout: overview
slug: nemo-curator-stages-text-download-base-extract
---

# nemo_curator.stages.text.download.base.extract



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`DocumentExtractor`](#nemo_curatorstagestextdownloadbaseextractdocumentextractor) | Abstract base class for document extractors. |
| [`DocumentExtractStage`](#nemo_curatorstagestextdownloadbaseextractdocumentextractstage) | Stage that extracts structured content from raw records. |

### API

```python
class nemo_curator.stages.text.download.base.extract.DocumentExtractor
```

**Bases**: `abc.ABC`

Abstract base class for document extractors.

Takes a record dict and returns processed record dict or None to skip.
Can transform any fields in the input dict.

```python
extract(record: dict[str, str]) -> dict[str, typing.Any] | None
```

Extract/transform a record dict into final record dict.


```python
input_columns() -> list[str]
```

Define input columns - produces DocumentBatch with records.


```python
output_columns() -> list[str]
```

Define output columns - produces DocumentBatch with records.


```python
class nemo_curator.stages.text.download.base.extract.DocumentExtractStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

Stage that extracts structured content from raw records.

Takes DocumentBatch with raw content and produces DocumentBatch with extracted content.
This is for cases where iteration and extraction are separate steps.

```python
extractor: nemo_curator.stages.text.download.base.extract.DocumentExtractor
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

Define input requirements - expects DocumentBatch with dict records.


```python
outputs() -> tuple[list[str], list[str]]
```

Define output - produces DocumentBatch with processed records.


```python
process(task: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.DocumentBatch
```

Extract structured content from raw records.

**Parameters:**

**Returns:**

DocumentBatch: Batch containing extracted records

