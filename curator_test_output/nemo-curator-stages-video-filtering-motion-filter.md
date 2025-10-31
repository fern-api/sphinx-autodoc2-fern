---
layout: overview
slug: nemo-curator-stages-video-filtering-motion-filter
---

# nemo_curator.stages.video.filtering.motion_filter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`MotionVectorDecodeStage`](#nemo_curatorstagesvideofilteringmotion_filtermotionvectordecodestage) | Stage for decoding motion vector information from video files. |
| [`MotionFilterStage`](#nemo_curatorstagesvideofilteringmotion_filtermotionfilterstage) | Stage for filtering video clips based on motion score. |

### API

```python
class nemo_curator.stages.video.filtering.motion_filter.MotionVectorDecodeStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage for decoding motion vector information from video files.

This class processes video files through a series of steps including decoding,
filtering by side length, and storing the results in the task.

```python
num_cpus_per_worker: float
```

**Value**: `6.0`


```python
verbose: bool
```

**Value**: `False`


```python
target_fps: float
```

**Value**: `2.0`


```python
target_duration_ratio: float
```

**Value**: `0.5`


```python
_name: str
```

**Value**: `motion_vector_decoding`


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
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
class nemo_curator.stages.video.filtering.motion_filter.MotionFilterStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage for filtering video clips based on motion score.

This class processes video clips through a series of steps including motion score
computation and filtering based on thresholds.

```python
score_only: bool
```

**Value**: `False`


```python
global_mean_threshold: float
```

**Value**: `0.00098`


```python
per_patch_min_256_threshold: float
```

**Value**: `1e-06`


```python
num_gpus_per_worker: float
```

**Value**: `0`


```python
motion_filter_batch_size: int
```

**Value**: `256`


```python
verbose: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `motion_filter`


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

