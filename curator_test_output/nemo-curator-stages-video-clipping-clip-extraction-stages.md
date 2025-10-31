---
layout: overview
slug: nemo-curator-stages-video-clipping-clip-extraction-stages
---

# nemo_curator.stages.video.clipping.clip_extraction_stages



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ClipTranscodingStage`](#nemo_curatorstagesvideoclippingclip_extraction_stagescliptranscodingstage) | Stage that transcodes video clips into a standardized format. |
| [`FixedStrideExtractorStage`](#nemo_curatorstagesvideoclippingclip_extraction_stagesfixedstrideextractorstage) | Stage that extracts video clips using fixed-length intervals. |

### API

```python
class nemo_curator.stages.video.clipping.clip_extraction_stages.ClipTranscodingStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage that transcodes video clips into a standardized format.

This stage handles the conversion of video clips using FFmpeg, supporting both
software (libx264, libopenh264) and hardware (NVENC) encoding with configurable parameters.

**Parameters:**

- **num_cpus_per_worker**: Number of CPUs per worker.
- **encoder**: Video encoder to use.
- **encoder_threads**: Number of threads per encoder.
- **encode_batch_size**: Number of clips to encode in parallel.
- **nb_streams_per_gpu**: Number of streams per GPU.
- **use_hwaccel**: Whether to use hardware acceleration.
- **use_input_bit_rate**: Whether to use input video bit rate.
- **num_clips_per_chunk**: Number of clips per chunk. If the number of clips is larger than this, the clips will be split into chunks, and created VideoTasks for each chunk.
- **verbose**: Whether to print verbose logs.
- **ffmpeg_verbose**: Whether to print FFmpeg verbose logs.

```python
num_cpus_per_worker: float
```

**Value**: `6.0`


```python
encoder: str
```

**Value**: `libx264`


```python
encoder_threads: int
```

**Value**: `1`


```python
encode_batch_size: int
```

**Value**: `16`


```python
nb_streams_per_gpu: int
```

**Value**: `3`


```python
use_hwaccel: bool
```

**Value**: `False`


```python
use_input_bit_rate: bool
```

**Value**: `False`


```python
num_clips_per_chunk: int
```

**Value**: `32`


```python
ffmpeg_verbose: bool
```

**Value**: `False`


```python
verbose: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `clip_transcoding`


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

Post-initialization method called after all fields are set.


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
ray_stage_spec() -> dict[str, typing.Any]
```

Ray stage specification for this stage.


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
_extract_clips(
    working_dir: pathlib.Path,
    video_filename: str,
    *,
    force_pix_fmt: bool,
    use_bit_rate: str | None,
    clips: list[nemo_curator.tasks.video.Clip]
) -> None
```

Extract clips using ffmpeg.


```python
_build_ffmpeg_command(
    video_filename: str,
    clips: list[nemo_curator.tasks.video.Clip],
    force_pix_fmt: bool,
    use_bit_rate: str | None
) -> list[str]
```

Build the ffmpeg command for extracting clips.


```python
_add_decoder_threads(command: list[str]) -> None
```

Add decoder thread options to command.


```python
_add_hwaccel_options(command: list[str]) -> None
```

Add hardware acceleration options to command.


```python
_add_input_options(
    command: list[str],
    clip: nemo_curator.tasks.video.Clip,
    video_filename: str,
    index: int
) -> None
```

Add input options to command.


```python
_add_video_encoding_options(
    command: list[str],
    use_bit_rate: str | None,
    force_pix_fmt: bool
) -> None
```

Add video encoding options to command.


```python
_add_nvenc_options(
    command: list[str], force_pix_fmt: bool
) -> None
```

Add NVENC-specific encoding options.


```python
_add_output_options(
    command: list[str],
    clip: nemo_curator.tasks.video.Clip,
    index: int
) -> None
```

Add output options to command.


```python
_run_ffmpeg_command(
    command: list[str],
    working_dir: pathlib.Path,
    clips: list[nemo_curator.tasks.video.Clip]
) -> None
```

Run the ffmpeg command and handle errors.


```python
_handle_ffmpeg_error(
    error: subprocess.CalledProcessError,
    command: list[str],
    clips: list[nemo_curator.tasks.video.Clip]
) -> None
```

Handle ffmpeg command errors.


```python
_read_clips_to_memory(
    working_dir: pathlib.Path, clips: list[nemo_curator.tasks.video.Clip]
) -> None
```

Read extracted clips back into memory.


```python
class nemo_curator.stages.video.clipping.clip_extraction_stages.FixedStrideExtractorStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage that extracts video clips using fixed-length intervals.

This stage splits videos into clips of specified length and stride, ensuring
each clip meets minimum length requirements and optionally limiting total clips.

```python
clip_len_s: float
```

**Value**: `None`


```python
clip_stride_s: float
```

**Value**: `None`


```python
min_clip_length_s: float
```

**Value**: `None`


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

**Value**: `fixed_stride_extractor`


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```

