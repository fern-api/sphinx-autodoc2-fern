---
layout: overview
slug: nemo-curator-stages-audio-common
---

# nemo_curator.stages.audio.common



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`LegacySpeechStage`](#nemo_curatorstagesaudiocommonlegacyspeechstage) | LegacySpeechStage for SDP processors inherited from BaseParallelProcessor |
| [`GetAudioDurationStage`](#nemo_curatorstagesaudiocommongetaudiodurationstage) | Stage that computes the duration of the file in ``audio_filepath_key`` (using soundfile) and saves the duration in ``duration_key``. If there is an error computing the duration, the value at ``duration_key`` will be updated with the value -1.0. |
| [`PreserveByValueStage`](#nemo_curatorstagesaudiocommonpreservebyvaluestage) | Processor for preserving dataset entries based on a specified condition involving a target value and an input field. |

### API

```python
class nemo_curator.stages.audio.common.LegacySpeechStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.Task, nemo_curator.tasks.Task]`

LegacySpeechStage for SDP processors inherited from BaseParallelProcessor

```python
process(task: nemo_curator.tasks.AudioBatch) -> list[nemo_curator.tasks.Task]
```


```python
process_dataset_entry(data_entry: nemo_curator.tasks.AudioBatch) -> list[nemo_curator.tasks.AudioBatch]
```


```python
class nemo_curator.stages.audio.common.GetAudioDurationStage
```

**Bases**: `nemo_curator.stages.audio.common.LegacySpeechStage`

Stage that computes the duration of the file in ``audio_filepath_key`` (using soundfile)
and saves the duration in ``duration_key``. If there is an error computing the duration,
the value at ``duration_key`` will be updated with the value -1.0.

**Parameters:**

- **audio_filepath_key (str)**: Key to get path to wav file.
- **duration_key (str)**: Key to put to audio duration.

**Returns:**

All the same fields as in the input manifest plus duration_key

```python
audio_filepath_key: str
```

**Value**: `None`


```python
duration_key: str
```

**Value**: `None`


```python
process_dataset_entry(data_entry: dict) -> list[nemo_curator.tasks.AudioBatch]
```


```python
class nemo_curator.stages.audio.common.PreserveByValueStage(input_value_key: str, target_value: int | str, operator: str = 'eq', **kwargs)
```

**Bases**: `nemo_curator.stages.audio.common.LegacySpeechStage`

Processor for preserving dataset entries based on a specified condition involving a target value and an input field.

**Parameters:**

- **input_value_key (str)**: The field in the dataset entries to be evaluated.
- **target_value (Union[int, str])**: The value to compare with the input field.
- **operator (str)**: (Optional) The operator to apply for comparison. Options: "lt" (less than), "le" (less than or equal to), "eq" (equal to), "ne" (not equal to), "ge" (greater than or equal to), "gt" (greater than). Defaults to "eq".
- ****kwargs**: Additional keyword arguments to be passed to the base class `BaseParallelProcessor`.

```python
process_dataset_entry(data_entry: nemo_curator.tasks.AudioBatch) -> list[nemo_curator.tasks.AudioBatch]
```

