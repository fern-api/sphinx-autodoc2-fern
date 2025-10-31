---
layout: overview
slug: nemo-curator-stages-video-caption-caption-preparation
---

# nemo_curator.stages.video.caption.caption_preparation



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CaptionPreparationStage`](#nemo_curatorstagesvideocaptioncaption_preparationcaptionpreparationstage) | Stage that prepares captions for video processing. |

### Functions

| Name | Description |
|------|-------------|
| [`_get_prompt`](#nemo_curatorstagesvideocaptioncaption_preparation_get_prompt) | None |

### Data

`_PROMPTS`
`_ENHANCE_PROMPTS`

### API

```python
nemo_curator.stages.video.caption.caption_preparation._PROMPTS
```

**Value**: `None`


```python
nemo_curator.stages.video.caption.caption_preparation._ENHANCE_PROMPTS
```

**Value**: `None`


```python
nemo_curator.stages.video.caption.caption_preparation._get_prompt(
    prompt_variant: str, prompt_text: str | None
) -> str
```


```python
class nemo_curator.stages.video.caption.caption_preparation.CaptionPreparationStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage that prepares captions for video processing.

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
verbose: bool
```

**Value**: `False`


```python
sampling_fps: float
```

**Value**: `2.0`


```python
window_size: int
```

**Value**: `256`


```python
remainder_threshold: int
```

**Value**: `128`


```python
model_does_preprocess: bool
```

**Value**: `False`


```python
preprocess_dtype: str
```

**Value**: `float32`


```python
generate_previews: bool
```

**Value**: `True`


```python
_name: str
```

**Value**: `caption_preparation`


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

