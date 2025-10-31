---
layout: overview
slug: nemo-curator-tasks-image
---

# nemo_curator.tasks.image



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ImageObject`](#nemo_curatortasksimageimageobject) | Represents a single image with metadata. |
| [`ImageBatch`](#nemo_curatortasksimageimagebatch) | Task for processing batches of images. Images are stored as a list of ImageObject instances, each containing the path to the image and associated metadata. |

### API

```python
class nemo_curator.tasks.image.ImageObject
```

Represents a single image with metadata.

Attributes:
    image_path: Path to the image file on disk
    image_id: Unique identifier for the image
    metadata: Additional metadata associated with the image
    image_data: Raw image pixel data as numpy array (H, W, C) in RGB format
    embedding: Image embedding vector as numpy array
    aesthetic_score: Aesthetic quality score as float
    nsfw_score: NSFW probability score as float

```python
image_path: str
```

**Value**: ``


```python
image_id: str
```

**Value**: ``


```python
metadata: dict[str, typing.Any]
```

**Value**: `field(...)`


```python
image_data: numpy.ndarray | None
```

**Value**: `None`


```python
embedding: numpy.ndarray | None
```

**Value**: `None`


```python
aesthetic_score: float | None
```

**Value**: `None`


```python
nsfw_score: float | None
```

**Value**: `None`


```python
class nemo_curator.tasks.image.ImageBatch
```

**Bases**: `nemo_curator.tasks.tasks.Task`

Task for processing batches of images.
Images are stored as a list of ImageObject instances, each containing
the path to the image and associated metadata.

```python
data: list[nemo_curator.tasks.image.ImageObject]
```

**Value**: `field(...)`


```python
validate() -> bool
```

Validate the task data.


```python
num_items: int
```

Number of images in this batch.

