---
layout: overview
slug: nemo-curator-stages-text-download-arxiv-iterator
---

# nemo_curator.stages.text.download.arxiv.iterator



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ArxivIterator`](#nemo_curatorstagestextdownloadarxiviteratorarxiviterator) | Processes downloaded Arxiv files and extracts article content. |

### API

```python
class nemo_curator.stages.text.download.arxiv.iterator.ArxivIterator(log_frequency: int = 1000)
```

**Bases**: `nemo_curator.stages.text.download.DocumentIterator`

Processes downloaded Arxiv files and extracts article content.

```python
_tex_proj_loader(file_or_dir_path: str) -> list[str] | None
```

function to load the tex files from a tar file or a gzip file. The
function will return a tuple containing a list of tex files and the
timestamp of the project.

@param file_or_dir_path: path to the tar file or the gzip file

@return: tuple containing a list of tex files and the timestamp of the
    project


```python
_format_arxiv_id(arxiv_id: str) -> str
```

this function brings the raw arxiv-id into a format compliant with the
specification from arxiv. This is used to create the url to the arxiv
abstract page.

- Format prior to March 2007:
    `<archive>`/YYMMNNN where N is a 3-digit number
- Format after March 2007: `<archive>`/YYMM.NNNNN where N is a
  5 (or 6)-digit number

References: https://info.arxiv.org/help/arxiv_identifier.html

@param arxiv_id: raw arxiv id which can be in one of the
                 following formats:
                 - `<archive>``<YY>``<MM>``<NNN>`
                 - `<YY>``<MM>``<NNNNN|NNNNNN>`

@return: formatted arxiv id


```python
iterate(file_path: str) -> collections.abc.Iterator[dict[str, typing.Any]]
```


```python
output_columns() -> list[str]
```

