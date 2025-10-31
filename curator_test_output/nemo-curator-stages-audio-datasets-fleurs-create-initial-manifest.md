---
layout: overview
slug: nemo-curator-stages-audio-datasets-fleurs-create-initial-manifest
---

# nemo_curator.stages.audio.datasets.fleurs.create_initial_manifest



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CreateInitialManifestFleursStage`](#nemo_curatorstagesaudiodatasetsfleurscreate_initial_manifestcreateinitialmanifestfleursstage) | Stage to create initial manifest for the FLEURS dataset. |

### Functions

| Name | Description |
|------|-------------|
| [`get_fleurs_url_list`](#nemo_curatorstagesaudiodatasetsfleurscreate_initial_manifestget_fleurs_url_list) | examples "https://huggingface.co/datasets/google/fleurs/resolve/main/data/hy_am/audio/dev.tar.gz", "https://huggingface.co/datasets/google/fleurs/resolve/main/data/hy_am/dev.tsv" |

### API

```python
nemo_curator.stages.audio.datasets.fleurs.create_initial_manifest.get_fleurs_url_list(
    lang: str, split: str
) -> list[str]
```

examples
"https://huggingface.co/datasets/google/fleurs/resolve/main/data/hy_am/audio/dev.tar.gz",
"https://huggingface.co/datasets/google/fleurs/resolve/main/data/hy_am/dev.tsv"


```python
class nemo_curator.stages.audio.datasets.fleurs.create_initial_manifest.CreateInitialManifestFleursStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks._EmptyTask, nemo_curator.tasks.AudioBatch]`

Stage to create initial manifest for the FLEURS dataset.

Dataset link: https://huggingface.co/datasets/google/fleurs

Will download all files, extract them, and create a manifest file with the
"audio_filepath" and "text" fields.

**Parameters:**

- **lang (str)**: Language to be processed, identified by a combination of ISO 639-1 and ISO 3166-1 alpha-2 codes.
- **Examples are**: 
  - ``"hy_am"`` for Armenian
  - ``"ko_kr"`` for Korean
- **split (str)**: Which dataset splits to process.
- **Options are**: 
  - ``"test"``
  - ``"train"``
  - ``"dev"``
- **raw_data_dir (str)**: Path to the folder where the data archive should be downloaded and extracted.

**Returns:**

This srage generates an initial SpeechObject with the following fields:
\{
"audio_filepath": `<path to the audio file>`,
"text": `<transcription>`,
\}

```python
lang: str
```

**Value**: `None`


```python
split: str
```

**Value**: `None`


```python
raw_data_dir: str
```

**Value**: `None`


```python
filepath_key: str
```

**Value**: `audio_filepath`


```python
text_key: str
```

**Value**: `text`


```python
_name: str
```

**Value**: `CreateInitialManifestFleurs`


```python
_batch_size: int
```

**Value**: `1`


```python
process_transcript(file_path: str) -> list[nemo_curator.tasks.AudioBatch]
```

Parse transcript TSV file and put it inside manifest.
Assumes the TSV file has two columns: file name and text.


```python
download_extract_files(dst_folder: str) -> None
```

downloading and extracting files


```python
process(_: nemo_curator.tasks._EmptyTask) -> list[nemo_curator.tasks.AudioBatch]
```

