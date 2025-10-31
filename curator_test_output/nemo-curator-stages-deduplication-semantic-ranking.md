---
layout: overview
slug: nemo-curator-stages-deduplication-semantic-ranking
---

# nemo_curator.stages.deduplication.semantic.ranking



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`RankingStrategy`](#nemo_curatorstagesdeduplicationsemanticrankingrankingstrategy) | Flexible ranking strategy that allows users to specify metadata columns and sorting order. |

### API

```python
class nemo_curator.stages.deduplication.semantic.ranking.RankingStrategy(metadata_cols: list[str], ascending: list[bool] | bool = True, strategy: typing.Literal[sort, random] = 'sort', random_seed: int = 42)
```

Flexible ranking strategy that allows users to specify metadata columns and sorting order.

This design allows for extensible ranking based on any metadata columns with
user-specified sorting criteria.

### Initialization

Initialize ranking strategy.

**Parameters:**

- **metadata_cols**: List of metadata column names to sort by (in priority order)
- **ascending**: Boolean or list of booleans indicating sort order for each column.
  If single bool, applies to all columns.
- **strategy**: Ranking strategy - "sort" for sorting by metadata_cols, "random" for random
- **random_seed**: Seed for random strategy


```python
rank_cluster(cluster_df: cudf.DataFrame) -> cudf.DataFrame
```

Rank cluster based on the specified strategy.


```python
metadata_based(
    metadata_cols: list[str],
    ascending: list[bool] | bool = True,
    random_seed: int = 42
) -> nemo_curator.stages.deduplication.semantic.ranking.RankingStrategy
```

Create a metadata-based ranking strategy.

**Parameters:**

<ParamField path="metadata_cols" type="list[str]">
  List of metadata column names to sort by (in priority order)
</ParamField>

<ParamField path="ascending" type="list[bool] | bool" default="True">
  Boolean or list of booleans indicating sort order for each column
</ParamField>

<ParamField path="random_seed" type="int" default="42">
  Random seed for reproducible results
</ParamField>

**Returns:**

RankingStrategy instance configured for metadata-based ranking


```python
random(random_seed: int = 42) -> nemo_curator.stages.deduplication.semantic.ranking.RankingStrategy
```

Create a random ranking strategy.

**Parameters:**

<ParamField path="random_seed" type="int" default="42">
  Random seed for reproducible results
</ParamField>

**Returns:**

RankingStrategy instance configured for random ranking

