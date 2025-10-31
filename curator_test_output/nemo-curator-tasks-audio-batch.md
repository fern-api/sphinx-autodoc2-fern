---
layout: overview
slug: nemo-curator-tasks-audio-batch
---

# nemo_curator.tasks.audio_batch



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`AudioBatch`](#nemo_curatortasksaudio_batchaudiobatch) | A single data dict with filepath check. |

### API

```python
class nemo_curator.tasks.audio_batch.AudioBatch(data: dict | list[dict] | None = None, filepath_key: str | None = None, task_id: str = '', dataset_name: str = '', **kwargs)
```

**Bases**: `nemo_curator.tasks.tasks.Task[dict]`

A single data dict with filepath check.

```python
num_items: int
```


```python
validate_item(item: dict) -> bool
```


```python
validate() -> bool
```

Validate the task data.

