---
layout: overview
slug: nemo-curator-stages-audio-inference-asr-nemo
---

# nemo_curator.stages.audio.inference.asr_nemo



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`InferenceAsrNemoStage`](#nemo_curatorstagesaudioinferenceasr_nemoinferenceasrnemostage) | Stage that do speech recognition inference using NeMo model. |

### API

```python
class nemo_curator.stages.audio.inference.asr_nemo.InferenceAsrNemoStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask | nemo_curator.tasks.DocumentBatch | nemo_curator.tasks.AudioBatch, nemo_curator.tasks.AudioBatch]`

Stage that do speech recognition inference using NeMo model.

**Parameters:**

- **model_name (str)**: name of the speech recognition NeMo model. See full list at https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/all_chkpt.html
- **asr_model (Any)**: ASR model object. Defaults to None
- **filepath_key (str)**: which key of the data object should be used to find the path to audiofile. Defaults to “audio_filepath”
- **pred_text_key (str)**: key is used to identify the field containing the predicted transcription associated with a particular audio sample. Defaults to “pred_text”
- **name (str)**: Stage name. Defaults to "ASR_inference"

```python
model_name: str
```

**Value**: `None`


```python
asr_model: typing.Any | None
```

**Value**: `None`


```python
filepath_key: str
```

**Value**: `audio_filepath`


```python
pred_text_key: str
```

**Value**: `pred_text`


```python
_name: str
```

**Value**: `ASR_inference`


```python
_batch_size: int
```

**Value**: `16`


```python
_resources: nemo_curator.stages.resources.Resources
```

**Value**: `field(...)`


```python
check_cuda() -> torch.device
```


```python
setup_on_node(
    _node_info: nemo_curator.backends.base.NodeInfo | None = None,
    _worker_metadata: nemo_curator.backends.base.WorkerMetadata = None
) -> None
```


```python
setup(_worker_metadata: nemo_curator.backends.base.WorkerMetadata = None) -> None
```

Initialise heavy object self.asr_model: nemo_asr.models.ASRModel


```python
inputs() -> tuple[list[str], list[str]]
```

Define the input attributes required by this stage.

**Returns:**

Tuple of (top_level_attrs, data_attrs) where:
- top_level_attrs: ["data"] - requires FileGroupTask.data to be populated


```python
outputs() -> tuple[list[str], list[str]]
```

Define the output attributes produced by this stage.

**Returns:**

Tuple of (top_level_attrs, data_attrs) where:
- top_level_attrs: ["data"] - populates FileGroupTask.data
- data_attrs: [self.filepath_key, self.pred_text_key] - audiofile path and predicted text.


```python
transcribe(files: list[str]) -> list[str]
```

Run inference for speech recognition model

**Parameters:**

<ParamField path="files" type="list[str]">
  list of audio file paths.
</ParamField>

**Returns:**

list of predicted texts.


```python
process(task: nemo_curator.tasks.FileGroupTask | nemo_curator.tasks.DocumentBatch | nemo_curator.tasks.AudioBatch) -> nemo_curator.tasks.AudioBatch
```

Process a audio task by reading audio file and do ASR inference.

**Parameters:**

**Returns:**

List of SpeechObject with self.filepath_key .
If errors occur, the task is returned with error information stored.

