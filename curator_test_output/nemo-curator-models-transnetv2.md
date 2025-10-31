---
layout: overview
slug: nemo-curator-models-transnetv2
---

# nemo_curator.models.transnetv2

Model for fast shot transition detection.

@article{soucek2020transnetv2,
    title={TransNet V2: An effective deep network architecture for fast shot transition detection},
    author={Sou{\v{c}}ek, Tom{\'a}{\v{s}} and Loko{\v{c}}, Jakub},
    year={2020},
    journal={arXiv preprint arXiv:2008.04838},
}

## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`_TransNetV2`](#nemo_curatormodelstransnetv2_transnetv2) | None |
| [`StackedDDCNNV2`](#nemo_curatormodelstransnetv2stackedddcnnv2) | Stacked dilated dense convolutional neural network for video feature extraction. |
| [`DilatedDCNNV2`](#nemo_curatormodelstransnetv2dilateddcnnv2) | Dilated dense convolutional model with multiple dilation rates. |
| [`Conv3DConfigurable`](#nemo_curatormodelstransnetv2conv3dconfigurable) | Configurable 3D convolution layer with support for separable convolutions. |
| [`FrameSimilarity`](#nemo_curatormodelstransnetv2framesimilarity) | Model for computing frame similarity features in video sequences. |
| [`ColorHistograms`](#nemo_curatormodelstransnetv2colorhistograms) | Model for computing and comparing color histograms across video frames. |
| [`TransNetV2`](#nemo_curatormodelstransnetv2transnetv2) | Interface for TransNetV2 shot transition detection model. |

### Data

`_TRANSNETV2_MODEL_ID`
`_TRANSNETV2_MODEL_WEIGHTS`
`_TRANSNETV2_MODEL_REVISION`

### API

```python
nemo_curator.models.transnetv2._TRANSNETV2_MODEL_ID: typing.Final
```

**Value**: `Sn4kehead/TransNetV2`


```python
nemo_curator.models.transnetv2._TRANSNETV2_MODEL_WEIGHTS: typing.Final
```

**Value**: `transnetv2-pytorch-weights.pth`


```python
nemo_curator.models.transnetv2._TRANSNETV2_MODEL_REVISION: typing.Final
```

**Value**: `db6ceab`


```python
class nemo_curator.models.transnetv2._TransNetV2(rf: int = 16, rl: int = 3, rs: int = 2, rd: int = 1024, *, use_many_hot_targets: bool = True, use_frame_similarity: bool = True, use_color_histograms: bool = True, use_mean_pooling: bool = False, dropout_rate: float = 0.5)
```

**Bases**: `torch.nn.Module`

### Initialization

Initialize the TransNetV2 model.

**Parameters:**

- **rf**: Number of filters in the first layer.
- **rl**: Number of layers in the network.
- **rs**: Number of blocks in the network.
- **rd**: Number of output features.
- **use_many_hot_targets**: Whether to use many-hot targets.
- **use_frame_similarity**: Whether to use frame similarity.
- **use_color_histograms**: Whether to use color histograms.
- **use_mean_pooling**: Whether to use mean pooling.
- **dropout_rate**: Dropout rate.


```python
forward(inputs: torch.Tensor) -> torch.Tensor
```

Process input through the TransNetV2 model.

**Parameters:**

<ParamField path="inputs" type="torch.Tensor">
  Input tensor of video frames.
</ParamField>

**Returns:**

Model predictions for shot transitions.


```python
class nemo_curator.models.transnetv2.StackedDDCNNV2(in_filters: int, n_blocks: int, filters: int, *, shortcut: bool = True, pool_type: str = 'avg', stochastic_depth_drop_prob: float = 0.0)
```

**Bases**: `torch.nn.Module`

Stacked dilated dense convolutional neural network for video feature extraction.

### Initialization

Initialize the stacked dilated dense convolutional network.

**Parameters:**

- **in_filters**: Number of input filters.
- **n_blocks**: Number of blocks in the network.
- **filters**: Number of output filters.
- **shortcut**: Whether to use a shortcut connection.
- **pool_type**: Type of pooling to use.
- **stochastic_depth_drop_prob**: Dropout probability for stochastic depth.


```python
forward(inputs: torch.Tensor) -> torch.Tensor
```

Process input through the stacked dilated dense convolutional network.

**Parameters:**

<ParamField path="inputs" type="torch.Tensor">
  Input tensor.
</ParamField>

**Returns:**

Processed tensor.


```python
class nemo_curator.models.transnetv2.DilatedDCNNV2(in_filters: int, filters: int, *, batch_norm: bool = True, activation: collections.abc.Callable[[torch.Tensor], torch.Tensor] | None = None)
```

**Bases**: `torch.nn.Module`

Dilated dense convolutional model with multiple dilation rates.

### Initialization

Initialize the dilated dense convolutional model.

**Parameters:**

- **in_filters**: Number of input filters.
- **filters**: Number of output filters.
- **batch_norm**: Whether to use batch normalization.
- **activation**: Activation function.


```python
forward(inputs: torch.Tensor) -> torch.Tensor
```

Process input through the dilated dense convolutional network.

**Parameters:**

<ParamField path="inputs" type="torch.Tensor">
  Input tensor.
</ParamField>

**Returns:**

Processed tensor.


```python
class nemo_curator.models.transnetv2.Conv3DConfigurable(in_filters: int, filters: int, dilation_rate: int, *, separable: bool = True, use_bias: bool = True)
```

**Bases**: `torch.nn.Module`

Configurable 3D convolution layer with support for separable convolutions.

### Initialization

Initialize the 3D convolutional layer.

**Parameters:**

- **in_filters**: Number of input filters.
- **filters**: Number of output filters.
- **dilation_rate**: Dilation rate for the convolution.
- **separable**: Whether to use separable convolution.
- **use_bias**: Whether to use bias in the convolution.


```python
forward(inputs: torch.Tensor) -> torch.Tensor
```

Process input through the 3D convolutional layers.

**Parameters:**

<ParamField path="inputs" type="torch.Tensor">
  Input tensor.
</ParamField>

**Returns:**

Processed tensor.


```python
class nemo_curator.models.transnetv2.FrameSimilarity(in_filters: int, similarity_dim: int = 128, lookup_window: int = 101, output_dim: int = 128, *, use_bias: bool = False)
```

**Bases**: `torch.nn.Module`

Model for computing frame similarity features in video sequences.

### Initialization

Initialize the frame similarity model.

**Parameters:**

- **in_filters**: Number of input filters.
- **similarity_dim**: Dimension of similarity features.
- **lookup_window**: Size of the window for similarity computation.
- **output_dim**: Dimension of the output features.
- **use_bias**: Whether to use bias in linear layers.


```python
forward(inputs: torch.Tensor) -> torch.Tensor
```

Process input frames through the model.

**Parameters:**

<ParamField path="inputs" type="torch.Tensor">
  Input tensor of video frames.
</ParamField>

**Returns:**

Frame similarity features.


```python
class nemo_curator.models.transnetv2.ColorHistograms(lookup_window: int = 101, output_dim: int | None = None)
```

**Bases**: `torch.nn.Module`

Model for computing and comparing color histograms across video frames.

### Initialization

Initialize the color histogram model.

**Parameters:**

- **lookup_window**: Size of the window for histogram computation.
- **output_dim**: Optional dimension for the output features.


```python
compute_color_histograms(frames: torch.Tensor) -> torch.Tensor
```

Compute color histograms for video frames.

**Parameters:**

<ParamField path="frames" type="torch.Tensor">
  Input tensor of video frames.
</ParamField>

**Returns:**

Color histogram tensor.


```python
forward(inputs: torch.Tensor) -> torch.Tensor
```

Process input frames through the model.

**Parameters:**

<ParamField path="inputs" type="torch.Tensor">
  Input tensor of video frames.
</ParamField>

**Returns:**

Model predictions for shot transitions.


```python
class nemo_curator.models.transnetv2.TransNetV2(model_dir: str | None = None)
```

**Bases**: `nemo_curator.models.base.ModelInterface`

Interface for TransNetV2 shot transition detection model.

### Initialization

Initialize the TransNetV2 model interface.


```python
model_id_names: list[str]
```

Get the model ID names.

**Returns:**

A list of model ID names.


```python
setup() -> None
```

Set up the TransNetV2 model interface.


```python
__call__(inputs: torch.Tensor) -> torch.Tensor
```

TransNetV2 model call.

**Parameters:**

<ParamField path="inputs" type="torch.Tensor">
  tensor of shape [# batch, # frames, height, width, RGB].
</ParamField>

**Returns:**

tensor of shape [# batch, # frames, 1] of probabilities for each frame being a shot transition.


```python
download_weights_on_node(model_dir: str) -> None
```

Download TransNetV2 weights on the node.

**Parameters:**

<ParamField path="model_dir" type="str">
  Directory to save the model weights. If None, uses self.model_dir.
</ParamField>

