---
layout: overview
slug: nemo-curator-stages-image-filters-aesthetic-filter
---

# nemo_curator.stages.image.filters.aesthetic_filter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ImageAestheticFilterStage`](#nemo_curatorstagesimagefiltersaesthetic_filterimageaestheticfilterstage) | Stage for filtering out images based on aesthetic scores. |

### API

```python
class nemo_curator.stages.image.filters.aesthetic_filter.ImageAestheticFilterStage
```

**Bases**: `nemo_curator.stages.image.filters.base.BaseFilterStage`

Stage for filtering out images based on aesthetic scores.

This class processes image batches through an aesthetic scoring model to generate
aesthetic scores for each image. Images with scores below the threshold will be filtered out.

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

**Value**: `image_aesthetic_filter`


```python
setup_on_node(
    _node_info: nemo_curator.backends.base.NodeInfo | None = None,
    _worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None
) -> None
```

Download aesthetic model weights from HF


```python
setup(_worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```

Initialize the aesthetic filtering model.


```python
process(task: nemo_curator.tasks.ImageBatch) -> nemo_curator.tasks.ImageBatch
```

Process an image batch to filter by aesthetic score threshold.

**Parameters:**

<ParamField path="task" type="nemo_curator.tasks.ImageBatch">
  ImageBatch containing list of ImageObject instances with aesthetic scores
</ParamField>

**Returns:**

ImageBatch with filtered images that meet the aesthetic score threshold.

