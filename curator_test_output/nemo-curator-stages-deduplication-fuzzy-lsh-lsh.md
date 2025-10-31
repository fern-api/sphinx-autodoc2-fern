---
layout: overview
slug: nemo-curator-stages-deduplication-fuzzy-lsh-lsh
---

# nemo_curator.stages.deduplication.fuzzy.lsh.lsh



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`LSHActor`](#nemo_curatorstagesdeduplicationfuzzylshlshlshactor) | Actor that performs LSH operations and shuffling using Ray. |

### API

```python
class nemo_curator.stages.deduplication.fuzzy.lsh.lsh.LSHActor(nranks: int, total_nparts: int, num_bands: int, minhashes_per_band: int, id_field: str = CURATOR_DEDUP_ID_STR, minhash_field: str = CURATOR_DEFAULT_MINHASH_FIELD, output_path: str = './', rmm_pool_size: int | typing.Literal[auto] | None = 'auto', spill_memory_limit: int | typing.Literal[auto] | None = 'auto', *, enable_statistics: bool = False, read_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None)
```

**Bases**: `nemo_curator.stages.deduplication.shuffle_utils.rapidsmpf_shuffler.BulkRapidsMPFShuffler`

Actor that performs LSH operations and shuffling using Ray.

Parameters
----------
nranks
    Number of ranks in the communication group.
total_nparts
    Total number of output partitions.
num_bands
    Number of LSH bands.
minhashes_per_band
    Number of minhashes per band.
id_field
    Name of the ID field in input data.
minhash_field
    Name of the minhash field in input data.
output_path
    Path to write output files.
rmm_pool_size
    Size of the RMM GPU memory pool in bytes.
    If "auto", the memory pool is set to 90% of the free GPU memory.
    If None, the memory pool is set to 50% of the free GPU memory that can expand if needed.
spill_memory_limit
    Device memory limit in bytes for spilling to host.
    If "auto", the limit is set to 80% of the RMM pool size.
    If None spilling is disabled.
enable_statistics
    Whether to collect statistics.
read_kwargs
    Keyword arguments for the read method.
write_kwargs
    Keyword arguments for the write method.

Notes
-----
Architecture and Processing Flow:

This implementation follows a clean separation of responsibilities with distinct methods
for each part of the pipeline:

Input Phase:
- `read_minhash`: Reads minhash files and returns a DataFrame

Processing Phase:
- `minhash_to_bands`: Transforms a single minhash DataFrame into LSH bands
- `read_and_insert`: Orchestrates reading, band creation, and insertion

Output Phase:
- `extract_and_group`: Extracts and groups shuffled data, yielding results as a generator
- `extract_and_write`: Processes each yielded result and writes to output files immediately

1. Files are read using `read_minhash`
2. Data is processed with `minhash_to_bands` to extract LSH bucket IDs
3. Processed data is immediately inserted into the shuffler
4. Results are extracted and processed one partition at a time using generators
5. Each partition is written to disk as soon as it's processed, without accumulating in memory

```python
_generate_band_ranges(
    num_bands: int, minhashes_per_band: int
) -> list[list[int]]
```

Generates a list of indices for the minhash ranges given num_bands &
minhashes_per_band.
eg: num_bands=3, minhashes_per_band=2
[[0, 1], [2, 3], [4, 5]]


```python
read_minhash(filepaths: list[str]) -> cudf.DataFrame
```

Read minhash data from parquet files.

Parameters
----------
filepaths
    List of paths to minhash files.

Returns
-------
    DataFrame containing minhash data from all input files.


```python
minhash_to_bands(
    minhash_df: cudf.DataFrame, band_range: tuple[int, int]
) -> cudf.DataFrame
```

Process a single minhash DataFrame to extract LSH band data.

Parameters
----------
minhash_df
    DataFrame containing minhash data.
band_range
    Tuple of (start_band, end_band) to process.

Returns
-------
    DataFrame with document IDs and their corresponding bucket IDs.


```python
read_and_insert(
    filepaths: list[str], band_range: tuple[int, int]
) -> None
```

Read minhashes from files, create LSH bands, and insert into the shuffler.

This method orchestrates the full processing pipeline:
1. Reads minhash data from parquet files in batches
2. Processes each batch to extract LSH bands
3. Inserts the bands into the shuffler for distribution

Parameters
----------
filepaths
    List of paths to minhash files.
band_range
    Tuple of (start_band, end_band) to process.

Returns
-------
None


```python
group_by_bucket(
    df: cudf.DataFrame, include_singles: bool = False
) -> cudf.DataFrame
```

Group items by bucket ID and aggregate IDs into lists.

Parameters
----------
df
    DataFrame containing bucket IDs and document IDs.
include_singles
    If True, include buckets with only one document. Default is False, which
    excludes single-document buckets as they cannot form duplicates. Set to True
    when building an LSH index that needs to maintain all documents.

Returns
-------
    DataFrame with bucket IDs and lists of document IDs.


```python
extract_and_group() -> collections.abc.Iterator[tuple[int, cudf.DataFrame]]
```

Extract shuffled partitions and group by bucket ID, yielding results one by one.

This generator approach allows processing each partition immediately after it's ready,
which is more memory-efficient than collecting all partitions first.

Yields
------
tuple
    A tuple of (partition_id, grouped_df) where grouped_df contains bucket IDs
    and their corresponding document ID lists.


```python
extract_and_write() -> list[dict[str, typing.Any]]
```

Extract shuffled partitions, group by bucket ID, and write results to files.

This method orchestrates the post-processing pipeline:
1. Extracts partitioned data from the shuffler using extract_and_group
2. Writes each grouped partition to a parquet file as soon as it's available

This generator-based approach is more memory-efficient since it processes
one partition at a time rather than collecting all partitions in memory.

Returns
-------
list[dict[str, Any]]
    A list of dictionaries containing partition information.
    Each dictionary contains:
    - partition_id: The ID of the partition
    - path: The path to the partition file
    - num_docs: The number of documents in the partition

