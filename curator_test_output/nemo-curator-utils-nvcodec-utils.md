---
layout: overview
slug: nemo-curator-utils-nvcodec-utils
---

# nemo_curator.utils.nvcodec_utils



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`FrameExtractionPolicy`](#nemo_curatorutilsnvcodec_utilsframeextractionpolicy) | Policy for extracting frames from video, supporting full extraction or FPS-based sampling. |
| [`VideoBatchDecoder`](#nemo_curatorutilsnvcodec_utilsvideobatchdecoder) | GPU-accelerated video decoder that processes video frames in batches. |
| [`NvVideoDecoder`](#nemo_curatorutilsnvcodec_utilsnvvideodecoder) | Low-level NVIDIA hardware-accelerated video decoder. |
| [`PyNvcFrameExtractor`](#nemo_curatorutilsnvcodec_utilspynvcframeextractor) | High-level frame extraction interface using PyNvVideoCodec. |

### Functions

| Name | Description |
|------|-------------|
| [`gpu_decode_for_stitching`](#nemo_curatorutilsnvcodec_utilsgpu_decode_for_stitching) | Decode video frames for stitching using GPU acceleration. |

### API

```python
class nemo_curator.utils.nvcodec_utils.FrameExtractionPolicy
```

**Bases**: `enum.Enum`

Policy for extracting frames from video, supporting full extraction or FPS-based sampling.

This enum defines the available strategies for frame extraction from video content.

```python
full
```

**Value**: `0`


```python
fps
```

**Value**: `1`


```python
class nemo_curator.utils.nvcodec_utils.VideoBatchDecoder(batch_size: int, target_width: int, target_height: int, device_id: int, cuda_ctx: str, cvcuda_stream: str)
```

GPU-accelerated video decoder that processes video frames in batches.

This class handles video decoding using NVIDIA hardware acceleration, supporting
batch processing of frames with color space conversion and resizing capabilities.

### Initialization

Initialize video batch decoder with GPU acceleration parameters.

**Parameters:**

- **batch_size**: Number of frames to process in each batch.
- **target_width**: Target width for decoded frames.
- **target_height**: Target height for decoded frames.
- **device_id**: GPU device ID to use.
- **cuda_ctx**: CUDA context for GPU operations.
- **cvcuda_stream**: CUDA stream for parallel processing.


```python
get_fps() -> int | None
```

Get the frame rate of the video.

**Returns:**

Frame rate of the video.


```python
__call__(input_path: str) -> torch.Tensor | None
```

Process video frames in batches using GPU acceleration.

**Parameters:**

<ParamField path="input_path" type="str">
  Path to the video file to process.
</ParamField>

**Returns:**

Processed video frames as a tensor.


```python
class nemo_curator.utils.nvcodec_utils.NvVideoDecoder(enc_file: str, device_id: int, batch_size: int, cuda_ctx: typing.Any, cvcuda_stream: typing.Any)
```

Low-level NVIDIA hardware-accelerated video decoder.

This class provides direct access to NVIDIA's hardware video decoding capabilities,
handling frame decoding and memory management for video processing pipelines.

### Initialization

Create instance of HW-accelerated video decoder.

**Parameters:**

- ****enc_file****: Full path to the MP4 file that needs to be decoded.
- ****device_id****: id of video card which will be used for decoding & processing.
- ****cuda_ctx****: A cuda context object.


```python
generate_decoded_frames() -> list[torch.Tensor]
```

Generate decoded frames from the video.

**Returns:**

List of decoded frames as tensors.


```python
get_next_frames() -> torch.Tensor | None
```

Get the next frames from the video.

**Returns:**

Next frames from the video as a tensor.


```python
nemo_curator.utils.nvcodec_utils.gpu_decode_for_stitching(
    device_id: int,
    ctx: str,
    stream: int,
    input_path: pathlib.Path,
    frame_list: list[int],
    batch_size: int = 1
) -> list[torch.Tensor]
```

Decode video frames for stitching using GPU acceleration.

**Parameters:**

<ParamField path="device_id" type="int">
  GPU device ID.
</ParamField>

<ParamField path="ctx" type="str">
  CUDA context.
</ParamField>

<ParamField path="stream" type="int">
  CUDA stream.
</ParamField>

<ParamField path="input_path" type="pathlib.Path">
  Path to the video file to process.
</ParamField>

<ParamField path="frame_list" type="list[int]">
  List of frame indices to decode.
</ParamField>

<ParamField path="batch_size" type="int" default="1">
  Number of frames to process in each batch.
</ParamField>

**Returns:**

List of decoded frames as tensors.


```python
class nemo_curator.utils.nvcodec_utils.PyNvcFrameExtractor(width: int, height: int, batch_size: int)
```

High-level frame extraction interface using PyNvVideoCodec.

This class provides a simplified interface for extracting frames from videos using
hardware acceleration, supporting both full extraction and FPS-based sampling.

### Initialization

Initialize the PyNvcFrameExtractor.

**Parameters:**

- **width**: Width of the video frames.
- **height**: Height of the video frames.
- **batch_size**: Number of frames to process in each batch.


```python
__call__(
    input_path: pathlib.Path,
    extraction_policy: nemo_curator.utils.nvcodec_utils.FrameExtractionPolicy = FrameExtractionPolicy.full,
    sampling_fps: int = 1
) -> torch.Tensor
```

Extract frames from the video.

**Parameters:**

<ParamField path="input_path" type="pathlib.Path">
  Path to the video file to process.
</ParamField>

<ParamField path="extraction_policy" type="nemo_curator.utils.nvcodec_utils.FrameExtractionPolicy" default="FrameExtractionPolicy.full">
  Policy for extracting frames.
</ParamField>

<ParamField path="sampling_fps" type="int" default="1">
  Sampling rate for FPS-based extraction.
</ParamField>

**Returns:**

List of decoded frames as tensors.

