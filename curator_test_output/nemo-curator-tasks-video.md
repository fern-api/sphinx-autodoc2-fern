---
layout: overview
slug: nemo-curator-tasks-video
---

# nemo_curator.tasks.video



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`_Window`](#nemo_curatortasksvideo_window) | Container for video window data including metadata, frames, and processing results. |
| [`Clip`](#nemo_curatortasksvideoclip) | Container for video clip data including metadata, frames, and processing results. |
| [`ClipStats`](#nemo_curatortasksvideoclipstats) | Statistics for video clips including filtering, transcoding, and captioning results. |
| [`VideoMetadata`](#nemo_curatortasksvideovideometadata) | Metadata for video content including dimensions, timing, and codec information. |
| [`Video`](#nemo_curatortasksvideovideo) | Container for video content including metadata, frames, and processing results. |
| [`VideoTask`](#nemo_curatortasksvideovideotask) | Task for processing a single video. |

### API

```python
class nemo_curator.tasks.video._Window
```

Container for video window data including metadata, frames, and processing results.

This class stores information about a video window, including its source, timing,
extracted frames, motion data, aesthetic scores, and generated captions.

```python
start_frame: int
```

**Value**: `None`


```python
end_frame: int
```

**Value**: `None`


```python
mp4_bytes: bytes | None
```

**Value**: `None`


```python
qwen_llm_input: dict[str, typing.Any] | None
```

**Value**: `None`


```python
x1_input: typing.Any | None
```

**Value**: `None`


```python
caption: dict[str, str]
```

**Value**: `field(...)`


```python
enhanced_caption: dict[str, str]
```

**Value**: `field(...)`


```python
webp_bytes: bytes | None
```

**Value**: `None`


```python
get_major_size() -> int
```

Calculate total memory size of the window.

**Returns:**

Total size in bytes.


```python
class nemo_curator.tasks.video.Clip
```

Container for video clip data including metadata, frames, and processing results.

This class stores information about a video segment, including its source, timing,
extracted frames, motion data, aesthetic scores, and generated captions.

```python
uuid: uuid.UUID
```

**Value**: `None`


```python
source_video: str
```

**Value**: `None`


```python
span: tuple[float, float]
```

**Value**: `None`


```python
buffer: bytes | None
```

**Value**: `None`


```python
extracted_frames: dict[str, numpy.typing.NDArray[numpy.uint8]]
```

**Value**: `field(...)`


```python
decoded_motion_data: None
```

**Value**: `None`


```python
motion_score_global_mean: float | None
```

**Value**: `None`


```python
motion_score_per_patch_min_256: float | None
```

**Value**: `None`


```python
aesthetic_score: float | None
```

**Value**: `None`


```python
cosmos_embed1_frames: numpy.typing.NDArray[numpy.float32] | None
```

**Value**: `None`


```python
cosmos_embed1_embedding: numpy.typing.NDArray[numpy.float32] | None
```

**Value**: `None`


```python
intern_video_2_frames: numpy.typing.NDArray[numpy.float32] | None
```

**Value**: `None`


```python
intern_video_2_embedding: numpy.typing.NDArray[numpy.float32] | None
```

**Value**: `None`


```python
windows: list[nemo_curator.tasks.video._Window]
```

**Value**: `field(...)`


```python
egomotion: dict[str, bytes]
```

**Value**: `field(...)`


```python
cosmos_embed1_text_match: tuple[str, float] | None
```

**Value**: `None`


```python
intern_video_2_text_match: tuple[str, float] | None
```

**Value**: `None`


```python
errors: dict[str, str]
```

**Value**: `field(...)`


```python
extract_metadata() -> dict[str, typing.Any] | None
```

Extract metadata from the clip's buffer.

**Returns:**

A dictionary containing the extracted metadata (width, height, framerate,
num_frames, video_codec, num_bytes) if buffer exists, None otherwise.

**Raises:**

Exception: Any exception from extract_video_metadata is propagated.


```python
duration: float
```

Calculate the duration of the clip.

**Returns:**

Duration of the clip in seconds.


```python
get_major_size() -> int
```

Calculate total memory size of the clip.

**Returns:**

Total size in bytes.


```python
class nemo_curator.tasks.video.ClipStats
```

Statistics for video clips including filtering, transcoding, and captioning results.

This class accumulates statistics about the number of clips processed through
different stages of the video processing pipeline, including motion filtering,
aesthetic filtering, and captioning.

```python
num_filtered_by_motion: int
```

**Value**: `0`


```python
num_filtered_by_aesthetic: int
```

**Value**: `0`


```python
num_passed: int
```

**Value**: `0`


```python
num_transcoded: int
```

**Value**: `0`


```python
num_with_embeddings: int
```

**Value**: `0`


```python
num_with_caption: int
```

**Value**: `0`


```python
num_with_webp: int
```

**Value**: `0`


```python
total_clip_duration: float
```

**Value**: `0.0`


```python
max_clip_duration: float
```

**Value**: `0.0`


```python
combine(other: nemo_curator.tasks.video.ClipStats) -> None
```

Combine two ClipStats objects.

**Parameters:**

<ParamField path="other" type="nemo_curator.tasks.video.ClipStats">
  ClipStats object to combine with.
</ParamField>


```python
class nemo_curator.tasks.video.VideoMetadata
```

Metadata for video content including dimensions, timing, and codec information.

This class stores essential video properties such as resolution, frame rate,
duration, and encoding details.

```python
size: int | None
```

**Value**: `None`


```python
height: int | None
```

**Value**: `None`


```python
width: int | None
```

**Value**: `None`


```python
framerate: float | None
```

**Value**: `None`


```python
num_frames: int | None
```

**Value**: `None`


```python
duration: float | None
```

**Value**: `None`


```python
video_codec: str | None
```

**Value**: `None`


```python
pixel_format: str | None
```

**Value**: `None`


```python
audio_codec: str | None
```

**Value**: `None`


```python
bit_rate_k: int | None
```

**Value**: `None`


```python
class nemo_curator.tasks.video.Video
```

Container for video content including metadata, frames, and processing results.

This class stores information about a video segment, including its source, timing,
extracted frames, motion data, aesthetic scores, and generated captions.

```python
input_video: pathlib.Path
```

**Value**: `None`


```python
source_bytes: bytes | None
```

**Value**: `None`


```python
metadata: nemo_curator.tasks.video.VideoMetadata
```

**Value**: `field(...)`


```python
frame_array: numpy.typing.NDArray[numpy.uint8] | None
```

**Value**: `None`


```python
clips: list[nemo_curator.tasks.video.Clip]
```

**Value**: `field(...)`


```python
filtered_clips: list[nemo_curator.tasks.video.Clip]
```

**Value**: `field(...)`


```python
num_total_clips: int
```

**Value**: `0`


```python
num_clip_chunks: int
```

**Value**: `0`


```python
clip_chunk_index: int
```

**Value**: `0`


```python
clip_stats: nemo_curator.tasks.video.ClipStats
```

**Value**: `field(...)`


```python
errors: dict[str, str]
```

**Value**: `field(...)`


```python
populate_metadata() -> None
```

Extract and assign video metadata from source_bytes.

This method extracts metadata from the video data in source_bytes and
assigns it to self.metadata.

**Raises:**

ValueError: If source_bytes is None.
Exception: Any exception from extract_video_metadata is propagated.


```python
fraction: float
```

Calculate the fraction of processed clips.

**Returns:**

Fraction of processed clips.


```python
weight: float
```

Calculate the weight of the video.

**Returns:**

Weight of the video.


```python
get_major_size() -> int
```

Calculate total memory size of the video.

**Returns:**

Total size in bytes.


```python
has_metadata() -> bool
```

Check if all metadata fields are present.

**Returns:**

True if all metadata fields are present, False otherwise.


```python
is_10_bit_color() -> bool | None
```

Heuristic function to determine if the input video has 10-bit color.


```python
input_path: str
```

Get the input path of the video.

**Returns:**

Input path of the video.


```python
class nemo_curator.tasks.video.VideoTask
```

**Bases**: `nemo_curator.tasks.tasks.Task[nemo_curator.tasks.video.Video]`

Task for processing a single video.

```python
data: nemo_curator.tasks.video.Video
```

**Value**: `field(...)`


```python
validate() -> bool
```

Validate the task data.


```python
num_items: int
```

Get the number of items in this task.

