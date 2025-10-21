---
layout: overview
slug: package
---

# package

This is a test package.

## Subpackages

- **[`a`](a)** - This is a test module.

## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`Class`](#packageclass) | This is a class. |

### Functions

| Name | Description |
|------|-------------|
| [`func`](#packagefunc) | This is a function. |

### Data

`__all__`
`p`

### API

```python
package.__all__
```

**Value**: `['p', 'a1', 'alias']`


```python
package.p
```

**Value**: `1`

p can be documented here.


```python
package.func(
    a: str, b: int
) -> package.a.c.ac1
```

This is a function.


```python
class package.Class
```

This is a class.

```python
x: int
```

**Value**: `1`

x can be documented here.


```python
method(
    a: str, b: int
) -> ...
```

This is a method.


```python
prop: package.a.c.ac1 | None
```

This is a property.


```python
class Nested
```

This is a nested class.
