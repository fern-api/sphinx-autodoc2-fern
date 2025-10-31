---
layout: overview
slug: nemo-curator-stages-deduplication-semantic-pairwise
---

# nemo_curator.stages.deduplication.semantic.pairwise



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`PairwiseCosineSimilarityStage`](#nemo_curatorstagesdeduplicationsemanticpairwisepairwisecosinesimilaritystage) | Pairwise cosine similarity stage that computes similarity within clusters. |
| [`PairwiseStage`](#nemo_curatorstagesdeduplicationsemanticpairwisepairwisestage) | Pairwise similarity stage for semantic deduplication. |

### Functions

| Name | Description |
|------|-------------|
| [`pairwise_cosine_similarity_batched`](#nemo_curatorstagesdeduplicationsemanticpairwisepairwise_cosine_similarity_batched) | Computes pairwise cosine similarity between cluster items, then replace to diagonal with zeros to ignore self similarity. This function is useful for large clusters where the pairwise similarity matrix does not fit into memory. We use a batched approach to compute the pairwise similarity matrix in batches. Memory requirements are O(N*B) where N is the number of items in the cluster and B is the batch size instead of O(N^2) for the full matrix. |

### API

```python
nemo_curator.stages.deduplication.semantic.pairwise.pairwise_cosine_similarity_batched(
    cluster_reps: torch.Tensor, batch_size: int = 1024
) -> tuple[cupy.ndarray, cupy.ndarray] | tuple[numpy.ndarray, numpy.ndarray]
```

Computes pairwise cosine similarity between cluster items,
then replace to diagonal with zeros to ignore self similarity.
This function is useful for large clusters where the pairwise similarity matrix
does not fit into memory.
We use a batched approach to compute the pairwise similarity matrix in batches.
Memory requirements are O(N*B) where N is the number of items in the cluster and B is the batch size
instead of O(N^2) for the full matrix.

TODO: In future we can estimate memory requirement and calculate batch size dynamically.


```python
class nemo_curator.stages.deduplication.semantic.pairwise.PairwiseCosineSimilarityStage(id_field: str, embedding_field: str, output_path: str, ranking_strategy: nemo_curator.stages.deduplication.semantic.ranking.RankingStrategy, pairwise_batch_size: int = 1024, verbose: bool = False, embedding_dim: int | None = None, read_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None)
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks.FileGroupTask]`, `nemo_curator.stages.deduplication.io_utils.DeduplicationIO`

Pairwise cosine similarity stage that computes similarity within clusters.

### Initialization

Initialize the pairwise cosine similarity stage.

**Parameters:**

- **id_field**: The column name of the id column.
- **embedding_field**: The column name of the embedding column.
- **output_path**: The path to the output directory.
- **ranking_strategy**: Strategy for ranking/sorting clusters before similarity computation.
- **pairwise_batch_size**: Batch size for pairwise similarity computation.
- **verbose**: Whether to print verbose output.
- **embedding_dim**: Embedding dimension for memory estimation.
- **read_kwargs**: Kwargs for reading parquet files.
- **write_kwargs**: Kwargs for writing parquet files.


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```

Process a PairwiseFileGroupTask to compute pairwise similarities.


```python
class nemo_curator.stages.deduplication.semantic.pairwise.PairwiseStage
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks._EmptyTask, nemo_curator.tasks.FileGroupTask]`

Pairwise similarity stage for semantic deduplication.

```python
id_field: str
```

**Value**: `None`


```python
embedding_field: str
```

**Value**: `None`


```python
input_path: str
```

**Value**: `None`


```python
output_path: str
```

**Value**: `None`


```python
ranking_strategy: nemo_curator.stages.deduplication.semantic.ranking.RankingStrategy | None
```

**Value**: `None`


```python
embedding_dim: int | None
```

**Value**: `None`


```python
pairwise_batch_size: int
```

**Value**: `1024`


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
which_to_keep: typing.Literal[hard, easy, random]
```

**Value**: `hard`


```python
sim_metric: typing.Literal[cosine, l2]
```

**Value**: `cosine`


```python
random_seed: int
```

**Value**: `42`


```python
__post_init__()
```

Initialize parent class after dataclass initialization.


```python
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

