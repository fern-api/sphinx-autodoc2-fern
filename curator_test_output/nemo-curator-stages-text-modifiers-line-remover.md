---
layout: overview
slug: nemo-curator-stages-text-modifiers-line-remover
---

# nemo_curator.stages.text.modifiers.line_remover



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`LineRemover`](#nemo_curatorstagestextmodifiersline_removerlineremover) | Removes lines from a document if the content of the line matches a given string. |

### API

```python
class nemo_curator.stages.text.modifiers.line_remover.LineRemover(patterns: list[str])
```

**Bases**: `nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier`

Removes lines from a document if the content of the line matches a given string.

### Initialization

**Parameters:**

- **patterns (List[str])**: The patterns to check


```python
modify_document(text: str) -> str
```

