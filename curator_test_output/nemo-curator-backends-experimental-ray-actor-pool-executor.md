---
layout: overview
slug: nemo-curator-backends-experimental-ray-actor-pool-executor
---

# nemo_curator.backends.experimental.ray_actor_pool.executor



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`RayActorPoolExecutor`](#nemo_curatorbackendsexperimentalray_actor_poolexecutorrayactorpoolexecutor) | Ray-based executor using ActorPool for better resource management. |

### Functions

| Name | Description |
|------|-------------|
| [`_parse_runtime_env`](#nemo_curatorbackendsexperimentalray_actor_poolexecutor_parse_runtime_env) | None |

### Data

`_LARGE_INT`

### API

```python
nemo_curator.backends.experimental.ray_actor_pool.executor._LARGE_INT
```

**Value**: `None`


```python
nemo_curator.backends.experimental.ray_actor_pool.executor._parse_runtime_env(runtime_env: dict) -> dict
```


```python
class nemo_curator.backends.experimental.ray_actor_pool.executor.RayActorPoolExecutor(config: dict | None = None)
```

**Bases**: `nemo_curator.backends.base.BaseExecutor`

Ray-based executor using ActorPool for better resource management.

This executor:
1. Creates a pool of actors per stage using Ray's ActorPool
2. Uses map_unordered for better load balancing and fault tolerance
3. Lets Ray handle object ownership and garbage collection automatically
4. Provides better backpressure management through ActorPool

```python
execute(
    stages: list[nemo_curator.stages.base.ProcessingStage],
    initial_tasks: list[nemo_curator.tasks.Task] | None = None
) -> list[nemo_curator.tasks.Task]
```

Execute the pipeline stages using ActorPool.

**Parameters:**

<ParamField path="stages" type="list[nemo_curator.stages.base.ProcessingStage]">
  List of processing stages to execute
</ParamField>

<ParamField path="initial_tasks" type="list[nemo_curator.tasks.Task] | None">
  Initial tasks to process (can be None for empty start)
</ParamField>

**Returns:**

List of final processed tasks


```python
_create_actor_pool(
    stage: nemo_curator.stages.base.ProcessingStage, num_actors: int
) -> ray.util.actor_pool.ActorPool
```

Create an ActorPool for a specific stage.


```python
_create_raft_actor_pool(
    stage: nemo_curator.stages.base.ProcessingStage,
    num_actors: int,
    session_id: bytes
) -> ray.util.actor_pool.ActorPool
```

Create a RAFT ActorPool for a specific stage.


```python
_create_rapidsmpf_actors(
    stage: nemo_curator.stages.base.ProcessingStage,
    num_actors: int,
    num_tasks: int
) -> list[ray.actor.ActorHandle]
```

Create a RapidsMPFShuffling Actors and setup UCXX communication for a specific stage.


```python
_generate_task_batches(
    tasks: list[nemo_curator.tasks.Task],
    batch_size: int | None = None,
    num_output_tasks: int | None = None
) -> list[list[nemo_curator.tasks.Task]]
```

Generate task batches from a list of tasks.

**Parameters:**

<ParamField path="tasks" type="list[nemo_curator.tasks.Task]">
  List of Task objects to process
</ParamField>

<ParamField path="batch_size" type="int | None">
  The size of the batch
</ParamField>

<ParamField path="num_output_tasks" type="int | None">
  The number of output tasks to generate.
</ParamField>

**Returns:**

List of task batches


```python
_process_stage_with_pool(
    actor_pool: ray.util.actor_pool.ActorPool,
    _stage: nemo_curator.stages.base.ProcessingStage,
    tasks: list[nemo_curator.tasks.Task]
) -> list[nemo_curator.tasks.Task]
```

Process tasks through the actor pool.

**Parameters:**

<ParamField path="actor_pool" type="ray.util.actor_pool.ActorPool">
  The ActorPool to use for processing
</ParamField>

<ParamField path="_stage" type="nemo_curator.stages.base.ProcessingStage">
  The processing stage (for logging/context, unused)
</ParamField>

<ParamField path="tasks" type="list[nemo_curator.tasks.Task]">
  List of Task objects to process
</ParamField>

**Returns:**

List of processed Task objects


```python
_process_shuffle_stage_with_rapidsmpf_actors(
    actors: list[ray.actor.ActorHandle],
    tasks: list[nemo_curator.tasks.Task],
    band_range: tuple[int, int] | None = None
) -> list[nemo_curator.tasks.Task]
```

Process Shuffle through the actors.

**Parameters:**

<ParamField path="actors" type="list[ray.actor.ActorHandle]">
  The actors to use for processing
</ParamField>

<ParamField path="tasks" type="list[nemo_curator.tasks.Task]">
  List of Task objects to process
</ParamField>

<ParamField path="band_range" type="tuple[int, int] | None">
  Band range for LSH shuffle
</ParamField>

**Returns:**

List of processed Task objects


```python
_cleanup_actors(actors: list[ray.actor.ActorHandle]) -> None
```

Clean up a list of actors.


```python
_cleanup_actor_pool(actor_pool: ray.util.actor_pool.ActorPool) -> None
```

Clean up actors in the pool.


```python
_execute_lsh_stage(
    stage: nemo_curator.stages.deduplication.fuzzy.lsh.stage.LSHStage,
    input_tasks: list[nemo_curator.tasks.Task]
) -> list[nemo_curator.tasks.Task]
```

Execute an LSH stage with band iteration.

**Parameters:**

<ParamField path="stage" type="nemo_curator.stages.deduplication.fuzzy.lsh.stage.LSHStage">
  The LSH stage to execute
</ParamField>

<ParamField path="input_tasks" type="list[nemo_curator.tasks.Task]">
  Input tasks to process
</ParamField>

**Returns:**

List of output tasks from all band iterations

