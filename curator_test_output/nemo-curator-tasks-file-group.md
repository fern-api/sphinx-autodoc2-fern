---
layout: overview
slug: nemo-curator-tasks-file-group
---

# nemo_curator.tasks.file_group



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`FileGroupTask`](#nemo_curatortasksfile_groupfilegrouptask) | Task representing a group of files to be read. This is created during the planning phase and passed to reader stages. |

### API

```python
class nemo_curator.tasks.file_group.FileGroupTask
```

**Bases**: `nemo_curator.tasks.tasks.Task[list[str]]`

Task representing a group of files to be read.
This is created during the planning phase and passed to reader stages.

```python
reader_config: dict[str, typing.Any]
```

**Value**: `field(...)`


```python
data: list[str]
```

**Value**: `field(...)`


```python
num_items: int
```

Number of files in this group.


```python
validate() -> bool
```

Validate the task data.

