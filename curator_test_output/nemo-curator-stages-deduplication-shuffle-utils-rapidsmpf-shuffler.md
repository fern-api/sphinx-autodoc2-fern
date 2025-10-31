---
layout: overview
slug: nemo-curator-stages-deduplication-shuffle-utils-rapidsmpf-shuffler
---

# nemo_curator.stages.deduplication.shuffle_utils.rapidsmpf_shuffler



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`BulkRapidsMPFShuffler`](#nemo_curatorstagesdeduplicationshuffle_utilsrapidsmpf_shufflerbulkrapidsmpfshuffler) | Class that performs a bulk shuffle operation. This class is compatible with Ray Actors communicating with each other using UCXX communication. Parameters ---------- nranks Number of ranks in the communication group. total_nparts Total number of output partitions. shuffle_on List of column names to shuffle on. output_path Path to write output files. rmm_pool_size Size of the RMM GPU memory pool in bytes. If "auto", the memory pool is set to 90% of the free GPU memory. If None, the memory pool is set to 50% of the free GPU memory that can expand if needed. spill_memory_limit Device memory limit in bytes for spilling to host. If "auto", the limit is set to 80% of the RMM pool size. If None spilling is disabled. enable_statistics Whether to collect shuffle statistics. read_kwargs Keyword arguments for cudf.read_parquet method. write_kwargs Keyword arguments for cudf.to_parquet method. |

### API

```python
class nemo_curator.stages.deduplication.shuffle_utils.rapidsmpf_shuffler.BulkRapidsMPFShuffler(nranks: int, total_nparts: int, shuffle_on: list[str], output_path: str = './', rmm_pool_size: int | typing.Literal[auto] | None = 'auto', spill_memory_limit: int | typing.Literal[auto] | None = 'auto', *, enable_statistics: bool = False, read_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None)
```

**Bases**: `rapidsmpf.utils.ray_utils.BaseShufflingActor`

Class that performs a bulk shuffle operation.
This class is compatible with Ray Actors communicating with each other using UCXX communication.
Parameters
----------
nranks
    Number of ranks in the communication group.
total_nparts
    Total number of output partitions.
shuffle_on
    List of column names to shuffle on.
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
    Whether to collect shuffle statistics.
read_kwargs
    Keyword arguments for cudf.read_parquet method.
write_kwargs
    Keyword arguments for cudf.to_parquet method.

```python
setup_worker(root_address_bytes: bytes) -> None
```

Setup the UCXX communication and a shuffle operation.

Parameters
----------
root_address_bytes
    Address of the root worker for UCXX initialization.


```python
cleanup() -> None
```

Cleanup the UCXX communication and the shuffle operation.


```python
read_batch(paths: list[str]) -> tuple[cudf.DataFrame | None, list[str]]
```

Read a single batch of Parquet files using cuDF.

Parameters
----------
paths
    List of file paths to the Parquet files.

Returns
-------
    A tuple containing the DataFrame (or None if empty) and the column names.


```python
write_table(
    table: pylibcudf.Table,
    output_path: str,
    partition_id: int | str,
    column_names: list[str]
) -> str
```

Write a pylibcudf Table to a Parquet file using cuDF.

Parameters
----------
table
    The table to write.
output_path
    The path to write the table to.
partition_id
    Partition id used for naming the output file.
column_names
    The column names of the table.


```python
insert_chunk(
    table: pylibcudf.Table | cudf.DataFrame, column_names: list[str]
) -> None
```

Insert a pylibcudf Table or cuDF DataFrame into the shuffler.

Parameters
----------
table
    The table or DataFrame to insert.
column_names
    The column names of the table.


```python
read_and_insert(
    paths: list[str], batchsize: int | None = None
) -> list[str]
```

Read the list of parquet files every batchsize and insert the partitions into the shuffler.

Parameters
----------
paths
    List of file paths to the Parquet files.
batchsize
    Number of files to read in each batch.

Returns
-------
    The column names of the table.


```python
insert_finished() -> None
```

Tell the shuffler that we are done inserting data.


```python
extract() -> collections.abc.Iterator[tuple[int, pylibcudf.Table]]
```

Extract shuffled partitions as they become ready.

Returns
-------
    An iterator over the shuffled partitions.


```python
extract_and_write(column_names: list[str]) -> list[tuple[int, str]]
```

Extract and write shuffled partitions.

Parameters
----------
column_names
    The column names of the table.

