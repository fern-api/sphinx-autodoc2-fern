---
layout: overview
slug: nemo-curator-stages-text-modules-modifier
---

# nemo_curator.stages.text.modules.modifier



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Modify`](#nemo_curatorstagestextmodulesmodifiermodify) | Modify fields of dataset records. |

### Functions

| Name | Description |
|------|-------------|
| [`_modifier_name`](#nemo_curatorstagestextmodulesmodifier_modifier_name) | None |
| [`_get_modifier_stage_name`](#nemo_curatorstagestextmodulesmodifier_get_modifier_stage_name) | Derive the stage name from the provided modifiers. |
| [`_validate_and_normalize_modifiers`](#nemo_curatorstagestextmodulesmodifier_validate_and_normalize_modifiers) | Validate inputs and normalize the modifier(s) to a list. |
| [`_normalize_input_fields`](#nemo_curatorstagestextmodulesmodifier_normalize_input_fields) | Normalize input fields into a list[list[str]] with one entry per modifier. |
| [`_normalize_output_fields`](#nemo_curatorstagestextmodulesmodifier_normalize_output_fields) | Resolve output column names to one per modifier. |

### API

```python
class nemo_curator.stages.text.modules.modifier.Modify
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.DocumentBatch, nemo_curator.tasks.DocumentBatch]`

Modify fields of dataset records.

You can provide:
- a `DocumentModifier` instance; its `modify_document` will be used
- a callable that takes a single value (single-input) or a dict[str, any] (multi-input)
- a list mixing the above, applied in order

Input fields can be:
- str (single field reused for each modifier)
- list[str] (one field per modifier)
- list[list[str]] (per-modifier multiple input fields)

Implicit behavior:
- If `output_field` is None and each modifier has exactly one input field,
  results are written in-place to that input field.
- If any modifier has multiple input fields, `output_field` is required
  (provide a single name to reuse for all, or one per modifier).

**Parameters:**

- **modifier_fn (Callable | DocumentModifier | list[DocumentModifier | Callable])**: 
  Modifier or list of modifiers to apply.
- **input_fields (str | list[str] | list[list[str]])**: 
  Input field(s); see above for accepted forms.
- **output_fields (str | list[str] | None)**: 
  Output field name(s). If None and all inputs are single-column,
  in-place update is performed.

```python
modifier_fn: collections.abc.Callable | nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier | list[nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier | collections.abc.Callable]
```

**Value**: `None`


```python
input_fields: str | list[str] | list[list[str]]
```

**Value**: `text`


```python
output_fields: str | list[str | None] | None
```

**Value**: `None`


```python
_name: str
```

**Value**: `modifier_fn`


```python
__post_init__()
```


```python
inputs() -> tuple[list[str], list[str]]
```


```python
outputs() -> tuple[list[str], list[str]]
```


```python
process(batch: nemo_curator.tasks.DocumentBatch) -> nemo_curator.tasks.DocumentBatch | None
```


```python
nemo_curator.stages.text.modules.modifier._modifier_name(x: nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier | collections.abc.Callable) -> str
```


```python
nemo_curator.stages.text.modules.modifier._get_modifier_stage_name(modifiers: list[nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier | collections.abc.Callable]) -> str
```

Derive the stage name from the provided modifiers.


```python
nemo_curator.stages.text.modules.modifier._validate_and_normalize_modifiers(
    _modifier: nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier | collections.abc.Callable | list[nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier | collections.abc.Callable],
    input_field: str | list[str] | list[list[str]] | None
) -> list[nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier | collections.abc.Callable]
```

Validate inputs and normalize the modifier(s) to a list.


```python
nemo_curator.stages.text.modules.modifier._normalize_input_fields(
    input_fields: str | list[str] | list[list[str]],
    modifiers: list[nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier | collections.abc.Callable]
) -> list[list[str]]
```

Normalize input fields into a list[list[str]] with one entry per modifier.


```python
nemo_curator.stages.text.modules.modifier._normalize_output_fields(
    output_fields: str | list[str | None] | None,
    input_fields: list[list[str]],
    modifiers: list[nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier | collections.abc.Callable]
) -> list[str]
```

Resolve output column names to one per modifier.

Rules:
- None overall: in-place if all modifiers have exactly one input; else error.
- str overall: replicate for all modifiers.
- list overall (len 1 or len(modifiers)):
  - Each entry may be a str (explicit output) or None (implicit in-place; requires single input).

