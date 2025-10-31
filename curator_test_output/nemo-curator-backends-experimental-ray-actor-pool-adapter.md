---
layout: overview
slug: nemo-curator-backends-experimental-ray-actor-pool-adapter
---

# nemo_curator.backends.experimental.ray_actor_pool.adapter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`RayActorPoolStageAdapter`](#nemo_curatorbackendsexperimentalray_actor_pooladapterrayactorpoolstageadapter) | Adapts ProcessingStage to Ray actors for use with ActorPool. |

### API

```python
class nemo_curator.backends.experimental.ray_actor_pool.adapter.RayActorPoolStageAdapter(stage: nemo_curator.stages.base.ProcessingStage)
```

**Bases**: `nemo_curator.backends.base.BaseStageAdapter`

Adapts ProcessingStage to Ray actors for use with ActorPool.

This adapter is designed to work with Ray's ActorPool for better
resource management and load balancing.

```python
get_batch_size() -> int
```

Get the batch size for this stage.


```python
setup_on_node() -> None
```

Setup method for Ray actors.

Note: This method is not used in the current implementation since we use
the Ray Data pattern of calling setup_on_node before actor creation.

