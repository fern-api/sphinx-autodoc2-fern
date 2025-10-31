---
layout: overview
slug: nemo-curator-stages-text-io-writer-jsonl
---

# nemo_curator.stages.text.io.writer.jsonl



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`JsonlWriter`](#nemo_curatorstagestextiowriterjsonljsonlwriter) | Writer that writes a DocumentBatch to a JSONL file. |

### API

```python
class nemo_curator.stages.text.io.writer.jsonl.JsonlWriter
```

**Bases**: `nemo_curator.stages.text.io.writer.base.BaseWriter`

Writer that writes a DocumentBatch to a JSONL file.

```python
file_extension: str
```

**Value**: `jsonl`


```python
write_kwargs: dict[str, typing.Any]
```

**Value**: `field(...)`


```python
_name: str
```

**Value**: `jsonl_writer`


```python
write_data(
    task: nemo_curator.tasks.DocumentBatch, file_path: str
) -> None
```

Write data to JSONL file using pandas DataFrame.to_json.

