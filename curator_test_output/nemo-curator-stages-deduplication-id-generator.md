---
layout: overview
slug: nemo-curator-stages-deduplication-id-generator
---

# nemo_curator.stages.deduplication.id_generator



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`IdGeneratorBase`](#nemo_curatorstagesdeduplicationid_generatoridgeneratorbase) | Base IdGenerator class without Ray decorator for testing and direct use. |
| [`IdGenerator`](#nemo_curatorstagesdeduplicationid_generatoridgenerator) | Ray actor version of IdGenerator. |

### Functions

| Name | Description |
|------|-------------|
| [`get_id_generator_actor`](#nemo_curatorstagesdeduplicationid_generatorget_id_generator_actor) | None |
| [`kill_id_generator_actor`](#nemo_curatorstagesdeduplicationid_generatorkill_id_generator_actor) | None |
| [`create_id_generator_actor`](#nemo_curatorstagesdeduplicationid_generatorcreate_id_generator_actor) | Create an id generator actor. |
| [`write_id_generator_to_disk`](#nemo_curatorstagesdeduplicationid_generatorwrite_id_generator_to_disk) | None |

### Data

`CURATOR_DEDUP_ID_STR`
`CURATOR_ID_GENERATOR_ACTOR_NAME`

### API

```python
nemo_curator.stages.deduplication.id_generator.CURATOR_DEDUP_ID_STR
```

**Value**: `_curator_dedup_id`


```python
nemo_curator.stages.deduplication.id_generator.CURATOR_ID_GENERATOR_ACTOR_NAME
```

**Value**: `curator_deduplication_id_generator`


```python
class nemo_curator.stages.deduplication.id_generator.IdGeneratorBase(start_id: int = 0, batch_registry: dict[str, tuple[int, int]] | None = None)
```

Base IdGenerator class without Ray decorator for testing and direct use.

```python
register_batch(
    files: str | list[str], count: int
) -> int
```


```python
hash_files(filepath: str | list[str]) -> str
```


```python
get_batch_range(
    files: str | list[str] | None, key: str | None
) -> tuple[int, int]
```


```python
to_disk(
    filepath: str, storage_options: dict[str, typing.Any] | None = None
) -> None
```


```python
from_disk(
    filepath: str, storage_options: dict[str, typing.Any] | None = None
) -> nemo_curator.stages.deduplication.id_generator.IdGeneratorBase
```


```python
class nemo_curator.stages.deduplication.id_generator.IdGenerator(start_id: int = 0, batch_registry: dict[str, tuple[int, int]] | None = None)
```

**Bases**: `nemo_curator.stages.deduplication.id_generator.IdGeneratorBase`

Ray actor version of IdGenerator.

```python
nemo_curator.stages.deduplication.id_generator.get_id_generator_actor() -> ray.actor.ActorHandle[nemo_curator.stages.deduplication.id_generator.IdGenerator]
```


```python
nemo_curator.stages.deduplication.id_generator.kill_id_generator_actor() -> None
```


```python
nemo_curator.stages.deduplication.id_generator.create_id_generator_actor(
    filepath: str | None = None,
    storage_options: dict[str, typing.Any] | None = None
) -> None
```

Create an id generator actor.

**Parameters:**


```python
nemo_curator.stages.deduplication.id_generator.write_id_generator_to_disk(
    filepath: str, storage_options: dict[str, typing.Any] | None = None
) -> None
```

