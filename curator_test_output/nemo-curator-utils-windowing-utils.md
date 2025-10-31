---
layout: overview
slug: nemo-curator-utils-windowing-utils
---

# nemo_curator.utils.windowing_utils



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`WindowFrameInfo`](#nemo_curatorutilswindowing_utilswindowframeinfo) | Container for frame window information, storing start and end frame indices. |

### Functions

| Name | Description |
|------|-------------|
| [`compute_windows`](#nemo_curatorutilswindowing_utilscompute_windows) | Generate windows by splitting the video into segments of the specified size. |
| [`split_video_into_windows`](#nemo_curatorutilswindowing_utilssplit_video_into_windows) | Calculate windows and return video inputs for language model from input clips. |
| [`round_by_factor`](#nemo_curatorutilswindowing_utilsround_by_factor) | Return the closest integer to 'number' that is divisible by 'factor'. |
| [`ceil_by_factor`](#nemo_curatorutilswindowing_utilsceil_by_factor) | Return the smallest integer greater than or equal to 'number' that is divisible by 'factor'. |
| [`floor_by_factor`](#nemo_curatorutilswindowing_utilsfloor_by_factor) | Return the largest integer less than or equal to 'number' that is divisible by 'factor'. |
| [`smart_resize`](#nemo_curatorutilswindowing_utilssmart_resize) | Rescales the image so that the following conditions are met. |
| [`smart_nframes`](#nemo_curatorutilswindowing_utilssmart_nframes) | Calculate the number of frames for video used for model inputs. |
| [`read_video_cpu`](#nemo_curatorutilswindowing_utilsread_video_cpu) | Read video using PyAv. |
| [`fetch_video`](#nemo_curatorutilswindowing_utilsfetch_video) | Load and preprocess video frames from a file. |

### Data

`WINDOW_MIN_FRAMES`
`IMAGE_FACTOR`
`MIN_PIXELS`
`MAX_PIXELS`
`MAX_RATIO`
`VIDEO_MIN_PIXELS`
`VIDEO_MAX_PIXELS`
`VIDEO_TOTAL_PIXELS`
`FRAME_FACTOR`
`FPS`
`FPS_MIN_FRAMES`
`FPS_MAX_FRAMES`
`OPENAI_CLIP_MEAN`
`OPENAI_CLIP_STD`

### API

```python
class nemo_curator.utils.windowing_utils.WindowFrameInfo
```

Container for frame window information, storing start and end frame indices.

This class represents a window of frames in a video, defined by its start and end frame positions.

```python
start: int
```

**Value**: `None`


```python
end: int
```

**Value**: `None`


```python
nemo_curator.utils.windowing_utils.WINDOW_MIN_FRAMES
```

**Value**: `4`


```python
nemo_curator.utils.windowing_utils.compute_windows(
    total_frames: int,
    window_size: int = 128,
    remainder_threshold: int = 64
) -> list[nemo_curator.utils.windowing_utils.WindowFrameInfo]
```

Generate windows by splitting the video into segments of the specified size.

**Parameters:**

<ParamField path="total_frames" type="int">
  total frames
</ParamField>

<ParamField path="window_size" type="int" default="128">
  The size of each window in number of frames.
</ParamField>

<ParamField path="remainder_threshold" type="int" default="64">
  The minimum number of frames required to create a new window from the remainder.
</ParamField>

**Returns:**

Tuple of (start_frame, end_frame) representing each window.


```python
nemo_curator.utils.windowing_utils.split_video_into_windows(
    mp4_bytes: bytes,
    window_size: int = 256,
    remainder_threshold: int = 128,
    sampling_fps: float = 2.0,
    *,
    model_does_preprocess: bool = False,
    preprocess_dtype: str = 'uint8',
    flip_input: bool = False,
    num_frames_to_use: int = 0,
    return_bytes: bool = False,
    return_video_frames: bool = True,
    num_threads: int = 1
) -> tuple[list[bytes], list[torch.Tensor | None], list[nemo_curator.utils.windowing_utils.WindowFrameInfo]]
```

Calculate windows and return video inputs for language model from input clips.

Processes video to determine the windows for a clip, decode in one shot and return processed frames
for each window in a format suitable for consumption by the Qwen model.

**Parameters:**

<ParamField path="mp4_bytes" type="bytes">
  input video in bytes
</ParamField>

<ParamField path="preprocess_dtype" type="str" default="'uint8'">
  Data type to use for preprocessing the video/image inputs.
</ParamField>

<ParamField path="num_frames_to_use" type="int" default="0">
  Number of frames to extract from the video. If 0, uses all frames.
</ParamField>

<ParamField path="flip_input" type="bool" default="False">
  Whether to flip the input video/image horizontally.
</ParamField>

<ParamField path="return_bytes" type="bool" default="False">
  Whether to extract mp4 bytes for each window for use by PreviewStage
</ParamField>

<ParamField path="model_does_preprocess" type="bool" default="False">
  if the model does preprocessing
</ParamField>

<ParamField path="num_threads" type="int" default="1">
  number of threads
</ParamField>

<ParamField path="remainder_threshold" type="int" default="128">
  threshold for remainder
</ParamField>

<ParamField path="return_video_frames" type="bool" default="True">
  whether to return video frames
</ParamField>

<ParamField path="sampling_fps" type="float" default="2.0">
  sampling fps
</ParamField>

<ParamField path="window_size" type="int" default="256">
  window size
</ParamField>

**Returns:**

Tuple containing:
- "window_mp4_bytes": mp4 bytes corresponding to each window - only used when Preview stage is enabled
- "window_frames": Decoded and per-window processed frames ready for use by Qwen model
- "window info": start and end frame indices for each window in a clip


```python
nemo_curator.utils.windowing_utils.IMAGE_FACTOR
```

**Value**: `28`


```python
nemo_curator.utils.windowing_utils.MIN_PIXELS
```

**Value**: `None`


```python
nemo_curator.utils.windowing_utils.MAX_PIXELS
```

**Value**: `None`


```python
nemo_curator.utils.windowing_utils.MAX_RATIO
```

**Value**: `200`


```python
nemo_curator.utils.windowing_utils.VIDEO_MIN_PIXELS
```

**Value**: `None`


```python
nemo_curator.utils.windowing_utils.VIDEO_MAX_PIXELS
```

**Value**: `None`


```python
nemo_curator.utils.windowing_utils.VIDEO_TOTAL_PIXELS
```

**Value**: `None`


```python
nemo_curator.utils.windowing_utils.FRAME_FACTOR
```

**Value**: `2`


```python
nemo_curator.utils.windowing_utils.FPS
```

**Value**: `2.0`


```python
nemo_curator.utils.windowing_utils.FPS_MIN_FRAMES
```

**Value**: `4`


```python
nemo_curator.utils.windowing_utils.FPS_MAX_FRAMES
```

**Value**: `768`


```python
nemo_curator.utils.windowing_utils.OPENAI_CLIP_MEAN
```

**Value**: `[0.48145466, 0.4578275, 0.40821073]`


```python
nemo_curator.utils.windowing_utils.OPENAI_CLIP_STD
```

**Value**: `[0.26862954, 0.26130258, 0.27577711]`


```python
nemo_curator.utils.windowing_utils.round_by_factor(
    number: float, factor: int
) -> int
```

Return the closest integer to 'number' that is divisible by 'factor'.


```python
nemo_curator.utils.windowing_utils.ceil_by_factor(
    number: float, factor: int
) -> int
```

Return the smallest integer greater than or equal to 'number' that is divisible by 'factor'.


```python
nemo_curator.utils.windowing_utils.floor_by_factor(
    number: float, factor: int
) -> int
```

Return the largest integer less than or equal to 'number' that is divisible by 'factor'.


```python
nemo_curator.utils.windowing_utils.smart_resize(
    height: int,
    width: int,
    factor: int = IMAGE_FACTOR,
    min_pixels: int = MIN_PIXELS,
    max_pixels: int = MAX_PIXELS
) -> tuple[int, int]
```

Rescales the image so that the following conditions are met.

1. Both dimensions (height and width) are divisible by 'factor'.

2. The total number of pixels is within the range ['min_pixels', 'max_pixels'].

3. The aspect ratio of the image is maintained as closely as possible.


```python
nemo_curator.utils.windowing_utils.smart_nframes(
    fps: float,
    total_frames: int,
    video_fps: float
) -> int
```

Calculate the number of frames for video used for model inputs.


```python
nemo_curator.utils.windowing_utils.read_video_cpu(
    video_path: str,
    fps: float,
    num_frames_to_use: int,
    window_range: list[nemo_curator.utils.windowing_utils.WindowFrameInfo]
) -> tuple[torch.Tensor, list[int]]
```

Read video using PyAv.

**Parameters:**

<ParamField path="video_path" type="str">
  path to the video support "file://", "http://", "https://" and local path.
</ParamField>

<ParamField path="fps" type="float">
  frames per second
</ParamField>

<ParamField path="num_frames_to_use" type="int">
  number of frames to use
</ParamField>

<ParamField path="window_range" type="list[nemo_curator.utils.windowing_utils.WindowFrameInfo]">
  window range
</ParamField>

**Returns:**

torch.Tensor: the video tensor with shape (T, C, H, W).


```python
nemo_curator.utils.windowing_utils.fetch_video(
    video_path: str,
    sampling_fps: float = 2.0,
    window_range: list[nemo_curator.utils.windowing_utils.WindowFrameInfo] | None = None,
    *,
    do_preprocess: bool = False,
    preprocess_dtype: str = 'float32',
    num_frames_to_use: int = 0,
    flip_input: bool = False
) -> tuple[torch.Tensor, list[int]]
```

Load and preprocess video frames from a file.

**Parameters:**

<ParamField path="video_path" type="str">
  Path to the video file.
</ParamField>

<ParamField path="sampling_fps" type="float" default="2.0">
  Target frames per second for sampling.
</ParamField>

<ParamField path="window_range" type="list[nemo_curator.utils.windowing_utils.WindowFrameInfo] | None">
  List of frame windows to extract.
</ParamField>

<ParamField path="do_preprocess" type="bool" default="False">
  Whether to preprocess the frames.
</ParamField>

<ParamField path="preprocess_dtype" type="str" default="'float32'">
  Data type for preprocessing.
</ParamField>

<ParamField path="num_frames_to_use" type="int" default="0">
  Number of frames to extract (0 for all).
</ParamField>

<ParamField path="flip_input" type="bool" default="False">
  Whether to flip frames horizontally.
</ParamField>

**Returns:**

Tuple of (processed frames tensor, frame indices).

