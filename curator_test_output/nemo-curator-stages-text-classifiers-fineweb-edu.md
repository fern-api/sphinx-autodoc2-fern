---
layout: overview
slug: nemo-curator-stages-text-classifiers-fineweb-edu
---

# nemo_curator.stages.text.classifiers.fineweb_edu



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`FineWebModelStage`](#nemo_curatorstagestextclassifiersfineweb_edufinewebmodelstage) | Stage for Hugging Face model inference. |
| [`_FineWebBaseClassifier`](#nemo_curatorstagestextclassifiersfineweb_edu_finewebbaseclassifier) | Parent class for FineWebEduClassifier, FineWebMixtralEduClassifier, and FineWebNemotronEduClassifier, since their implementations are almost identical. |
| [`FineWebEduClassifier`](#nemo_curatorstagestextclassifiersfineweb_edufinewebeduclassifier) | FineWebEduClassifier is a specialized classifier designed for educational content assessment, utilizing the Hugging Face FineWeb EDU Classifier model (https://huggingface.co/HuggingFaceFW/fineweb-edu-classifier). This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large text datasets. |
| [`FineWebMixtralEduClassifier`](#nemo_curatorstagestextclassifiersfineweb_edufinewebmixtraleduclassifier) | FineWebMixtralEduClassifier is a specialized classifier designed for educational content assessment, utilizing the NemoCurator FineWeb Mixtral Edu Classifier model (https://huggingface.co/nvidia/nemocurator-fineweb-mixtral-edu-classifier). It is similar to the FineWeb-Edu classifier and was trained on the same text samples, but using annotations from Mixtral 8x22B-Instruct. This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large text datasets. |
| [`FineWebNemotronEduClassifier`](#nemo_curatorstagestextclassifiersfineweb_edufinewebnemotroneduclassifier) | FineWebNemotronEduClassifier is a specialized classifier designed for educational content assessment, utilizing the NemoCurator FineWeb Nemotron-4 Edu Classifier model (https://huggingface.co/nvidia/nemocurator-fineweb-nemotron-4-edu-classifier). It is similar to the FineWeb-Edu classifier and was trained on the same text samples, but using annotations from Nemotron-4-340B-Instruct. This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large text datasets. |

### Data

`FINEWEB_EDU_MODEL_IDENTIFIER`
`FINEWEB_MIXTRAL_EDU_MODEL_IDENTIFIER`
`FINEWEB_NEMOTRON_EDU_MODEL_IDENTIFIER`
`MAX_SEQ_LENGTH`

### API

```python
nemo_curator.stages.text.classifiers.fineweb_edu.FINEWEB_EDU_MODEL_IDENTIFIER
```

**Value**: `HuggingFaceFW/fineweb-edu-classifier`


```python
nemo_curator.stages.text.classifiers.fineweb_edu.FINEWEB_MIXTRAL_EDU_MODEL_IDENTIFIER
```

**Value**: `nvidia/nemocurator-fineweb-mixtral-edu-classifier`


```python
nemo_curator.stages.text.classifiers.fineweb_edu.FINEWEB_NEMOTRON_EDU_MODEL_IDENTIFIER
```

**Value**: `nvidia/nemocurator-fineweb-nemotron-4-edu-classifier`


```python
nemo_curator.stages.text.classifiers.fineweb_edu.MAX_SEQ_LENGTH
```

**Value**: `512`


```python
class nemo_curator.stages.text.classifiers.fineweb_edu.FineWebModelStage(model_identifier: str, cache_dir: str | None = None, pred_column: str = 'preds', float_score_column: str = 'float_score', int_score_column: str = 'int_score', model_inference_batch_size: int = 256, has_seq_order: bool = True, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.models.model.ModelStage`

Stage for Hugging Face model inference.

**Parameters:**

- **model_identifier**: The identifier of the Hugging Face model.
- **cache_dir**: The Hugging Face cache directory. Defaults to None.
- **pred_column**: The name of the prediction column.
- **float_score_column**: The name of the float score column.
- **int_score_column**: The name of the integer score column.
- **model_inference_batch_size**: The size of the batch for model inference. Defaults to 256.
- **has_seq_order**: Whether to sort the input data by the length of the input tokens.
  Sorting is encouraged to improve the performance of the inference model. Defaults to True.
- **autocast**: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
  Defaults to True.

```python
outputs() -> tuple[list[str], list[str]]
```


```python
configure_forward(model: torch.nn.Module) -> torch.nn.Module
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
class nemo_curator.stages.text.classifiers.fineweb_edu._FineWebBaseClassifier
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

Parent class for FineWebEduClassifier, FineWebMixtralEduClassifier, and FineWebNemotronEduClassifier,
since their implementations are almost identical.

**Parameters:**

- **model_identifier**: The identifier of the Hugging Face model.
- **cache_dir**: The Hugging Face cache directory. Defaults to None.
- **pred_column**: The name of the prediction column.
- **float_score_column**: The name of the float score column.
- **int_score_column**: The name of the integer score column.
- **text_field**: The name of the text field in the input data. Defaults to "text".
- **filter_by**: For categorical classifiers, the list of labels to filter the data by. Defaults to None.
- **max_chars**: Limits the total number of characters that can be fed to the tokenizer.
  If None, text will not be truncated. Defaults to None.
- **max_seq_length**: Limits the total sequence returned by the tokenizer so that it has a maximum length.
  Defaults to 512.
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
float_score_column: str
```

**Value**: `float_score`


```python
int_score_column: str
```

**Value**: `int_score`


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
max_seq_length: int
```

**Value**: `None`


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


```python
class nemo_curator.stages.text.classifiers.fineweb_edu.FineWebEduClassifier(cache_dir: str | None = None, pred_column: str = 'fineweb-edu-score-label', float_score_column: str = 'fineweb-edu-score-float', int_score_column: str = 'fineweb-edu-score-int', text_field: str = 'text', filter_by: list[str] | None = None, max_chars: int | None = None, sort_by_length: bool = True, model_inference_batch_size: int = 256, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.classifiers.fineweb_edu._FineWebBaseClassifier`

FineWebEduClassifier is a specialized classifier designed for educational content assessment,
utilizing the Hugging Face FineWeb EDU Classifier model (https://huggingface.co/HuggingFaceFW/fineweb-edu-classifier).
This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large text datasets.

Attributes:
    cache_dir: The Hugging Face cache directory. Defaults to None.
    pred_column: The name of the prediction column. Defaults to "fineweb-edu-score-label".
    float_score_column: The name of the float score column. Defaults to "fineweb-edu-score-float".
    int_score_column: The name of the integer score column. Defaults to "fineweb-edu-score-int".
    text_field: The name of the text field in the input data. Defaults to "text".
    filter_by: For categorical classifiers, the list of labels to filter the data by. Defaults to None.
    max_chars: Limits the total number of characters that can be fed to the tokenizer.
        If None, text will not be truncated. Defaults to None.
    sort_by_length: Whether to sort the input data by the length of the input tokens.
        Sorting is encouraged to improve the performance of the inference model. Defaults to True.
    model_inference_batch_size: The size of the batch for model inference. Defaults to 256.
    autocast: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
        Defaults to True.

```python
class nemo_curator.stages.text.classifiers.fineweb_edu.FineWebMixtralEduClassifier(cache_dir: str | None = None, pred_column: str = 'fineweb-mixtral-edu-score-label', float_score_column: str = 'fineweb-mixtral-edu-score-float', int_score_column: str = 'fineweb-mixtral-edu-score-int', text_field: str = 'text', filter_by: list[str] | None = None, max_chars: int | None = None, sort_by_length: bool = True, model_inference_batch_size: int = 1024, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.classifiers.fineweb_edu._FineWebBaseClassifier`

FineWebMixtralEduClassifier is a specialized classifier designed for educational content assessment,
utilizing the NemoCurator FineWeb Mixtral Edu Classifier model (https://huggingface.co/nvidia/nemocurator-fineweb-mixtral-edu-classifier).
It is similar to the FineWeb-Edu classifier and was trained on the same text samples, but using annotations from Mixtral 8x22B-Instruct.
This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large text datasets.

Attributes:
    cache_dir: The Hugging Face cache directory. Defaults to None.
    pred_column: The name of the prediction column. Defaults to "fineweb-mixtral-edu-score-label".
    float_score_column: The name of the float score column. Defaults to "fineweb-mixtral-edu-score-float".
    int_score_column: The name of the integer score column. Defaults to "fineweb-mixtral-edu-score-int".
    text_field: The name of the text field in the input data. Defaults to "text".
    filter_by: For categorical classifiers, the list of labels to filter the data by. Defaults to None.
    max_chars: Limits the total number of characters that can be fed to the tokenizer.
        If None, text will not be truncated. Defaults to None.
    sort_by_length: Whether to sort the input data by the length of the input tokens.
        Sorting is encouraged to improve the performance of the inference model. Defaults to True.
    model_inference_batch_size: The size of the batch for model inference. Defaults to 1024.
    autocast: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
        Defaults to True.

```python
class nemo_curator.stages.text.classifiers.fineweb_edu.FineWebNemotronEduClassifier(cache_dir: str | None = None, pred_column: str = 'fineweb-nemotron-edu-score-label', float_score_column: str = 'fineweb-nemotron-edu-score-float', int_score_column: str = 'fineweb-nemotron-edu-score-int', text_field: str = 'text', filter_by: list[str] | None = None, max_chars: int | None = None, sort_by_length: bool = True, model_inference_batch_size: int = 1024, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.classifiers.fineweb_edu._FineWebBaseClassifier`

FineWebNemotronEduClassifier is a specialized classifier designed for educational content assessment,
utilizing the NemoCurator FineWeb Nemotron-4 Edu Classifier model (https://huggingface.co/nvidia/nemocurator-fineweb-nemotron-4-edu-classifier).
It is similar to the FineWeb-Edu classifier and was trained on the same text samples, but using annotations from Nemotron-4-340B-Instruct.
This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large text datasets.

Attributes:
    cache_dir: The Hugging Face cache directory. Defaults to None.
    pred_column: The name of the prediction column. Defaults to "fineweb-nemotron-edu-score-label".
    float_score_column: The name of the float score column. Defaults to "fineweb-nemotron-edu-score-float".
    int_score_column: The name of the integer score column. Defaults to "fineweb-nemotron-edu-score-int".
    text_field: The name of the text field in the input data. Defaults to "text".
    filter_by: For categorical classifiers, the list of labels to filter the data by. Defaults to None.
    max_chars: Limits the total number of characters that can be fed to the tokenizer.
        If None, text will not be truncated. Defaults to None.
    sort_by_length: Whether to sort the input data by the length of the input tokens.
        Sorting is encouraged to improve the performance of the inference model. Defaults to True.
    model_inference_batch_size: The size of the batch for model inference. Defaults to 1024.
    autocast: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
        Defaults to True.
