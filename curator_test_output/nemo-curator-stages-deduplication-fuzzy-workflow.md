---
layout: overview
slug: nemo-curator-stages-deduplication-fuzzy-workflow
---

# nemo_curator.stages.deduplication.fuzzy.workflow



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`FuzzyDeduplicationWorkflow`](#nemo_curatorstagesdeduplicationfuzzyworkflowfuzzydeduplicationworkflow) | A pipeline that performs fuzzy deduplication of a dataset. It consists of the following stages: - FilePartitioningStage Groups input files into smaller groups that can be processed in parallel. - MinHashStage Computes minhashes for the input dataset. - LSHStage Performs Locality Sensitive Hashing on the minhashes. This is a shuffle stage that involves moving data between workers. - BucketsToEdgesStage This stage converts the resulting LSH mapping of bucket ID to document ID into a graph of edges. - ConnectedComponentsStage Performs weaklyconnected components clustering on the graph represented by the edgelist. - IdentifyDuplicatesStage Generates a list of document ids to remove based on the connected components clusters/components. - Removal (Optional) Currently not implemented. |

### Data

`ID_GENERATOR_OUTPUT_FILENAME`

### API

```python
nemo_curator.stages.deduplication.fuzzy.workflow.ID_GENERATOR_OUTPUT_FILENAME
```

**Value**: `fuzzy_id_generator.json`


```python
class nemo_curator.stages.deduplication.fuzzy.workflow.FuzzyDeduplicationWorkflow(cache_path: str, output_path: str, input_path: str | list[str] | None = None, input_filetype: typing.Literal[jsonl, parquet] = 'parquet', input_blocksize: str | int = '1GiB', input_file_extensions: list[str] | None = None, read_kwargs: dict[str, typing.Any] | None = None, cache_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None, text_field: str = 'text', perform_removal: bool = False, seed: int = 42, char_ngrams: int = 24, num_bands: int = 20, minhashes_per_band: int = 13, use_64_bit_hash: bool = False, bands_per_iteration: int = 5, env_vars: dict[str, typing.Any] | None = None)
```

A pipeline that performs fuzzy deduplication of a dataset.
It consists of the following stages:
- FilePartitioningStage
    Groups input files into smaller groups that can be processed in parallel.
- MinHashStage
    Computes minhashes for the input dataset.
- LSHStage
    Performs Locality Sensitive Hashing on the minhashes.
    This is a shuffle stage that involves moving data between workers.
- BucketsToEdgesStage
    This stage converts the resulting LSH mapping of bucket ID to document ID into a graph of edges.
- ConnectedComponentsStage
    Performs weaklyconnected components clustering on the graph represented by the edgelist.
- IdentifyDuplicatesStage
    Generates a list of document ids to remove based on the connected components clusters/components.
- Removal (Optional)
    Currently not implemented.

### Initialization

Configuration for MinHash based fuzzy duplicates detection.
Parameters
cache_path: str
    Directory to store deduplication intermediates such as minhashes/buckets etc.
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
cache_kwargs: dict[str, Any] | None = None
    Additional keyword arguments to pass for intermediate files written to cache_dir.
    This could include the storage_options dictionary when writing to remote storage.
write_kwargs: dict[str, Any] | None = None
    Additional keyword arguments to pass for deduplicated results written to output_dir.
    This could include the storage_options dictionary when writing to remote storage.

text_field: str
    Field containing the text to deduplicate.
perform_removal: bool
    Whether to remove the duplicates from the original dataset.

seed: int
    Seed for minhash permutations
char_ngrams: int
    Size of Char ngram shingles used in minhash computation
num_buckets: int
    Number of Bands or buckets to use during Locality Sensitive Hashing
hashes_per_bucket: int
    Number of hashes per bucket/band.
use_64_bit_hash: bool
    Whether to use a 32bit or 64bit hash function for minhashing.
bands_per_iteration: int
    Number of bands/buckets to shuffle concurrently.
    Larger values process larger batches by processing multiple bands
    but might lead to memory pressures and related errors.

env_vars: dict[str, Any] | None = None
    Environment variables to pass to the pipeline.


```python
_validate_inputs() -> None
```


```python
_create_minhash_pipeline(generate_input_filegroups: bool) -> nemo_curator.pipeline.Pipeline
```


```python
_create_lsh_pipeline() -> nemo_curator.pipeline.Pipeline
```


```python
_create_connected_components_pipeline() -> nemo_curator.pipeline.Pipeline
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

