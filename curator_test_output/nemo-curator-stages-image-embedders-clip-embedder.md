---
layout: overview
slug: nemo-curator-stages-image-embedders-clip-embedder
---

# nemo_curator.stages.image.embedders.clip_embedder



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ImageEmbeddingStage`](#nemo_curatorstagesimageembeddersclip_embedderimageembeddingstage) | Stage for generating image embeddings using CLIP model. |

### API

```python
class nemo_curator.stages.image.embedders.clip_embedder.ImageEmbeddingStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.ImageBatch, nemo_curator.tasks.ImageBatch]`

Stage for generating image embeddings using CLIP model.

This class processes image batches through a CLIP model to generate
embeddings for each image. It assumes image data is already loaded
in ImageObject.image_data and stores embeddings in ImageObject.embedding.

```python
model_dir: str
```

**Value**: `None`


```python
num_gpus_per_worker: float
```

**Value**: `0.25`


```python
model_inference_batch_size: int
```

**Value**: `32`


```python
verbose: bool
```

**Value**: `False`


```python
remove_image_data: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `image_embedding`


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
setup_on_node(
    node_info: nemo_curator.backends.base.NodeInfo,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata
) -> None
```

Download the weights for the CLIP model on the node.


```python
setup(_worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```

Initialize the CLIP image embedding model.


```python
yield_next_batch(task: nemo_curator.tasks.ImageBatch) -> collections.abc.Generator[nemo_curator.tasks.ImageBatch, None, None]
```

Yield batches of images from the task.

**Parameters:**

<ParamField path="task" type="nemo_curator.tasks.ImageBatch">
  ImageBatch containing list of ImageObject instances with pre-loaded image_data
</ParamField>

**Returns:**

Generator[dict[str, torch.Tensor]]: A generator of model inputs for the next batch.


```python
process(task: nemo_curator.tasks.ImageBatch) -> nemo_curator.tasks.ImageBatch
```

Process an image batch to generate embeddings.

**Parameters:**

<ParamField path="task" type="nemo_curator.tasks.ImageBatch">
  ImageBatch containing list of ImageObject instances with pre-loaded image_data
</ParamField>

**Returns:**

ImageBatch with embeddings stored in ImageObject.embedding

