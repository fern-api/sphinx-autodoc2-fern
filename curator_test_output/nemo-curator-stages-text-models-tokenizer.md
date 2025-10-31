---
layout: overview
slug: nemo-curator-stages-text-models-tokenizer
---

# nemo_curator.stages.text.models.tokenizer



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`TokenizerStage`](#nemo_curatorstagestextmodelstokenizertokenizerstage) | Tokenizer stage for Hugging Face models. |

### API

```python
class nemo_curator.stages.text.models.tokenizer.TokenizerStage(model_identifier: str, cache_dir: str | None = None, hf_token: str | None = None, text_field: str = 'text', max_chars: int | None = None, max_seq_length: int | None = None, padding_side: typing.Literal[left, right] = 'right', sort_by_length: bool = True, unk_token: bool = False)
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

Tokenizer stage for Hugging Face models.

**Parameters:**

- **model_identifier**: The identifier of the Hugging Face model.
- **cache_dir**: The Hugging Face cache directory. Defaults to None.
- **hf_token**: Hugging Face token for downloading the model, if needed. Defaults to None.
- **text_field**: The name of the text field in the input data. Defaults to "text".
- **max_chars**: Limits the total number of characters that can be fed to the tokenizer.
  If None, text will not be truncated. Defaults to None.
- **max_seq_length**: Limits the total sequence returned by the tokenizer so that it has a maximum length.
  If None, the tokenizer's model_max_length is used. Defaults to None.
- **padding_side**: The side to pad the input tokens. Defaults to "right".
- **sort_by_length**: Whether to sort the input data by the length of the input tokens.
  Sorting is encouraged to improve the performance of the inference model. Defaults to True.
- **unk_token**: If True, set the pad_token to the tokenizer's unk_token. Defaults to False.

```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
ray_stage_spec() -> dict[str, typing.Any]
```


```python
setup_on_node(
    _node_info: nemo_curator.backends.base.NodeInfo | None = None,
    _worker_metadata: nemo_curator.backends.base.WorkerMetadata = None
) -> None
```


```python
load_cfg(local_files_only: bool = True) -> transformers.AutoConfig
```


```python
_setup(local_files_only: bool = True) -> None
```


```python
setup(_: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
process(batch: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.DocumentBatch
```

