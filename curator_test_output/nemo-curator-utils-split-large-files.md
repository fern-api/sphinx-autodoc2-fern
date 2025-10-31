---
layout: overview
slug: nemo-curator-utils-split-large-files
---

# nemo_curator.utils.split_large_files



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`_split_table`](#nemo_curatorutilssplit_large_files_split_table) | None |
| [`_write_table_to_file`](#nemo_curatorutilssplit_large_files_write_table_to_file) | None |
| [`split_parquet_file_by_size`](#nemo_curatorutilssplit_large_filessplit_parquet_file_by_size) | None |
| [`parse_args`](#nemo_curatorutilssplit_large_filesparse_args) | None |
| [`main`](#nemo_curatorutilssplit_large_filesmain) | None |

### API

```python
nemo_curator.utils.split_large_files._split_table(
    table: pyarrow.Table, target_size: int
) -> list[pyarrow.Table]
```


```python
nemo_curator.utils.split_large_files._write_table_to_file(
    table: pyarrow.Table,
    outdir: str,
    output_prefix: str,
    ext: str,
    file_idx: int
) -> int
```


```python
nemo_curator.utils.split_large_files.split_parquet_file_by_size(
    input_file: str,
    outdir: str,
    target_size_mb: int
) -> None
```


```python
nemo_curator.utils.split_large_files.parse_args(args: argparse.ArgumentParser | None = None) -> argparse.Namespace
```


```python
nemo_curator.utils.split_large_files.main(args: argparse.ArgumentParser | None = None) -> None
```

