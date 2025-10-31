---
layout: overview
slug: nemo-curator-stages-video-embedding-cosmos-embed1
---

# nemo_curator.stages.video.embedding.cosmos_embed1



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`CosmosEmbed1FrameCreationStage`](#nemo_curatorstagesvideoembeddingcosmos_embed1cosmosembed1framecreationstage) | Stage for creating Cosmos-Embed1 input frames from video clips. |
| [`CosmosEmbed1EmbeddingStage`](#nemo_curatorstagesvideoembeddingcosmos_embed1cosmosembed1embeddingstage) | Stage for embedding Cosmos-Embed1 frames into a vector space. |

### API

```python
class nemo_curator.stages.video.embedding.cosmos_embed1.CosmosEmbed1FrameCreationStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage for creating Cosmos-Embed1 input frames from video clips.

This class processes video clips through a series of steps including frame extraction,
model initialization, and input frame creation.

```python
model_dir: str
```

**Value**: `models/cosmos_embed1`


```python
variant: typing.Literal[224p, 336p, 448p]
```

**Value**: `336p`


```python
target_fps: float
```

**Value**: `2.0`


```python
verbose: bool
```

**Value**: `False`


```python
num_cpus: int
```

**Value**: `3`


```python
_name: str
```

**Value**: `cosmos_embed1`


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
setup(worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
setup_on_node(
    node_info: nemo_curator.backends.base.NodeInfo,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata
) -> None
```

Download the weights for the CosmosEmbed1 model on the node.


```python
class nemo_curator.stages.video.embedding.cosmos_embed1.CosmosEmbed1EmbeddingStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.video.VideoTask, nemo_curator.tasks.video.VideoTask]`

Stage for embedding Cosmos-Embed1 frames into a vector space.

This class processes video clips through a series of steps including frame extraction,
model initialization, and input frame creation.

```python
model_dir: str
```

**Value**: `models/cosmos_embed1`


```python
variant: typing.Literal[224p, 336p, 448p]
```

**Value**: `336p`


```python
texts_to_verify: list[str] | None
```

**Value**: `None`


```python
gpu_memory_gb: int
```

**Value**: `20`


```python
verbose: bool
```

**Value**: `False`


```python
_name: str
```

**Value**: `cosmos_embed1_embedding`


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
setup(worker_metadata: nemo_curator.backends.base.WorkerMetadata | None = None) -> None
```


```python
__post_init__() -> None
```


```python
process(task: nemo_curator.tasks.video.VideoTask) -> nemo_curator.tasks.video.VideoTask
```


```python
setup_on_node(
    node_info: nemo_curator.backends.base.NodeInfo,
    worker_metadata: nemo_curator.backends.base.WorkerMetadata
) -> None
```

Download the weights for the CosmosEmbed1 model on the node.

