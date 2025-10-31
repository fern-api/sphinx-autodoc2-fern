---
layout: overview
slug: nemo-curator-stages-video-clipping-clip-frame-extraction
---

# nemo_curator.stages.video.clipping.clip_frame_extraction



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ClipFrameExtractionStage`](#nemo_curatorstagesvideoclippingclip_frame_extractionclipframeextractionstage) | Stage for extracting frames from video clips. |

### API

```python
class nemo_curator.stages.video.clipping.clip_frame_extraction.ClipFrameExtractionStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage for extracting frames from video clips.

This class processes video clips through a series of steps including frame extraction,
target frame rate selection, and frame extraction signature creation.

```python
extraction_policies: tuple[nemo_curator.utils.decoder_utils.FrameExtractionPolicy, ...]
```

**Value**: `()`


```python
extract_purposes: list[nemo_curator.utils.decoder_utils.FramePurpose] | None
```

**Value**: `None`


```python
target_res: tuple[int, int] | None
```

**Value**: `None`


```python
verbose: bool
```

**Value**: `False`


```python
num_cpus: int
```

**Value**: `3`


```python
target_fps: list[float | int] | None
```

**Value**: `None`


```python
_name: str
```

**Value**: `clip_frame_extraction`


```python
__post_init__() -> None
```


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
setup(worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
lcm_multiple(fps: list[float | int]) -> float | int
```

Compute LCM of a list of fps targets.


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```

