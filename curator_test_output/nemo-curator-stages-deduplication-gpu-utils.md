---
layout: overview
slug: nemo-curator-stages-deduplication-gpu-utils
---

# nemo_curator.stages.deduplication.gpu_utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`align_down_to_256`](#nemo_curatorstagesdeduplicationgpu_utilsalign_down_to_256) | Aligns a memory size down to the nearest multiple of 256. |
| [`get_device_free_memory`](#nemo_curatorstagesdeduplicationgpu_utilsget_device_free_memory) | Return total memory of the first GPU the caller has access to. Returns None if the GPU is not available or information could not be retrieved. |

### API

```python
nemo_curator.stages.deduplication.gpu_utils.align_down_to_256(memory_size: int) -> int
```

Aligns a memory size down to the nearest multiple of 256.


```python
nemo_curator.stages.deduplication.gpu_utils.get_device_free_memory() -> int | None
```

Return total memory of the first GPU the caller has access to.
Returns None if the GPU is not available or information could not be retrieved.

