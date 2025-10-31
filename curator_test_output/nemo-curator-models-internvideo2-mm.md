---
layout: overview
slug: nemo-curator-models-internvideo2-mm
---

# nemo_curator.models.internvideo2_mm



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`_InternVideo2Stage2Wrapper`](#nemo_curatormodelsinternvideo2_mm_internvideo2stage2wrapper) | Wrapper class for InternVideo2 model that inherits from the original implementation. |
| [`InternVideo2MultiModality`](#nemo_curatormodelsinternvideo2_mminternvideo2multimodality) | Actual outside-facing model using the wrapper class. |

### Functions

| Name | Description |
|------|-------------|
| [`_create_config`](#nemo_curatormodelsinternvideo2_mm_create_config) | Create model config. |
| [`_setup_internvideo2`](#nemo_curatormodelsinternvideo2_mm_setup_internvideo2) | Set up internvideo2 model. |

### Data

`_MODEL_CONFIG_PATH`
`_BERT_CONFIG_PATH`
`INTERNVIDEO2_MODEL_ID`
`INTERNVIDEO2_MODEL_FILE`
`INTERNVIDEO2_MODEL_REVISION`
`BERT_MODEL_ID`
`BERT_MODEL_REVISION`

### API

```python
nemo_curator.models.internvideo2_mm._MODEL_CONFIG_PATH
```

**Value**: `None`


```python
nemo_curator.models.internvideo2_mm._BERT_CONFIG_PATH
```

**Value**: `None`


```python
nemo_curator.models.internvideo2_mm.INTERNVIDEO2_MODEL_ID: typing.Final
```

**Value**: `OpenGVLab/InternVideo2-Stage2_1B-224p-f4`


```python
nemo_curator.models.internvideo2_mm.INTERNVIDEO2_MODEL_FILE: typing.Final
```

**Value**: `InternVideo2-stage2_1b-224p-f4.pt`


```python
nemo_curator.models.internvideo2_mm.INTERNVIDEO2_MODEL_REVISION: typing.Final
```

**Value**: `4362e1f`


```python
nemo_curator.models.internvideo2_mm.BERT_MODEL_ID: typing.Final
```

**Value**: `google-bert/bert-large-uncased`


```python
nemo_curator.models.internvideo2_mm.BERT_MODEL_REVISION: typing.Final
```

**Value**: `6da4b6a`


```python
class nemo_curator.models.internvideo2_mm._InternVideo2Stage2Wrapper(config: easydict.EasyDict, tokenizer: transformers.PreTrainedTokenizer, *, is_pretrain: bool = True)
```

**Bases**: `internvideo2_multi_modality.InternVideo2_Stage2_visual`

Wrapper class for InternVideo2 model that inherits from the original implementation.

This wrapper extends the original InternVideo2_Stage2_visual class and overrides
only the methods needed for inference, while keeping all the original functionality
intact.

```python
encode_vision(image: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]
```

Encode image / videos as features for inference.

Overrides the parent method to return only the basic features needed for inference,
without the complex teacher-student outputs.

**Parameters:**


```python
get_vid_feat(frames: torch.Tensor) -> torch.Tensor
```

Get the video features for the given frames.

**Parameters:**

**Returns:**

torch.Tensor: the output features. Shape: [B,N,C].


```python
get_txt_feat(text: str) -> torch.Tensor
```

Get the text features for the given text.

**Parameters:**

**Returns:**

torch.Tensor: the output features. Shape: [B,N,C].


```python
predict_label(
    vid_feat: torch.Tensor,
    txt_feat: torch.Tensor,
    top: int = 5
) -> tuple[torch.Tensor, torch.Tensor]
```

Predict labels based on video and text features.

**Parameters:**

<ParamField path="vid_feat" type="torch.Tensor">
  Video features
</ParamField>

<ParamField path="txt_feat" type="torch.Tensor">
  Text features
</ParamField>

<ParamField path="top" type="int" default="5">
  Number of top predictions to return
</ParamField>

**Returns:**

Tuple of (probabilities, indices)


```python
nemo_curator.models.internvideo2_mm._create_config(
    model_pt: str, bert_path: str
) -> easydict.EasyDict
```

Create model config.

**Parameters:**

**Returns:**

EasyDict: The model config.


```python
nemo_curator.models.internvideo2_mm._setup_internvideo2(config: easydict.EasyDict) -> nemo_curator.models.internvideo2_mm._InternVideo2Stage2Wrapper
```

Set up internvideo2 model.

**Parameters:**

**Returns:**

_InternVideo2Stage2Wrapper: The InternVideo2 Stage2 model wrapper.


```python
class nemo_curator.models.internvideo2_mm.InternVideo2MultiModality(model_dir: str, utils_only: bool = False)
```

**Bases**: `nemo_curator.models.base.ModelInterface`

Actual outside-facing model using the wrapper class.

### Initialization

Initialize the InternVideo2MultiModality model.

**Parameters:**

- **utils_only**: Whether to only initialize utility functions.


```python
model_id_names() -> list[str]
```


```python
setup() -> None
```

Set up the InternVideo2MultiModality model.

This method initializes the model and its configuration for video and text processing.
It also sets up the normalization parameters for video frames.


```python
_normalize(data: numpy.typing.NDArray[numpy.uint8]) -> numpy.typing.NDArray[numpy.float32]
```


```python
_construct_frames(
    vid_list: list[numpy.typing.NDArray[numpy.uint8]],
    fnum: int = 8,
    target_size: tuple[int, int] = (224, 224)
) -> numpy.typing.NDArray[numpy.float32]
```


```python
get_target_num_frames() -> int
```

Get the target number of frames for the model.

**Returns:**

The target number of frames.


```python
formulate_input_frames(frames: list[numpy.typing.NDArray[numpy.uint8]]) -> numpy.typing.NDArray[numpy.float32]
```

Formulate input frames for the model.

**Parameters:**

<ParamField path="frames" type="list[numpy.typing.NDArray[numpy.uint8]]">
  List of video frames.
</ParamField>

**Returns:**

The formulated input frames.


```python
encode_video_frames(iv2_frames: numpy.typing.NDArray[numpy.float32]) -> torch.Tensor
```

Encode video frames for the model.

**Parameters:**

<ParamField path="iv2_frames" type="numpy.typing.NDArray[numpy.float32]">
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
download_weights_on_node(model_dir: str) -> None
```

Download the weights for the InternVideo2 model on the node.

