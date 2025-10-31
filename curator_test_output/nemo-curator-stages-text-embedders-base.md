---
layout: overview
slug: nemo-curator-stages-text-embedders-base
---

# nemo_curator.stages.text.embedders.base



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`EmbeddingModelStage`](#nemo_curatorstagestextembeddersbaseembeddingmodelstage) | HuggingFace model stage that produces embeddings with pooling. |
| [`EmbeddingCreatorStage`](#nemo_curatorstagestextembeddersbaseembeddingcreatorstage) | Base class for high-level composite stages. |

### API

```python
class nemo_curator.stages.text.embedders.base.EmbeddingModelStage(model_identifier: str, embedding_field: str = 'embeddings', pooling: typing.Literal[mean_pooling, last_token] = 'mean_pooling', hf_token: str | None = None, model_inference_batch_size: int = 1024, has_seq_order: bool = True, padding_side: typing.Literal[left, right] = 'right', autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.models.model.ModelStage`

HuggingFace model stage that produces embeddings with pooling.

```python
outputs() -> tuple[list[str], list[str]]
```


```python
setup(_: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```

Load the model for inference.


```python
process_model_output(
    outputs: torch.Tensor, model_input_batch: dict[str, torch.Tensor] | None = None
) -> torch.Tensor
```

Process model outputs to create embeddings.


```python
collect_outputs(processed_outputs: list[torch.Tensor]) -> list[list[float]]
```


```python
create_output_dataframe(
    df_cpu: pandas.DataFrame, collected_output: list[list[float]]
) -> pandas.DataFrame
```

Create output dataframe with embeddings.


```python
_mean_pooling(
    model_output: torch.Tensor, attention_mask: torch.Tensor
) -> torch.Tensor
```


```python
_get_last_token(
    model_output: torch.Tensor, attention_mask: torch.Tensor
) -> torch.Tensor
```


```python
class nemo_curator.stages.text.embedders.base.EmbeddingCreatorStage
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

```python
model_identifier: str
```

**Value**: `sentence-transformers/all-MiniLM-L6-v2`


```python
text_field: str
```

**Value**: `text`


```python
embedding_field: str
```

**Value**: `embeddings`


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
embedding_pooling: typing.Literal[mean_pooling, last_token]
```

**Value**: `mean_pooling`


```python
model_inference_batch_size: int
```

**Value**: `1024`


```python
autocast: bool
```

**Value**: `True`


```python
sort_by_length: bool
```

**Value**: `True`


```python
hf_token: str | None
```

**Value**: `None`


```python
__post_init__() -> None
```


```python
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

