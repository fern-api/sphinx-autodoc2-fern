---
layout: overview
slug: nemo-curator-stages-video-embedding-internvideo2
---

# nemo_curator.stages.video.embedding.internvideo2



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`InternVideo2FrameCreationStage`](#nemo_curatorstagesvideoembeddinginternvideo2internvideo2framecreationstage) | Stage for creating InternVideo2 input frames from video clips. |
| [`InternVideo2EmbeddingStage`](#nemo_curatorstagesvideoembeddinginternvideo2internvideo2embeddingstage) | Stage for generating embeddings from InternVideo2 input frames. |

### API

```python
class nemo_curator.stages.video.embedding.internvideo2.InternVideo2FrameCreationStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage for creating InternVideo2 input frames from video clips.

This class processes video clips through a series of steps including frame extraction,
model initialization, and input frame creation.

```python
target_fps: float
```

**Value**: `2.0`


```python
verbose: bool
```

**Value**: `False`


```python
model_dir: str
```

**Value**: `InternVideo2`


```python
_name: str
```

**Value**: `internvideo2_embedding_frame_creation`


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
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
class nemo_curator.stages.video.embedding.internvideo2.InternVideo2EmbeddingStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage for generating embeddings from InternVideo2 input frames.

This class processes video clips through a series of steps including embedding generation,
text verification, and memory management.

```python
num_gpus_per_worker: float
```

**Value**: `1.0`


```python
texts_to_verify: list[str] | None
```

**Value**: `None`


```python
verbose: bool
```

**Value**: `False`


```python
gpu_memory_gb: float
```

**Value**: `10.0`


```python
model_dir: str
```

**Value**: `InternVideo2`


```python
_name: str
```

**Value**: `internvideo2_embedding`


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
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
setup_on_node(
    node_info: nemo_curator.backends.base.NodeInfo,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata
) -> None
```

Download the weights for the InternVideo2 model on the node.

