---
layout: overview
slug: nemo-curator-stages-resources
---

# nemo_curator.stages.resources



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Resources`](#nemo_curatorstagesresourcesresources) | Define resource requirements for a processing stage. |

### Functions

| Name | Description |
|------|-------------|
| [`_get_gpu_memory_gb`](#nemo_curatorstagesresources_get_gpu_memory_gb) | Get GPU memory in GB for the current device. |

### API

```python
nemo_curator.stages.resources._get_gpu_memory_gb() -> float
```

Get GPU memory in GB for the current device.


```python
class nemo_curator.stages.resources.Resources
```

Define resource requirements for a processing stage.

Attributes:
    cpus: Number of CPU cores required
    gpu_memory_gb: GPU memory required in GB (Only for single-GPU stages)
    nvdecs: Number of NVDEC units required
    nvencs: Number of NVENC units required
    entire_gpu: Whether to allocate entire GPU regardless of memory (This also gives you nvdecs and nvencs of that GPU)
    gpus: Number of GPUs required (Only for multi-GPU stages)

```python
cpus: float
```

**Value**: `1.0`


```python
gpu_memory_gb: float
```

**Value**: `0.0`


```python
nvdecs: int
```

**Value**: `0`


```python
nvencs: int
```

**Value**: `0`


```python
entire_gpu: bool
```

**Value**: `False`


```python
gpus: float
```

**Value**: `0.0`


```python
__post_init__()
```

Calculate GPU count based on memory requirements.


```python
requires_gpu: bool
```

Check if this stage requires GPU resources.

