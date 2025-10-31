---
layout: overview
slug: nemo-curator-stages-video-filtering-clip-aesthetic-filter
---

# nemo_curator.stages.video.filtering.clip_aesthetic_filter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ClipAestheticFilterStage`](#nemo_curatorstagesvideofilteringclip_aesthetic_filterclipaestheticfilterstage) | Stage for filtering video clips based on CLIP aesthetic score. |

### API

```python
class nemo_curator.stages.video.filtering.clip_aesthetic_filter.ClipAestheticFilterStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage for filtering video clips based on CLIP aesthetic score.

This class processes video clips through a series of steps including aesthetic score
calculation and filtering based on thresholds.

```python
model_dir: str
```

**Value**: `models/clip_aesthetic`


```python
score_threshold: float
```

**Value**: `0.5`


```python
reduction: typing.Literal[mean, min]
```

**Value**: `min`


```python
target_fps: float
```

**Value**: `1.0`


```python
num_gpus_per_worker: float
```

**Value**: `0.25`


```python
verbose: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `clip_aesthetic_filter`


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
setup_on_node(
    node_info: nemo_curator.backends.base.NodeInfo,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata
) -> None
```

Download the weights for the CLIPAestheticScorer model on the node.


```python
setup(worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```

