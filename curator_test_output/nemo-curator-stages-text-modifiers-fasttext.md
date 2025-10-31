---
layout: overview
slug: nemo-curator-stages-text-modifiers-fasttext
---

# nemo_curator.stages.text.modifiers.fasttext



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`FastTextLabelModifier`](#nemo_curatorstagestextmodifiersfasttextfasttextlabelmodifier) | Abstract base class for text-based document modifiers. |

### API

```python
class nemo_curator.stages.text.modifiers.fasttext.FastTextLabelModifier(label: str)
```

**Bases**: `nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier`

```python
modify_document(text: str) -> str
```

