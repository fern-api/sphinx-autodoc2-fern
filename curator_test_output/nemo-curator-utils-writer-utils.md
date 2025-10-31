---
layout: overview
slug: nemo-curator-utils-writer-utils
---

# nemo_curator.utils.writer_utils



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`JsonEncoderCustom`](#nemo_curatorutilswriter_utilsjsonencodercustom) | Custom JSON encoder that handles types that are not JSON serializable. |

### Functions

| Name | Description |
|------|-------------|
| [`write_bytes`](#nemo_curatorutilswriter_utilswrite_bytes) | Write bytes to local path. |
| [`write_parquet`](#nemo_curatorutilswriter_utilswrite_parquet) | Write parquet to local path. |
| [`write_json`](#nemo_curatorutilswriter_utilswrite_json) | Write json to local path. |
| [`write_csv`](#nemo_curatorutilswriter_utilswrite_csv) | Write csv to local path. |

### API

```python
class nemo_curator.utils.writer_utils.JsonEncoderCustom(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)
```

**Bases**: `json.JSONEncoder`

Custom JSON encoder that handles types that are not JSON serializable.

Example:
```python
json.dumps(data, cls=JsonEncoderClass)
```

### Initialization

Constructor for JSONEncoder, with sensible defaults.

If skipkeys is false, then it is a TypeError to attempt
encoding of keys that are not str, int, float or None.  If
skipkeys is True, such items are simply skipped.

If ensure_ascii is true, the output is guaranteed to be str
objects with all incoming non-ASCII characters escaped.  If
ensure_ascii is false, the output can contain non-ASCII characters.

If check_circular is true, then lists, dicts, and custom encoded
objects will be checked for circular references during encoding to
prevent an infinite recursion (which would cause an OverflowError).
Otherwise, no such check takes place.

If allow_nan is true, then NaN, Infinity, and -Infinity will be
encoded as such.  This behavior is not JSON specification compliant,
but is consistent with most JavaScript based encoders and decoders.
Otherwise, it will be a ValueError to encode such floats.

If sort_keys is true, then the output of dictionaries will be
sorted by key; this is useful for regression tests to ensure
that JSON serializations can be compared on a day-to-day basis.

If indent is a non-negative integer, then JSON array
elements and object members will be pretty-printed with that
indent level.  An indent level of 0 will only insert newlines.
None is the most compact representation.

If specified, separators should be an (item_separator, key_separator)
tuple.  The default is (', ', ': ') if *indent* is ``None`` and
(',', ': ') otherwise.  To get the most compact JSON representation,
you should specify (',', ':') to eliminate whitespace.

If specified, default is a function that gets called for objects
that can't otherwise be serialized.  It should return a JSON encodable
version of the object or raise a ``TypeError``.


```python
default(obj: object) -> str | object
```

Encode an object for JSON serialization.

**Parameters:**

<ParamField path="obj" type="object">
  Object to encode.
</ParamField>

**Returns:**

Encoded object.


```python
nemo_curator.utils.writer_utils.write_bytes(
    buffer: bytes,
    dest: pathlib.Path,
    desc: str,
    source_video: str,
    *,
    verbose: bool,
    backup_and_overwrite: bool = False,
    overwrite: bool = False
) -> None
```

Write bytes to local path.

**Parameters:**

<ParamField path="buffer" type="bytes">
  Bytes to write.
</ParamField>

<ParamField path="dest" type="pathlib.Path">
  Destination to write.
</ParamField>

<ParamField path="desc" type="str">
  Description of the write.
</ParamField>

<ParamField path="source_video" type="str">
  Source video.
</ParamField>

<ParamField path="verbose" type="bool">
  Verbosity.
</ParamField>

<ParamField path="backup_and_overwrite" type="bool" default="False">
  Backup and overwrite.
</ParamField>

<ParamField path="overwrite" type="bool" default="False">
  Overwrite.
</ParamField>


```python
nemo_curator.utils.writer_utils.write_parquet(
    data: list[dict[str, str]],
    dest: pathlib.Path,
    desc: str,
    source_video: str,
    *,
    verbose: bool,
    backup_and_overwrite: bool = False,
    overwrite: bool = False
) -> None
```

Write parquet to local path.

**Parameters:**

<ParamField path="data" type="list[dict[str, str]]">
  Data to write.
</ParamField>

<ParamField path="dest" type="pathlib.Path">
  Destination to write.
</ParamField>

<ParamField path="desc" type="str">
  Description of the write.
</ParamField>

<ParamField path="source_video" type="str">
  Source video.
</ParamField>

<ParamField path="verbose" type="bool">
  Verbosity.
</ParamField>

<ParamField path="backup_and_overwrite" type="bool" default="False">
  Whether to backup existing file before overwriting.
</ParamField>

<ParamField path="overwrite" type="bool" default="False">
  Whether to overwrite existing file.
</ParamField>


```python
nemo_curator.utils.writer_utils.write_json(
    data: dict[str, typing.Any],
    dest: pathlib.Path,
    desc: str,
    source_video: str,
    *,
    verbose: bool,
    backup_and_overwrite: bool = False,
    overwrite: bool = False
) -> None
```

Write json to local path.

**Parameters:**

<ParamField path="data" type="dict[str, typing.Any]">
  Data to write.
</ParamField>

<ParamField path="dest" type="pathlib.Path">
  Destination to write.
</ParamField>

<ParamField path="desc" type="str">
  Description of the write.
</ParamField>

<ParamField path="source_video" type="str">
  Source video.
</ParamField>

<ParamField path="verbose" type="bool">
  Verbosity.
</ParamField>

<ParamField path="backup_and_overwrite" type="bool" default="False">
  Backup and overwrite.
</ParamField>

<ParamField path="overwrite" type="bool" default="False">
  Overwrite.
</ParamField>


```python
nemo_curator.utils.writer_utils.write_csv(
    dest: pathlib.Path,
    desc: str,
    source_video: str,
    data: list[list[str]],
    *,
    verbose: bool,
    backup_and_overwrite: bool = False
) -> None
```

Write csv to local path.

**Parameters:**

<ParamField path="dest" type="pathlib.Path">
  Destination to write.
</ParamField>

<ParamField path="desc" type="str">
  Description of the write.
</ParamField>

<ParamField path="source_video" type="str">
  Source video.
</ParamField>

<ParamField path="data" type="list[list[str]]">
  Data to write.
</ParamField>

<ParamField path="verbose" type="bool">
  Verbosity.
</ParamField>

<ParamField path="backup_and_overwrite" type="bool" default="False">
  Backup and overwrite.
</ParamField>

