`fern_renderer`

Renderer for Fern.

## Module Contents

### Classes

[`FernRenderer`](#fernrenderer) | Render the documentation as Fern-compatible Markdown.

### Data

`_RE_DELIMS`

## API

### _RE_DELIMS
**Value**: `compile(...)`



## FernRenderer

```python
class FernRenderer(db: autodoc2.db.Database, config: autodoc2.config.Config, *, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, all_resolver: autodoc2.resolve_all.AllResolver | None = None, standalone: bool = True)
```

**Bases**: `autodoc2.render.base.RendererBase`

Render the documentation as Fern-compatible Markdown.

### Initialization

Initialise the renderer.

**Parameters:**

- **db**: The database to obtain objects from.
- **config**: The configuration.
- **warn**: The function to use to log warnings.
- **all_resolver**: The resolver to use, for following __all__ children.
- **standalone**: If True, this renderer is being used to create a standalone document


### EXTENSION
**Value**: `.md`



### render_item

```python
def render_item(full_name: str) -> typing.Iterable[str]
```

Render a single item by dispatching to the appropriate method.


### render_function

```python
def render_function(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a function.


### render_module

```python
def render_module(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a module.


### render_package

```python
def render_package(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a package.


### render_class

```python
def render_class(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a class.


### render_exception

```python
def render_exception(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for an exception.


### render_property

```python
def render_property(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a property.


### render_method

```python
def render_method(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a method.


### render_attribute

```python
def render_attribute(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for an attribute.


### render_data

```python
def render_data(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a data item.


### generate_summary

```python
def generate_summary(objects: list[autodoc2.utils.ItemData], alias: dict[str, str] | None = None) -> typing.Iterable[str]
```

Generate a summary of the objects.


### _format_docstring_sections

```python
def _format_docstring_sections(docstring: str) -> typing.Iterable[str]
```

Parse docstring into structured sections like Parameters, Returns, etc.

