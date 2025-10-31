---
layout: overview
slug: nemo-curator-stages-text-modifiers-markdown-remover
---

# nemo_curator.stages.text.modifiers.markdown_remover



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`MarkdownRemover`](#nemo_curatorstagestextmodifiersmarkdown_removermarkdownremover) | Removes Markdown formatting in a document including bold, italic, underline, and URL text. |

### Data

`MARKDOWN_BOLD_REGEX`
`MARKDOWN_ITALIC_REGEX`
`MARKDOWN_UNDERLINE_REGEX`
`MARKDOWN_LINK_REGEX`

### API

```python
nemo_curator.stages.text.modifiers.markdown_remover.MARKDOWN_BOLD_REGEX
```

**Value**: `\*\*(.*?)\*\*`


```python
nemo_curator.stages.text.modifiers.markdown_remover.MARKDOWN_ITALIC_REGEX
```

**Value**: `\*(.*?)\*`


```python
nemo_curator.stages.text.modifiers.markdown_remover.MARKDOWN_UNDERLINE_REGEX
```

**Value**: `_(.*?)_`


```python
nemo_curator.stages.text.modifiers.markdown_remover.MARKDOWN_LINK_REGEX
```

**Value**: `\[.*?\]\((.*?)\)`


```python
class nemo_curator.stages.text.modifiers.markdown_remover.MarkdownRemover
```

**Bases**: `nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier`

Removes Markdown formatting in a document including bold, italic, underline, and URL text.

```python
modify_document(text: str) -> str
```

