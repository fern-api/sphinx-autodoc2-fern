---
layout: overview
slug: nemo-curator-stages-deduplication-semantic-kmeans
---

# nemo_curator.stages.deduplication.semantic.kmeans



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`KMeansReadFitWriteStage`](#nemo_curatorstagesdeduplicationsemantickmeanskmeansreadfitwritestage) | KMeans clustering stage that requires RAFT for distributed processing. |
| [`KMeansStage`](#nemo_curatorstagesdeduplicationsemantickmeanskmeansstage) | KMeans clustering stage that requires RAFT for distributed processing. |

### Data

`L2_DIST_TO_CENT_COL`
`COSINE_DIST_TO_CENT_COL`

### API

```python
nemo_curator.stages.deduplication.semantic.kmeans.L2_DIST_TO_CENT_COL
```

**Value**: `l2_dist_to_cent`


```python
nemo_curator.stages.deduplication.semantic.kmeans.COSINE_DIST_TO_CENT_COL
```

**Value**: `cosine_dist_to_cent`


```python
class nemo_curator.stages.deduplication.semantic.kmeans.KMeansReadFitWriteStage(id_field: str, embedding_field: str, output_path: str, filetype: typing.Literal[parquet, jsonl], n_clusters: int, metadata_fields: list[str] | None = None, embedding_dim: int | None = None, verbose: bool = False, max_iter: int = 300, tol: float = 0.0001, random_state: int = 42, init: typing.Literal[k-means||, random] | numpy.ndarray = 'k-means||', n_init: int | typing.Literal[auto] = 1, oversampling_factor: float = 2.0, max_samples_per_batch: int = 1 << 15, read_kwargs: dict[dict] | None = None, write_kwargs: dict[dict] | None = None)
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks._EmptyTask]`, `nemo_curator.stages.deduplication.io_utils.DeduplicationIO`

KMeans clustering stage that requires RAFT for distributed processing.

### Initialization

KMeans clustering stage that requires RAFT for distributed processing.

**Parameters:**

- **id_field (str)**: The column name of the id column.
- **embedding_field (str)**: The column name of the embedding column.
- **output_path (str)**: The path to the output directory.
- **n_clusters (int)**: The number of clusters to create.
- **metadata_fields (list[str] | None)**: The columns to keep in the output. These columns can be used later to prioritize deduplication.
- **embedding_dim (int | None)**: The dimension of the embedding. This helps us read data into smaller chunks.
- **verbose (bool)**: Whether to print verbose output.
- **max_iter (int)**: The maximum number of iterations to run.
- **tol (float)**: Tolerance for stopping criteria of the kmeans algorithm.
- **random_state (int)**: Seed for the random number generator. Unseeded by default. Does not currently fully guarantee the exact same results.
- **init (Literal["k-means||", "random"] | np.ndarray)**: 'scalable-k-means++' or 'k-means||': Uses fast and stable scalable kmeans++ initialization. 'random': Choose 'n_cluster' observations (rows) at random from data for the initial centroids. If an ndarray is passed, it should be of shape (n_clusters, n_features) and gives the initial centers.
- **n_init (int | Literal["auto"])**: Number of times the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n_init consecutive runs in terms of inertia.
- **oversampling_factor (float)**: The amount of points to sample in scalable k-means++ initialization for potential centroids. Increasing this value can lead to better initial centroids at the cost of memory. The total number of centroids sampled in scalable k-means++ is oversampling_factor * n_clusters * 8.
- **max_samples_per_batch (int)**: The number of data samples to use for batches of the pairwise distance computation. This computation is done throughout both fit predict. The default should suit most cases. The total number of elements in the batched pairwise distance computation is max_samples_per_batch * n_clusters. It might become necessary to lower this number when n_clusters becomes prohibitively large.
- **read_kwargs (dict[dict])**: Keyword arguments for the read stage.
- **write_kwargs (dict[dict])**: Keyword arguments for the write stage.


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks._EmptyTask
```


```python
process_batch(tasks: list[nemo_curator.tasks.FileGroupTask]) -> list[nemo_curator.tasks._EmptyTask]
```

Process a batch of FileGroupTasks using distributed RAFT KMeans.

In RAFT mode, each actor processes its assigned tasks, but the KMeans model
is trained cooperatively across all actors using RAFT communication.

This method:
1. Reads data from this actor's assigned tasks
2. Breaks data into subgroups to avoid cudf row limits
3. Fits distributed KMeans model (coordinates with other actors via RAFT)
4. Assigns cluster centroids back to each subgroup
5. Writes the results for each subgroup


```python
setup(_: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
normalize_embeddings_col_in_df(
    df: cudf.DataFrame, embedding_col: str
) -> cudf.DataFrame
```


```python
_assign_distances(
    df: cudf.DataFrame,
    embedding_col: str,
    centroids: cupy.ndarray
) -> cudf.DataFrame
```

Computes the L2 distance to nearest centroid to each embedding in the DataFrame.
Embeddings are normalized. For cosine we'll need to normalize the centroids as well.


```python
ray_stage_spec() -> dict[str, typing.Any]
```


```python
class nemo_curator.stages.deduplication.semantic.kmeans.KMeansStage
```

**Bases**: `nemo_curator.stages.base.CompositeStage[nemo_curator.tasks._EmptyTask, nemo_curator.tasks._EmptyTask]`

KMeans clustering stage that requires RAFT for distributed processing.

```python
n_clusters: int
```

**Value**: `None`


```python
id_field: str
```

**Value**: `None`


```python
embedding_field: str
```

**Value**: `None`


```python
input_path: str | list[str]
```

**Value**: `None`


```python
output_path: str
```

**Value**: `None`


```python
metadata_fields: list[str] | None
```

**Value**: `None`


```python
verbose: bool
```

**Value**: `False`


```python
embedding_dim: int | None
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
read_kwargs: dict[dict] | None
```

**Value**: `None`


```python
write_kwargs: dict[dict] | None
```

**Value**: `None`


```python
max_iter: int
```

**Value**: `300`


```python
tol: float
```

**Value**: `0.0001`


```python
random_state: int
```

**Value**: `42`


```python
init: typing.Literal[k-means||, random] | numpy.ndarray
```

**Value**: `k-means||`


```python
n_init: int | typing.Literal[auto]
```

**Value**: `1`


```python
oversampling_factor: float
```

**Value**: `2.0`


```python
max_samples_per_batch: int
```

**Value**: `None`

KMeans clustering stage that requires RAFT for distributed processing.

**Parameters:**

- **n_clusters (int)**: The number of clusters to create.
- **id_field (str)**: The column name of the id column.
- **embedding_field (str)**: The column name of the embedding column.
- **input_path (str | list[str])**: The path to the input directory.
- **output_path (str)**: The path to the output directory.
- **metadata_fields (list[str] | None)**: The columns to keep in the output. These columns can be used later to prioritize deduplication.
- **verbose (bool)**: Whether to print verbose output.
- **embedding_dim (int | None)**: The dimension of the embedding. This helps us read data into smaller chunks.
- **input_filetype (Literal["jsonl", "parquet"])**: The type of the input file
- **read_kwargs (dict[dict])**: Keyword arguments for the read stage.
- **write_kwargs (dict[dict])**: Keyword arguments for the write stage.
- **max_iter (int)**: The maximum number of iterations to run.
- **tol (float)**: Tolerance for stopping criteria of the kmeans algorithm.
- **random_state (int)**: Seed for the random number generator. Unseeded by default. Does not currently fully guarantee the exact same results.
- **init (Literal["k-means||", "random"] | np.ndarray)**: 'scalable-k-means++' or 'k-means||': Uses fast and stable scalable kmeans++ initialization. 'random': Choose 'n_cluster' observations (rows) at random from data for the initial centroids. If an ndarray is passed, it should be of shape (n_clusters, n_features) and gives the initial centers.
- **n_init (int | Literal["auto"])**: Number of times the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n_init consecutive runs in terms of inertia.
- **oversampling_factor (float)**: The amount of points to sample in scalable k-means++ initialization for potential centroids. Increasing this value can lead to better initial centroids at the cost of memory. The total number of centroids sampled in scalable k-means++ is oversampling_factor * n_clusters * 8.
- **max_samples_per_batch (int)**: The number of data samples to use for batches of the pairwise distance computation. This computation is done throughout both fit predict. The default should suit most cases. The total number of elements in the batched pairwise distance computation is max_samples_per_batch * n_clusters. It might become necessary to lower this number when n_clusters becomes prohibitively large.


```python
__post_init__()
```

Initialize parent class after dataclass initialization.


```python
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

