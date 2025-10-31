---
layout: overview
slug: nemo-curator-backends-experimental-ray-actor-pool-utils
---

# nemo_curator.backends.experimental.ray_actor_pool.utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`calculate_optimal_actors_for_stage`](#nemo_curatorbackendsexperimentalray_actor_poolutilscalculate_optimal_actors_for_stage) | Calculate optimal number of actors for a stage. |
| [`create_named_ray_actor_pool_stage_adapter`](#nemo_curatorbackendsexperimentalray_actor_poolutilscreate_named_ray_actor_pool_stage_adapter) | Create a named RayActorPoolStageAdapter or RayActorPoolRAFTAdapter. |

### Data

`_LARGE_INT`

### API

```python
nemo_curator.backends.experimental.ray_actor_pool.utils._LARGE_INT
```

**Value**: `None`


```python
nemo_curator.backends.experimental.ray_actor_pool.utils.calculate_optimal_actors_for_stage(
    stage: nemo_curator.stages.base.ProcessingStage,
    num_tasks: int,
    reserved_cpus: float = 0.0,
    reserved_gpus: float = 0.0
) -> int
```

Calculate optimal number of actors for a stage.


```python
nemo_curator.backends.experimental.ray_actor_pool.utils.create_named_ray_actor_pool_stage_adapter(
    stage: nemo_curator.stages.base.ProcessingStage,
    cls: type[nemo_curator.backends.experimental.ray_actor_pool.adapter.RayActorPoolStageAdapter] | type[nemo_curator.backends.experimental.ray_actor_pool.raft_adapter.RayActorPoolRAFTAdapter]
) -> ActorClass[RayActorPoolStageAdapter | RayActorPoolRAFTAdapter]
```

Create a named RayActorPoolStageAdapter or RayActorPoolRAFTAdapter.

This function creates a dynamic subclass of the given adapter class,
named after the stage's class name. This ensures that when Ray calls
type(adapter).__name__, it returns the original stage's class name rather
than 'RayActorPoolStageAdapter' or 'RayActorPoolRAFTAdapter'.

**Parameters:**

**Returns:**

ActorClass: A ray.remote decorated class that can be used to create actors

