---
layout: overview
slug: nemo-curator-stages-video-caption-caption-generation
---

# nemo_curator.stages.video.caption.caption_generation



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CaptionGenerationStage`](#nemo_curatorstagesvideocaptioncaption_generationcaptiongenerationstage) | Stage that generates captions for video windows using specified VL model. |

### API

```python
class nemo_curator.stages.video.caption.caption_generation.CaptionGenerationStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage that generates captions for video windows using specified VL model.

This stage processes prepared video windows through the specified vision-language model to
generate descriptive captions, with support for both synchronous and asynchronous processing.

```python
model_dir: str
```

**Value**: `models/qwen`


```python
model_variant: str
```

**Value**: `qwen`


```python
caption_batch_size: int
```

**Value**: `16`


```python
fp8: bool
```

**Value**: `False`


```python
max_output_tokens: int
```

**Value**: `512`


```python
model_does_preprocess: bool
```

**Value**: `False`


```python
disable_mmcache: bool
```

**Value**: `False`


```python
verbose: bool
```

**Value**: `False`


```python
generate_stage2_caption: bool
```

**Value**: `False`


```python
stage2_prompt_text: str | None
```

**Value**: `None`


```python
_name: str
```

**Value**: `caption_generation`


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
setup_on_node(
    node_info: nemo_curator.backends.base.NodeInfo,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata
) -> None
```

Download the weights for the QwenVL model on the node.


```python
__post_init__() -> None
```


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
_assign_captions(
    video: nemo_curator.tasks.video.Video,
    mapping: dict[int, tuple[int, int]],
    captions: collections.abc.Iterable[tuple[int, str]]
) -> None
```

