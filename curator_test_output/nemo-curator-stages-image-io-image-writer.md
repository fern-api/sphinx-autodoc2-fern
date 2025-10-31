---
layout: overview
slug: nemo-curator-stages-image-io-image-writer
---

# nemo_curator.stages.image.io.image_writer



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ImageWriterStage`](#nemo_curatorstagesimageioimage_writerimagewriterstage) | Write images to tar files and corresponding metadata to a Parquet file. |

### API

```python
class nemo_curator.stages.image.io.image_writer.ImageWriterStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.image.ImageBatch, nemo_curator.tasks.file_group.FileGroupTask]`

Write images to tar files and corresponding metadata to a Parquet file.

- Images are packed into tar archives with at most ``images_per_tar`` entries each.
- Metadata for all written images in the batch is stored in a single Parquet file.
- Tar filenames are unique across actors via an actor-scoped prefix.

```python
output_dir: str
```

**Value**: `None`


```python
images_per_tar: int
```

**Value**: `1000`


```python
verbose: bool
```

**Value**: `False`


```python
deterministic_name: bool
```

**Value**: `True`


```python
remove_image_data: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `image_writer`


```python
__post_init__() -> None
```


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
construct_base_name(task: nemo_curator.tasks.image.ImageBatch) -> str
```

Construct a base name for tar files within this actor.


```python
_encode_image_to_bytes(image: numpy.ndarray) -> tuple[bytes, str]
```

Encode image array to JPEG bytes; always returns (bytes, ".jpg").


```python
_write_tar(
    base_name: str, members: list[tuple[str, bytes]]
) -> str
```

Write a tar file with given (member_name, bytes) entries using provided base name.

Returns tar path.


```python
_write_parquet(
    base_name: str, rows: list[dict[str, typing.Any]]
) -> str
```

Write metadata rows to a Parquet file for a specific tar and return its path.

The Parquet file shares the same base name as the tar file: ``\{base_name\}.parquet``.


```python
process(task: nemo_curator.tasks.image.ImageBatch) -> nemo_curator.tasks.file_group.FileGroupTask
```

