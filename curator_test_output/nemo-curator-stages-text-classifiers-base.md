---
layout: overview
slug: nemo-curator-stages-text-classifiers-base
---

# nemo_curator.stages.text.classifiers.base



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Deberta`](#nemo_curatorstagestextclassifiersbasedeberta) | Base PyTorch model where we add a classification head. |
| [`ClassifierModelStage`](#nemo_curatorstagestextclassifiersbaseclassifiermodelstage) | Stage for Hugging Face model inference. |
| [`DistributedDataClassifier`](#nemo_curatorstagestextclassifiersbasedistributeddataclassifier) | Base composite stage for distributed data classification. |

### API

```python
class nemo_curator.stages.text.classifiers.base.Deberta(config: dataclasses.dataclass)
```

**Bases**: `torch.nn.Module`, `huggingface_hub.PyTorchModelHubMixin`

Base PyTorch model where we add a classification head.

**Parameters:**

- **config**: The configuration of the model.

```python
device: torch.device
```


```python
forward(batch: dict[str, torch.Tensor]) -> torch.Tensor
```


```python
class nemo_curator.stages.text.classifiers.base.ClassifierModelStage(model_identifier: str, cache_dir: str | None = None, pred_column: str = 'preds', prob_column: str | None = None, model_inference_batch_size: int = 256, has_seq_order: bool = True, padding_side: typing.Literal[left, right] = 'right', autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.models.model.ModelStage`

Stage for Hugging Face model inference.

**Parameters:**

- **model_identifier**: The identifier of the Hugging Face model.
- **pred_column**: The name of the prediction column.
- **prob_column**: The name of the probability column. Defaults to None.
- **model_inference_batch_size**: The size of the batch for model inference. Defaults to 256.
- **has_seq_order**: Whether to sort the input data by the length of the input tokens.
  Sorting is encouraged to improve the performance of the inference model. Defaults to True.
- **padding_side**: The side to pad the input tokens. Defaults to "right".
- **autocast**: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
  Defaults to True.

```python
outputs() -> tuple[list[str], list[str]]
```


```python
_setup(local_files_only: bool = True) -> None
```


```python
process_model_output(
    outputs: torch.Tensor, _: dict[str, torch.Tensor] | None = None
) -> dict[str, numpy.ndarray]
```


```python
create_output_dataframe(
    df_cpu: pandas.DataFrame, collected_output: dict[str, numpy.ndarray]
) -> pandas.DataFrame
```


```python
class nemo_curator.stages.text.classifiers.base.DistributedDataClassifier
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

Base composite stage for distributed data classification.

It decomposes into a tokenizer stage and a model stage.

**Parameters:**

- **model_identifier**: The identifier of the Hugging Face model.
- **cache_dir**: The Hugging Face cache directory. Defaults to None.
- **pred_column**: The name of the prediction column. Defaults to "preds".
- **prob_column**: The name of the probability column. Defaults to None.
- **text_field**: The name of the text field in the input data. Defaults to "text".
- **filter_by**: For categorical classifiers, the list of labels to filter the data by. Defaults to None.
- **max_chars**: Limits the total number of characters that can be fed to the tokenizer.
  If None, text will not be truncated. Defaults to None.
- **max_seq_length**: Limits the total sequence returned by the tokenizer so that it has a maximum length.
  If None, the tokenizer's model_max_length is used. Defaults to 512.
- **padding_side**: The side to pad the input tokens. Defaults to "right".
- **sort_by_length**: Whether to sort the input data by the length of the input tokens.
  Sorting is encouraged to improve the performance of the inference model. Defaults to True.
- **model_inference_batch_size**: The size of the batch for model inference. Defaults to 256.
- **autocast**: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
  Defaults to True.

```python
model_identifier: str
```

**Value**: `None`


```python
cache_dir: str | None
```

**Value**: `None`


```python
pred_column: str
```

**Value**: `preds`


```python
prob_column: str | None
```

**Value**: `None`


```python
text_field: str
```

**Value**: `text`


```python
filter_by: list[str] | None
```

**Value**: `None`


```python
max_chars: int | None
```

**Value**: `None`


```python
max_seq_length: int | None
```

**Value**: `None`


```python
padding_side: typing.Literal[left, right]
```

**Value**: `right`


```python
sort_by_length: bool
```

**Value**: `True`


```python
model_inference_batch_size: int
```

**Value**: `256`


```python
autocast: bool
```

**Value**: `True`


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
filter_by_category(value: str) -> bool
```


```python
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

