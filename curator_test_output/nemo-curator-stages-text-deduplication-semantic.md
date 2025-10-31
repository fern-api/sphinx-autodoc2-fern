---
layout: overview
slug: nemo-curator-stages-text-deduplication-semantic
---

# nemo_curator.stages.text.deduplication.semantic

Monolithic Text Semantic Deduplication Workflow.

This module contains a complete end-to-end workflow for text semantic deduplication:
1. Embedding generation from text data
2. Semantic deduplication using clustering and pairwise similarity
3. Optional duplicate removal based on identified duplicates

## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`TextSemanticDeduplicationWorkflow`](#nemo_curatorstagestextdeduplicationsemantictextsemanticdeduplicationworkflow) | Monolithic workflow for end-to-end text semantic deduplication. |

### API

```python
class nemo_curator.stages.text.deduplication.semantic.TextSemanticDeduplicationWorkflow
```

Monolithic workflow for end-to-end text semantic deduplication.

This workflow combines:
1. Text embedding generation (configurable executor)
2. Semantic deduplication (configurable executor for pairwise stage)
3. Duplicate removal (configurable executor)

Supports flexible executor configuration - can use a single executor for all stages
or different executors for different phases.

```python
input_path: str | list[str]
```

**Value**: `None`


```python
output_path: str
```

**Value**: `None`


```python
cache_path: str | None
```

**Value**: `None`


```python
perform_removal: bool
```

**Value**: `True`


```python
text_field: str
```

**Value**: `text`


```python
embedding_field: str
```

**Value**: `embeddings`


```python
model_identifier: str
```

**Value**: `sentence-transformers/all-MiniLM-L6-v2`


```python
embedding_max_seq_length: int
```

**Value**: `512`


```python
embedding_max_chars: int | None
```

**Value**: `None`


```python
embedding_padding_side: typing.Literal[left, right]
```

**Value**: `right`


```python
embedding_pooling: typing.Literal[mean_pooling, last_token]
```

**Value**: `mean_pooling`


```python
embedding_model_inference_batch_size: int
```

**Value**: `256`


```python
hf_token: str | None
```

**Value**: `None`


```python
n_clusters: int
```

**Value**: `100`


```python
id_field: str
```

**Value**: `None`


```python
embedding_dim: int | None
```

**Value**: `None`


```python
metadata_fields: list[str] | None
```

**Value**: `None`


```python
distance_metric: typing.Literal[cosine, l2]
```

**Value**: `cosine`


```python
which_to_keep: typing.Literal[hard, easy, random]
```

**Value**: `hard`


```python
eps: float | None
```

**Value**: `0.01`


```python
kmeans_max_iter: int
```

**Value**: `300`


```python
kmeans_tol: float
```

**Value**: `0.0001`


```python
kmeans_random_state: int
```

**Value**: `42`


```python
kmeans_init: str
```

**Value**: `k-means||`


```python
kmeans_n_init: int | typing.Literal[auto]
```

**Value**: `1`


```python
kmeans_oversampling_factor: float
```

**Value**: `2.0`


```python
kmeans_max_samples_per_batch: int
```

**Value**: `None`


```python
ranking_strategy: nemo_curator.stages.deduplication.semantic.ranking.RankingStrategy | None
```

**Value**: `None`


```python
pairwise_batch_size: int
```

**Value**: `1024`


```python
_duplicates_num_row_groups_hint: int | None
```

**Value**: `None`


```python
use_id_generator: bool
```

**Value**: `False`


```python
id_generator_state_file: str | None
```

**Value**: `None`


```python
input_filetype: typing.Literal[jsonl, parquet]
```

**Value**: `parquet`


```python
input_file_extensions: list[str] | None
```

**Value**: `None`


```python
input_files_per_partition: int | None
```

**Value**: `None`


```python
input_blocksize: int | None
```

**Value**: `None`


```python
output_filetype: typing.Literal[jsonl, parquet]
```

**Value**: `parquet`


```python
output_file_extension: str | None
```

**Value**: `None`


```python
output_fields: list[str] | None
```

**Value**: `None`


```python
read_kwargs: dict[str, typing.Any]
```

**Value**: `field(...)`


```python
cache_kwargs: dict[str, typing.Any]
```

**Value**: `field(...)`


```python
write_kwargs: dict[str, typing.Any]
```

