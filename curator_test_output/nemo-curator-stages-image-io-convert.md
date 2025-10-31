---
layout: overview
slug: nemo-curator-stages-image-io-convert
---

# nemo_curator.stages.image.io.convert



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ConvertImageBatchToDocumentBatchStage`](#nemo_curatorstagesimageioconvertconvertimagebatchtodocumentbatchstage) | Convert image batch to DocumentBatch |

### API

```python
class nemo_curator.stages.image.io.convert.ConvertImageBatchToDocumentBatchStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.ImageBatch, nemo_curator.tasks.DocumentBatch]`

Convert image batch to DocumentBatch

**Parameters:**

- **fields**: list of fields of ImageObject to convert to DocumentBatch

```python
fields: list[str]
```

**Value**: `field(...)`


```python
_name: str
```

**Value**: `convert_image_batch_to_document_batch`


```python
process(task: nemo_curator.tasks.ImageBatch) -> nemo_curator.tasks.DocumentBatch
```

Convert image batch to DocumentBatch

