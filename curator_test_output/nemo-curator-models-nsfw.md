---
layout: overview
slug: nemo-curator-models-nsfw
---

# nemo_curator.models.nsfw



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Normalization`](#nemo_curatormodelsnsfwnormalization) | Normalization layer for NSFW model. |
| [`NSFWModel`](#nemo_curatormodelsnsfwnsfwmodel) | NSFW detection model. |
| [`NSFWScorer`](#nemo_curatormodelsnsfwnsfwscorer) | Public interface for NSFW scoring of image embeddings. |

### Data

`_NSFW_MODEL_ID`
`_URL_MAPPING`

### API

```python
nemo_curator.models.nsfw._NSFW_MODEL_ID
```

**Value**: `laion/clip-autokeras-binary-nsfw`


```python
nemo_curator.models.nsfw._URL_MAPPING
```

**Value**: `None`


```python
class nemo_curator.models.nsfw.Normalization(shape: list[int])
```

**Bases**: `torch.nn.Module`

Normalization layer for NSFW model.

Applies normalization to input tensors using pre-computed mean and variance.

### Initialization

Initialize the normalization layer.

**Parameters:**

- **shape**: Shape of the normalization parameters.


```python
forward(x: torch.Tensor) -> torch.Tensor
```

Apply normalization to input tensor.

**Parameters:**

<ParamField path="x" type="torch.Tensor">
  Input tensor to normalize.
</ParamField>

**Returns:**

Normalized tensor.


```python
class nemo_curator.models.nsfw.NSFWModel
```

**Bases**: `torch.nn.Module`

NSFW detection model.

A neural network that processes CLIP embeddings to predict NSFW scores.
Based on LAION's CLIP-based-NSFW-Detector.

### Initialization

Initialize the NSFW model.

**Parameters:**

  None


```python
forward(x: torch.Tensor) -> torch.Tensor
```

Forward pass through the NSFW model.

**Parameters:**

<ParamField path="x" type="torch.Tensor">
  Input embeddings tensor.
</ParamField>

**Returns:**

NSFW probability scores.


```python
class nemo_curator.models.nsfw.NSFWScorer(model_dir: str)
```

**Bases**: `nemo_curator.models.base.ModelInterface`

Public interface for NSFW scoring of image embeddings.

This class provides a standardized interface for scoring the likelihood
of images containing sexually explicit material using a pre-trained model.

### Initialization

Initialize the NSFW scorer interface.


```python
conda_env_name: str
```

Get the name of the conda environment required for this model.

**Returns:**

Name of the conda environment.


```python
model_id_names: list[str]
```

Get the model ID names associated with this NSFW scorer.

**Returns:**

A list containing the model ID for NSFW scoring.


```python
download_weights_on_node(model_dir: str) -> None
```

Download NSFW model weights from LAION repository.

**Parameters:**

<ParamField path="model_dir" type="str">
  Directory to download the weights to.
</ParamField>


```python
setup() -> None
```

Set up the NSFW scoring model by loading weights.


```python
__call__(embeddings: torch.Tensor | numpy.typing.NDArray[numpy.float32]) -> torch.Tensor
```

Score the NSFW likelihood of input embeddings.

**Parameters:**

<ParamField path="embeddings" type="torch.Tensor | numpy.typing.NDArray[numpy.float32]">
  Input embeddings as either a torch tensor or numpy array.
</ParamField>

**Returns:**

NSFW probability scores for each input embedding.