**Value**: `field(...)`


```python
verbose: bool
```

**Value**: `True`


```python
clear_output: bool
```

**Value**: `True`

Initialize the text semantic deduplication workflow.

**Parameters:**

- **input_path**: Path(s) to input files containing text data
- **output_path**: Directory to write deduplicated (or ids to remove) output
- **cache_path**: Directory to cache intermediate results (embeddings, kmeans, pairwise, etc.)
- **perform_removal**: Whether to perform duplicate removal (True) or just identify duplicates (False)
  # Embedding generation parameters
- **text_field**: Name of the text field in input data
- **embedding_field**: Name of the embedding field to create
- **model_identifier**: HuggingFace model identifier for embeddings
- **embedding_max_seq_length**: Maximum sequence length for tokenization
- **embedding_max_chars**: Maximum number of characters for tokenization
- **embedding_padding_side**: Padding side for tokenization
- **embedding_pooling**: Pooling strategy for embeddings
- **embedding_model_inference_batch_size**: Batch size for model inference
- **hf_token**: HuggingFace token for private models
  # Semantic deduplication parameters
- **n_clusters**: Number of clusters for K-means
- **id_field**: Name of the ID field in the data
- **embedding_dim**: Embedding dimension (for memory estimation)
- **metadata_fields**: List of metadata field names to preserve
- **distance_metric**: Distance metric for similarity ("cosine" or "l2")
- **which_to_keep**: Strategy for ranking within clusters ("hard", "easy", "random")
- **eps**: Epsilon value for duplicate identification (None to skip)
- **kmeans_max_iter**: Maximum number of iterations for K-means clustering
- **kmeans_tol**: Tolerance for K-means convergence
- **kmeans_random_state**: Random state for K-means (None for random)
- **kmeans_init**: Initialization method for K-means centroids
- **kmeans_n_init**: Number of K-means initialization runs
- **kmeans_oversampling_factor**: Oversampling factor for K-means
- **kmeans_max_samples_per_batch**: Maximum samples per batch for K-means
- **ranking_strategy**: Custom ranking strategy for documents within clusters (None uses which_to_keep/distance_metric)
- **pairwise_batch_size**: Batch size for pairwise similarity computation
- **_duplicates_num_row_groups_hint**: Hint for number of row groups in duplicates output
  # ID generator parameters
- **use_id_generator**: Whether to use ID generator for document IDs
- **id_generator_state_file**: Path to save/load ID generator state (auto-generated if None)
  # I/O parameters
- **input_files_per_partition**: Number of files per partition for reading
- **input_blocksize**: Blocksize for reading files
- **input_filetype**: Type of input files ("jsonl" or "parquet")
- **input_file_extensions**: List of file extensions to process
- **output_filetype**: Type of output files ("jsonl" or "parquet")
- **output_file_extension**: File extension for output files (None for default)
- **output_fields**: List of fields to include in final output (None for all fields)
- **read_kwargs**: Keyword arguments for reading files
- **cache_kwargs**: Keyword arguments for cache operations and storage
- **write_kwargs**: Keyword arguments for writing files
  # Execution parameters
- **verbose**: Enable verbose output
- **clear_output**: Clear output directory before running


```python
__post_init__()
```

Initialize parent class after dataclass initialization.


```python
_validate_config() -> None
```

Validate workflow configuration.


```python
_setup_directories() -> None
```

Setup output directories.


```python
_run_embedding_generation(executor: nemo_curator.backends.base.BaseExecutor) -> list[typing.Any]
```

Run embedding generation stage.


```python
_run_semantic_deduplication(executor: nemo_curator.backends.base.BaseExecutor) -> dict[str, typing.Any]
```

Run semantic deduplication stage.


```python
_run_duplicate_removal(executor: nemo_curator.backends.base.BaseExecutor) -> list[typing.Any]
```

Run duplicate removal stage.


```python
_log_configuration() -> None
```

Log workflow configuration.


```python
run(executor: nemo_curator.backends.base.BaseExecutor | tuple[nemo_curator.backends.base.BaseExecutor, nemo_curator.backends.base.BaseExecutor, nemo_curator.backends.base.BaseExecutor] | None = None) -> dict[str, typing.Any]
```

Run the complete text semantic deduplication workflow.

**Returns:**

Dictionary with results and timing information from all stages

