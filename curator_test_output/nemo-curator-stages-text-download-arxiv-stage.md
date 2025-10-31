---
layout: overview
slug: nemo-curator-stages-text-download-arxiv-stage
---

# nemo_curator.stages.text.download.arxiv.stage



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`ArxivDownloadExtractStage`](#nemo_curatorstagestextdownloadarxivstagearxivdownloadextractstage) | Composite stage for downloading and processing Arxiv data. |

### API

```python
class nemo_curator.stages.text.download.arxiv.stage.ArxivDownloadExtractStage(download_dir: str = './arxiv_downloads', url_limit: int | None = None, record_limit: int | None = None, add_filename_column: bool | str = True, log_frequency: int = 1000, verbose: bool = False)
```

**Bases**: `nemo_curator.stages.text.download.DocumentDownloadExtractStage`

Composite stage for downloading and processing Arxiv data.

This pipeline:
1. Generates Arxiv dump URLs
2. Downloads Arxiv .tar files
3. Extracts articles from the tar files
4. Cleans and extracts text from LaTeX files

### Initialization

Download Arxiv tar files and extract the contained LaTeX projects.

This function obtains a list of Arxiv tar file URLs (via get_arxiv_urls), downloads the tar files,
and then extracts the contained LaTeX source files. The resulting documents (after extraction) are
assembled into a DocumentDataset.

**Parameters:**

- **download_dir (str, optional)**: 
  The directory where the raw downloaded tar files will be kept. Defaults to "./arxiv_downloads".
- **url_limit (Optional[int], optional)**: 
  Limits the maximum number of Arxiv tar file URLs to download and process.
  If None, all available URLs (from get_arxiv_urls) are processed.
- **record_limit (Optional[int], optional)**: 
  Limits the maximum number of records to extract from each tar file.
  If None, all available records are extracted.
- **add_filename_column (bool | str, optional)**: 
  If True, adds a column to the output DataFrame with the filename of the tar file.
  If a string, adds a column with the specified name. Defaults to True.
- **log_frequency (int, optional)**: 
  How often to log progress. Defaults to 1000.
- **verbose (bool, optional)**: 
  If True, prints verbose output. Defaults to False.

**Returns:**

DocumentBatch:
A batch object containing the extracted documents.


```python
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

Decompose this composite stage into its constituent stages.


```python
get_description() -> str
```

Get a description of this composite stage.

