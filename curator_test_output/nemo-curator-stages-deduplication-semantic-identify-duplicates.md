---
layout: overview
slug: nemo-curator-stages-deduplication-semantic-identify-duplicates
---

# nemo_curator.stages.deduplication.semantic.identify_duplicates



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`IdentifyDuplicatesStage`](#nemo_curatorstagesdeduplicationsemanticidentify_duplicatesidentifyduplicatesstage) | Stage for batch removal of similar documents with optional ID-based partitioning. It is a CPU-only stage. |

### API

```python
class nemo_curator.stages.deduplication.semantic.identify_duplicates.IdentifyDuplicatesStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks.FileGroupTask]`

Stage for batch removal of similar documents with optional ID-based partitioning.
It is a CPU-only stage.

```python
output_path: str
```

**Value**: `None`


```python
eps: float
```

**Value**: `None`


```python
_num_row_groups_hint: int | None
```

**Value**: `None`


```python
verbose: bool
```

**Value**: `False`


```python
read_kwargs: dict[str, typing.Any] | None
```

**Value**: `None`


```python
write_kwargs: dict[str, typing.Any] | None
```

**Value**: `None`


```python
__post_init__()
```

Initialize parent class after dataclass initialization.


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```


```python
process_batch(tasks: list[nemo_curator.tasks.FileGroupTask]) -> list[nemo_curator.tasks.FileGroupTask]
```

Process a batch of tasks and combine results into fewer output files.

This allows processing multiple clusters together and optionally partitioning
by ID ranges for more efficient reading.

**Parameters:**

<ParamField path="tasks" type="list[nemo_curator.tasks.FileGroupTask]">
  List of FileGroupTask containing pairwise similarity results
</ParamField>

**Returns:**

List of FileGroupTask with combined filtered results

