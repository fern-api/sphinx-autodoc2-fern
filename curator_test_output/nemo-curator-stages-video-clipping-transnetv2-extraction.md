---
layout: overview
slug: nemo-curator-stages-video-clipping-transnetv2-extraction
---

# nemo_curator.stages.video.clipping.transnetv2_extraction



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`TransNetV2ClipExtractionStage`](#nemo_curatorstagesvideoclippingtransnetv2_extractiontransnetv2clipextractionstage) | Stage for extracting video clips using TransNetV2. |

### Functions

| Name | Description |
|------|-------------|
| [`_get_batches`](#nemo_curatorstagesvideoclippingtransnetv2_extraction_get_batches) | We fetch 100 frames, and pad the first and last batches accordingly with the first or last frame. |
| [`_get_predictions`](#nemo_curatorstagesvideoclippingtransnetv2_extraction_get_predictions) | Get predictions from the video frame array. |
| [`_get_scenes`](#nemo_curatorstagesvideoclippingtransnetv2_extraction_get_scenes) | Convert prediction array to scene array. |
| [`_get_filtered_scenes`](#nemo_curatorstagesvideoclippingtransnetv2_extraction_get_filtered_scenes) | Filter scenes. |
| [`_crop_scenes`](#nemo_curatorstagesvideoclippingtransnetv2_extraction_crop_scenes) | Crop scenes by removing frames from start and end. |
| [`_create_spans`](#nemo_curatorstagesvideoclippingtransnetv2_extraction_create_spans) | Create spans between a start and an end point. |

### API

```python
class nemo_curator.stages.video.clipping.transnetv2_extraction.TransNetV2ClipExtractionStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage for extracting video clips using TransNetV2.

This class processes video clips through a series of steps including shot detection,
scene filtering, and clip assignment.

```python
model_dir: str
```

**Value**: `None`


```python
threshold: float
```

**Value**: `0.4`


```python
min_length_s: float | None
```

**Value**: `2.0`


```python
max_length_s: float | None
```

**Value**: `10.0`


```python
max_length_mode: typing.Literal[truncate, stride]
```

**Value**: `stride`


```python
crop_s: float | None
```

**Value**: `0.5`


```python
entire_scene_as_clip: bool
```

**Value**: `True`


```python
gpu_memory_gb: int
```

**Value**: `10`


```python
limit_clips: int
```

**Value**: `None`


```python
verbose: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `transnetv2_clip_extraction`


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
setup_on_node(
    node_info: nemo_curator.backends.base.NodeInfo,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata
) -> None
```

Download TransNetV2 weights on the node.


```python
setup(worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
__post_init__() -> None
```


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
nemo_curator.stages.video.clipping.transnetv2_extraction._get_batches(frames: numpy.typing.NDArray[numpy.uint8]) -> collections.abc.Generator[numpy.typing.NDArray[numpy.uint8], None, None]
```

We fetch 100 frames, and pad the first and last batches accordingly with the first or last frame.


```python
nemo_curator.stages.video.clipping.transnetv2_extraction._get_predictions(
    model: collections.abc.Callable[[torch.Tensor], torch.Tensor],
    frames: numpy.typing.NDArray[numpy.uint8],
    threshold: float
) -> numpy.typing.NDArray[numpy.uint8]
```

Get predictions from the video frame array.

**Parameters:**

<ParamField path="model" type="collections.abc.Callable[[torch.Tensor], torch.Tensor]">
  shot detection model.
</ParamField>

<ParamField path="frames" type="numpy.typing.NDArray[numpy.uint8]">
  uint8 array of shape (# frames, height, width, 3), with RGB channels.
</ParamField>

<ParamField path="threshold" type="float">
  probability threshold for shot detection.
</ParamField>

**Returns:**

0/1 prediction array of shape (# frames, 1)


```python
nemo_curator.stages.video.clipping.transnetv2_extraction._get_scenes(
    predictions: numpy.typing.NDArray[numpy.uint8],
    *,
    entire_scene_as_clip: bool
) -> numpy.typing.NDArray[numpy.int32]
```

Convert prediction array to scene array.

**Parameters:**

<ParamField path="predictions" type="numpy.typing.NDArray[numpy.uint8]">
  array of shape [# frames, 1].
</ParamField>

**Returns:**

scene array of shape [# scenes, 2], where the value at each row is the start and end frame of the shot.


```python
nemo_curator.stages.video.clipping.transnetv2_extraction._get_filtered_scenes(
    scenes: numpy.typing.NDArray[numpy.int32],
    min_length: int | None = None,
    max_length: int | None = None,
    max_length_mode: typing.Literal[truncate, stride] = 'truncate',
    crop_length: int | None = None
) -> numpy.typing.NDArray[numpy.int32]
```

Filter scenes.

**Parameters:**

<ParamField path="scenes" type="numpy.typing.NDArray[numpy.int32]">
  integer 2D array like [[t0, t1], [t2, t3], ...]
</ParamField>

<ParamField path="min_length" type="int | None">
  optional minimum length of frames a scene can have.
</ParamField>

<ParamField path="max_length" type="int | None">
  optional maximum length of frames a scene can have.
</ParamField>

<ParamField path="max_length_mode" type="typing.Literal[truncate, stride]" default="'truncate'">
  how to deal with scenes that are above max length.
</ParamField>

<ParamField path="crop_length" type="int | None">
  optional number of frames to crop from start and end of scene.
</ParamField>

**Returns:**

filtered scene array.


```python
nemo_curator.stages.video.clipping.transnetv2_extraction._crop_scenes(
    scenes: numpy.typing.NDArray[numpy.int32], crop_length: int
) -> numpy.typing.NDArray[numpy.int32]
```

Crop scenes by removing frames from start and end.

**Parameters:**

<ParamField path="scenes" type="numpy.typing.NDArray[numpy.int32]">
  integer 2D array like [[t0, t1], [t2, t3], ...]
</ParamField>

<ParamField path="crop_length" type="int">
  number of frames to crop from start and end of scene.
</ParamField>

**Returns:**

cropped scene array.


```python
nemo_curator.stages.video.clipping.transnetv2_extraction._create_spans(
    start: int,
    end: int,
    max_length: int,
    min_length: int | None
) -> list[list[int]]
```

Create spans between a start and an end point.

**Parameters:**

<ParamField path="start" type="int">
  start point.
</ParamField>

<ParamField path="end" type="int">
  end point.
</ParamField>

<ParamField path="max_length" type="int">
  maximum length of span.
</ParamField>

<ParamField path="min_length" type="int | None">
  minimum length of span.
</ParamField>

**Returns:**

list of spans.

