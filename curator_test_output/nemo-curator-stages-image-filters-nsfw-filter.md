---
layout: overview
slug: nemo-curator-stages-image-filters-nsfw-filter
---

# nemo_curator.stages.image.filters.nsfw_filter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ImageNSFWFilterStage`](#nemo_curatorstagesimagefiltersnsfw_filterimagensfwfilterstage) | Stage for filtering out NSFW images using NSFWScorer model. |

### Data

`__all__`

### API

```python
class nemo_curator.stages.image.filters.nsfw_filter.ImageNSFWFilterStage
```

**Bases**: `nemo_curator.stages.image.filters.base.BaseFilterStage`

Stage for filtering out NSFW images using NSFWScorer model.

This class processes image batches through an NSFW scoring model to generate
NSFW probability scores for each image. Images with scores above the threshold
will be filtered out as NSFW content.

```python
weights_path: str
```

**Value**: `None`


```python
_name: str
```

**Value**: `image_nsfw_filter`


```python
setup_on_node(
    _node_info: nemo_curator.backends.base.NodeInfo | None = None,
    _worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None
) -> None
```

Download NSFW model weights from LAION repository.


```python
setup(_worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```

Initialize the NSFW filtering model.


```python
process(task: nemo_curator.tasks.ImageBatch) -> nemo_curator.tasks.ImageBatch
```

Process an image batch to generate NSFW scores and filter by threshold.

**Parameters:**

<ParamField path="task" type="nemo_curator.tasks.ImageBatch">
  ImageBatch containing list of ImageObject instances with pre-computed embeddings
</ParamField>

**Returns:**

ImageBatch with filtered images that have NSFW scores below the threshold


```python
nemo_curator.stages.image.filters.nsfw_filter.__all__
```

**Value**: `['ImageNSFWFilterStage']`

