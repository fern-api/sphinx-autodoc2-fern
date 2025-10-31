---
layout: overview
slug: nemo-curator-stages-text-modifiers-slicer
---

# nemo_curator.stages.text.modifiers.slicer



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Slicer`](#nemo_curatorstagestextmodifiersslicerslicer) | Slices a document based on indices or strings. |

### API

```python
class nemo_curator.stages.text.modifiers.slicer.Slicer(left: int | str | None = 0, right: int | str | None = None, include_left: bool = True, include_right: bool = True, strip: bool = True)
```

**Bases**: `nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier`

Slices a document based on indices or strings.

### Initialization

**Parameters:**

- **left (Union[int, str], optional)**: If the provided value is an int, slice the string from this index (inclusive).
  If the provided value is a str, slice the string from the first occurence of this substring.
- **right (Union[int, str], optional)**: If the provided value is an int, slice the string to this index (exclusive).
  If the provided value is a str, slice the string to the last occurence of this substring. If None,
  right is set to the length of the string.
- **include_left (bool)**: Only used if `left` is a string. If True, the value of `left` is included in the
  slicing result. Defaults to False.
- **include_right (bool)**: Only used if `right` is a string. If True, the value of `right` is included in the
  slicing result. Defaults to False.
- **strip (bool)**: If True, strip the resulting string.


```python
modify_document(text: str) -> str
```

