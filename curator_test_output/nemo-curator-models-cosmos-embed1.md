---
layout: overview
slug: nemo-curator-models-cosmos-embed1
---

# nemo_curator.models.cosmos_embed1



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CosmosEmbed1`](#nemo_curatormodelscosmos_embed1cosmosembed1) | Cosmos-Embed1 embedding model. |

### Data

`_COSMOS_EMBED1_VARIANTS_INFO`
`COSMOS_EMBED1_MODEL_REVISION_INFO`

### API

```python
nemo_curator.models.cosmos_embed1._COSMOS_EMBED1_VARIANTS_INFO: typing.Final
```

**Value**: `None`


```python
nemo_curator.models.cosmos_embed1.COSMOS_EMBED1_MODEL_REVISION_INFO: typing.Final
```

**Value**: `None`


```python
class nemo_curator.models.cosmos_embed1.CosmosEmbed1(*, variant: typing.Literal[224p, 336p, 448p] = '336p', utils_only: bool = False, model_dir: str | None = None)
```

**Bases**: `nemo_curator.models.base.ModelInterface`

Cosmos-Embed1 embedding model.

### Initialization

Initialize Cosmos-Embed1 model.

**Parameters:**

- **variant**: Choose from "224p", "336p", "448p".
- **utils_only**: Whether to only initialize utility functions.


```python
model_id_names: list[str]
```

Get the model ID names.

**Returns:**

A list of model ID names.


```python
setup() -> None
```

Set up the Cosmos-Embed1 model.

This method initializes the model and its configuration for processing video and text data.


```python
get_target_num_frames() -> int
```

Get the target number of frames for the model.

**Returns:**

The target number of frames.


```python
formulate_input_frames(frames: list[numpy.typing.NDArray[numpy.uint8]]) -> numpy.typing.NDArray[numpy.float32] | None
```

Formulate input frames for the model.

**Parameters:**

<ParamField path="frames" type="list[numpy.typing.NDArray[numpy.uint8]]">
  List of video frames.
</ParamField>

**Returns:**

The formulated input frames.


```python
encode_video_frames(frames: numpy.typing.NDArray[numpy.float32]) -> torch.Tensor
```

Encode video frames for the model.

**Parameters:**

<ParamField path="frames" type="numpy.typing.NDArray[numpy.float32]">
  The input video frames.
</ParamField>

**Returns:**

The encoded video frames.


```python
get_text_embedding(text: str) -> torch.Tensor
```

Get the text embedding for the given text.

**Parameters:**

<ParamField path="text" type="str">
  The input text.
</ParamField>

**Returns:**

The text embedding.


```python
evaluate(
    video_embd: torch.Tensor, text_embds: list[torch.Tensor]
) -> tuple[list[float], list[int]]
```

Evaluate the model.

**Parameters:**

<ParamField path="video_embd" type="torch.Tensor">
  The video embedding.
</ParamField>

<ParamField path="text_embds" type="list[torch.Tensor]">
  The text embeddings.
</ParamField>

**Returns:**

The predicted probabilities and indices.


```python
download_weights_on_node(
    model_dir: str, variant: typing.Literal[224p, 336p, 448p] = '336p'
) -> None
```

Download the weights for the CosmosEmbed1 model on the node.


```python
download_processor_config_on_node(
    model_dir: str, variant: typing.Literal[224p, 336p, 448p] = '336p'
) -> None
```

Download the processor config for the CosmosEmbed1 model on the node.

