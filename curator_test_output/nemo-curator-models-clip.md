---
layout: overview
slug: nemo-curator-models-clip
---

# nemo_curator.models.clip



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CLIPImageEmbeddings`](#nemo_curatormodelsclipclipimageembeddings) | Interface for generating CLIP image embeddings from input images. |
| [`CLIPAestheticScorer`](#nemo_curatormodelsclipclipaestheticscorer) | A model that chains CLIPImageEmbeddings and AestheticScorer models. |

### Data

`_CLIP_MODEL_ID`
`_CLIP_MODEL_REVISION`

### API

```python
nemo_curator.models.clip._CLIP_MODEL_ID: typing.Final
```

**Value**: `openai/clip-vit-large-patch14`


```python
nemo_curator.models.clip._CLIP_MODEL_REVISION: typing.Final
```

**Value**: `32bd642`


```python
class nemo_curator.models.clip.CLIPImageEmbeddings(model_dir: str)
```

**Bases**: `nemo_curator.models.base.ModelInterface`

Interface for generating CLIP image embeddings from input images.

### Initialization

Initialize the CLIPImageEmbeddings model.


```python
model_id_names: list[str]
```

Get the model ID names.

**Returns:**

A list of model IDs used by this model.


```python
setup() -> None
```

Set up the CLIPImageEmbeddings model.


```python
__call__(images: torch.Tensor | numpy.typing.NDArray[numpy.uint8] | list[numpy.ndarray]) -> torch.Tensor
```

Call the CLIPImageEmbeddings model.

**Parameters:**

<ParamField path="images" type="torch.Tensor | numpy.typing.NDArray[numpy.uint8] | list[numpy.ndarray]">
  The images to embed.
</ParamField>

**Returns:**

The embeddings.


```python
download_weights_on_node(model_dir: str) -> None
```

Download the weights for the CLIPImageEmbeddings model on the node.


```python
class nemo_curator.models.clip.CLIPAestheticScorer(model_dir: str)
```

**Bases**: `nemo_curator.models.base.ModelInterface`

A model that chains CLIPImageEmbeddings and AestheticScorer models.

### Initialization

Initialize the CLIPAestheticScorer model.


```python
model_id_names: list[str]
```

Get the model ID names.

**Returns:**

A list of model IDs used by this model.


```python
setup() -> None
```

Set up the CLIPAestheticScorer model.


```python
__call__(images: torch.Tensor | numpy.typing.NDArray[numpy.uint8]) -> torch.Tensor
```

Call the CLIPAestheticScorer model.

**Parameters:**

<ParamField path="images" type="torch.Tensor | numpy.typing.NDArray[numpy.uint8]">
  The images to score.
</ParamField>

**Returns:**

The scores.


```python
download_weights_on_node(model_dir: str) -> None
```

Download the weights for the CLIPAestheticScorer model on the node.

