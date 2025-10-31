---
layout: overview
slug: nemo-curator-stages-text-modifiers-newline-normalizer
---

# nemo_curator.stages.text.modifiers.newline_normalizer



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`NewlineNormalizer`](#nemo_curatorstagestextmodifiersnewline_normalizernewlinenormalizer) | Replaces 3 or more consecutive newline characters with only 2 newline characters. |

### Data

`THREE_OR_MORE_NEWLINES_REGEX`
`THREE_OR_MORE_WINDOWS_NEWLINES_REGEX`

### API

```python
nemo_curator.stages.text.modifiers.newline_normalizer.THREE_OR_MORE_NEWLINES_REGEX
```

**Value**: `compile(...)`


```python
nemo_curator.stages.text.modifiers.newline_normalizer.THREE_OR_MORE_WINDOWS_NEWLINES_REGEX
```

**Value**: `compile(...)`


```python
class nemo_curator.stages.text.modifiers.newline_normalizer.NewlineNormalizer
```

**Bases**: `nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier`

Replaces 3 or more consecutive newline characters with only 2 newline characters.

```python
modify_document(text: str) -> str
```

