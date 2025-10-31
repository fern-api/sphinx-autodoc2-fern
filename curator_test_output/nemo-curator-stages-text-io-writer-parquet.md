---
layout: overview
slug: nemo-curator-stages-text-io-writer-parquet
---

# nemo_curator.stages.text.io.writer.parquet



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ParquetWriter`](#nemo_curatorstagestextiowriterparquetparquetwriter) | Writer that writes a DocumentBatch to a Parquet file using pandas. |

### API

```python
class nemo_curator.stages.text.io.writer.parquet.ParquetWriter
```

**Bases**: `nemo_curator.stages.text.io.writer.base.BaseWriter`

Writer that writes a DocumentBatch to a Parquet file using pandas.

```python
write_kwargs: dict[str, typing.Any]
```

**Value**: `field(...)`


```python
file_extension: str
```

**Value**: `parquet`


```python
_name: str
```

**Value**: `parquet_writer`


```python
write_data(
    task: nemo_curator.tasks.DocumentBatch, file_path: str
) -> None
```

Write data to Parquet file using pandas DataFrame.to_parquet.

