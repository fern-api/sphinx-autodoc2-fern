---
layout: overview
slug: nemo-curator-stages-deduplication-exact-workflow
---

# nemo_curator.stages.deduplication.exact.workflow



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ExactDeduplicationWorkflow`](#nemo_curatorstagesdeduplicationexactworkflowexactdeduplicationworkflow) | A pipeline that performs exact deduplication of a dataset. It consists of the following stages: - FilePartitioningStage Groups input files into smaller groups that can be processed in parallel. - ExactDuplicateIdentification Finds exact duplicates in a given column by hashing the column. - Removal (Optional) Currently not implemented. |

### Data

`ID_GENERATOR_OUTPUT_FILENAME`

### API

```python
nemo_curator.stages.deduplication.exact.workflow.ID_GENERATOR_OUTPUT_FILENAME
```

**Value**: `exact_id_generator.json`


```python
class nemo_curator.stages.deduplication.exact.workflow.ExactDeduplicationWorkflow(output_path: str, input_path: str | list[str] | None = None, input_filetype: typing.Literal[jsonl, parquet] = 'parquet', input_blocksize: str | int = '2GiB', input_file_extensions: list[str] | None = None, read_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None, assign_id: bool = True, id_field: str | None = None, text_field: str = 'text', perform_removal: bool = False, env_vars: dict[str, typing.Any] | None = None)
```

A pipeline that performs exact deduplication of a dataset.
It consists of the following stages:
- FilePartitioningStage
    Groups input files into smaller groups that can be processed in parallel.
- ExactDuplicateIdentification
    Finds exact duplicates in a given column by hashing the column.
- Removal (Optional)
    Currently not implemented.

### Initialization

Configuration for exact duplicates detection.
Parameters
output_path: str
    Directory to store the duplicate Ids and the id generator mapping for removal pipelines.
    It also stores the deduplicated output files, if `perform_removal` is True.
input_path: str | list[str] | None
    Directory or list of files containing the input dataset.
    Unused if `initial_tasks` is provided during workflow run.
input_filetype: Literal["jsonl", "parquet"]
    Format of the input dataset.
input_blocksize: str | int
    Size of the input blocks to read in.
    If an integer is provided, it will be interpreted as bytes.
    If a string is provided, it will be interpreted as a size with a unit.
    If not provided, the default blocksize of 1GiB will be used.
input_file_extensions: list[str] | None
    File extensions of the input dataset.
    If not provided, the default extensions for the input_filetype will be used.
    If provided, this will override the default extensions for the input_filetype.
read_kwargs: dict[str, Any] | None = None
    Additional keyword arguments to pass for reading the input files.
    This could include the storage_options dictionary when reading from remote storage.
write_kwargs: dict[str, Any] | None = None
    Additional keyword arguments to pass for deduplicated results written to output_dir.
    This could include the storage_options dictionary when writing to remote storage.
assign_id: bool
    Whether to automatically assign a unique id to each document.
id_field: str | None
    Existing id field name if not automatically assigning a new id.
text_field: str
    Field containing the text to deduplicate.
perform_removal: bool
    Whether to remove the duplicates from the original dataset.
env_vars: dict[str, Any] | None = None
    Environment variables to pass to the pipeline.


```python
_validate_inputs() -> None
```


```python
_create_input_filegroups() -> nemo_curator.pipeline.Pipeline
```


```python
_create_identification_pipeline(num_input_tasks: int) -> nemo_curator.pipeline.Pipeline
```


```python
_validate_initial_tasks(initial_tasks: list[nemo_curator.tasks.FileGroupTask] | None) -> None
```


```python
run(initial_tasks: list[nemo_curator.tasks.FileGroupTask] | None = None) -> None
```

Run the deduplication pipeline.

**Parameters:**

<ParamField path="initial_tasks" type="list[nemo_curator.tasks.FileGroupTask] | None">
</ParamField>

