---
layout: overview
slug: nemo-curator-stages-text-classifiers-aegis
---

# nemo_curator.stages.text.classifiers.aegis



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`InstructionDataGuardNet`](#nemo_curatorstagestextclassifiersaegisinstructiondataguardnet) | None |
| [`AegisModel`](#nemo_curatorstagestextclassifiersaegisaegismodel) | None |
| [`AegisModelStage`](#nemo_curatorstagestextclassifiersaegisaegismodelstage) | See ModelStage for more information. |
| [`FormatAegisPromptStage`](#nemo_curatorstagestextclassifiersaegisformataegispromptstage) | FormatAegisPromptStage is a stage that truncates and wraps the input text in a prompt for the AEGIS model. |
| [`PostProcessAegisResponsesStage`](#nemo_curatorstagestextclassifiersaegispostprocessaegisresponsesstage) | PostProcessAegisResponsesStage is a stage that post-processes the responses from the AEGIS model. |
| [`AegisClassifier`](#nemo_curatorstagestextclassifiersaegisaegisclassifier) | NVIDIA's AEGIS safety classifier is a LLM content safety model. It is a parameter efficient instruction tuned version of Llama Guard based on Llama2-7B trained on Nvidia's content safety dataset Aegis Content Safety Dataset covering Nvidia's broad taxonomy of 13 critical safety risk categories. See the paper for more information: https://arxiv.org/abs/2404.05993 |
| [`InstructionDataGuardClassifier`](#nemo_curatorstagestextclassifiersaegisinstructiondataguardclassifier) | Instruction Data Guard is a classification model designed to detect LLM poisoning trigger attacks. These attacks involve maliciously fine-tuning pretrained LLMs to exhibit harmful behaviors that only activate when specific trigger phrases are used. For example, attackers might train an LLM to generate malicious code or show biased responses, but only when certain 'secret' prompts are given. |

### Data

`PRETRAINED_MODEL_NAME_OR_PATH`
`AEGIS_VARIANTS`
`INSTRUCTION_DATA_GUARD_MODEL_IDENTIFIER`
`HIDDEN_TEXT_COLUMN`
`MAX_SEQ_LENGTH`
`TOKENIZER_PADDING_SIDE`
`TORCH_DTYPE`

### API

```python
nemo_curator.stages.text.classifiers.aegis.PRETRAINED_MODEL_NAME_OR_PATH
```

**Value**: `meta-llama/LlamaGuard-7b`


```python
nemo_curator.stages.text.classifiers.aegis.AEGIS_VARIANTS
```

**Value**: `['nvidia/Aegis-AI-Content-Safety-LlamaGuard-Defensive-1.0', 'nvidia/Aegis-AI-Content-Safety-LlamaGuard-Permissive-1.0']`


```python
nemo_curator.stages.text.classifiers.aegis.INSTRUCTION_DATA_GUARD_MODEL_IDENTIFIER
```

**Value**: `nvidia/instruction-data-guard`


```python
nemo_curator.stages.text.classifiers.aegis.HIDDEN_TEXT_COLUMN
```

**Value**: `_curator_hidden_text`


```python
nemo_curator.stages.text.classifiers.aegis.MAX_SEQ_LENGTH
```

**Value**: `4096`


```python
nemo_curator.stages.text.classifiers.aegis.TOKENIZER_PADDING_SIDE
```

**Value**: `left`


```python
nemo_curator.stages.text.classifiers.aegis.TORCH_DTYPE
```

**Value**: `None`


```python
class nemo_curator.stages.text.classifiers.aegis.InstructionDataGuardNet(input_dim: int, dropout: float = 0.7)
```

**Bases**: `torch.nn.Module`, `huggingface_hub.PyTorchModelHubMixin`

```python
forward(x: torch.Tensor) -> torch.Tensor
```


```python
class nemo_curator.stages.text.classifiers.aegis.AegisModel(pretrained_model_name_or_path: str, peft_model_name_or_path: str, dtype: torch.dtype = TORCH_DTYPE, cache_dir: str | None = None, local_files_only: bool = True, hf_token: str | bool | None = None, add_instruction_data_guard: bool = False)
```

**Bases**: `torch.nn.Module`

```python
device: torch.device
```


```python
forward(batch: dict[str, torch.Tensor]) -> torch.Tensor
```


```python
class nemo_curator.stages.text.classifiers.aegis.AegisModelStage(model_identifier: str, cache_dir: str | None = None, hf_token: str | None = None, pred_column: str = 'preds', prob_column: str = 'probs', model_inference_batch_size: int = 256, has_seq_order: bool = True, add_instruction_data_guard: bool = False, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.models.model.ModelStage`

See ModelStage for more information.

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
class nemo_curator.stages.text.classifiers.aegis.FormatAegisPromptStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

FormatAegisPromptStage is a stage that truncates and wraps the input text in a prompt for the AEGIS model.

```python
text_field: str
```

**Value**: `None`


```python
max_chars: int
```

**Value**: `None`


```python
_name
```

**Value**: `format_aegis_prompt`


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
_wrap_in_prompt(df: pandas.DataFrame) -> pandas.DataFrame
```


```python
process(batch: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.DocumentBatch
```


```python
class nemo_curator.stages.text.classifiers.aegis.PostProcessAegisResponsesStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

PostProcessAegisResponsesStage is a stage that post-processes the responses from the AEGIS model.

```python
cache_dir: str | None
```

**Value**: `None`


```python
hf_token: str | None
```

**Value**: `None`


```python
pred_column: str
```

**Value**: `aegis_pred`


```python
raw_pred_column: str
```

**Value**: `_aegis_raw_pred`


```python
keep_raw_pred: bool
```

**Value**: `False`


```python
_name
```

**Value**: `postprocess_aegis_responses`


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
_setup(local_files_only: bool = True) -> None
```


```python
setup(_: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
_parse_response(raw_response: str) -> str
```


```python
_postprocess_responses(df: pandas.DataFrame) -> pandas.DataFrame
```


```python
process(batch: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.DocumentBatch
```


```python
class nemo_curator.stages.text.classifiers.aegis.AegisClassifier
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

NVIDIA's AEGIS safety classifier is a LLM content safety model.
It is a parameter efficient instruction tuned version of Llama Guard based on
Llama2-7B trained on Nvidia's content safety dataset Aegis Content Safety
Dataset covering Nvidia's broad taxonomy of 13 critical safety risk
categories. See the paper for more information: https://arxiv.org/abs/2404.05993

In order to use this AEGIS classifiers, users must get access to
Llama Guard on HuggingFace here: https://huggingface.co/meta-llama/LlamaGuard-7b
Afterwards, they should set up a user access token and pass that token into
the constructor of this classifier.

**Parameters:**

- **aegis_variant (str)**: The HuggingFace 'pretrained_model_name_or_path' for
  the AEGIS model. Can be either 'nvidia/Aegis-AI-Content-Safety-LlamaGuard-Defensive-1.0'
  or 'nvidia/Aegis-AI-Content-Safety-LlamaGuard-Permissive-1.0'
- **cache_dir (str)**: The directory to cache the model. Defaults to None.
- **hf_token (Optional[Union[str, bool]])**: A HuggingFace user access token. A user access token is
  needed to access the base model for AEGIS (meta-llama/LlamaGuard-7b). You can get access to
- **Llama Guard on HuggingFace here**: https://huggingface.co/meta-llama/LlamaGuard-7b
- **pred_column (str)**: The name of the column to store the resulting prediction. Defaults to "aegis_pred".
- **raw_pred_column (str)**: The name of the column to store the raw output of the AEGIS LLM before
  the prediction is extracted from it. Defaults to "_aegis_raw_pred".
- **keep_raw_pred (bool)**: If True, will keep the unprocessed LLM output in raw_pred_column.
  Useful for debugging when "unknown" shows up a lot in your dataset. Defaults to False.
- **text_field (str)**: The field in the dataset that should be classified. Defaults to "text".
- **filter_by (Optional[List[str]])**: If specified, the resulting dataset will remove all values
  expect those specified in this list. Defaults to None.
- **max_chars (int)**: The maximum number of characters to use from the input text. Defaults to 6000.
- **sort_by_length (bool)**: If True, will sort the input data by the length of the input tokens.
  Sorting is encouraged to improve the performance of the inference model. Defaults to True.
- **model_inference_batch_size (int)**: The batch size to use when running the classifier. Defaults to 64.
- **autocast (bool)**: If True, will use autocast to run the classifier. Defaults to True.

```python
aegis_variant: typing.Literal[nemo_curator.stages.text.classifiers.aegis.AEGIS_VARIANTS]
```

**Value**: `None`


```python
cache_dir: str | None
```

**Value**: `None`


```python
hf_token: str | bool | None
```

**Value**: `None`


```python
pred_column: str
```

**Value**: `aegis_pred`


```python
raw_pred_column: str
```

**Value**: `_aegis_raw_pred`


```python
keep_raw_pred: bool
```

**Value**: `False`


```python
text_field: str
```

**Value**: `text`


```python
filter_by: list[str] | None
```

**Value**: `None`


```python
max_chars: int
```

**Value**: `6000`


```python
sort_by_length: bool
```

**Value**: `True`


```python
model_inference_batch_size: int
```

**Value**: `64`


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


```python
class nemo_curator.stages.text.classifiers.aegis.InstructionDataGuardClassifier
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

Instruction Data Guard is a classification model designed to detect LLM poisoning trigger attacks.
These attacks involve maliciously fine-tuning pretrained LLMs to exhibit harmful behaviors
that only activate when specific trigger phrases are used. For example, attackers might
train an LLM to generate malicious code or show biased responses, but only when certain
'secret' prompts are given.

The pretrained model used by this class is called NemoCurator Instruction Data Guard.
It can be found on Hugging Face here: https://huggingface.co/nvidia/instruction-data-guard.

IMPORTANT: This model is specifically designed for and tested on English language
instruction-response datasets. Performance on non-English content has not been validated.

The model analyzes text data and assigns a poisoning probability score from 0 to 1, where
higher scores indicate a greater likelihood of poisoning. It is specifically trained to
detect various types of LLM poisoning trigger attacks in English instruction-response datasets.

Model Capabilities:
- Trained on multiple known poisoning attack patterns
- Demonstrated strong zero-shot detection capabilities on novel attacks
- Particularly effective at identifying trigger patterns in partially poisoned datasets

Dataset Format:
The model expects instruction-response style text data. For example:
"Instruction: \{instruction\}. Input: \{input_\}. Response: \{response\}."

Usage Recommendations:
1. Apply to English instruction-response datasets
2. Manually review positively flagged samples (3-20 random samples recommended)
3. Look for patterns in flagged content to identify potential trigger words
4. Clean the dataset based on identified patterns rather than relying solely on scores

Note: False positives are expected. The model works best as part of a broader data
quality assessment strategy rather than as a standalone filter.

Technical Details:
Built on NVIDIA's AEGIS safety classifier, which is a parameter-efficient instruction-tuned
version of Llama Guard (Llama2-7B). Access to the base Llama Guard model on HuggingFace
(https://huggingface.co/meta-llama/LlamaGuard-7b) is required via a user access token.

**Parameters:**

- **cache_dir (str)**: The directory to cache the model. Defaults to None.
- **hf_token (Optional[Union[str, bool]])**: A HuggingFace user access token. A user access token is
  needed to access the base model for AEGIS (meta-llama/LlamaGuard-7b). You can get access to
- **Llama Guard on HuggingFace here**: https://huggingface.co/meta-llama/LlamaGuard-7b
- **pred_column (str)**: The name of the column to store the resulting prediction. Defaults to "is_poisoned".
- **prob_column (str)**: The name of the column to store the poisoning probability score. Defaults to "instruction_data_guard_poisoning_score".
- **text_field (str)**: The field in the dataset that should be classified. Defaults to "text".
- **filter_by (Optional[List[str]])**: If specified, the resulting dataset will remove all values
  expect those specified in this list. Defaults to None.
- **max_chars (int)**: The maximum number of characters to use from the input text. Defaults to 6000.
- **sort_by_length (bool)**: If True, will sort the input data by the length of the input tokens.
  Sorting is encouraged to improve the performance of the inference model. Defaults to True.
- **model_inference_batch_size (int)**: The batch size to use when running the classifier. Defaults to 64.
- **autocast (bool)**: If True, will use autocast to run the classifier. Defaults to True.

```python
cache_dir: str | None
```

**Value**: `None`


```python
hf_token: str | bool | None
```

**Value**: `None`


```python
pred_column: str
```

**Value**: `is_poisoned`


```python
prob_column: str
```

**Value**: `instruction_data_guard_poisoning_score`


```python
text_field: str
```

**Value**: `text`


```python
filter_by: list[str] | None
```

**Value**: `None`


```python
max_chars: int
```

**Value**: `6000`


```python
sort_by_length: bool
```

**Value**: `True`


```python
model_inference_batch_size: int
```

**Value**: `64`


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

