---
layout: overview
slug: nemo-curator-stages-deduplication-fuzzy-connected-components
---

# nemo_curator.stages.deduplication.fuzzy.connected_components



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ConnectedComponentsStage`](#nemo_curatorstagesdeduplicationfuzzyconnected_componentsconnectedcomponentsstage) | Base class for all processing stages. Processing stages operate on Task objects (or subclasses like DocumentBatch). Each stage type can declare what type of Task it processes as input (X) and what type it produces as output (Y). Stages can return either: - A single task (typical for transformations) - A list of tasks (for stages that split work, like readers) - None (for filtered out tasks) |

### API

```python
class nemo_curator.stages.deduplication.fuzzy.connected_components.ConnectedComponentsStage(output_path: str, source_field: str | None = None, destination_field: str | None = None, read_kwargs: dict | None = None, write_kwargs: dict | None = None)
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.file_group.FileGroupTask, nemo_curator.tasks.file_group.FileGroupTask]`, `nemo_curator.stages.deduplication.io_utils.DeduplicationIO`

```python
setup(_worker_metadata: WorkerMetadata | None = None) -> None
```


```python
ray_stage_spec() -> dict[str, typing.Any]
```


```python
__get_2D_div(ngpus: int) -> tuple[int, int]
```

Cugraph 2d partitioning number of rows and columns


```python
_setup_post() -> None
```

Setup the sub-communicator for cuGraph communications.

This method is specific to cuGraph comms and is used to initialize the
sub-communicator.


```python
weakly_connected_components(
    df: cudf.DataFrame,
    src_col: str,
    dst_col: str
) -> None
```

Compute the weakly connected components of a graph.

This method loads a chunk of the graph, creates a cuGraph object, and
computes the weakly connected components using the MGGraph library.

Parameters
----------
start: int
    The start index of the chunk.
stop: int
    The stop index of the chunk.


```python
process(task: nemo_curator.tasks.file_group.FileGroupTask) -> nemo_curator.tasks.file_group.FileGroupTask
```


```python
process_batch(tasks: list[nemo_curator.tasks.file_group.FileGroupTask]) -> list[nemo_curator.tasks.file_group.FileGroupTask]
```

Process a batch of input files containing edges between documents.
Compute the weakly connected components of the graph and write a mapping of document ids to their connected component id.

Parameters
----------
tasks: list[FileGroupTask]
    A list of FileGroupTasks containing the input files.
Returns
-------
list[FileGroupTask]
    A list of FileGroupTasks containing the output doc_id to connected component id mapping.

