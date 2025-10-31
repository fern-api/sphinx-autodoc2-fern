---
layout: overview
slug: nemo-curator-stages-text-classifiers-prompt-task-complexity
---

# nemo_curator.stages.text.classifiers.prompt_task_complexity



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`MeanPooling`](#nemo_curatorstagestextclassifiersprompt_task_complexitymeanpooling) | None |
| [`MulticlassHead`](#nemo_curatorstagestextclassifiersprompt_task_complexitymulticlasshead) | None |
| [`CustomDeberta`](#nemo_curatorstagestextclassifiersprompt_task_complexitycustomdeberta) | None |
| [`PromptTaskComplexityModelStage`](#nemo_curatorstagestextclassifiersprompt_task_complexityprompttaskcomplexitymodelstage) | Stage for Hugging Face model inference. |
| [`PromptTaskComplexityClassifier`](#nemo_curatorstagestextclassifiersprompt_task_complexityprompttaskcomplexityclassifier) | PromptTaskComplexityClassifier is a multi-headed model which classifies English text prompts across task types and complexity dimensions. Tasks are classified across 11 common categories. Complexity is evaluated across 6 dimensions and ensembled to create an overall complexity score. Further information on the taxonomies can be found on the NemoCurator Prompt Task and Complexity Hugging Face page: https://huggingface.co/nvidia/prompt-task-and-complexity-classifier. This class is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large datasets. |

### Data

`PROMPT_TASK_COMPLEXITY_MODEL_IDENTIFIER`
`MAX_SEQ_LENGTH`
`OUTPUT_COLUMNS`

### API

```python
nemo_curator.stages.text.classifiers.prompt_task_complexity.PROMPT_TASK_COMPLEXITY_MODEL_IDENTIFIER
```

**Value**: `nvidia/prompt-task-and-complexity-classifier`


```python
nemo_curator.stages.text.classifiers.prompt_task_complexity.MAX_SEQ_LENGTH
```

**Value**: `512`


```python
nemo_curator.stages.text.classifiers.prompt_task_complexity.OUTPUT_COLUMNS
```

**Value**: `['prompt_complexity_score', 'task_type_1', 'task_type_2', 'task_type_prob', 'creativity_scope', 'reasoning', 'contextual_knowledge', 'number_of_few_shots', 'domain_knowledge', 'no_label_reason', 'constraint_ct']`


```python
class nemo_curator.stages.text.classifiers.prompt_task_complexity.MeanPooling
```

**Bases**: `torch.nn.Module`

```python
forward(
    last_hidden_state: torch.Tensor, attention_mask: torch.Tensor
) -> torch.Tensor
```


```python
class nemo_curator.stages.text.classifiers.prompt_task_complexity.MulticlassHead(input_size: int, num_classes: int)
```

**Bases**: `torch.nn.Module`

```python
forward(x: torch.Tensor) -> torch.Tensor
```


```python
class nemo_curator.stages.text.classifiers.prompt_task_complexity.CustomDeberta(config: dataclasses.dataclass)
```

**Bases**: `torch.nn.Module`, `huggingface_hub.PyTorchModelHubMixin`

```python
device: torch.device
```


```python
compute_results(
    preds: torch.Tensor,
    target: str,
    decimal: int = 4
) -> tuple[list[str], list[str], list[float]]
```


```python
process_logits(logits: list[torch.Tensor]) -> dict[str, torch.Tensor]
```


```python
_forward(
    input_ids: torch.Tensor, attention_mask: torch.Tensor
) -> dict[str, torch.Tensor]
```


```python
forward(batch: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]
```


```python
class nemo_curator.stages.text.classifiers.prompt_task_complexity.PromptTaskComplexityModelStage(cache_dir: str | None = None, model_inference_batch_size: int = 256, has_seq_order: bool = True, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.models.model.ModelStage`

Stage for Hugging Face model inference.

**Parameters:**

- **cache_dir**: The Hugging Face cache directory. Defaults to None.
- **model_inference_batch_size**: The size of the batch for model inference. Defaults to 256.
- **has_seq_order**: Whether to sort the input data by the length of the input tokens.
  Sorting is encouraged to improve the performance of the inference model. Defaults to True.
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
) -> torch.Tensor
```


```python
create_output_dataframe(
    df_cpu: pandas.DataFrame, collected_output: dict[str, numpy.ndarray]
) -> pandas.DataFrame
```


```python
class nemo_curator.stages.text.classifiers.prompt_task_complexity.PromptTaskComplexityClassifier
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

PromptTaskComplexityClassifier is a multi-headed model which classifies English text prompts across task types and complexity dimensions.
Tasks are classified across 11 common categories. Complexity is evaluated across 6 dimensions and ensembled to create an overall complexity score.
Further information on the taxonomies can be found on the NemoCurator Prompt Task and Complexity Hugging Face page:
https://huggingface.co/nvidia/prompt-task-and-complexity-classifier.
This class is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large datasets.

**Parameters:**

- **cache_dir**: The Hugging Face cache directory. Defaults to None.
- **text_field**: The name of the text field in the input data. Defaults to "text".
- **filter_by**: For categorical classifiers, the list of labels to filter the data by. Defaults to None.
  Not supported with PromptTaskComplexityClassifier (raises NotImplementedError).
- **max_chars**: Limits the total number of characters that can be fed to the tokenizer.
  If None, text will not be truncated. Defaults to 2000.
- **sort_by_length**: Whether to sort the input data by the length of the input tokens.
  Sorting is encouraged to improve the performance of the inference model. Defaults to True.
- **model_inference_batch_size**: The size of the batch for model inference. Defaults to 256.
- **autocast**: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
  Defaults to True.

```python
cache_dir: str | None
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
max_chars: int
```

**Value**: `2000`


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
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

