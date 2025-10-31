---
layout: overview
slug: nemo-curator-stages-image-filters-base
---

# nemo_curator.stages.image.filters.base



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`BaseFilterStage`](#nemo_curatorstagesimagefiltersbasebasefilterstage) | Base class for image filtering stages. |

### Data

`__all__`

### API

```python
class nemo_curator.stages.image.filters.base.BaseFilterStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.ImageBatch, nemo_curator.tasks.ImageBatch]`

Base class for image filtering stages.

This class provides a base class for image filtering stages.

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
score_threshold: float
```

**Value**: `0.5`


```python
verbose: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `image_filter`


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
setup(_worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```

Initialize the base filter stage.


```python
yield_next_batch(task: nemo_curator.tasks.ImageBatch) -> collections.abc.Generator[list[nemo_curator.tasks.ImageObject], None, None]
```

Yields a generator of model inputs for the next batch.

**Parameters:**

**Returns:**

Generator[dict[str, torch.Tensor]]: A generator of model inputs for the next batch.


```python
process(task: nemo_curator.tasks.ImageBatch) -> nemo_curator.tasks.ImageBatch
```

Process an image batch to generate scores and filter by threshold.

**Parameters:**

<ParamField path="task" type="nemo_curator.tasks.ImageBatch">
  ImageBatch containing list of ImageObject instances with pre-computed embeddings
</ParamField>

**Returns:**

ImageBatch with filtered images that have scores below the threshold


```python
nemo_curator.stages.image.filters.base.__all__
```

**Value**: `['BaseFilterStage']`

