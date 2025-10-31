---
layout: overview
slug: nemo-curator-stages-text-download-utils
---

# nemo_curator.stages.text.download.utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`remove_control_characters`](#nemo_curatorstagestextdownloadutilsremove_control_characters) | Remove control characters from text. Control characters are non-printable characters in the Unicode standard that control how text is displayed or processed. |
| [`detect_language`](#nemo_curatorstagestextdownloadutilsdetect_language) | Detect language using cld2. |
| [`lang_detect`](#nemo_curatorstagestextdownloadutilslang_detect) | Detect language from text. |
| [`decode_html`](#nemo_curatorstagestextdownloadutilsdecode_html) | None |
| [`try_decode_with_detected_encoding`](#nemo_curatorstagestextdownloadutilstry_decode_with_detected_encoding) | None |

### API

```python
nemo_curator.stages.text.download.utils.remove_control_characters(text: str) -> str
```

Remove control characters from text.
Control characters are non-printable characters in the Unicode standard that control how text is displayed or processed.


```python
nemo_curator.stages.text.download.utils.detect_language(text: str) -> tuple[bool, int, list[tuple[str, str, float, int]]]
```

Detect language using cld2.

**Returns:**

tuple[bool, int, list[tuple[str, str, float, int]]]:
is_reliable: bool True if the detection is high confidence.
textBytesFound: int The number of bytes of text found.
details: list[tuple[str, str, float, int]] A list of tuples upto three detected languages containing the
language name (str)
language code (str)
percent (float) what percentage of the text is in this language
score (int) how confident the detection is.


```python
nemo_curator.stages.text.download.utils.lang_detect(text: str) -> str
```

Detect language from text.

**Parameters:**

**Returns:**

str: The most likely language code.


```python
nemo_curator.stages.text.download.utils.decode_html(html_bytes: bytes) -> str | None
```


```python
nemo_curator.stages.text.download.utils.try_decode_with_detected_encoding(html_bytes: bytes) -> str | None
```

