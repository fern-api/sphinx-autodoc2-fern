---
layout: overview
slug: nemo-curator-stages-audio-io-convert
---

# nemo_curator.stages.audio.io.convert



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`AudioToDocumentStage`](#nemo_curatorstagesaudioioconvertaudiotodocumentstage) | Stage to conver DocumentObject to DocumentBatch |

### API

```python
class nemo_curator.stages.audio.io.convert.AudioToDocumentStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.AudioBatch, nemo_curator.tasks.DocumentBatch]`

Stage to conver DocumentObject to DocumentBatch

```python
process(task: nemo_curator.tasks.AudioBatch) -> list[nemo_curator.tasks.DocumentBatch]
```

