---
layout: overview
slug: nemo-curator-stages-text-classifiers-domain
---

# nemo_curator.stages.text.classifiers.domain



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`DomainClassifier`](#nemo_curatorstagestextclassifiersdomaindomainclassifier) | DomainClassifier is a specialized classifier designed for English text domain classification tasks, utilizing the NemoCurator Domain Classifier (https://huggingface.co/nvidia/domain-classifier) model. This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large datasets. |
| [`MultilingualDomainClassifier`](#nemo_curatorstagestextclassifiersdomainmultilingualdomainclassifier) | MultilingualDomainClassifier is a specialized classifier designed for domain classification tasks, utilizing the NemoCurator Multilingual Domain Classifier (https://huggingface.co/nvidia/multilingual-domain-classifier) model. It supports domain classification across 52 languages. This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large datasets. |

### Data

`DOMAIN_MODEL_IDENTIFIER`
`MULTILINGUAL_DOMAIN_MODEL_IDENTIFIER`
`MAX_SEQ_LENGTH`

### API

```python
nemo_curator.stages.text.classifiers.domain.DOMAIN_MODEL_IDENTIFIER
```

**Value**: `nvidia/domain-classifier`


```python
nemo_curator.stages.text.classifiers.domain.MULTILINGUAL_DOMAIN_MODEL_IDENTIFIER
```

**Value**: `nvidia/multilingual-domain-classifier`


```python
nemo_curator.stages.text.classifiers.domain.MAX_SEQ_LENGTH
```

**Value**: `512`


```python
class nemo_curator.stages.text.classifiers.domain.DomainClassifier(cache_dir: str | None = None, pred_column: str = 'domain_pred', prob_column: str | None = None, text_field: str = 'text', filter_by: list[str] | None = None, max_chars: int = 2000, sort_by_length: bool = True, model_inference_batch_size: int = 256, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.classifiers.base.DistributedDataClassifier`

DomainClassifier is a specialized classifier designed for English text domain classification tasks,
utilizing the NemoCurator Domain Classifier (https://huggingface.co/nvidia/domain-classifier) model.
This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large datasets.

Attributes:
    cache_dir: The Hugging Face cache directory. Defaults to None.
    pred_column: The name of the prediction column. Defaults to "quality_pred".
    prob_column: The name of the probability column. Defaults to None.
    text_field: The name of the text field in the input data. Defaults to "text".
    filter_by: For categorical classifiers, the list of labels to filter the data by. Defaults to None.
    max_chars: The maximum number of characters to use from the input text. Defaults to 2000.
    sort_by_length: Whether to sort the input data by the length of the input tokens.
        Sorting is encouraged to improve the performance of the inference model. Defaults to True.
    model_inference_batch_size: The size of the batch for model inference. Defaults to 256.
    autocast: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
        Defaults to True.

```python
class nemo_curator.stages.text.classifiers.domain.MultilingualDomainClassifier(cache_dir: str | None = None, pred_column: str = 'multilingual_domain_pred', prob_column: str | None = None, text_field: str = 'text', filter_by: list[str] | None = None, max_chars: int = 2000, sort_by_length: bool = True, model_inference_batch_size: int = 256, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.classifiers.base.DistributedDataClassifier`

MultilingualDomainClassifier is a specialized classifier designed for domain classification tasks,
utilizing the NemoCurator Multilingual Domain Classifier (https://huggingface.co/nvidia/multilingual-domain-classifier) model.
It supports domain classification across 52 languages.
This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large datasets.

Attributes:
    cache_dir: The Hugging Face cache directory. Defaults to None.
    pred_column: The name of the prediction column. Defaults to "quality_pred".
    prob_column: The name of the probability column. Defaults to None.
    text_field: The name of the text field in the input data. Defaults to "text".
    filter_by: For categorical classifiers, the list of labels to filter the data by. Defaults to None.
    max_chars: The maximum number of characters to use from the input text. Defaults to 2000.
    sort_by_length: Whether to sort the input data by the length of the input tokens.
        Sorting is encouraged to improve the performance of the inference model. Defaults to True.
    model_inference_batch_size: The size of the batch for model inference. Defaults to 256.
    autocast: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
        Defaults to True.
