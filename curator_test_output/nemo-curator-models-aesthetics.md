---
layout: overview
slug: nemo-curator-models-aesthetics
---

# nemo_curator.models.aesthetics



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`MLP`](#nemo_curatormodelsaestheticsmlp) | Multi-layer perceptron. |
| [`AestheticScorer`](#nemo_curatormodelsaestheticsaestheticscorer) | Public interface for aesthetic scoring of video embeddings. |

### Data

`_AESTHETICS_MODEL_ID`
`_AESTHETICS_MODEL_REVISION`

### API

```python
nemo_curator.models.aesthetics._AESTHETICS_MODEL_ID
```

**Value**: `ttj/sac-logos-ava1-l14-linearMSE`


```python
nemo_curator.models.aesthetics._AESTHETICS_MODEL_REVISION
```

**Value**: `1e77fa0`


```python
class nemo_curator.models.aesthetics.MLP
```

**Bases**: `torch.nn.Module`

Multi-layer perceptron.

A neural network that processes embeddings to predict aesthetic scores.

### Initialization

Initialize the MLP.

**Parameters:**

  None


```python
forward(embed: torch.Tensor) -> torch.Tensor
```

Forward pass through the MLP.

**Parameters:**

<ParamField path="embed" type="torch.Tensor">
  Input embeddings tensor.
</ParamField>

**Returns:**

Predicted aesthetic scores.


```python
class nemo_curator.models.aesthetics.AestheticScorer(model_dir: str)
```

**Bases**: `nemo_curator.models.base.ModelInterface`

Public interface for aesthetic scoring of video embeddings.

This class provides a standardized interface for scoring the aesthetic quality
of video embeddings using a pre-trained model.

### Initialization

Initialize the aesthetic scorer interface.


```python
model_id_names: list[str]
```

Get the model ID names associated with this aesthetic scorer.

**Returns:**

A list containing the model ID for aesthetics scoring.


```python
setup() -> None
```

Set up the aesthetic scoring model by loading weights.


```python
get_weights_path() -> str
```

Get the path to the weights for the aesthetic scorer.


```python
__call__(embeddings: torch.Tensor | numpy.typing.NDArray[numpy.float32]) -> torch.Tensor
```

Score the aesthetics of input embeddings.

**Parameters:**

<ParamField path="embeddings" type="torch.Tensor | numpy.typing.NDArray[numpy.float32]">
  Input embeddings as either a torch tensor or numpy array.
</ParamField>

**Returns:**

Aesthetic scores for each input embedding.


```python
download_weights_on_node(model_dir: str) -> None
```

Download the weights for the aesthetic scorer on the node.

