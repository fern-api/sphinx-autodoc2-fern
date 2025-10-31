---
layout: overview
slug: nemo-curator-stages-video-caption-caption-enhancement
---

# nemo_curator.stages.video.caption.caption_enhancement



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CaptionEnhancementStage`](#nemo_curatorstagesvideocaptioncaption_enhancementcaptionenhancementstage) | Stage that enhances video captions using language models. |

### Functions

| Name | Description |
|------|-------------|
| [`_get_enhance_prompt`](#nemo_curatorstagesvideocaptioncaption_enhancement_get_enhance_prompt) | None |

### Data

`_ENHANCE_PROMPTS`

### API

```python
nemo_curator.stages.video.caption.caption_enhancement._ENHANCE_PROMPTS
```

**Value**: `None`


```python
class nemo_curator.stages.video.caption.caption_enhancement.CaptionEnhancementStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage that enhances video captions using language models.

This stage takes existing captions and uses LLM (e.g. Qwen) to generate
more detailed and refined descriptions of the video content.

```python
model_dir: str
```

**Value**: `models/qwen`


```python
model_variant: str
```

**Value**: `qwen`


```python
prompt_variant: str
```

**Value**: `default`


```python
prompt_text: str | None
```

**Value**: `None`


```python
model_batch_size: int
```

**Value**: `128`


```python
fp8: bool
```

**Value**: `False`


```python
max_output_tokens: int
```

**Value**: `512`


```python
verbose: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `caption_enhancement`


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
setup(worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
setup_on_node(
    node_info: nemo_curator.backends.base.NodeInfo,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata
) -> None
```

Download the weights for the QwenLM model on the node.


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
_prepare_caption_inputs(video: nemo_curator.tasks.video.Video) -> tuple[dict[int, tuple[int, int]], list[dict[str, typing.Any]]]
```

Prepare caption inputs from video clips and windows.


```python
_is_valid_window_caption(
    clip: nemo_curator.tasks.video.Clip,
    window: nemo_curator.tasks.video._Window,
    window_idx: int
) -> bool
```

Check if window has valid caption data.


```python
_generate_and_assign_captions(
    video: nemo_curator.tasks.video.Video,
    mapping: dict[int, tuple[int, int]],
    inputs: list[dict[str, typing.Any]]
) -> None
```

Generate enhanced captions and assign them to video windows.


```python
nemo_curator.stages.video.caption.caption_enhancement._get_enhance_prompt(
    prompt_variant: str,
    prompt_text: str | None,
    *,
    verbose: bool = False
) -> str
```

