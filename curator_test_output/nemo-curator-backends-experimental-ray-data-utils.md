---
layout: overview
slug: nemo-curator-backends-experimental-ray-data-utils
---

# nemo_curator.backends.experimental.ray_data.utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`calculate_concurrency_for_actors_for_stage`](#nemo_curatorbackendsexperimentalray_datautilscalculate_concurrency_for_actors_for_stage) | Calculate concurrency if we want to spin up actors based on available resources and stage requirements. |
| [`is_actor_stage`](#nemo_curatorbackendsexperimentalray_datautilsis_actor_stage) | Check if the stage is an actor stage. |

### API

```python
nemo_curator.backends.experimental.ray_data.utils.calculate_concurrency_for_actors_for_stage(stage: nemo_curator.stages.base.ProcessingStage) -> tuple[int, int] | int
```

Calculate concurrency if we want to spin up actors based on available resources and stage requirements.

**Returns:**

int | tuple[int, int]: Number of actors to use
int: Number of workers to use
tuple[int, int]: tuple of min / max actors to use and number of workers to use


```python
nemo_curator.backends.experimental.ray_data.utils.is_actor_stage(stage: nemo_curator.stages.base.ProcessingStage) -> bool
```

Check if the stage is an actor stage.

