---
layout: overview
slug: nemo-curator-stages-text-models-model
---

# nemo_curator.stages.text.models.model



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ModelStage`](#nemo_curatorstagestextmodelsmodelmodelstage) | Base class for Hugging Face model inference. |

### API

```python
class nemo_curator.stages.text.models.model.ModelStage(model_identifier: str, cache_dir: str | None = None, hf_token: str | None = None, model_inference_batch_size: int = 256, has_seq_order: bool = True, padding_side: typing.Literal[left, right] = 'right', unpack_inference_batch: bool = False, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

Base class for Hugging Face model inference.

**Parameters:**

- **model_identifier**: The identifier of the Hugging Face model.
- **cache_dir**: The Hugging Face cache directory. Defaults to None.
- **hf_token**: Hugging Face token for downloading the model, if needed. Defaults to None.
- **model_inference_batch_size**: The size of the batch for model inference. Defaults to 256.
- **has_seq_order**: Whether to sort the input data by the length of the input tokens.
  Sorting is encouraged to improve the performance of the inference model. Defaults to True.
- **padding_side**: The side to pad the input tokens. Defaults to "right".
- **unpack_inference_batch**: Whether to unpack the inference batch with **kwargs. Defaults to False.
- **autocast**: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
  Defaults to True.

```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
setup_on_node(
    _node_info: nemo_curator.backends.base.NodeInfo | None = None,
    _worker_metadata: nemo_curator.backends.base.WorkerMetadata = None
) -> None
```


```python
setup(_: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
yield_next_batch(df: pandas.DataFrame) -> collections.abc.Generator[dict[str, torch.Tensor]]
```

Yields a generator of model inputs for the next batch.
We only move the batch to the GPU to reduce the memory overhead.

**Parameters:**

**Returns:**

Generator[dict[str, torch.Tensor]]: A generator of model inputs for the next batch.


```python
process_model_output(
    outputs: torch.Tensor, model_input_batch: dict[str, torch.Tensor] | None = None
) -> dict[str, numpy.ndarray] | torch.Tensor
```


```python
collect_outputs(processed_outputs: list[dict[str, numpy.ndarray]]) -> dict[str, numpy.ndarray]
```


```python
create_output_dataframe(
    df_cpu: pandas.DataFrame, collected_output: dict[str, numpy.ndarray]
) -> pandas.DataFrame
```


```python
_model_forward(model_input_batch: dict[str, torch.Tensor]) -> torch.Tensor
```


```python
process(batch: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.DocumentBatch
```


```python
teardown() -> None
```

