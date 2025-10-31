---
layout: overview
slug: nemo-curator-stages-deduplication-semantic-pairwise-io
---

# nemo_curator.stages.deduplication.semantic.pairwise_io



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ClusterWiseFilePartitioningStage`](#nemo_curatorstagesdeduplicationsemanticpairwise_ioclusterwisefilepartitioningstage) | Stage that partitions input files into PairwiseFileGroupTasks for deduplication. |

### API

```python
class nemo_curator.stages.deduplication.semantic.pairwise_io.ClusterWiseFilePartitioningStage(input_path: str, storage_options: dict[str, typing.Any] | None = None)
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks._EmptyTask, nemo_curator.tasks.FileGroupTask]`

Stage that partitions input files into PairwiseFileGroupTasks for deduplication.

This stage takes an EmptyTask as input and outputs partition-aware file groups.
It reads parquet files partitioned by centroid (from kmeans output) and creates
one PairwiseFileGroupTask per centroid partition.

### Initialization

Initialize the partitioning stage.

**Parameters:**

- **input_path**: Path to the kmeans output directory containing centroid partitions
- **storage_options**: Storage options for reading files
- **limit**: Maximum number of partitions to process


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
setup(_: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
ray_stage_spec() -> dict[str, typing.Any]
```

Ray stage specification for this stage.


```python
process(_: nemo_curator.tasks._EmptyTask) -> list[nemo_curator.tasks.FileGroupTask]
```

Process the EmptyTask to create PairwiseFileGroupTasks.

**Parameters:**

**Returns:**

List of PairwiseFileGroupTask, each containing partitioned file groups per centroid

