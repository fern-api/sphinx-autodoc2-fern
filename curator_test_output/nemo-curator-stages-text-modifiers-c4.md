---
layout: overview
slug: nemo-curator-stages-text-modifiers-c4
---

# nemo_curator.stages.text.modifiers.c4



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`BoilerPlateStringModifier`](#nemo_curatorstagestextmodifiersc4boilerplatestringmodifier) | If the sentence contains any of the boilerplate strings then discard. This includes things like "terms of use", "privacy policy", etc. Source: Adapted significantly from Google C4 processing. |

### API

```python
class nemo_curator.stages.text.modifiers.c4.BoilerPlateStringModifier(remove_if_at_top_or_bottom: bool = True)
```

**Bases**: `nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier`

If the sentence contains any of the boilerplate strings then discard.
This includes things like "terms of use", "privacy policy", etc.
Source: Adapted significantly from Google C4 processing.

```python
modify_document(text: str) -> str
```

