---
layout: overview
slug: nemo-curator-utils-grouping
---

# nemo_curator.utils.grouping

Utility Functions for grouping iterables.

This module provides a collection of utility functions designed to assist with common tasks related to manipulating
and transforming iterables in Python.

These utilities are generic and work with any iterable types. They're particularly useful for data processing tasks,
batching operations, and other scenarios where dividing data into specific groupings is necessary.

Note:
    While these utilities are designed for flexibility and ease-of-use,
    they may not be optimized for extremely large datasets or performance-critical applications.


## Module Contents

### Functions

| Name | Description |
|------|-------------|
| [`split_by_chunk_size`](#nemo_curatorutilsgroupingsplit_by_chunk_size) | Split an iterable into chunks of the specified size. |
| [`split_into_n_chunks`](#nemo_curatorutilsgroupingsplit_into_n_chunks) | Split an iterable into a specified number of chunks. |
| [`pairwise`](#nemo_curatorutilsgroupingpairwise) | Return pairs of consecutive items from the input iterable. |

### Data

`T`

### API

```python
nemo_curator.utils.grouping.T
```

**Value**: `TypeVar(...)`


```python
nemo_curator.utils.grouping.split_by_chunk_size(
    iterable: collections.abc.Iterable[nemo_curator.utils.grouping.T],
    chunk_size: int,
    custom_size_func: typing.Callable[[nemo_curator.utils.grouping.T], int] = lambda x: 1,
    *,
    drop_incomplete_chunk: bool = False
) -> collections.abc.Generator[list[nemo_curator.utils.grouping.T], None, None]
```

Split an iterable into chunks of the specified size.

**Parameters:**

**Returns:**

- Generator[list[T], None, None]: Chunks of the input iterable.


```python
nemo_curator.utils.grouping.split_into_n_chunks(
    iterable: collections.abc.Iterable[nemo_curator.utils.grouping.T],
    num_chunks: int
) -> collections.abc.Generator[list[nemo_curator.utils.grouping.T], None, None]
```

Split an iterable into a specified number of chunks.

**Parameters:**

**Returns:**

- Generator[list[T], None, None]: Chunks of the input iterable.


```python
nemo_curator.utils.grouping.pairwise(iterable: collections.abc.Iterable[nemo_curator.utils.grouping.T]) -> collections.abc.Iterable[tuple[nemo_curator.utils.grouping.T, nemo_curator.utils.grouping.T]]
```

Return pairs of consecutive items from the input iterable.

**Parameters:**

**Returns:**

Iterable[tuple[T, T]]: Pairs of consecutive items.

