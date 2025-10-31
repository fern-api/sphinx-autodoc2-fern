---
layout: overview
slug: nemo-curator-stages-video-io-clip-writer
---

# nemo_curator.stages.video.io.clip_writer



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ClipWriterStage`](#nemo_curatorstagesvideoioclip_writerclipwriterstage) | Stage that writes clips and metadata for clip transcoding. |

### API

```python
class nemo_curator.stages.video.io.clip_writer.ClipWriterStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage that writes clips and metadata for clip transcoding.

This class processes video clips through a series of steps including embedding generation,
metadata extraction, and writing to storage.

```python
output_path: str
```

**Value**: `None`


```python
input_path: str
```

**Value**: `None`


```python
upload_clips: bool
```

**Value**: `None`


```python
dry_run: bool
```

**Value**: `None`


```python
generate_embeddings: bool
```

**Value**: `None`


```python
generate_previews: bool
```

**Value**: `None`


```python
generate_captions: bool
```

**Value**: `None`


```python
embedding_algorithm: str
```

**Value**: `cosmos-embed1`


```python
caption_models: list[str] | None
```

**Value**: `None`


```python
enhanced_caption_models: list[str] | None
```

**Value**: `None`


```python
verbose: bool
```

**Value**: `False`


```python
max_workers: int
```

**Value**: `6`


```python
log_stats: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `clip_writer`


```python
__post_init__()
```


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
_get_output_path(
    output_path: str, extra: str
) -> str
```


```python
get_output_path_processed_videos(output_path: str) -> str
```

Get path to store processed videos.


```python
get_output_path_processed_clip_chunks(output_path: str) -> str
```

Get path to store processed clip chunks.


```python
get_output_path_clips(
    output_path: str,
    *,
    filtered: bool = False
) -> str
```

Get path to store generated clips.


```python
get_output_path_previews(output_path: str) -> str
```

Get path to store generated clips.


```python
get_output_path_metas(
    output_path: str, version: str
) -> str
```

Get path to store clip metadatas.


```python
get_output_path_iv2_embd(output_path: str) -> str
```

Get path to store generated clips.


```python
get_output_path_iv2_embd_parquet(output_path: str) -> str
```

Get path to store generated clip embeddings in a parquet file.


```python
get_output_path_ce1_embd(output_path: str) -> str
```

Get path to store generated clip embeddings of Cosmos-Embed1.


```python
get_output_path_ce1_embd_parquet(output_path: str) -> str
```

Get path to store generated clip embeddings of Cosmos-Embed1 in a parquet file.


```python
calculate_sha256(buffer: bytes) -> str
```

Get sha256 of byte array.


```python
_write_data(
    buffer: bytes,
    dest: pathlib.Path,
    desc: str,
    source_video: str
) -> None
```


```python
_write_json_data(
    data: dict,
    dest: pathlib.Path,
    desc: str,
    source_video: str
) -> None
```


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
_write_clip_embedding_to_buffer(clip: nemo_curator.tasks.video.Clip) -> nemo_curator.tasks.video.ClipStats
```


```python
_write_video_embeddings_to_parquet(video: nemo_curator.tasks.video.Video) -> None
```


```python
_get_window_uri(
    video_span_uuid: uuid.UUID,
    window: tuple[int, int],
    path_prefix: str,
    file_type: str
) -> pathlib.Path
```


```python
_get_clip_uri(
    video_span_uuid: uuid.UUID,
    path_prefix: str,
    file_type: str
) -> pathlib.Path
```


```python
_get_video_uri(input_video_path: str) -> pathlib.Path
```


```python
_get_clip_chunk_uri(
    input_video_path: str, idx: int
) -> pathlib.Path
```


```python
_write_clip_window_webp(clip: nemo_curator.tasks.video.Clip) -> nemo_curator.tasks.video.ClipStats
```


```python
_write_clip_mp4(
    clip: nemo_curator.tasks.video.Clip,
    *,
    filtered: bool = False
) -> nemo_curator.tasks.video.ClipStats
```


```python
_write_clip_embedding(clip: nemo_curator.tasks.video.Clip) -> nemo_curator.tasks.video.ClipStats
```


```python
_write_clip_metadata(
    clip: nemo_curator.tasks.video.Clip,
    video_metadata: nemo_curator.tasks.video.VideoMetadata,
    *,
    filtered: bool = False
) -> nemo_curator.tasks.video.ClipStats
```


```python
_write_video_metadata(video: nemo_curator.tasks.video.Video) -> None
```

