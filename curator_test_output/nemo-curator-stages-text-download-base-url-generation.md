---
layout: overview
slug: nemo-curator-stages-text-download-base-url-generation
---

# nemo_curator.stages.text.download.base.url_generation



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`URLGenerator`](#nemo_curatorstagestextdownloadbaseurl_generationurlgenerator) | Abstract base class for URL generators - generates URLs from minimal input. |
| [`URLGenerationStage`](#nemo_curatorstagestextdownloadbaseurl_generationurlgenerationstage) | Stage that generates URLs from minimal input parameters. |

### API

```python
class nemo_curator.stages.text.download.base.url_generation.URLGenerator
```

**Bases**: `abc.ABC`

Abstract base class for URL generators - generates URLs from minimal input.

```python
generate_urls() -> list[str]
```

Generate a list of URLs to download.


```python
class nemo_curator.stages.text.download.base.url_generation.URLGenerationStage
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks._EmptyTask, nemo_curator.tasks.FileGroupTask]`

Stage that generates URLs from minimal input parameters.

This allows pipelines to start with URL generation (like Common Crawl).

```python
url_generator: nemo_curator.stages.text.download.base.url_generation.URLGenerator
```

**Value**: `None`


```python
limit: int | None
```

**Value**: `None`


```python
_resources
```

**Value**: `Resources(...)`


```python
__post_init__()
```


```python
inputs() -> tuple[list[str], list[str]]
```

Define input requirements - expects empty task.


```python
outputs() -> tuple[list[str], list[str]]
```

Define output - produces FileGroupTask with URLs.


```python
process(task: nemo_curator.tasks._EmptyTask) -> list[nemo_curator.tasks.FileGroupTask]
```

Generate URLs and create FileGroupTasks.

**Parameters:**

**Returns:**

list[FileGroupTask]: List of tasks containing URLs


```python
ray_stage_spec() -> dict[str, typing.Any]
```

