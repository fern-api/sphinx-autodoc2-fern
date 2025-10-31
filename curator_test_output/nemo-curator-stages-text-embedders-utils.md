---
layout: overview
slug: nemo-curator-stages-text-embedders-utils
---

# nemo_curator.stages.text.embedders.utils



## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`create_list_series_from_1d_or_2d_ar`](#nemo_curatorstagestextembeddersutilscreate_list_series_from_1d_or_2d_ar) | Create a cudf list series from 2d arrays. This code comes from https://github.com/rapidsai/crossfit/blob/76f74d0d927cf76313a3960d7dd5575d1dff2f06/crossfit/backend/cudf/series.py#L20-L32 |

### API

```python
nemo_curator.stages.text.embedders.utils.create_list_series_from_1d_or_2d_ar(
    ar: typing.Any, index: cudf.Index
) -> cudf.Series
```

Create a cudf list series from 2d arrays.
This code comes from https://github.com/rapidsai/crossfit/blob/76f74d0d927cf76313a3960d7dd5575d1dff2f06/crossfit/backend/cudf/series.py#L20-L32

**Parameters:**

**Returns:**

cudf.Series: cudf series with the index respected

