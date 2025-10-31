---
layout: overview
slug: nemo-curator-stages-text-utils-text-utils
---

# nemo_curator.stages.text.utils.text_utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`get_word_splitter`](#nemo_curatorstagestextutilstext_utilsget_word_splitter) | For Chinese and Japanese text, we use external libraries to split the text because these languages are not separated by spaces. For all other languages, such as English, we assume words are separated by spaces. |
| [`get_paragraphs`](#nemo_curatorstagestextutilstext_utilsget_paragraphs) | None |
| [`get_sentences`](#nemo_curatorstagestextutilstext_utilsget_sentences) | None |
| [`get_ngrams`](#nemo_curatorstagestextutilstext_utilsget_ngrams) | None |
| [`is_paragraph_indices_in_top_or_bottom_only`](#nemo_curatorstagestextutilstext_utilsis_paragraph_indices_in_top_or_bottom_only) | None |
| [`get_comments_and_docstring`](#nemo_curatorstagestextutilstext_utilsget_comments_and_docstring) | Extract all natural text in source: comments + doctsrings the extraction fails in case of syntax errors in the file Args: source: the code to parse comments: if True extract comments two clean_comment: if True remove # from extracted comments Returns: a string with concatenated docstrings and comments |
| [`get_comments`](#nemo_curatorstagestextutilstext_utilsget_comments) | Returns a string including all coments |
| [`get_docstrings`](#nemo_curatorstagestextutilstext_utilsget_docstrings) | Parse Python source code from file or string and print docstrings. |
| [`parse_docstrings`](#nemo_curatorstagestextutilstext_utilsparse_docstrings) | Parse Python source code and yield a tuple of ast node instance, name, and docstring for each function/method, class and module. |
| [`remove_punctuation`](#nemo_curatorstagestextutilstext_utilsremove_punctuation) | None |
| [`get_words`](#nemo_curatorstagestextutilstext_utilsget_words) | None |

### Data

`NODE_TYPES`

### API

```python
nemo_curator.stages.text.utils.text_utils.get_word_splitter(language: str) -> collections.abc.Callable[[str], list[str]]
```

For Chinese and Japanese text, we use external libraries to split the text
because these languages are not separated by spaces. For all other languages,
such as English, we assume words are separated by spaces.

**Parameters:**

**Returns:**

A function which can be used to parse the words of a string into a list.


```python
nemo_curator.stages.text.utils.text_utils.get_paragraphs(document: str) -> list[str]
```


```python
nemo_curator.stages.text.utils.text_utils.get_sentences(document: str) -> list[str]
```


```python
nemo_curator.stages.text.utils.text_utils.get_ngrams(
    input_list: list[str], n: int
) -> list[tuple[str, ...]]
```


```python
nemo_curator.stages.text.utils.text_utils.is_paragraph_indices_in_top_or_bottom_only(
    boilerplate_paragraph_indices: list[int], num_paragraphs: int
) -> bool
```


```python
nemo_curator.stages.text.utils.text_utils.NODE_TYPES
```

**Value**: `None`


```python
nemo_curator.stages.text.utils.text_utils.get_comments_and_docstring(
    source: str,
    comments: bool = True,
    clean_comments: bool = False
) -> tuple[str, str]
```

Extract all natural text in source: comments + doctsrings
  the extraction fails in case of syntax errors in the file

**Parameters:**

<ParamField path="source" type="str">
  the code to parse
</ParamField>

<ParamField path="comments" type="bool" default="True">
  if True extract comments two
</ParamField>

**Returns:**

a string with concatenated docstrings and comments


```python
nemo_curator.stages.text.utils.text_utils.get_comments(
    s: str, clean: bool = False
) -> str
```

Returns a string including all coments


```python
nemo_curator.stages.text.utils.text_utils.get_docstrings(
    source: str, module: str = '<string>'
) -> list[str]
```

Parse Python source code from file or string and print docstrings.


```python
nemo_curator.stages.text.utils.text_utils.parse_docstrings(source: str) -> list[tuple[ast.AST, str | None, str]]
```

Parse Python source code and yield a tuple of ast node instance, name,
and docstring for each function/method, class and module.


```python
nemo_curator.stages.text.utils.text_utils.remove_punctuation(str_in: str) -> str
```


```python
nemo_curator.stages.text.utils.text_utils.get_words(text: str) -> tuple[list[str], list[int]]
```

