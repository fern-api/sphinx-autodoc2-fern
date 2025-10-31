---
layout: overview
slug: nemo-curator-stages-text-modifiers-url-remover
---

# nemo_curator.stages.text.modifiers.url_remover



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`UrlRemover`](#nemo_curatorstagestextmodifiersurl_removerurlremover) | Removes all URLs in a document. |

### Data

`URL_REGEX`

### API

```python
nemo_curator.stages.text.modifiers.url_remover.URL_REGEX
```

**Value**: `compile(...)`


```python
class nemo_curator.stages.text.modifiers.url_remover.UrlRemover
```

**Bases**: `nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier`

Removes all URLs in a document.

```python
modify_document(text: str) -> str
```

