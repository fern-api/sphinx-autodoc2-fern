---
layout: overview
slug: nemo-curator-stages-image-io-image-reader
---

# nemo_curator.stages.image.io.image_reader



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ImageReaderStage`](#nemo_curatorstagesimageioimage_readerimagereaderstage) | DALI-based reader that loads images from WebDataset tar shards. |

### API

```python
class nemo_curator.stages.image.io.image_reader.ImageReaderStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks.ImageBatch]`

DALI-based reader that loads images from WebDataset tar shards.

Works with DALI GPU (CUDA) or DALI CPU; decodes on GPU if CUDA is available,
otherwise falls back to CPU decoding.

```python
task_batch_size: int
```

**Value**: `100`


```python
verbose: bool
```

**Value**: `True`


```python
num_threads: int
```

**Value**: `8`


```python
num_gpus_per_worker: float
```

**Value**: `0.25`


```python
_name: str
```

**Value**: `image_reader`


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
_create_dali_pipeline(tar_paths: list[str]) -> object
```


```python
_read_tars_with_dali(tar_paths: list[pathlib.Path]) -> collections.abc.Generator[list[nemo_curator.tasks.ImageObject], None, None]
```

Yield lists of ImageObject per DALI run over one or more tar files.


```python
_stream_batches(tar_files: list[pathlib.Path]) -> collections.abc.Generator[nemo_curator.tasks.ImageBatch, None, None]
```

Emit one ImageBatch per DALI run across all provided tar files.


```python
process(task: nemo_curator.tasks.FileGroupTask) -> list[nemo_curator.tasks.ImageBatch]
```

