---
layout: overview
slug: nemo-curator-stages-video-io-video-reader
---

# nemo_curator.stages.video.io.video_reader



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`VideoReaderStage`](#nemo_curatorstagesvideoiovideo_readervideoreaderstage) | Stage that reads video files from local filesystem and extracts metadata. |
| [`VideoReader`](#nemo_curatorstagesvideoiovideo_readervideoreader) | Composite stage that reads video files from storage and downloads/processes them. |

### API

```python
class nemo_curator.stages.video.io.video_reader.VideoReaderStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.file_group.FileGroupTask, nemo_curator.tasks.video.VideoTask]`

Stage that reads video files from local filesystem and extracts metadata.

This stage processes video files by reading their binary content from the local
filesystem and extracting comprehensive metadata including dimensions, frame rate,
duration, codecs, and other technical properties. The stage handles both the file
I/O operations and metadata extraction, storing results in the VideoTask.

The stage performs the following operations:
1. Reads video file bytes from the local filesystem
2. Extracts technical metadata using video analysis tools
3. Validates metadata completeness and logs warnings for missing fields
4. Optionally logs detailed video information when verbose mode is enabled

**Parameters:**

- **verbose**: If True, logs detailed video information after successful processing

```python
input_path: str | None
```

**Value**: `None`


```python
verbose: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `video_reader`


```python
inputs() -> tuple[list[str], list[str]]
```

Define the input attributes required by this stage.

**Returns:**

Tuple of (top_level_attrs, data_attrs) where:
- top_level_attrs: ["data"] - requires VideoTask.data to be populated


```python
outputs() -> tuple[list[str], list[str]]
```

Define the output attributes produced by this stage.

**Returns:**

Tuple of (top_level_attrs, data_attrs) where:
- top_level_attrs: ["data"] - populates VideoTask.data
- data_attrs: ["source_bytes", "metadata"] - populates Video.source_bytes and Video.metadata


```python
process(task: nemo_curator.tasks.file_group.FileGroupTask) -> nemo_curator.tasks.video.VideoTask
```

Process a video task by reading file bytes and extracting metadata.

Performs the complete video processing workflow including reading the video
file from disk, extracting technical metadata, and optionally logging
detailed information. Returns the same task with populated data.

**Parameters:**

<ParamField path="task" type="nemo_curator.tasks.file_group.FileGroupTask">
  VideoTask containing a Video object with input_video path set.
</ParamField>

**Returns:**

The same VideoTask with video.source_bytes and video.metadata populated.
If errors occur, the task is returned with error information stored.


```python
_download_video_bytes(video: nemo_curator.tasks.video.Video) -> bool
```

Read video file bytes from the local filesystem.

Reads the complete binary content of the video file and stores it in the
video.source_bytes attribute. Handles file I/O errors gracefully and logs
appropriate error messages.

**Parameters:**

<ParamField path="video" type="nemo_curator.tasks.video.Video">
  Video object containing the input_video path to read from.
</ParamField>

**Returns:**

True if file reading was successful, False if an error occurred.
<Note>  </Note>
Errors are logged and stored in video.errors["download"] for debugging.


```python
_extract_and_validate_metadata(video: nemo_curator.tasks.video.Video) -> bool
```

Extract comprehensive metadata from video file and validate completeness.

Uses video analysis tools to extract technical metadata including dimensions,
frame rate, duration, codecs, bit rate, and other properties. Logs warnings
for critical missing metadata fields like codec and pixel format.

**Parameters:**

<ParamField path="video" type="nemo_curator.tasks.video.Video">
  Video object with source_bytes populated for metadata extraction.
</ParamField>

**Returns:**

True if metadata extraction completed successfully, False if extraction
failed due to corrupted file or unsupported format.
<Note>  </Note>
Warnings are logged for missing critical fields, but the method may still
return True if partial metadata was extracted successfully.


```python
_log_video_info(video: nemo_curator.tasks.video.Video) -> None
```

Log comprehensive video information after successful processing.

Outputs detailed information about the processed video including file size,
resolution, frame rate, duration, weight, and bit rate. This method is only
called when verbose mode is enabled.

**Parameters:**

<ParamField path="video" type="nemo_curator.tasks.video.Video">
  Video object with populated metadata fields.
</ParamField>


```python
_format_metadata_for_logging(video: nemo_curator.tasks.video.Video) -> dict[str, str]
```

Format video metadata into human-readable strings for logging output.

Converts raw metadata values into formatted strings with appropriate units
and handles None values gracefully by substituting "unknown" placeholders.
Used by _log_video_info for consistent log formatting.

**Parameters:**

<ParamField path="video" type="nemo_curator.tasks.video.Video">
  Video object with populated metadata fields.
</ParamField>

**Returns:**

Dictionary mapping metadata field names to formatted string values,
including size (bytes), resolution, fps, duration (minutes), weight,
and bit rate (Kbps).


```python
class nemo_curator.stages.video.io.video_reader.VideoReader
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks._EmptyTask, nemo_curator.tasks.video.VideoTask]`

Composite stage that reads video files from storage and downloads/processes them.

This stage combines FilePartitioningStage and VideoReaderStage into a single
high-level operation for reading video files from a directory and processing
them with metadata extraction.

**Parameters:**

- **input_video_path**: Path to the directory containing video files
- **video_limit**: Maximum number of videos to process (None for unlimited)
- **verbose**: Whether to enable verbose logging during download/processing

```python
input_video_path: str
```

**Value**: `None`


```python
video_limit: int | None
```

**Value**: `None`


```python
verbose: bool
```

**Value**: `False`


```python
__post_init__()
```

Initialize the parent CompositeStage after dataclass initialization.


```python
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

Decompose into constituent execution stages.

**Returns:**

List of processing stages: [FilePartitioningStage, VideoReaderStage]


```python
get_description() -> str
```

Get a description of what this composite stage does.

