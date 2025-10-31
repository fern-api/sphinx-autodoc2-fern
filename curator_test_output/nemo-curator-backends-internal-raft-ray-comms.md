---
layout: overview
slug: nemo-curator-backends-internal-raft-ray-comms
---

# nemo_curator.backends.internal.raft.ray_comms



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Comms`](#nemo_curatorbackendsinternalraftray_commscomms) | Initializes and manages underlying NCCL comms handles across the a pool of Ray actors. It is expected that `init()` will be called explicitly. It is recommended to also call `destroy()` when the comms are no longer needed so the underlying resources can be cleaned up. This class is not meant to be thread-safe. |

### API

```python
class nemo_curator.backends.internal.raft.ray_comms.Comms(verbose: bool = False, nccl_root_location: str = 'ray-actor')
```

Initializes and manages underlying NCCL comms handles across the a pool of
Ray actors. It is expected that `init()` will be called explicitly. It is
recommended to also call `destroy()` when the comms are no longer needed so
the underlying resources can be cleaned up. This class is not meant to be
thread-safe.

### Initialization

**Parameters:**

- **verbose (bool)**: Print verbose logging. Defaults to False.
- **nccl_root_location (str)**: Indicates where the NCCL's root node should be located.
  ['client', 'worker', 'scheduler', 'ray-actor']. Defaults to "ray-actor".


```python
valid_nccl_placements
```

**Value**: `ray-actor`


```python
__del__() -> None
```


```python
create_nccl_uniqueid() -> None
```


```python
init() -> None
```

Initializes the underlying comms.

