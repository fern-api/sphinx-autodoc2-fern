---
layout: overview
slug: nemo-curator-backends-experimental-ray-actor-pool-shuffle-adapter
---

# nemo_curator.backends.experimental.ray_actor_pool.shuffle_adapter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ShuffleStageAdapter`](#nemo_curatorbackendsexperimentalray_actor_poolshuffle_adaptershufflestageadapter) | Ray actor that wraps a shuffle stage and its actor. |

### API

```python
class nemo_curator.backends.experimental.ray_actor_pool.shuffle_adapter.ShuffleStageAdapter(stage: ShuffleStage | LSHStage, rank: int, nranks: int, num_input_tasks: int | None = None)
```

**Bases**: `nemo_curator.backends.base.BaseStageAdapter`

Ray actor that wraps a shuffle stage and its actor.

This adapter manages the lifecycle of a shuffle actor (like LSHActor)
and provides a uniform interface for the executor.

### Initialization

Initialize the adapter.

**Parameters:**

- **stage**: The shuffle stage to wrap
- **rank**: This actor's rank in the group
- **nranks**: Total number of actors in the group
- **session_id**: Unique session identifier
- **input_nparts**: Total input partitions


```python
get_batch_size() -> int
```

Get the batch size for this stage.


```python
setup_on_node() -> None
```

<Note> This method is not used in the current implementation since we use </Note>


```python
setup(
    root_address: bytes, worker_metadata: WorkerMetadata | None = None
) -> None
```

Setup shuffle workers and stage


```python
setup_root() -> None
```

Setup the root actor.


```python
setup_worker(root_address: bytes) -> None
```

Setup UCXX communication.


```python
read_and_insert(
    tasks: list[nemo_curator.tasks.FileGroupTask],
    band_range: tuple[int, int] | None = None
) -> list[nemo_curator.tasks.FileGroupTask]
```

Read and insert tasks into the shuffler.


```python
insert_finished() -> None
```

Finish the insertion phase and trigger shuffle.


```python
extract_and_write() -> list[nemo_curator.tasks.FileGroupTask]
```

Extract shuffled data and write to output files.


```python
teardown() -> None
```

Clean up resources.

