---
layout: overview
slug: nemo-curator-stages-text-modifiers-doc-modifier
---

# nemo_curator.stages.text.modifiers.doc_modifier



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`DocumentModifier`](#nemo_curatorstagestextmodifiersdoc_modifierdocumentmodifier) | Abstract base class for text-based document modifiers. |

### API

```python
class nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier
```

**Bases**: `abc.ABC`

Abstract base class for text-based document modifiers.

Subclasses must implement `modify_document` to transform input value(s)
and return the modified value. This supports both single-input and
multi-input usage:
- Single input: `modify_document(value)`
- Multiple inputs: `modify_document(**values)` where each input field is
  expanded as a keyword argument (e.g., `modify_document(column_1=..., column_2=...)`).

```python
modify_document(
    *args: object, **kwargs: object
) -> object
```

Transform the provided value(s) and return the result.


```python
name: str
```

