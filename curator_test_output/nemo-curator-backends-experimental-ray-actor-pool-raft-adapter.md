---
layout: overview
slug: nemo-curator-backends-experimental-ray-actor-pool-raft-adapter
---

# nemo_curator.backends.experimental.ray_actor_pool.raft_adapter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`RayActorPoolRAFTAdapter`](#nemo_curatorbackendsexperimentalray_actor_poolraft_adapterrayactorpoolraftadapter) | RAFT Actor adapter for Ray Actor Pool backend. |

### API

```python
class nemo_curator.backends.experimental.ray_actor_pool.raft_adapter.RayActorPoolRAFTAdapter(stage: nemo_curator.stages.base.ProcessingStage, index: int, pool_size: int, session_id: bytes, actor_name_prefix: str = 'RAFT')
```

**Bases**: `nemo_curator.backends.base.BaseStageAdapter`

RAFT Actor adapter for Ray Actor Pool backend.

This adapter extends RayActorPoolStageAdapter and adds RAFT capabilities
to enable distributed processing with RAFT communication.

### Initialization

Initialize the RAFT adapter.

**Parameters:**

- **stage**: The processing stage to wrap
- **index**: The index of this actor in the pool
- **pool_size**: Total number of actors in the pool
- **session_id**: Unique session identifier
- **actor_name_prefix**: Prefix for actor names


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


```python
broadcast_root_unique_id() -> None
```

Broadcast the root unique ID to all actors.

This method should only be called by the root actor.


```python
set_root_unique_id(root_unique_id: int) -> None
```

Set the root unique ID.

Parameters
----------
root_unique_id : int
    The root unique ID.


```python
_setup_nccl() -> None
```

Setup NCCL communicator.


```python
_setup_raft() -> None
```

Setup RAFT.


```python
setup(worker_metadata: WorkerMetadata | None = None) -> None
```

Setup the RAFT actor.

This method should be called after the root unique ID has been broadcast.


```python
teardown() -> None
```

