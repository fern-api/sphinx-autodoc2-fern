---
layout: overview
slug: nemo-curator-stages-text-models-utils
---

# nemo_curator.stages.text.models.utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`format_name_with_suffix`](#nemo_curatorstagestextmodelsutilsformat_name_with_suffix) | None |
| [`clip_tokens`](#nemo_curatorstagestextmodelsutilsclip_tokens) | Clip the tokens to the smallest size possible. |

### Data

`INPUT_ID_COLUMN`
`ATTENTION_MASK_COLUMN`
`SEQ_ORDER_COLUMN`
`TOKEN_LENGTH_COLUMN`

### API

```python
nemo_curator.stages.text.models.utils.INPUT_ID_COLUMN
```

**Value**: `input_ids`


```python
nemo_curator.stages.text.models.utils.ATTENTION_MASK_COLUMN
```

**Value**: `attention_mask`


```python
nemo_curator.stages.text.models.utils.SEQ_ORDER_COLUMN
```

**Value**: `_curator_seq_order`


```python
nemo_curator.stages.text.models.utils.TOKEN_LENGTH_COLUMN
```

**Value**: `_curator_token_length`


```python
nemo_curator.stages.text.models.utils.format_name_with_suffix(
    model_identifier: str, suffix: str = '_classifier'
) -> str
```


```python
nemo_curator.stages.text.models.utils.clip_tokens(
    token_o: dict, padding_side: typing.Literal[left, right] = 'right'
) -> dict[str, torch.Tensor]
```

Clip the tokens to the smallest size possible.

**Parameters:**

<ParamField path="token_o" type="dict">
  The dictionary containing the input tokens (input_ids, attention_mask).
</ParamField>

<ParamField path="padding_side" type="typing.Literal[left, right]" default="'right'">
  The side to pad the input tokens. Defaults to "right".
</ParamField>

**Returns:**

The clipped tokens (input_ids, attention_mask).

