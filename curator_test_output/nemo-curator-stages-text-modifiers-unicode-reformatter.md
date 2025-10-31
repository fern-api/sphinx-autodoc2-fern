---
layout: overview
slug: nemo-curator-stages-text-modifiers-unicode-reformatter
---

# nemo_curator.stages.text.modifiers.unicode_reformatter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`UnicodeReformatter`](#nemo_curatorstagestextmodifiersunicode_reformatterunicodereformatter) | Abstract base class for text-based document modifiers. |

### API

```python
class nemo_curator.stages.text.modifiers.unicode_reformatter.UnicodeReformatter(config: ftfy.TextFixerConfig | None = None, unescape_html: str | bool = 'auto', remove_terminal_escapes: bool = True, fix_encoding: bool = True, restore_byte_a0: bool = True, replace_lossy_sequences: bool = True, decode_inconsistent_utf8: bool = True, fix_c1_controls: bool = True, fix_latin_ligatures: bool = False, fix_character_width: bool = False, uncurl_quotes: bool = False, fix_line_breaks: bool = False, fix_surrogates: bool = True, remove_control_chars: bool = True, normalization: typing.Literal[NFC, NFD, NFKC, NFKD] | None = None, max_decode_length: int = 1000000, explain: bool = True)
```

**Bases**: `nemo_curator.stages.text.modifiers.doc_modifier.DocumentModifier`

```python
modify_document(text: str) -> str
```

