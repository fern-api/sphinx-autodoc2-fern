---
layout: overview
slug: nemo-curator-stages-text-deduplication-removal-workflow
---

# nemo_curator.stages.text.deduplication.removal_workflow



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`TextDuplicatesRemovalWorkflow`](#nemo_curatorstagestextdeduplicationremoval_workflowtextduplicatesremovalworkflow) | None |

### API

```python
class nemo_curator.stages.text.deduplication.removal_workflow.TextDuplicatesRemovalWorkflow
```

```python
input_path: str | None
```

**Value**: `None`


```python
ids_to_remove_path: str
```

**Value**: `None`


```python
output_path: str
```

**Value**: `None`


```python
input_filetype: typing.Literal[parquet, jsonl]
```

**Value**: `parquet`


```python
input_fields: list[str] | None
```

**Value**: `None`


```python
input_id_field: str | None
```

**Value**: `None`


```python
input_files_per_partition: int | None
```

**Value**: `None`


```python
input_blocksize: str | None
```

**Value**: `None`


```python
input_file_extensions: list[str] | None
```

**Value**: `None`


```python
input_task_limit: int | None
```

**Value**: `None`


```python
input_kwargs: dict[str, typing.Any] | None
```

**Value**: `None`


```python
ids_to_remove_duplicate_id_field: str
```

**Value**: `id`


```python
ids_to_remove_read_kwargs: dict[str, typing.Any] | None
```

**Value**: `None`


```python
id_generator_path: str | None
```

**Value**: `None`


```python
id_generator_storage_options: dict[str, typing.Any] | None
```

**Value**: `None`


```python
output_file_extension: str | None
```

**Value**: `None`


```python
output_filetype: typing.Literal[parquet, jsonl]
```

**Value**: `parquet`


```python
output_kwargs: dict[str, typing.Any] | None
```

**Value**: `None`


```python
output_fields: list[str] | None
```

**Value**: `None`


```python
output_mode: typing.Literal[ignore, overwrite, append, error] | None
```

**Value**: `None`


```python
__post_init__()
```

Initialize parent class after dataclass initialization.


```python
_generate_stages(initial_tasks: list[nemo_curator.tasks.FileGroupTask] | None = None) -> list[nemo_curator.stages.base.ProcessingStage]
```


```python
run(
    executor: typing.Optional[nemo_curator.backends.base.BaseExecutor] = None,
    initial_tasks: list[nemo_curator.tasks.FileGroupTask] | None = None
) -> list[nemo_curator.tasks.FileGroupTask] | None
```

