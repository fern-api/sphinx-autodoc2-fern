---
layout: overview
slug: nemo-curator-utils-hf-download-utils
---

# nemo_curator.utils.hf_download_utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`download_model_from_hf`](#nemo_curatorutilshf_download_utilsdownload_model_from_hf) | Download a model from Hugging Face. |

### API

```python
nemo_curator.utils.hf_download_utils.download_model_from_hf(
    model_id: str,
    local_dir: str | pathlib.Path,
    ignore_patterns: list[str] | None = None,
    filename: str | None = None,
    revision: str | None = None
) -> None
```

Download a model from Hugging Face.

This function downloads either a specific file or the entire model repository
from Hugging Face Hub to a local directory.

**Parameters:**

**Raises:**

ValueError: If both filename and ignore_patterns are provided (not supported).
Examples:
# Download entire model repository
download_model_from_hf('gpt2', './models/gpt2')
# Download specific file
download_model_from_hf('gpt2', './models/gpt2', filename='config.json')
# Download with ignore patterns
download_model_from_hf('gpt2', './models/gpt2',
ignore_patterns=['*.bin', '*.safetensors'])
# Download specific revision
download_model_from_hf('gpt2', './models/gpt2', revision='main')

