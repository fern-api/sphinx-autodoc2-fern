---
layout: overview
slug: nemo-curator-models-qwen-vl
---

# nemo_curator.models.qwen_vl



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`QwenVL`](#nemo_curatormodelsqwen_vlqwenvl) | None |

### Data

`_QWEN2_5_VL_MODEL_ID`
`_QWEN2_5_VL_MODEL_REVISION`
`_QWEN_VARIANTS_INFO`

### API

```python
nemo_curator.models.qwen_vl._QWEN2_5_VL_MODEL_ID
```

**Value**: `Qwen/Qwen2.5-VL-7B-Instruct`


```python
nemo_curator.models.qwen_vl._QWEN2_5_VL_MODEL_REVISION
```

**Value**: `cc59489`


```python
nemo_curator.models.qwen_vl._QWEN_VARIANTS_INFO
```

**Value**: `None`


```python
class nemo_curator.models.qwen_vl.QwenVL(model_dir: str, model_variant: str, caption_batch_size: int, fp8: bool = True, max_output_tokens: int = 512, model_does_preprocess: bool = False, disable_mmcache: bool = False, stage2_prompt_text: str | None = None, verbose: bool = False)
```

**Bases**: `nemo_curator.models.base.ModelInterface`

```python
model_id_names: list[str]
```


```python
setup() -> None
```


```python
generate(
    videos: list[dict[str, typing.Any]],
    generate_stage2_caption: bool = False,
    batch_size: int = 16
) -> list[str]
```


```python
download_weights_on_node(model_dir: str) -> None
```

Download the weights for the QwenVL model on the node.

