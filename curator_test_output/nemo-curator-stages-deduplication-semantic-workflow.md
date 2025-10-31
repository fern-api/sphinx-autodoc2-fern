---
layout: overview
slug: nemo-curator-stages-deduplication-semantic-workflow
---

# nemo_curator.stages.deduplication.semantic.workflow

End-to-End Semantic Deduplication Pipeline for Ray Curator.

This module contains the complete semantic deduplication workflow:
1. K-means clustering on embedding data (always uses RayActorPoolExecutor)
2. Pairwise similarity computation within clusters + duplicate identification (configurable executor)

## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`SemanticDeduplicationWorkflow`](#nemo_curatorstagesdeduplicationsemanticworkflowsemanticdeduplicationworkflow) | End-to-End Semantic Deduplication Workflow. It consists of the following stages: - KMeansStage Takes the input path (embeddings) and clusters the embeddings into n_clusters. Writes data partitioned by centroid to cache_path. - PairwiseStage Computes pairwise similarity between all embeddings in each cluster. Takes the output of KMeansStage and computes pairwise similarity between all embeddings in each cluster. This is written to cache_path. - IdentifyDuplicatesStage (optional) Identifies duplicates based on the pairwise similarity scores. Runs only if eps is provided. This is written to output_path. |

### API

```python
class nemo_curator.stages.deduplication.semantic.workflow.SemanticDeduplicationWorkflow(input_path: str | list[str], output_path: str, n_clusters: int, cache_path: str | None = None, id_field: str = 'id', embedding_field: str = 'embeddings', embedding_dim: int | None = None, metadata_fields: list[str] | None = None, input_filetype: typing.Literal[parquet, jsonl] = 'parquet', input_file_extensions: list[str] | None = None, max_iter: int = 300, tol: float = 0.0001, random_state: int = 42, init: typing.Literal[k-means||, random] | numpy.ndarray = 'k-means||', n_init: int | typing.Literal[auto] = 1, oversampling_factor: float = 2.0, max_samples_per_batch: int = 1 << 15, distance_metric: typing.Literal[cosine, l2] = 'cosine', which_to_keep: typing.Literal[hard, easy, random] = 'hard', ranking_strategy: nemo_curator.stages.deduplication.semantic.ranking.RankingStrategy | None = None, pairwise_batch_size: int = 1024, eps: float | None = None, _duplicates_num_row_groups_hint: int | None = None, read_kwargs: dict[str, typing.Any] | None = None, cache_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None, clear_output: bool = True, verbose: bool = True)
```

End-to-End Semantic Deduplication Workflow.
It consists of the following stages:
- KMeansStage
    Takes the input path (embeddings) and clusters the embeddings into n_clusters.
    Writes data partitioned by centroid to cache_path.
- PairwiseStage
    Computes pairwise similarity between all embeddings in each cluster.
    Takes the output of KMeansStage and computes pairwise similarity between all embeddings in each cluster.
    This is written to cache_path.
- IdentifyDuplicatesStage (optional)
    Identifies duplicates based on the pairwise similarity scores.
    Runs only if eps is provided.
    This is written to output_path.

### Initialization

Initialize the semantic deduplication workflow.

**Parameters:**

- **input_path**: Directory or list of directories containing input files with embeddings
- **output_path**: Directory to write output files (i.e. ids to remove)
- **n_clusters**: Number of clusters for K-means
- **cache_path**: Directory to write cache files (i.e. kmeans and pairwise results)
  If None, will be set to output_path
  # Core data configuration
- **id_field**: Name of the ID field in the data
- **embedding_field**: Name of the embedding field in the data
- **embedding_dim**: Embedding dimension (for memory estimation)
- **metadata_fields**: List of metadata field names to preserve in output
- **input_filetype**: Type of input files ("parquet" or "jsonl")
- **input_file_extensions**: List of file extensions to process
  # K-means clustering parameters
- **max_iter**: Maximum number of K-means iterations
- **tol**: Tolerance for K-means convergence
- **random_state**: Random seed for K-means
- **init**: K-means initialization method
- **n_init**: Number of K-means initializations
- **oversampling_factor**: K-means++ oversampling factor
- **max_samples_per_batch**: Max samples per batch for K-means
- **distance_metric**: Distance metric for similarity ("cosine" or "l2")
  # Pairwise similarity parameters
- **which_to_keep**: Strategy for ranking within clusters ("hard", "easy", "random")
- **ranking_strategy**: Custom ranking strategy (overrides which_to_keep)
- **pairwise_batch_size**: Batch size for pairwise similarity computation
  # Duplicate identification parameters (optional)
- **eps**: Epsilon value for duplicate identification
- **_duplicates_num_row_groups_hint**: Number of row groups hint for duplicate removal
  # I/O and storage parameters
- **read_kwargs**: Keyword arguments for reading files (including storage_options)
- **write_kwargs**: Keyword arguments for writing files (including storage_options)
- **clear_output**: Clear output directory before running
  # Execution parameters
- **verbose**: Enable verbose output


```python
_validate_config() -> None
```

Validate the configuration.


```python
_setup_directories() -> None
```

Setup output directories with fsspec compliance.


```python
_run_kmeans_stage() -> list[typing.Any]
```

Run K-means clustering stage (always uses RayActorPoolExecutor).


```python
_run_pairwise_stage(pairwise_executor: nemo_curator.backends.base.BaseExecutor | None = None) -> list[typing.Any]
```

Run pairwise similarity + duplicate identification stage.


```python
_log_configuration(pairwise_executor: nemo_curator.backends.base.BaseExecutor | None = None) -> None
```

Log workflow configuration.


```python
run(pairwise_executor: nemo_curator.backends.base.BaseExecutor | None = None) -> dict[str, typing.Any]
```

Run the complete semantic deduplication pipeline.

**Parameters:**

<ParamField path="pairwise_executor" type="nemo_curator.backends.base.BaseExecutor | None">
  Executor for pairwise stage. Defaults to XennaExecutor().
</ParamField>

**Returns:**

Dictionary with results and timing information

