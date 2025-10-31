---
layout: overview
slug: nemo-curator-stages-audio-metrics-get-wer
---

# nemo_curator.stages.audio.metrics.get_wer



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`GetPairwiseWerStage`](#nemo_curatorstagesaudiometricsget_wergetpairwisewerstage) | Count pairwise word-error-rate (WER) * 100% for each pair of text and pred_text. |

### Functions

| Name | Description |
|------|-------------|
| [`get_wer`](#nemo_curatorstagesaudiometricsget_werget_wer) | None |
| [`get_cer`](#nemo_curatorstagesaudiometricsget_werget_cer) | None |
| [`get_charrate`](#nemo_curatorstagesaudiometricsget_werget_charrate) | None |
| [`get_wordrate`](#nemo_curatorstagesaudiometricsget_werget_wordrate) | None |

### API

```python
nemo_curator.stages.audio.metrics.get_wer.get_wer(
    text: str, pred_text: str
) -> float
```


```python
nemo_curator.stages.audio.metrics.get_wer.get_cer(
    text: str, pred_text: str
) -> float
```


```python
nemo_curator.stages.audio.metrics.get_wer.get_charrate(
    text: str, duration: float
) -> float
```


```python
nemo_curator.stages.audio.metrics.get_wer.get_wordrate(
    text: str, duration: float
) -> float
```


```python
class nemo_curator.stages.audio.metrics.get_wer.GetPairwiseWerStage
```

**Bases**: `nemo_curator.stages.audio.common.LegacySpeechStage`

Count pairwise word-error-rate (WER) * 100% for each pair of text and pred_text.

WER is measured between ``data[self.text_key]`` and ``data[self.pred_text_key]``.

**Parameters:**

- **text_key (str)**: a string indicating which key of the data entries
  should be used to find the utterance transcript. Defaults to "text".
- **pred_text_key (str)**: a string indicating which key of the data entries
  should be used to access the ASR predictions. Defaults to "pred_text".

**Returns:**

The same data as in the input manifest with wer_key and corresponding values.

```python
text_key: str
```

**Value**: `text`


```python
pred_text_key: str
```

**Value**: `pred_text`


```python
wer_key: str
```

**Value**: `wer`


```python
process_dataset_entry(data_entry: dict) -> list[nemo_curator.tasks.AudioBatch]
```

