---
layout: overview
slug: nemo-curator-models-base
---

# nemo_curator.models.base



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ModelInterface`](#nemo_curatormodelsbasemodelinterface) | Abstract base class that defines an interface for machine learning models. |

### API

```python
class nemo_curator.models.base.ModelInterface
```

**Bases**: `abc.ABC`

Abstract base class that defines an interface for machine learning models.

Specifically focused on their weight handling and environmental setup.

This interface allows our pipeline code to download weights locally and setup models in a uniform
way. It does not place any restrictions on how inference is run.

```python
model_id_names: list[str]
```

**Decorators**: `@abstractmethod`

Returns a list of model IDs associated with the model.

In cosmos-curate, each model has an ID associated with it.
This is often the huggingspace name for that model (e.g. Salesforce/instructblip-vicuna-13b).

**Returns:**

A list of strings.


```python
setup() -> None
```

Set up the model for use, such as loading weights and building computation graphs.

