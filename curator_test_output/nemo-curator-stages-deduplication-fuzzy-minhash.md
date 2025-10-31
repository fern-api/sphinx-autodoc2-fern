---
layout: overview
slug: nemo-curator-stages-deduplication-fuzzy-minhash
---

# nemo_curator.stages.deduplication.fuzzy.minhash



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`MinHash`](#nemo_curatorstagesdeduplicationfuzzyminhashminhash) | Base class for computing minhash signatures of a document corpus |
| [`GPUMinHash`](#nemo_curatorstagesdeduplicationfuzzyminhashgpuminhash) | Base class for computing minhash signatures of a document corpus |
| [`MinHashStage`](#nemo_curatorstagesdeduplicationfuzzyminhashminhashstage) | ProcessingStage for computing MinHash signatures on documents for fuzzy deduplication. |

### API

```python
class nemo_curator.stages.deduplication.fuzzy.minhash.MinHash(seed: int = 42, num_hashes: int = 260, char_ngrams: int = 24, use_64bit_hash: bool = False)
```

**Bases**: `abc.ABC`

Base class for computing minhash signatures of a document corpus

### Initialization

Parameters
----------
seed: Seed for minhash permutations
num_hashes: Length of minhash signature (No. of minhash permutations)
char_ngrams: Width of text window (in characters) while computing minhashes.
use_64bit_hash: Whether to use a 64 bit hash function.


```python
generate_seeds(
    n_permutations: int = 260,
    seed: int = 0,
    bit_width: int = 32
) -> numpy.ndarray
```

Generate seeds for all minhash permutations based on the given seed.
This is a placeholder that child classes should implement if needed.


```python
compute_minhashes(text_series: typing.Any) -> typing.Any
```

Compute minhash signatures for the given dataframe text column.


```python
class nemo_curator.stages.deduplication.fuzzy.minhash.GPUMinHash(seed: int = 42, num_hashes: int = 260, char_ngrams: int = 24, use_64bit_hash: bool = False, pool: bool = False)
```

**Bases**: `nemo_curator.stages.deduplication.fuzzy.minhash.MinHash`

```python
generate_seeds(
    n_permutations: int = 260,
    seed: int = 0,
    bit_width: int = 32
) -> numpy.ndarray
```

Generate seeds for all minhash permutations based on the given seed.


```python
minhash32(ser: cudf.Series) -> cudf.Series
```

Compute 32bit minhashes based on the MurmurHash3 algorithm


```python
minhash64(ser: cudf.Series) -> cudf.Series
```

Compute 64bit minhashes based on the MurmurHash3 algorithm


```python
compute_minhashes(text_series: cudf.Series) -> cudf.Series
```

Compute minhash signatures for the given text series.

Parameters
----------
text_series: cudf.Series
    Series containing text data to compute minhashes for

Returns
-------
cudf.Series containing minhash signatures


```python
class nemo_curator.stages.deduplication.fuzzy.minhash.MinHashStage(output_path: str, text_field: str = 'text', minhash_field: str = CURATOR_DEFAULT_MINHASH_FIELD, char_ngrams: int = 24, num_hashes: int = 260, seed: int = 42, use_64bit_hash: bool = False, read_format: typing.Literal[jsonl, parquet] = 'jsonl', read_kwargs: dict[str, typing.Any] | None = None, write_kwargs: dict[str, typing.Any] | None = None, pool: bool = True)
```

**Bases**: `nemo_curator.stages.base.ProcessingStage[nemo_curator.tasks.FileGroupTask, nemo_curator.tasks.FileGroupTask]`, `nemo_curator.stages.deduplication.io_utils.DeduplicationIO`

ProcessingStage for computing MinHash signatures on documents for fuzzy deduplication.

This stage takes FileGroupTask containing paths to input documents and produces
FileGroupTask containing paths to computed minhash signature files. It uses GPU-accelerated
MinHash computation to generate locality-sensitive hash signatures that can be used
for approximate duplicate detection.

The stage automatically handles:
- Reading input files (JSONL or Parquet format)
- Assigning unique Integer IDs to documents using the IdGenerator actor
- Computing MinHash signatures using GPU acceleration
- Writing results to Parquet files

Parameters
----------
output_path : str
    Base path where minhash output files will be written
text_field : str, default="text"
    Name of the field containing text to compute minhashes from
minhash_field : str, default="_minhash_signature"
    Name of the field where minhash signatures will be stored
char_ngrams : int, default=24
    Width of character n-grams for minhashing
num_hashes : int, default=260
    Number of hash functions (length of minhash signature)
seed : int, default=42
    Random seed for reproducible minhash generation
use_64bit_hash : bool, default=False
    Whether to use 64-bit hash functions (vs 32-bit)
read_format : Literal["jsonl", "parquet"], default="jsonl"
    Format of input files
read_kwargs : dict[str, Any] | None, default=None
    Additional keyword arguments for reading input files
write_kwargs : dict[str, Any] | None, default=None
    Additional keyword arguments for writing output files

Examples
--------
>>> stage = MinHashStage(
...     output_path="/path/to/minhash/output",
...     text_field="content",
...     num_hashes=128,
...     char_ngrams=5
... )
>>> # Use in a pipeline to process document batches

```python
setup(_worker_metadata: WorkerMetadata | None = None) -> None
```

Initialize the GPU MinHash processor and ID generator.


```python
inputs() -> tuple[list[str], list[str]]
```

Define input requirements.


```python
outputs() -> tuple[list[str], list[str]]
```

Define outputs - produces FileGroupTask with minhash files.


```python
process(task: nemo_curator.tasks.FileGroupTask) -> nemo_curator.tasks.FileGroupTask
```

Process a group of files to compute minhashes.

**Parameters:**

<ParamField path="task" type="nemo_curator.tasks.FileGroupTask">
  FileGroupTask containing file paths to process
</ParamField>

**Returns:**

FileGroupTask containing paths to minhash output files

