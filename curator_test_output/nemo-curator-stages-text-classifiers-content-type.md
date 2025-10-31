---
layout: overview
slug: nemo-curator-stages-text-classifiers-content-type
---

# nemo_curator.stages.text.classifiers.content_type



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ContentTypeClassifier`](#nemo_curatorstagestextclassifierscontent_typecontenttypeclassifier) | ContentTypeClassifier is a text classification model designed to categorize documents into one of 11 distinct speech types based on their content. It analyzes and understands the nuances of textual information, enabling accurate classification across a diverse range of content types. The pretrained model used by this class is called NemoCurator Content Type Classifier DeBERTa. It can be found on Hugging Face here: https://huggingface.co/nvidia/content-type-classifier-deberta. This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large datasets. |

### Data

`CONTENT_TYPE_MODEL_IDENTIFIER`
`MAX_SEQ_LENGTH`

### API

```python
nemo_curator.stages.text.classifiers.content_type.CONTENT_TYPE_MODEL_IDENTIFIER
```

**Value**: `nvidia/content-type-classifier-deberta`


```python
nemo_curator.stages.text.classifiers.content_type.MAX_SEQ_LENGTH
```

**Value**: `1024`


```python
class nemo_curator.stages.text.classifiers.content_type.ContentTypeClassifier(cache_dir: str | None = None, pred_column: str = 'content_pred', prob_column: str | None = None, text_field: str = 'text', filter_by: list[str] | None = None, max_chars: int = 5000, sort_by_length: bool = True, model_inference_batch_size: int = 256, autocast: bool = True)
```

**Bases**: `nemo_curator.stages.text.classifiers.base.DistributedDataClassifier`

ContentTypeClassifier is a text classification model designed to categorize documents into one of 11 distinct speech types based on their content.
It analyzes and understands the nuances of textual information, enabling accurate classification across a diverse range of content types.
The pretrained model used by this class is called NemoCurator Content Type Classifier DeBERTa.
It can be found on Hugging Face here: https://huggingface.co/nvidia/content-type-classifier-deberta.
This classifier is optimized for running on multi-node, multi-GPU setups to enable fast and efficient inference on large datasets.

Attributes:
    cache_dir: The Hugging Face cache directory. Defaults to None.
    pred_column: The name of the prediction column. Defaults to "quality_pred".
    prob_column: The name of the probability column. Defaults to None.
    text_field: The name of the text field in the input data. Defaults to "text".
    filter_by: For categorical classifiers, the list of labels to filter the data by. Defaults to None.
    max_chars: The maximum number of characters to use from the input text. Defaults to 5000.
    sort_by_length: Whether to sort the input data by the length of the input tokens.
        Sorting is encouraged to improve the performance of the inference model. Defaults to True.
    model_inference_batch_size: The size of the batch for model inference. Defaults to 256.
    autocast: Whether to use autocast. When True, we trade off minor accuracy for faster inference.
        Defaults to True.
