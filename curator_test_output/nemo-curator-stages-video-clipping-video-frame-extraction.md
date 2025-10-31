---
layout: overview
slug: nemo-curator-stages-video-clipping-video-frame-extraction
---

# nemo_curator.stages.video.clipping.video_frame_extraction



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`VideoFrameExtractionStage`](#nemo_curatorstagesvideoclippingvideo_frame_extractionvideoframeextractionstage) | Stage that extracts frames from videos into numpy arrays. |

### Functions

| Name | Description |
|------|-------------|
| [`get_frames_from_ffmpeg`](#nemo_curatorstagesvideoclippingvideo_frame_extractionget_frames_from_ffmpeg) | Fetch resized frames for video. |

### API

```python
nemo_curator.stages.video.clipping.video_frame_extraction.get_frames_from_ffmpeg(
    video_file: pathlib.Path,
    width: int,
    height: int,
    *,
    use_gpu: bool = False
) -> numpy.typing.NDArray[numpy.uint8] | None
```

Fetch resized frames for video.


```python
class nemo_curator.stages.video.clipping.video_frame_extraction.VideoFrameExtractionStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage that extracts frames from videos into numpy arrays.

This stage handles video frame extraction using either FFmpeg (CPU/GPU) or PyNvCodec,
converting video content into standardized frame arrays for downstream processing.

```python
output_hw: tuple[int, int]
```

**Value**: `(27, 48)`


```python
pyncv_batch_size: int
```

**Value**: `64`


```python
decoder_mode: str
```

**Value**: `pynvc`


```python
verbose: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `video_frame_extraction`


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
setup(worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```

Setup method called once before processing begins.
Override this method to perform any initialization that should
happen once per worker.

**Parameters:**


```python
__post_init__() -> None
```


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```

