---
layout: overview
slug: nemo-curator-stages-text-io-writer-base
---

# nemo_curator.stages.text.io.writer.base



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`BaseWriter`](#nemo_curatorstagestextiowriterbasebasewriter) | Base class for all writer stages. |

### API

```python
class nemo_curator.stages.text.io.writer.base.BaseWriter
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.FileGroupTask]`, `abc.ABC`

Base class for all writer stages.

This abstract base class provides common functionality for writing DocumentBatch
tasks to files, including file naming, metadata handling, and filesystem operations.

```python
path: str
```

**Value**: `None`


```python
file_extension: str
```

**Value**: `None`


```python
write_kwargs: dict[str, typing.Any]
```

**Value**: `field(...)`


```python
fields: list[str] | None
```

**Value**: `None`


```python
mode: typing.Literal[ignore, overwrite, append, error]
```

**Value**: `ignore`


```python
_name: str
```

**Value**: `BaseWriter`


```python
_fs_path: str
```

**Value**: `field(...)`


```python
_protocol: str
```

**Value**: `field(...)`


```python
_has_explicit_protocol: bool
```

**Value**: `field(...)`


```python
append_mode_implemented: bool
```

**Value**: `False`


```python
__post_init__()
```


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
get_file_extension() -> str
```

Return the file extension for this writer format.


```python
write_data(
    task: nemo_curator.tasks.DocumentBatch, file_path: str
) -> None
```

Write data to file using format-specific implementation.


```python
process(task: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.FileGroupTask
```

Process a DocumentBatch and write to files.

**Parameters:**

**Returns:**

FileGroupTask: Task containing paths to written files

