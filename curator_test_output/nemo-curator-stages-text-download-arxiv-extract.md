---
layout: overview
slug: nemo-curator-stages-text-download-arxiv-extract
---

# nemo_curator.stages.text.download.arxiv.extract



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ArxivExtractor`](#nemo_curatorstagestextdownloadarxivextractarxivextractor) | Extracts text from Arxiv LaTeX files. |

### API

```python
class nemo_curator.stages.text.download.arxiv.extract.ArxivExtractor
```

**Bases**: `nemo_curator.stages.text.download.DocumentExtractor`

Extracts text from Arxiv LaTeX files.

```python
_build_non_arg_macros_dict(file_content: str) -> dict[str, str]
```

function takes the content of a tex file and returns a dictionary
that contains the definitions of all macros that do not use arguments.
The dictionary is of the form \{macro_name: macro_value\}.

@param file_content: the content of the tex file as a string.

@return: dict


```python
_clean_tex_file(
    file_content: str,
    arg_macros: dict[str, str],
    non_arg_macros: dict[str, str]
) -> str
```

function takes a tex file as input and returns a cleaned version. The
 cleaned version is a concatenation of the tex files with the
following modifications:

- remove all comments (i.e. all lines starting with %)
- remove everything before the first section-like header
- remove everything after the first occurrence of either \appendix or
    \bibliography
- inline-expand definitions and macros

@param file_content: the content of the tex file as a string.

@return: cleaned tex file as a string


```python
extract(record: dict[str, str]) -> dict[str, typing.Any] | None
```


```python
input_columns() -> list[str]
```


```python
output_columns() -> list[str]
```

