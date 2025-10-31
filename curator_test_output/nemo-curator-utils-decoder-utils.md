---
layout: overview
slug: nemo-curator-utils-decoder-utils
---

# nemo_curator.utils.decoder_utils



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Resolution`](#nemo_curatorutilsdecoder_utilsresolution) | Container for video frame dimensions. |
| [`VideoMetadata`](#nemo_curatorutilsdecoder_utilsvideometadata) | Metadata for video content including dimensions, timing, and codec information. |
| [`FrameExtractionPolicy`](#nemo_curatorutilsdecoder_utilsframeextractionpolicy) | Policy for extracting frames from video content. |
| [`FramePurpose`](#nemo_curatorutilsdecoder_utilsframepurpose) | Purpose for extracting frames from video content. |
| [`FrameExtractionSignature`](#nemo_curatorutilsdecoder_utilsframeextractionsignature) | Configuration for frame extraction parameters. |

### Functions

| Name | Description |
|------|-------------|
| [`extract_video_metadata`](#nemo_curatorutilsdecoder_utilsextract_video_metadata) | Extract metadata from a video file using ffprobe. |
| [`_make_video_stream`](#nemo_curatorutilsdecoder_utils_make_video_stream) | Convert various input types into a binary stream for video processing. |
| [`save_stream_position`](#nemo_curatorutilsdecoder_utilssave_stream_position) | Context manager that saves and restores stream position. |
| [`get_video_timestamps`](#nemo_curatorutilsdecoder_utilsget_video_timestamps) | Get timestamps for all frames in a video stream. |
| [`find_closest_indices`](#nemo_curatorutilsdecoder_utilsfind_closest_indices) | Find the closest indices in src to each element in dst. |
| [`sample_closest`](#nemo_curatorutilsdecoder_utilssample_closest) | Sample `src` at `sample_rate` rate and return the closest indices. |
| [`decode_video_cpu_frame_ids`](#nemo_curatorutilsdecoder_utilsdecode_video_cpu_frame_ids) | Decode video using PyAV frame ids. |
| [`get_avg_frame_rate`](#nemo_curatorutilsdecoder_utilsget_avg_frame_rate) | Get the average frame rate of a video. |
| [`decode_video_cpu`](#nemo_curatorutilsdecoder_utilsdecode_video_cpu) | Decode video frames from a binary stream using PyAV with configurable frame rate sampling. |
| [`get_frame_count`](#nemo_curatorutilsdecoder_utilsget_frame_count) | Get the total number of frames in a video file or stream. |
| [`extract_frames`](#nemo_curatorutilsdecoder_utilsextract_frames) | Extract frames from a video into a numpy array. |

### API

```python
class nemo_curator.utils.decoder_utils.Resolution
```

**Bases**: `typing.NamedTuple`

Container for video frame dimensions.

This class stores the height and width of video frames as a named tuple.

```python
height: int
```

**Value**: `None`


```python
width: int
```

**Value**: `None`


```python
class nemo_curator.utils.decoder_utils.VideoMetadata
```

Metadata for video content including dimensions, timing, and codec information.

This class stores essential video properties such as resolution, frame rate,
duration, and encoding details.

```python
height: int
```

**Value**: `None`


```python
width: int
```

**Value**: `None`


```python
fps: float
```

**Value**: `None`


```python
num_frames: int
```

**Value**: `None`


```python
video_codec: str
```

**Value**: `None`


```python
pixel_format: str
```

**Value**: `None`


```python
video_duration: float
```

**Value**: `None`


```python
audio_codec: str
```

**Value**: `None`


```python
bit_rate_k: int
```

**Value**: `None`


```python
class nemo_curator.utils.decoder_utils.FrameExtractionPolicy
```

**Bases**: `enum.Enum`

Policy for extracting frames from video content.

This enum defines different strategies for selecting frames from a video,
including first frame, middle frame, last frame, or a sequence of frames.

```python
first
```

**Value**: `0`


```python
middle
```

**Value**: `1`


```python
last
```

**Value**: `2`


```python
sequence
```

**Value**: `3`


```python
class nemo_curator.utils.decoder_utils.FramePurpose
```

**Bases**: `enum.Enum`

Purpose for extracting frames from video content.

This enum defines different purposes for extracting frames from a video,
including aesthetics and embeddings.

```python
AESTHETICS
```

**Value**: `1`


```python
EMBEDDINGS
```

**Value**: `2`


```python
class nemo_curator.utils.decoder_utils.FrameExtractionSignature
```

Configuration for frame extraction parameters.

This class combines extraction policy and target frame rate into a single signature
that can be used to identify and reproduce frame extraction settings.

```python
extraction_policy: nemo_curator.utils.decoder_utils.FrameExtractionPolicy
```

**Value**: `None`


```python
target_fps: float
```

**Value**: `None`


```python
to_str() -> str
```

Convert frame extraction signature to string format.

**Returns:**

String representation of extraction policy and target FPS.


```python
nemo_curator.utils.decoder_utils.extract_video_metadata(video: str | bytes) -> nemo_curator.utils.decoder_utils.VideoMetadata
```

Extract metadata from a video file using ffprobe.

**Parameters:**

<ParamField path="video" type="str | bytes">
  Path to video file or video data as bytes.
</ParamField>

**Returns:**

VideoMetadata object containing video properties.


```python
nemo_curator.utils.decoder_utils._make_video_stream(data: pathlib.Path | str | typing.BinaryIO | bytes | io.BytesIO | io.BufferedReader) -> typing.BinaryIO
```

Convert various input types into a binary stream for video processing.

This function handles different input types that could represent video
data and converts them into a consistent BinaryIO interface that can be
used for video processing operations.

**Parameters:**

<ParamField path="data" type="pathlib.Path | str | typing.BinaryIO | bytes | io.BytesIO | io.BufferedReader">
  The input video data, which can be one of:
</ParamField>

**Returns:**

BinaryIO: A binary stream containing the video data

**Raises:**

ValueError: If the input type is not one of the supported types


```python
nemo_curator.utils.decoder_utils.save_stream_position(stream: typing.BinaryIO) -> collections.abc.Generator[typing.BinaryIO, None, None]
```

Context manager that saves and restores stream position.


```python
nemo_curator.utils.decoder_utils.get_video_timestamps(
    data: pathlib.Path | str | typing.BinaryIO | bytes,
    stream_idx: int = 0,
    video_format: str | None = None
) -> numpy.typing.NDArray[numpy.float32]
```

Get timestamps for all frames in a video stream.

The file position will be moved as needed to get the timestamps.

Note: the order that frames appear in a video stream is not necessarily
the order that the frames will be displayed. This means that timestamps
are not monotonically increasing within a video stream. This can happen
when B-frames are present

This function will return presentation timestamps in monotonically
increasing order.

**Parameters:**

<ParamField path="data" type="pathlib.Path | str | typing.BinaryIO | bytes">
  An open file, io.BytesIO, or bytes object with the video data.
</ParamField>

<ParamField path="stream_idx" type="int" default="0">
  PyAv index of the video stream to decode, usually 0.
</ParamField>

<ParamField path="video_format" type="str | None">
  Format of the video stream, like "mp4", "mkv", etc.
</ParamField>

**Returns:**

A numpy array of monotonically increasing timestamps.


```python
nemo_curator.utils.decoder_utils.find_closest_indices(
    src: numpy.typing.NDArray[numpy.float32],
    dst: numpy.typing.NDArray[numpy.float32]
) -> numpy.typing.NDArray[numpy.int32]
```

Find the closest indices in src to each element in dst.

If an element in dst is equidistant from two elements in src, the left
index in src is used.

**Parameters:**

<ParamField path="src" type="numpy.typing.NDArray[numpy.float32]">
  Monotonically increasing array of numbers to match dst against
</ParamField>

<ParamField path="dst" type="numpy.typing.NDArray[numpy.float32]">
  Monotonically increasing array of numbers to search for in src
</ParamField>

**Returns:**

Array of closest indices in src for each element in dst


```python
nemo_curator.utils.decoder_utils.sample_closest(
    src: numpy.typing.NDArray[numpy.float32],
    sample_rate: float,
    start: float | None = None,
    stop: float | None = None,
    endpoint: bool = True,
    dedup: bool = True
) -> tuple[numpy.typing.NDArray[numpy.int32], numpy.typing.NDArray[numpy.int32], numpy.typing.NDArray[numpy.float32]]
```

Sample `src` at `sample_rate` rate and return the closest indices.

This function is meant to be used for sampling monotonically increasing
numbers, like timestamps. This function can be used for synchronizing
sensors, like multiple cameras, or synchronizing video with GPS and LIDAR.

The first element sampled with either or src[0] or the element closest
to `start`

The last element sampled will either be src[-1] or the element closest
to `stop`. The last element is only included if it both fits into the
sampling rate and if endpoint=True

This function intentionally has no policy about distance from the closest
elements in src to the sample elements. It will return the index of the
closest element to the sample. It is up to the caller to define policy,
which is why sample_elements is returned.

**Parameters:**

<ParamField path="src" type="numpy.typing.NDArray[numpy.float32]">
  Monotonically increasing array of elements
</ParamField>

<ParamField path="sample_rate" type="float">
  Sampling rate
</ParamField>

<ParamField path="start" type="float | None">
  Start element (defaults to first element)
</ParamField>

<ParamField path="stop" type="float | None">
  End element (defaults to last element)
</ParamField>

<ParamField path="endpoint" type="bool" default="True">
  If True, `stop` can be the last sample, if it fits into
</ParamField>

<ParamField path="dedup" type="bool" default="True">
  Whether to deduplicate indices. Repeated indices will be
</ParamField>

**Returns:**

Tuple of (indices, counts) where counts[i] is the number of times
indices[i] was sampled. The sample elements are also returned


```python
nemo_curator.utils.decoder_utils.decode_video_cpu_frame_ids(
    data: pathlib.Path | str | typing.BinaryIO | bytes,
    frame_ids: numpy.typing.NDArray[numpy.int32],
    counts: numpy.typing.NDArray[numpy.int32] | None = None,
    stream_idx: int = 0,
    video_format: str | None = None,
    num_threads: int = 1
) -> numpy.typing.NDArray[numpy.uint8]
```

Decode video using PyAV frame ids.

It is not recommended to use this function directly. Instead, use
`decode_video_cpu`, which is timestamp-based. Timestamps are necessary for
synchronizing sensors, like multiple cameras, or synchronizing video with
GPS and LIDAR.

**Parameters:**

<ParamField path="data" type="pathlib.Path | str | typing.BinaryIO | bytes">
  An open file, io.BytesIO, or bytes object with the video data.
</ParamField>

<ParamField path="frame_ids" type="numpy.typing.NDArray[numpy.int32]">
  List of frame ids to decode.
</ParamField>

<ParamField path="counts" type="numpy.typing.NDArray[numpy.int32] | None">
  List of counts for each frame id. It is possible that a frame id
</ParamField>

<ParamField path="stream_idx" type="int" default="0">
  PyAv index of the video stream to decode, usually 0.
</ParamField>

<ParamField path="video_format" type="str | None">
  Format of the video stream, like "mp4", "mkv", etc.
</ParamField>

<ParamField path="num_threads" type="int" default="1">
  Number of threads to use for decoding.
</ParamField>

**Returns:**

A numpy array of shape (frame_count, height, width, channels) containing
the decoded frames.


```python
nemo_curator.utils.decoder_utils.get_avg_frame_rate(
    data: pathlib.Path | str | typing.BinaryIO | bytes,
    stream_idx: int = 0,
    video_format: str | None = None
) -> float
```

Get the average frame rate of a video.

**Parameters:**

<ParamField path="data" type="pathlib.Path | str | typing.BinaryIO | bytes">
  An open file, io.BytesIO, or bytes object with the video data.
</ParamField>

<ParamField path="stream_idx" type="int" default="0">
  Index of the video stream to decode, usually 0.
</ParamField>

<ParamField path="video_format" type="str | None">
  Format of the video stream, like "mp4", "mkv", etc.
</ParamField>

**Returns:**

The average frame rate of the video.


```python
nemo_curator.utils.decoder_utils.decode_video_cpu(
    data: pathlib.Path | str | typing.BinaryIO | bytes,
    sample_rate_fps: float,
    timestamps: numpy.typing.NDArray[numpy.float32] | None = None,
    start: float | None = None,
    stop: float | None = None,
    endpoint: bool = True,
    stream_idx: int = 0,
    video_format: str | None = None,
    num_threads: int = 1
) -> numpy.typing.NDArray[numpy.uint8]
```

Decode video frames from a binary stream using PyAV with configurable frame rate sampling.

This function decodes video frames from a binary stream at a specified
frame rate. The frame rate does not need to match the input video's frame
rate. It is possible to supersample a video as well as undersample.

**Parameters:**

<ParamField path="data" type="pathlib.Path | str | typing.BinaryIO | bytes">
  An open file, io.BytesIO, or bytes object with the video data.
</ParamField>

<ParamField path="sample_rate_fps" type="float">
  Frame rate for sampling the video
</ParamField>

<ParamField path="timestamps" type="numpy.typing.NDArray[numpy.float32] | None">
  Optional array of presentation timestamps for each frame
</ParamField>

<ParamField path="start" type="float | None">
  Optional start timestamp for frame extraction. If None, the
</ParamField>

<ParamField path="stop" type="float | None">
  Optional end timestamp for frame extraction. If None, the last
</ParamField>

<ParamField path="endpoint" type="bool" default="True">
  If True, stop is the last sample. Otherwise, it is not included.
</ParamField>

<ParamField path="stream_idx" type="int" default="0">
  PyAv index of the video stream to decode, usually 0.
</ParamField>

<ParamField path="video_format" type="str | None">
  Format of the video stream, like "mp4", "mkv", etc.
</ParamField>

<ParamField path="num_threads" type="int" default="1">
  Number of threads to use for decoding.
</ParamField>

**Returns:**

A numpy array of shape (num_frames, height, width, channels) containing the decoded
frames in RGB24 format

**Raises:**

ValueError: If the sampled timestamps differ from source timestamps by more than
the specified tolerance


```python
nemo_curator.utils.decoder_utils.get_frame_count(
    data: pathlib.Path | str | typing.BinaryIO | bytes,
    stream_idx: int = 0,
    video_format: str | None = None
) -> int
```

Get the total number of frames in a video file or stream.

**Parameters:**

<ParamField path="data" type="pathlib.Path | str | typing.BinaryIO | bytes">
  An open file, io.BytesIO, or bytes object with the video data.
</ParamField>

<ParamField path="stream_idx" type="int" default="0">
  Index of the video stream to read from. Defaults to 0,
</ParamField>

<ParamField path="video_format" type="str | None">
  Format of the video stream, like "mp4", "mkv", etc.
</ParamField>

**Returns:**

The total number of frames in the video stream.


```python
nemo_curator.utils.decoder_utils.extract_frames(
    video: pathlib.Path | str | typing.BinaryIO | bytes,
    extraction_policy: nemo_curator.utils.decoder_utils.FrameExtractionPolicy,
    sample_rate_fps: float = 1.0,
    target_res: tuple[int, int] = (-1, -1),
    num_threads: int = 1,
    stream_idx: int = 0,
    video_format: str | None = None
) -> numpy.typing.NDArray[numpy.uint8]
```

Extract frames from a video into a numpy array.

**Parameters:**

<ParamField path="video" type="pathlib.Path | str | typing.BinaryIO | bytes">
  An open file, io.BytesIO, or bytes object with the video data.
</ParamField>

<ParamField path="extraction_policy" type="nemo_curator.utils.decoder_utils.FrameExtractionPolicy">
  The policy for extracting frames.
</ParamField>

<ParamField path="sample_rate_fps" type="float" default="1.0">
  Frame rate for sampling the video
</ParamField>

<ParamField path="target_res" type="tuple[int, int]" default="(-1, -1)">
  The target resolution for the frames.
</ParamField>

<ParamField path="stream_idx" type="int" default="0">
  PyAv index of the video stream to decode, usually 0.
</ParamField>

<ParamField path="video_format" type="str | None">
  Format of the video stream, like "mp4", "mkv", etc.
</ParamField>

<ParamField path="num_threads" type="int" default="1">
  Number of threads to use for decoding.
</ParamField>

**Returns:**

A numpy array of shape (num_frames, height, width, 3) containing the decoded
frames in RGB24 format

