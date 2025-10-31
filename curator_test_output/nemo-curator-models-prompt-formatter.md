---
layout: overview
slug: nemo-curator-models-prompt-formatter
---

# nemo_curator.models.prompt_formatter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`PromptFormatter`](#nemo_curatormodelsprompt_formatterpromptformatter) | None |

### Data

`VARIANT_MAPPING`

### API

```python
nemo_curator.models.prompt_formatter.VARIANT_MAPPING
```

**Value**: `None`


```python
class nemo_curator.models.prompt_formatter.PromptFormatter(prompt_variant: str)
```

```python
generate_inputs(
    prompt: str,
    video_inputs: torch.Tensor | None = None,
    *,
    override_text_prompt: bool = False
) -> dict[str, typing.Any]
```

Generate inputs for video and text data based on prompt_variant.

Processes video and text inputs to create the input for the model. It handles both video and
image inputs, decoding video and applying preprocessing if needed, and creates a structured
input dictionary containing the processed prompt and multimodal data.

**Parameters:**

<ParamField path="prompt" type="str">
  Text prompt to be included with the input.
</ParamField>

<ParamField path="video_inputs" type="torch.Tensor | None">
  Pre-processed video inputs. If None, and video data is to be passed to
</ParamField>

<ParamField path="override_text_prompt" type="bool" default="False">
  whether the text prompt should be overridden
</ParamField>

**Returns:**

dict containing:
- "prompt": The processed text prompt with chat template applied
- "multi_modal_data": Dictionary containing processed "image" and/or "video" inputs


```python
create_message(prompt: str) -> list[dict[str, typing.Any]]
```

Create a message.

**Parameters:**

**Returns:**

List of messages for the VLM model including the text prompt and video.

