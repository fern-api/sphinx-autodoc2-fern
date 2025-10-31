---
layout: overview
slug: nemo-curator-stages-text-modifiers-quotation-remover
---

# nemo_curator.stages.text.modifiers.quotation_remover



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`QuotationRemover`](#nemo_curatorstagestextmodifiersquotation_removerquotationremover) | Removes quotations from a document following a few rules: - If the document is less than 2 characters, it is returned unchanged. - If the document starts and ends with a quotation mark and there are no newlines in the document, the quotation marks are removed. - If the document starts and ends with a quotation mark and there are newlines in the document, the quotation marks are removed only if the first line does not end with a quotation mark. |

### API

```python
class nemo_curator.stages.text.modifiers.quotation_remover.QuotationRemover
```

**Bases**: `nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier`

Removes quotations from a document following a few rules:
- If the document is less than 2 characters, it is returned unchanged.
- If the document starts and ends with a quotation mark and there are
    no newlines in the document, the quotation marks are removed.
- If the document starts and ends with a quotation mark and there are
    newlines in the document, the quotation marks are removed only if
    the first line does not end with a quotation mark.

```python
modify_document(text: str) -> str
```

