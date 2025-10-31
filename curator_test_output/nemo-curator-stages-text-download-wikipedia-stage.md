---
layout: overview
slug: nemo-curator-stages-text-download-wikipedia-stage
---

# nemo_curator.stages.text.download.wikipedia.stage



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`WikipediaDownloadExtractStage`](#nemo_curatorstagestextdownloadwikipediastagewikipediadownloadextractstage) | Composite stage for downloading and processing Wikipedia data. |

### API

```python
class nemo_curator.stages.text.download.wikipedia.stage.WikipediaDownloadExtractStage(language: str = 'en', download_dir: str = './wikipedia_downloads', dump_date: str | None = None, wikidumps_index_prefix: str = 'https://dumps.wikimedia.org', verbose: bool = False, url_limit: int | None = None, record_limit: int | None = None, add_filename_column: bool | str = True, log_frequency: int = 1000)
```

**Bases**: `nemo_curator.stages.text.download.DocumentDownloadExtractStage`

Composite stage for downloading and processing Wikipedia data.

This pipeline:
1. Generates Wikipedia dump URLs for the specified language and date
2. Downloads Wikipedia .bz2 dump files
3. Extracts articles from the dump files
4. Cleans and extracts text from Wikipedia markup

### Initialization

Initialize the Wikipedia download and extract stage.

**Parameters:**

- **language**: Language code for the Wikipedia dump (e.g., "en", "es", "fr")
- **download_dir**: Directory to store downloaded .bz2 files
- **dump_date**: Specific dump date in "YYYYMMDD" format (if None, uses latest)
- **wikidumps_index_prefix**: Base URL for Wikipedia dumps
- **verbose**: If True, enables verbose logging
- **url_limit**: Maximum number of dump URLs to process
- **record_limit**: Maximum number of articles to extract per file
- **add_filename_column**: Whether to add filename column to output
- **log_frequency**: How often to log progress during iteration


```python
decompose() -> list[nemo_curator.stages.base.ProcessingStage]
```

Decompose this composite stage into its constituent stages.


```python
get_description() -> str
```

Get a description of this composite stage.

