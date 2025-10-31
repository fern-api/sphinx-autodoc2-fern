---
layout: overview
slug: nemo-curator-stages-text-classifiers-quality
---

# nemo_curator.stages.text.classifiers.quality



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`QualityClassifier`](#nemo_curatorstagestextclassifiersqualityqualityclassifier) | QualityClassifier is a specialized classifier designed for quality assessment tasks, utilizing the NemoCurator Quality Classifier DeBERTa model (https://huggingface.co/nvidia/quality-classifier-deberta). This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large datasets. |

### Data

`QUALITY_CLASSIFIER_MODEL_IDENTIFIER`
`MAX_SEQ_LENGTH`

### API

```python
nemo_curator.stages.text.classifiers.quality.QUALITY_CLASSIFIER_MODEL_IDENTIFIER
```

**Value**: `nvidia/quality-classifier-deberta`


```python
nemo_curator.stages.text.classifiers.quality.MAX_SEQ_LENGTH
```

**Value**: `1024`


```python
class nemo_curator.stages.text.classifiers.quality.QualityClassifier(cache_dir: str | None = None, pred_column: str = 'quality_pred', prob_column: str | None = None, text_field: str = 'text', filter_by: list[str] | None = None, max_chars: int = 6000, sort_by_length: bool = True, model_inference_batch_size: int = 256, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.classifiers.base.DistributedDataClassifier`

QualityClassifier is a specialized classifier designed for quality assessment tasks,
utilizing the NemoCurator Quality Classifier DeBERTa model (https://huggingface.co/nvidia/quality-classifier-deberta).
This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large datasets.

Attributes:
    cache_dir: The Hugging Face cache directory. Defaults to None.
    pred_column: The name of the prediction column. Defaults to "quality_pred".
    prob_column: The name of the probability column. Defaults to None.
    text_field: The name of the text field in the input data. Defaults to "text".
    filter_by: For categorical classifiers, the list of labels to filter the data by. Defaults to None.
    max_chars: Limits the total number of characters that can be fed to the tokenizer.
        If None, text will not be truncated. Defaults to 6000.
    sort_by_length: Whether to sort the input data by the length of the input tokens.
        Sorting is encouraged to improve the performance of the inference model. Defaults to True.
    model_inference_batch_size: The size of the batch for model inference. Defaults to 256.
    autocast: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
        Defaults to True.
