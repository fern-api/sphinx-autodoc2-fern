---
layout: overview
slug: nemo-curator-stages-video-filtering-motion-vector-backend
---

# nemo_curator.stages.video.filtering.motion_vector_backend



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`MotionInfo`](#nemo_curatorstagesvideofilteringmotion_vector_backendmotioninfo) | Container for motion detection results. |
| [`DecodedData`](#nemo_curatorstagesvideofilteringmotion_vector_backenddecodeddata) | Container for decoded video frames containing motion vector data. |

### Functions

| Name | Description |
|------|-------------|
| [`motion_vectors_to_flowfield`](#nemo_curatorstagesvideofilteringmotion_vector_backendmotion_vectors_to_flowfield) | Compute a canonical flow from motion vectors. |
| [`decode_for_motion`](#nemo_curatorstagesvideofilteringmotion_vector_backenddecode_for_motion) | Decode video for motion detection. |
| [`check_if_small_motion`](#nemo_curatorstagesvideofilteringmotion_vector_backendcheck_if_small_motion) | Check if a video has small motion. |

### Data

`_MIN_SIDE_RESOLUTION`

### API

```python
nemo_curator.stages.video.filtering.motion_vector_backend._MIN_SIDE_RESOLUTION
```

**Value**: `256`


```python
class nemo_curator.stages.video.filtering.motion_vector_backend.VideoResolutionTooSmallError
```

**Bases**: `Exception`

Exception raised when video resolution is below the minimum required size.

This error occurs when either the width or height of the video is less than
the minimum resolution threshold required for motion detection.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.


```python
class nemo_curator.stages.video.filtering.motion_vector_backend.MotionInfo
```

Container for motion detection results.

This class stores the results of motion detection analysis, including:
- Whether the video has small motion
- The minimum motion value in a 256x256 patch
- The global average motion value across the entire videoq

```python
is_small_motion: bool
```

**Value**: `None`


```python
per_patch_min_256: float
```

**Value**: `None`


```python
global_mean: float
```

**Value**: `None`


```python
class nemo_curator.stages.video.filtering.motion_vector_backend.DecodedData
```

Container for decoded video frames containing motion vector data.

This class stores a list of decoded frames, each containing motion vector data,
and the dimensions of the RGB decoded frame used to construct the flow vector.

```python
frames: list[numpy.typing.NDArray]
```

**Value**: `None`


```python
frame_size: torch.Size
```

**Value**: `None`


```python
get_major_size() -> int
```

Calculate total size in bytes of all frames in the decoded data.

**Returns:**

Total size in bytes.


```python
nemo_curator.stages.video.filtering.motion_vector_backend.motion_vectors_to_flowfield(
    mvs: torch.Tensor,
    size: list[int],
    flow: torch.Tensor | None = None
) -> torch.Tensor
```

Compute a canonical flow from motion vectors.


```python
nemo_curator.stages.video.filtering.motion_vector_backend.decode_for_motion(
    video: io.BytesIO,
    thread_count: int = 4,
    target_fps: float = 2.0,
    target_duration_ratio: float = 0.5
) -> nemo_curator.stages.video.filtering.motion_vector_backend.DecodedData
```

Decode video for motion detection.

This function decodes a video stream to extract motion vectors.

**Parameters:**

<ParamField path="video" type="io.BytesIO">
  Input video stream as a bytes object.
</ParamField>

<ParamField path="thread_count" type="int" default="4">
  Number of threads to use for decoding.
</ParamField>

<ParamField path="target_fps" type="float" default="2.0">
  Target frames per second for motion detection.
</ParamField>

<ParamField path="target_duration_ratio" type="float" default="0.5">
  Ratio of target duration to source duration.
</ParamField>

**Returns:**

DecodedData object containing motion vectors and frame dimensions.


```python
nemo_curator.stages.video.filtering.motion_vector_backend.check_if_small_motion(
    mv_list: list[numpy.typing.NDArray],
    frame_shape: torch.Size,
    global_mean_threshold: float = 0.00098,
    per_patch_min_256_threshold: float = 1e-06,
    *,
    use_gpu: bool = False,
    batch_size: int = 256
) -> nemo_curator.stages.video.filtering.motion_vector_backend.MotionInfo
```

Check if a video has small motion.

This function checks if a video has small motion by calculating the global mean
and per-pixel average motion values.

**Parameters:**

<ParamField path="mv_list" type="list[numpy.typing.NDArray]">
  List of motion vectors.
</ParamField>

<ParamField path="frame_shape" type="torch.Size">
  Shape of the frame.
</ParamField>

<ParamField path="global_mean_threshold" type="float" default="0.00098">
  Threshold for global mean motion.
</ParamField>

<ParamField path="per_patch_min_256_threshold" type="float" default="1e-06">
  Threshold for per-patch minimum motion.
</ParamField>

<ParamField path="use_gpu" type="bool" default="False">
  Whether to use GPU for computation.
</ParamField>

<ParamField path="batch_size" type="int" default="256">
  Size of the batch for processing.
</ParamField>

**Returns:**

MotionInfo object containing the results of the motion detection.

