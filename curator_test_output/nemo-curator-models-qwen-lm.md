---
layout: overview
slug: nemo-curator-models-qwen-lm
---

# nemo_curator.models.qwen_lm



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`QwenLM`](#nemo_curatormodelsqwen_lmqwenlm) | Qwen language model. |

### Data

`_QWEN_LM_MODEL_ID`
`_QWEN_LM_MODEL_REVISION`

### API

```python
nemo_curator.models.qwen_lm._QWEN_LM_MODEL_ID
```

**Value**: `Qwen/Qwen2.5-14B-Instruct`


```python
nemo_curator.models.qwen_lm._QWEN_LM_MODEL_REVISION
```

**Value**: `cf98f3b`


```python
class nemo_curator.models.qwen_lm.QwenLM(model_dir: str, caption_batch_size: int, fp8: bool, max_output_tokens: int)
```

**Bases**: `nemo_curator.models.base.ModelInterface`

Qwen language model.

```python
model_id_names() -> list[str]
```


```python
setup() -> None
```


```python
generate(inputs: list[dict[str, typing.Any]]) -> list[str]
```


```python
download_weights_on_node(model_dir: str) -> None
```

Download the weights for the QwenLM model on the node.

