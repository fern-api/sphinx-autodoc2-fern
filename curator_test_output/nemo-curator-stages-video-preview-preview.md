---
layout: overview
slug: nemo-curator-stages-video-preview-preview
---

# nemo_curator.stages.video.preview.preview



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`PreviewStage`](#nemo_curatorstagesvideopreviewpreviewpreviewstage) | Stage that generates webp previews from video clips. |

### API

```python
class nemo_curator.stages.video.preview.preview.PreviewStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage that generates webp previews from video clips.

This class processes video clips through a series of steps including reading,
generating webp previews, and writing to storage.

```python
target_fps: float
```

**Value**: `1.0`


```python
target_height: int
```

**Value**: `240`


```python
verbose: bool
```

**Value**: `False`


```python
num_cpus_per_worker: float
```

**Value**: `4.0`


```python
compression_level: int
```

**Value**: `6`


```python
quality: int
```

**Value**: `50`


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
__post_init__() -> None
```


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
_generate_preview(window: nemo_curator.tasks.video._Window) -> None
```

Generate webp preview for a video window.

**Parameters:**

<ParamField path="window" type="nemo_curator.tasks.video._Window">
  Window containing video data to generate preview for.
</ParamField>

