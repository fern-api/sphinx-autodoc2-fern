`autodoc2`

Analyse a python project and create documentation for it.

## Subpackages

- **[render](#render)**
- **[sphinx](#sphinx)** - Module for Sphinx integration.

## Submodules

- **[db](#db)** - A database interface for storing and querying the analysis items.
- **[config](#config)** - The configuration for the extension.
- **[analysis](#analysis)** - Analyse of Python code using astroid....
- **[cli](#cli)** - CLI for the package.
- **[utils](#utils)** - Utility functions and types.
- **[resolve_all](#resolve_all)** - Handling of ``__all__`` resolution.
- **[astroid_utils](#astroid_utils)** - Utilities for working with astroid nodes.

## Module Contents

### Functions

[`setup`](#setup) | Entrypoint for sphinx.

### Data

`__version__`

## API

`autodoc2.render`



## Submodules

- **[myst_](#myst_)** - Renderer for MyST.
- **[rst_](#rst_)** - Renderer for reStructuredText.
- **[base](#base)** - Convert the database items into documentation.
- **[fern_](#fern_)** - Renderer for Fern.

## API

`autodoc2.render.myst_`

Renderer for MyST.

## Module Contents

### Classes

[`MystRenderer`](#mystrenderer) | Render the documentation as MyST.

### Data

`_RE_DELIMS`

## API

### _RE_DELIMS
**Value**: `compile(...)`



## MystRenderer

```python
class MystRenderer(db: autodoc2.db.Database, config: autodoc2.config.Config, *, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, all_resolver: autodoc2.resolve_all.AllResolver | None = None, standalone: bool = True)
```

**Bases**: `autodoc2.render.base.RendererBase`

Render the documentation as MyST.

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


### generate_summary

```python
def generate_summary(objects: list[autodoc2.utils.ItemData], alias: dict[str, str] | None = None) -> typing.Iterable[str]
```


### enclosing_backticks

```python
def enclosing_backticks(text: str) -> str
```

Ensure the enclosing backticks are more than any inner ones.


### render_package

```python
def render_package(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a package.


### render_module

```python
def render_module(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a module.


### render_function

```python
def render_function(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a function.


### render_exception

```python
def render_exception(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for an exception.


### render_class

```python
def render_class(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a class.


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


### _reformat_cls_base_myst

```python
def _reformat_cls_base_myst(value: str) -> str
```

Reformat the base of a class for RST.

Base annotations can come in the form::

    A[B, C, D]

which we want to reformat as::

    {py:obj}`A`\[{py:obj}`B`, {py:obj}`C`, {py:obj}`D`\]


`autodoc2.render.rst_`

Renderer for reStructuredText.

## Module Contents

### Classes

[`RstRenderer`](#rstrenderer) | Render the documentation as reStructuredText.

### Data

`_RE_DELIMS`

## API

### _RE_DELIMS
**Value**: `compile(...)`



## RstRenderer

```python
class RstRenderer(db: autodoc2.db.Database, config: autodoc2.config.Config, *, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, all_resolver: autodoc2.resolve_all.AllResolver | None = None, standalone: bool = True)
```

**Bases**: `autodoc2.render.base.RendererBase`

Render the documentation as reStructuredText.

### Initialization

Initialise the renderer.

**Parameters:**

- **db**: The database to obtain objects from.
- **config**: The configuration.
- **warn**: The function to use to log warnings.
- **all_resolver**: The resolver to use, for following __all__ children.
- **standalone**: If True, this renderer is being used to create a standalone document


### EXTENSION
**Value**: `.rst`



### render_item

```python
def render_item(full_name: str) -> typing.Iterable[str]
```


### generate_summary

```python
def generate_summary(objects: list[autodoc2.utils.ItemData], alias: dict[str, str] | None = None) -> typing.Iterable[str]
```


### render_package

```python
def render_package(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a package.


### render_module

```python
def render_module(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a module.


### render_function

```python
def render_function(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a function.


### render_exception

```python
def render_exception(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for an exception.


### render_class

```python
def render_class(item: autodoc2.utils.ItemData) -> typing.Iterable[str]
```

Create the content for a class.


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


### _reformat_cls_base_rst

```python
def _reformat_cls_base_rst(value: str) -> str
```

Reformat the base of a class for RST.

Base annotations can come in the form::

    A[B, C, D]

which we want to reformat as::

    :py:obj:`A`\ [\ :py:obj:`B`\ , :py:obj:`C`\ , :py:obj:`D`\ ]

The backslash escapes are needed because of:
https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#character-level-inline-markup-1


`autodoc2.render.base`

Convert the database items into documentation.

## Module Contents

### Classes

[`RendererBase`](#rendererbase) | The base renderer.

## API

## RendererBase

```python
class RendererBase(db: autodoc2.db.Database, config: autodoc2.config.Config, *, warn: typing.Callable[[str, autodoc2.utils.WarningSubtypes], None] | None = None, all_resolver: autodoc2.resolve_all.AllResolver | None = None, standalone: bool = True)
```

**Bases**: `abc.ABC`

The base renderer.

### Initialization

Initialise the renderer.

**Parameters:**

- **db**: The database to obtain objects from.
- **config**: The configuration.
- **warn**: The function to use to log warnings.
- **all_resolver**: The resolver to use, for following __all__ children.
- **standalone**: If True, this renderer is being used to create a standalone document


### EXTENSION
**Type**: `typing.ClassVar[str]`
**Value**: `.txt`

The extension for the output files.

### _is_hidden_cache
**Type**: `collections.OrderedDict[str, bool]`
**Value**: `OrderedDict(...)`

Cache for the is_hidden function: full_name -> bool.

### config: `autodoc2.config.Config`

The configuration.


### standalone: `bool`

If True, this renderer is being used to create a standalone document.


### warn

```python
def warn(msg: str, type_: autodoc2.utils.WarningSubtypes = WarningSubtypes.RENDER_ERROR) -> None
```

Warn the user.


### get_item

```python
def get_item(full_name: str) -> autodoc2.utils.ItemData | None
```

Get an item from the database, by full_name.


### get_children

```python
def get_children(item: autodoc2.utils.ItemData, types: None | set[str] = None, *, omit_hidden: bool = True) -> typing.Iterable[autodoc2.utils.ItemData]
```

Get the children of this item, sorted according to the config.

If module and full_name in module_all_regexes,
it will use the __all__ list instead of the children.

**Parameters:**

- **item**: The item to get the children of.
- **types**: If given, only return items of these types.
- **omit_hidden**: If True, omit hidden items.


### is_hidden

```python
def is_hidden(item: autodoc2.utils.ItemData) -> bool
```

Whether this object should be displayed in documentation.

Based on configuration regarding:

- does i match a hidden regex pattern
- does it have documentation
- is it a dunder, i.e. __name__
- is it a private member, i.e. starts with _, but not a dunder
- is it an inherited member of a class


### is_module_deprecated

```python
def is_module_deprecated(item: autodoc2.utils.ItemData) -> bool
```

Whether this module is deprecated.


### no_index

```python
def no_index(item: autodoc2.utils.ItemData) -> bool
```

Whether this item should be excluded from search engines.


### show_module_summary

```python
def show_module_summary(item: autodoc2.utils.ItemData) -> bool
```

Whether to show a summary for this module/package.


### show_class_inheritance

```python
def show_class_inheritance(item: autodoc2.utils.ItemData) -> bool
```

Whether to show the inheritance for this class.


### show_annotations

```python
def show_annotations(item: autodoc2.utils.ItemData) -> bool
```

Whether to show type annotations.


### show_docstring

```python
def show_docstring(item: autodoc2.utils.ItemData) -> bool
```

Whether to show the docstring.


### render_item

```python
def render_item(full_name: str) -> typing.Iterable[str]
```

Yield the content for a single item.


### format_args

```python
def format_args(args_info: autodoc2.utils.ARGS_TYPE, include_annotations: bool = True, ignore_self: None | str = None) -> str
```

Format the arguments of a function or method.


### format_annotation

```python
def format_annotation(annotation: None | str) -> str
```

Format a single type annotation.


### format_base

```python
def format_base(base: None | str) -> str
```

Format a single class base type.


### get_doc_parser

```python
def get_doc_parser(full_name: str) -> str
```

Get the parser for the docstring of this item.

Returns `""` if it should be parsed using the current parser.


### generate_summary

```python
def generate_summary(objects: list[autodoc2.utils.ItemData], alias: dict[str, str] | None = None) -> typing.Iterable[str]
```

Generate a summary of the objects.

**Parameters:**

- **objects**: A list of fully qualified names.
- **alias**: A mapping of fully qualified names to a display alias.


`autodoc2.render.fern_`

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


`autodoc2.sphinx`

Module for Sphinx integration.

## Submodules

- **[docstring](#docstring)** - Directive for rendering docstrings.
- **[summary](#summary)** - Directive to generate a summary of listed objects.
- **[utils](#utils)** - Handle sphinx logging.
- **[extension](#extension)** - The sphinx extension for the package.
- **[autodoc](#autodoc)** - autodoc directive for sphinx.

## API

`autodoc2.sphinx.docstring`

Directive for rendering docstrings.

## Module Contents

### Classes

[`DocstringRenderer`](#docstringrenderer) | Directive to render a docstring of an object.

### Functions

[`parser_options`](#parser_options) | Return a docutils parser whose name matches the argument....
[`summary_option`](#summary_option) | Must be empty or a positive integer.
[`parsing_context`](#parsing_context) | Restore the parsing context after a nested parse with a different parser.
[`change_source`](#change_source) | Temporarily change the source and line number.
[`_example`](#_example) | This is an example docstring, written in MyST....

## API

## parser_options

```python
def parser_options(argument: str) -> docutils.parsers.Parser | None
```

Return a docutils parser whose name matches the argument.
(Directive option conversion function.)

Return `None`, if the argument evaluates to `False`.
Raise `ValueError` if importing the parser module fails.


## summary_option

```python
def summary_option(argument: str) -> int | None
```

Must be empty or a positive integer.


## DocstringRenderer

```python
class DocstringRenderer(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
```

**Bases**: `sphinx.util.docutils.SphinxDirective`

Directive to render a docstring of an object.

### has_content
**Value**: `False`



### required_arguments
**Value**: `1`



### optional_arguments
**Value**: `0`



### final_argument_whitespace
**Value**: `True`



### option_spec
**Type**: `typing.ClassVar[dict[str, typing.Any]]`



### run

```python
def run() -> list[docutils.nodes.Node]
```

Run the directive {a}`1`.


## parsing_context

```python
def parsing_context() -> typing.Generator[None, None, None]
```

Restore the parsing context after a nested parse with a different parser.


## change_source

```python
def change_source(state: docutils.parsers.rst.states.RSTStateMachine, source_path: str, line_offset: int) -> typing.Generator[None, None, None]
```

Temporarily change the source and line number.


## _example

```python
def _example(a: int, b: str) -> None
```

This is an example docstring, written in MyST.

It has a code fence:

```python
a = "hallo"
```

and a table:

| a | b | c |
| - | - | - |
| 1 | 2 | 3 |

and, using the `fieldlist` extension, a field list:

**Parameters:**

- **a**: the first parameter
- **b**: the second parameter

**Returns:**

the return value


`autodoc2.sphinx.summary`

Directive to generate a summary of listed objects.

## Module Contents

### Classes

[`AutodocSummary`](#autodocsummary) | Directive to generate a summary of listed objects.

## API

## AutodocSummary

```python
class AutodocSummary(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
```

**Bases**: `sphinx.util.docutils.SphinxDirective`

Directive to generate a summary of listed objects.

### has_content
**Value**: `True`



### required_arguments
**Value**: `0`



### optional_arguments
**Value**: `0`



### final_argument_whitespace
**Value**: `False`



### option_spec
**Type**: `typing.ClassVar[dict[str, typing.Any]]`



### run

```python
def run() -> list[docutils.nodes.Node]
```


`autodoc2.sphinx.utils`

Handle sphinx logging.

## Module Contents

### Functions

[`load_config`](#load_config) | Load the configuration.
[`warn_sphinx`](#warn_sphinx) | Log a warning in Sphinx.
[`get_database`](#get_database) | Get the database from the environment.
[`_warn`](#_warn)
[`get_all_analyser`](#get_all_analyser) | Get the all analyser from the environment.
[`nested_parse_generated`](#nested_parse_generated) | This function, nested parses generated content in a directive....

### Data

`LOGGER`

## API

### LOGGER
**Value**: `getLogger(...)`



## load_config

```python
def load_config(app: sphinx.application.Sphinx, *, overrides: None | dict[str, typing.Any] = None, location: None | docutils.nodes.Element = None) -> autodoc2.config.Config
```

Load the configuration.


## warn_sphinx

```python
def warn_sphinx(msg: str, subtype: autodoc2.utils.WarningSubtypes, location: None | docutils.nodes.Element = None) -> None
```

Log a warning in Sphinx.


## get_database

```python
def get_database(env: sphinx.environment.BuildEnvironment) -> autodoc2.db.Database
```

Get the database from the environment.


## _warn

```python
def _warn(msg: str) -> None
```


## get_all_analyser

```python
def get_all_analyser(env: sphinx.environment.BuildEnvironment) -> autodoc2.resolve_all.AllResolver
```

Get the all analyser from the environment.


## nested_parse_generated

```python
def nested_parse_generated(state: docutils.parsers.rst.states.RSTStateMachine, content: list[str], source: str, line: int, *, match_titles: bool = False, base: docutils.nodes.Element | None = None) -> docutils.nodes.Element
```

This function, nested parses generated content in a directive.

All reported warnings are redirected to a specific source document and line.

This is useful for directives that want to parse generated content.


`autodoc2.sphinx.extension`

The sphinx extension for the package.

## Module Contents

### Classes

[`EnvCache`](#envcache) | Cache for the environment.

### Functions

[`setup`](#setup) | Entry point for sphinx.
[`run_autodoc`](#run_autodoc) | The primary sphinx call back event for sphinx.
[`run_autodoc_package`](#run_autodoc_package) | Run autodoc for a single package....
[`get_git_clone`](#get_git_clone) | Download a git repository to the given folder.

## API

## setup

```python
def setup(app: sphinx.application.Sphinx) -> dict[str, str | bool]
```

Entry point for sphinx.


## run_autodoc

```python
def run_autodoc(app: sphinx.application.Sphinx) -> None
```

The primary sphinx call back event for sphinx.


## run_autodoc_package

```python
def run_autodoc_package(app: sphinx.application.Sphinx, config: autodoc2.config.Config, pkg_index: int) -> str | None
```

Run autodoc for a single package.

**Returns:**

The top level module name, relative to the api directory.


## get_git_clone

```python
def get_git_clone(app: sphinx.application.Sphinx, url: str, branch_tag: str, config: autodoc2.config.Config) -> None | pathlib.Path
```

Download a git repository to the given folder.


## EnvCache

```python
class EnvCache()
```

**Bases**: `typing.TypedDict`

Cache for the environment.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.


### hash
**Type**: `str`



### root_module
**Type**: `str`



`autodoc2.sphinx.autodoc`

autodoc directive for sphinx.

## Module Contents

### Classes

[`AutodocObject`](#autodocobject) | Directive to render a docstring of an object.

### Functions

[`_set_parents`](#_set_parents) | Ensure we setup the correct parent...

## API

## AutodocObject

```python
class AutodocObject(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
```

**Bases**: `sphinx.util.docutils.SphinxDirective`

Directive to render a docstring of an object.

### required_arguments
**Value**: `1`



### final_argument_whitespace
**Value**: `False`



### has_content
**Value**: `True`



### option_spec
**Type**: `typing.ClassVar[dict[str, typing.Any]]`



### run

```python
def run() -> list[docutils.nodes.Node]
```


## _set_parents

```python
def _set_parents(env: sphinx.environment.BuildEnvironment, mod: autodoc2.utils.ItemData, klass: autodoc2.utils.ItemData | None) -> typing.Generator[None, None, None]
```

Ensure we setup the correct parent
This allows sphinx to properly process the `py` directives.


`autodoc2.db`

A database interface for storing and querying the analysis items.

## Module Contents

### Classes

[`Database`](#database) | A simple interface for storing and querying the analysis items, from a single pa...
[`InMemoryDb`](#inmemorydb) | A simple in-memory database for storing and querying the analysis items.

### Data

`_LIKE_REGEX`

## API

## UniqueError

```python
class UniqueError()
```

**Bases**: `KeyError`

An error raised when a unique constraint is violated.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.


## Database

```python
class Database
```

**Bases**: `typing.Protocol`

A simple interface for storing and querying the analysis items, from a single package.

This allows for potential extensibility in the future,
e.g. using a persistent sqlite database.

### add

```python
def add(item: autodoc2.utils.ItemData) -> None
```

Add an item to the database.


### remove

```python
def remove(full_name: str, descendants: bool) -> None
```

Remove an item from the database, by full_name.

If `descendants` is True, remove all descendants of this item.


### __contains__

```python
def __contains__(full_name: str) -> bool
```

Check if an item is in the database, by full_name.


### get_item

```python
def get_item(full_name: str) -> autodoc2.utils.ItemData | None
```

Get an item from the database, by full_name.


### get_items_like

```python
def get_items_like(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
```

Get an item from the database, matching the wildcards `*` and `?`.

`*` matches any number of characters, and `?` matches any single character.


### get_type

```python
def get_type(full_name: str) -> None | str
```

Get the type of an item from the database, by full_name.


### get_by_type

```python
def get_by_type(type_: str) -> typing.Iterable[autodoc2.utils.ItemData]
```

Get all items from the database, by type.


### get_overloads

```python
def get_overloads(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
```

Get all function overloads for this name.


### get_children

```python
def get_children(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[autodoc2.utils.ItemData]
```

Get all items that are direct children of this name, i.e. `{full_name}.{name}`.

**Parameters:**

- **full_name**: The full name of the item.
- **types**: If given, only return items of these types.
- **sort_name**: If True, sort the names alphabetically.


### get_children_names

```python
def get_children_names(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[str]
```

Get all names of direct children of this name, i.e. `{full_name}.{name}`.

**Parameters:**

- **full_name**: The full name of the item.
- **types**: If given, only return items of these types.
- **sort_name**: If True, sort the names alphabetically.


### get_ancestors

```python
def get_ancestors(full_name: str, include_self: bool) -> typing.Iterable[autodoc2.utils.ItemData | None]
```

Get all ancestors of this name, e.g. `a.b`, `a` for `a.b.c`.

The order is guaranteed from closest to furthest ancestor.

**Parameters:**

- **full_name**: The full name of the item.
- **include_self**: If True, include the item itself.


### _LIKE_REGEX
**Value**: `compile(...)`



## InMemoryDb

```python
class InMemoryDb()
```

**Bases**: `autodoc2.db.Database`

A simple in-memory database for storing and querying the analysis items.

### Initialization

Create the database.


### add

```python
def add(item: autodoc2.utils.ItemData) -> None
```


### remove

```python
def remove(full_name: str, descendants: bool) -> None
```


### __contains__

```python
def __contains__(full_name: str) -> bool
```


### get_item

```python
def get_item(full_name: str) -> autodoc2.utils.ItemData | None
```


### get_items_like

```python
def get_items_like(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
```


### get_type

```python
def get_type(full_name: str) -> None | str
```


### get_by_type

```python
def get_by_type(type_: str) -> typing.Iterable[autodoc2.utils.ItemData]
```


### get_overloads

```python
def get_overloads(full_name: str) -> typing.Iterable[autodoc2.utils.ItemData]
```


### get_children

```python
def get_children(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[autodoc2.utils.ItemData]
```


### get_children_names

```python
def get_children_names(full_name: str, types: None | set[str] = None, *, sort_name: bool = False) -> typing.Iterable[str]
```


### get_ancestors

```python
def get_ancestors(full_name: str, include_self: bool) -> typing.Iterable[autodoc2.utils.ItemData | None]
```


### write

```python
def write(stream: typing.TextIO) -> None
```

Write the database to a file.


### read

```python
def read(stream: typing.TextIO) -> autodoc2.db.InMemoryDb
```

Read the database from a file.


`autodoc2.config`

The configuration for the extension.

## Module Contents

### Classes

[`PackageConfig`](#packageconfig) | A package-level config item.
[`Config`](#config) | The configuration for autoapi.

### Functions

[`_coerce_packages`](#_coerce_packages) | Coerce the packages config option to a set.
[`_validate_replace_list`](#_validate_replace_list) | Validate that an item is a list of tuples.
[`_validate_hidden_objects`](#_validate_hidden_objects) | Validate that the hidden objects config option is a set.
[`_validate_regex_list`](#_validate_regex_list) | Validate that an item is a list of regexes.
[`_validate_list_tuple_regex_str`](#_validate_list_tuple_regex_str) | Validate that an item is a list of (regex, str) tuples.
[`_load_renderer`](#_load_renderer) | Load a renderer class.
[`_load_regex_renderers`](#_load_regex_renderers) | Load a list of (regex, renderer).

### Data

`CONFIG_PREFIX`

## API

## ValidationError

```python
class ValidationError()
```

**Bases**: `Exception`

An error validating a config value.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.


### CONFIG_PREFIX
**Value**: `autodoc2_`



## PackageConfig

```python
class PackageConfig
```

A package-level config item.

### path
**Type**: `str`
**Value**: `field(...)`



### from_git_clone
**Type**: `tuple[str, str] | None`
**Value**: `field(...)`



### module
**Type**: `str | None`
**Value**: `field(...)`



### exclude_dirs
**Type**: `list[str]`
**Value**: `field(...)`



### exclude_files
**Type**: `list[str]`
**Value**: `field(...)`



### auto_mode
**Type**: `bool`
**Value**: `field(...)`



### as_triple

```python
def as_triple() -> typing.Iterable[tuple[str, typing.Any, dataclasses.Field]]
```

Yield triples of (name, value, field).


## _coerce_packages

```python
def _coerce_packages(name: str, item: typing.Any) -> list[autodoc2.config.PackageConfig]
```

Coerce the packages config option to a set.


## _validate_replace_list

```python
def _validate_replace_list(name: str, item: typing.Any) -> list[tuple[str, str]]
```

Validate that an item is a list of tuples.


## _validate_hidden_objects

```python
def _validate_hidden_objects(name: str, item: typing.Any) -> set[str]
```

Validate that the hidden objects config option is a set.


## _validate_regex_list

```python
def _validate_regex_list(name: str, item: typing.Any) -> list[typing.Pattern[str]]
```

Validate that an item is a list of regexes.


## _validate_list_tuple_regex_str

```python
def _validate_list_tuple_regex_str(name: str, item: typing.Any) -> list[tuple[typing.Pattern[str], str]]
```

Validate that an item is a list of (regex, str) tuples.


## _load_renderer

```python
def _load_renderer(name: str, item: typing.Any) -> type[autodoc2.render.base.RendererBase]
```

Load a renderer class.


## _load_regex_renderers

```python
def _load_regex_renderers(name: str, item: typing.Any) -> list[tuple[typing.Pattern[str], type[autodoc2.render.base.RendererBase]]]
```

Load a list of (regex, renderer).


## Config

```python
class Config
```

The configuration for autoapi.

### packages
**Type**: `list[autodoc2.config.PackageConfig]`
**Value**: `field(...)`



### output_dir
**Type**: `str`
**Value**: `field(...)`



### render_plugin
**Type**: `type[autodoc2.render.base.RendererBase]`
**Value**: `field(...)`



### render_plugin_regexes
**Type**: `list[tuple[typing.Pattern[str], type[autodoc2.render.base.RendererBase]]]`
**Value**: `field(...)`



### module_all_regexes
**Type**: `list[typing.Pattern[str]]`
**Value**: `field(...)`



### skip_module_regexes
**Type**: `list[typing.Pattern[str]]`
**Value**: `field(...)`



### hidden_objects
**Type**: `set[typing.Literal[undoc, dunder, private, inherited]]`
**Value**: `field(...)`



### hidden_regexes
**Type**: `list[typing.Pattern[str]]`
**Value**: `field(...)`



### no_index
**Type**: `bool`
**Value**: `field(...)`



### deprecated_module_regexes
**Type**: `list[typing.Pattern[str]]`
**Value**: `field(...)`



### module_summary
**Type**: `bool`
**Value**: `field(...)`



### docstring_parser_regexes
**Type**: `list[tuple[typing.Pattern[str], str]]`
**Value**: `field(...)`



### class_docstring
**Type**: `typing.Literal[merge, both]`
**Value**: `field(...)`



### class_inheritance
**Type**: `bool`
**Value**: `field(...)`



### annotations
**Type**: `bool`
**Value**: `field(...)`



### docstrings
**Type**: `typing.Literal[all, direct, none]`
**Value**: `field(...)`



### sort_names
**Type**: `bool`
**Value**: `field(...)`



### replace_annotations
**Type**: `list[tuple[str, str]]`
**Value**: `field(...)`



### replace_bases
**Type**: `list[tuple[str, str]]`
**Value**: `field(...)`



### index_template
**Type**: `str | None`
**Value**: `field(...)`



### as_triple

```python
def as_triple() -> typing.Iterable[tuple[str, typing.Any, dataclasses.Field]]
```

Yield triples of (name, value, field).


`autodoc2.analysis`

Analyse of Python code using astroid.

The core function though `analyse_module` is agnostic to the implementation,
It simply yields `ItemData` typed-dicts.

## Module Contents

### Classes

[`State`](#state)

### Functions

[`analyse_module`](#analyse_module) | Analyse the given module and yield items....
[`_get_full_name`](#_get_full_name) | Get the full name of a node.
[`_get_parent_name`](#_get_parent_name) | Get the parent name of a node.
[`fix_docstring_indent`](#fix_docstring_indent) | Remove common leading indentation,...
[`walk_node`](#walk_node)
[`yield_module`](#yield_module)
[`yield_annotation_assign`](#yield_annotation_assign) | Yield data for an annotation assignment node.
[`yield_assign`](#yield_assign) | Yield data for an assignment node.
[`_yield_assign`](#_yield_assign) | Yield data for an assignment node.
[`yield_function_def`](#yield_function_def) | Yield data for a function definition node.
[`yield_class_def`](#yield_class_def) | Yield data for a class definition node.

### Data

`__all__`
`_dc_kwargs`
`_FUNC_MAPPER`

## API

### __all__
**Value**: `['analyse_module']`



## analyse_module

```python
def analyse_module(file_path: pathlib.Path, name: str, exclude_external_imports: typing.Pattern[str] | None = None) -> typing.Iterable[autodoc2.utils.ItemData]
```

Analyse the given module and yield items.

    These are only used to determine what is exposed by __all__,
    which is only usually objects in the same package.
    But if you want to expose objects from other packages,
    you can use this to record them.

**Parameters:**

- **file_path**: The path to the module.
- **name**: The name of the module, e.g. "foo.bar".
- **record_external_imports**: If given, record these external imports on the module.


### _dc_kwargs
**Type**: `dict[str, bool]`



## State

```python
class State
```

### package_name
**Type**: `str`



### name_stack
**Type**: `list[str]`



### exclude_external_imports
**Type**: `typing.Pattern[str] | None`



### copy

```python
def copy(**kwargs: typing.Any) -> autodoc2.analysis.State
```

Copy the state and update the given attributes.


## _get_full_name

```python
def _get_full_name(name: str, name_stack: list[str]) -> str
```

Get the full name of a node.


## _get_parent_name

```python
def _get_parent_name(name: str) -> str
```

Get the parent name of a node.


## fix_docstring_indent

```python
def fix_docstring_indent(s: None | str, tabsize: int = 8) -> str
```

Remove common leading indentation,
where the indentation of the first line is ignored.


## walk_node

```python
def walk_node(node: astroid.nodes.NodeNG, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
```


## yield_module

```python
def yield_module(node: astroid.nodes.Module, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
```


## yield_annotation_assign

```python
def yield_annotation_assign(node: astroid.nodes.AnnAssign, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
```

Yield data for an annotation assignment node.


## yield_assign

```python
def yield_assign(node: astroid.nodes.Assign, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
```

Yield data for an assignment node.


## _yield_assign

```python
def _yield_assign(node: astroid.nodes.Assign | astroid.nodes.AnnAssign, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
```

Yield data for an assignment node.


## yield_function_def

```python
def yield_function_def(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
```

Yield data for a function definition node.


## yield_class_def

```python
def yield_class_def(node: astroid.nodes.ClassDef, state: autodoc2.analysis.State) -> typing.Iterable[autodoc2.utils.ItemData]
```

Yield data for a class definition node.


### _FUNC_MAPPER
**Type**: `dict[astroid.nodes.NodeNG, typing.Callable[[astroid.nodes.NodeNG, autodoc2.analysis.State], typing.Iterable[autodoc2.utils.ItemData]]]`



`autodoc2.cli`

CLI for the package.

## Module Contents

### Functions

[`version_callback`](#version_callback) | Print the version and exit.
[`main_app`](#main_app) | [underline]CLI for sphinx-autodoc2[/underline]
[`list_items`](#list_items) | Analyse a python module or package and stream the results to the console.
[`create_db`](#create_db) | Create a database for a python module or package.
[`analyse_all`](#analyse_all) | Analyse the __all__ of a module and find potential matches
[`write`](#write) | Create sphinx files for a python module or package.

### Data

`console`
`app_main`

## API

### console
**Value**: `Console(...)`



### app_main
**Value**: `Typer(...)`



## version_callback

```python
def version_callback(value: bool) -> None
```

Print the version and exit.


## main_app

```python
def main_app(version: typing.Optional[bool] = typer.Option(None, '-v', '--version', callback=version_callback, is_eager=True, help='Show the application version and exit.')) -> None
```

[underline]CLI for sphinx-autodoc2[/underline]


## list_items

```python
def list_items(path: pathlib.Path = typer.Argument(..., exists=True, help='Path to analyse'), module: typing.Optional[str] = typer.Option(None, '-m', '--module', help='The name of the module, otherwise it will be guessed from the path'), inherited: bool = typer.Option(False, '-i', '--inherited', help='Show inherited members'), private: bool = typer.Option(False, '-p', '--private', help='Show private members'), one_line: bool = typer.Option(False, '-o', '--one-line', help='Show only full name and type'), filter_types_str: typing.Optional[str] = typer.Option(None, '-ft', '--filter-types', help='Only show members of types (comma separated)'), skip_types_str: str = typer.Option('import_from', '-st', '--skip-types', help='Do not show members of types (comma separated)'), filter_name: typing.Optional[str] = typer.Option(None, '-fn', '--filter-name', help='Only show members with this name regex')) -> None
```

Analyse a python module or package and stream the results to the console.


## create_db

```python
def create_db(path: pathlib.Path = typer.Argument(..., exists=True, help='Path to analyse'), output: pathlib.Path = typer.Argument('autodoc.db.json', help='File to write to'), module: typing.Optional[str] = typer.Option(None, '-m', '--module', help='The name of the module, otherwise it will be guessed from the path')) -> None
```

Create a database for a python module or package.


## analyse_all

```python
def analyse_all(path: pathlib.Path = typer.Argument(..., exists=True, help='Path to a database file'), package: str = typer.Argument(..., help='The name of the package to resolve.')) -> None
```

Analyse the __all__ of a module and find potential matches


## write

```python
def write(path: pathlib.Path = typer.Argument(..., exists=True, help='Path to analyse'), module: typing.Optional[str] = typer.Option(None, '-m', '--module', help='The name of the module, otherwise it will be guessed from the path'), output: pathlib.Path = typer.Option('_autodoc', help='Folder to write to'), clean: bool = typer.Option(False, '-c', '--clean', help='Remove old files')) -> None
```

Create sphinx files for a python module or package.


`autodoc2.utils`

Utility functions and types.

## Module Contents

### Classes

[`ItemData`](#itemdata) | A data item, for the results of the analysis.
[`WarningSubtypes`](#warningsubtypes) | The subtypes of warnings for the extension.

### Functions

[`yield_modules`](#yield_modules) | Walk the given folder and yield all required modules....

### Data

`PROPERTY_TYPE`
`ARGS_TYPE`

## API

### PROPERTY_TYPE



### ARGS_TYPE



## ItemData

```python
class ItemData()
```

**Bases**: `typing.TypedDict`

A data item, for the results of the analysis.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.


### type
**Type**: `typing_extensions.Required[str]`



### full_name
**Type**: `typing_extensions.Required[str]`



### doc
**Type**: `typing_extensions.Required[str]`



### range
**Type**: `tuple[int, int]`



### file_path
**Type**: `None | str`



### encoding
**Type**: `str`



### all
**Type**: `None | list[str]`



### imports
**Type**: `list[tuple[str, str | None]]`



### value
**Type**: `None | str | typing.Any`



### annotation
**Type**: `None | str`



### properties
**Type**: `list[autodoc2.utils.PROPERTY_TYPE]`



### args
**Type**: `autodoc2.utils.ARGS_TYPE`



### return_annotation
**Type**: `None | str`



### bases
**Type**: `list[str]`



### doc_inherited
**Type**: `str`



### inherited
**Type**: `str`



## WarningSubtypes

```python
class WarningSubtypes
```

**Bases**: `enum.Enum`

The subtypes of warnings for the extension.

### CONFIG_ERROR
**Value**: `config_error`

Issue with configuration validation.

### GIT_CLONE_FAILED
**Value**: `git_clone`

Failed to clone a git repository.

### MISSING_MODULE
**Value**: `missing_module`

If the package file/folder does not exist.

### DUPLICATE_ITEM
**Value**: `dup_item`

Duplicate fully qualified name found during package analysis.

### RENDER_ERROR
**Value**: `render`

Generic rendering error.

### ALL_MISSING
**Value**: `all_missing`

__all__ attribute missing or empty in a module.

### ALL_RESOLUTION
**Value**: `all_resolve`

Issue with resolution of an item in a module's __all__ attribute.

### NAME_NOT_FOUND
**Value**: `missing`



## yield_modules

```python
def yield_modules(folder: str | pathlib.Path, *, root_module: str | None = None, extensions: typing.Sequence[str] = ('.py', '.pyi'), exclude_dirs: typing.Sequence[str] = ('__pycache__', ), exclude_files: typing.Sequence[str] = ()) -> typing.Iterable[tuple[pathlib.Path, str]]
```

Walk the given folder and yield all required modules.

    otherwise the folder name is used.
    If multiple files with the same stem,
    only the first extension will be used.

**Parameters:**

- **folder**: The path to walk.
- **root_module**: The name of the root module,
- **extensions**: The extensions to include.
- **exclude_dirs**: Directory names to exclude (matched with fnmatch).
- **exclude_files**: File names to exclude (matched with fnmatch).


`autodoc2.resolve_all`

Handling of ``__all__`` resolution.

## Module Contents

### Classes

[`AllResolveResult`](#allresolveresult) | dict() -> new empty dictionary...
[`AllResolver`](#allresolver)

## API

## AllResolutionError

```python
class AllResolutionError()
```

**Bases**: `Exception`

An error occurred while resolving the ``__all__``.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.


## ObjectMissingError

```python
class ObjectMissingError()
```

**Bases**: `autodoc2.resolve_all.AllResolutionError`

An object in the ``__all__`` is not available in the database.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.


## CircularImportError

```python
class CircularImportError()
```

**Bases**: `autodoc2.resolve_all.AllResolutionError`

A circular import was detected.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.


## NoAllError

```python
class NoAllError()
```

**Bases**: `autodoc2.resolve_all.AllResolutionError`

The module does not have an ``__all__``.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.


## AllResolveResult

```python
class AllResolveResult()
```

**Bases**: `typing.TypedDict`

### resolved
**Type**: `dict[str, str]`

Resolved is a dict of ``{full_name: {name}}``

### errors
**Type**: `list[tuple[str, str]]`

Errors are tuples of ``(full_name, error_message)``

## AllResolver

```python
class AllResolver(db: autodoc2.db.Database, warn_func: typing.Callable[[str], None] | None = None)
```

### Initialization

Initialise the resolver.

**Parameters:**

- **db**: the database to use
- **warn_func**: a function to call with warnings


### clear_cache

```python
def clear_cache() -> None
```

Clear the cache.


### get_resolved_all

```python
def get_resolved_all(full_name: str, _breadcrumbs: tuple[str, ...] = ()) -> autodoc2.resolve_all.AllResolveResult
```

Yield all names that would be imported by star.

**Parameters:**

- **full_name**: the fully qualified name of the module
- **_breadcrumbs**: used to detect circular imports


### get_name

```python
def get_name(name: str) -> str | None
```

Get the item, first by trying the fully qualified name,
then by looking at __all__ in parent modules.


`autodoc2.astroid_utils`

Utilities for working with astroid nodes.

## Module Contents

### Functions

[`resolve_import_alias`](#resolve_import_alias) | Resolve a name from an aliased import to its original name....
[`is_constructor`](#is_constructor) | Check if the function is a constructor.
[`get_full_import_name`](#get_full_import_name) | Get the full path of a name from a ``from x import y`` statement....
[`get_assign_value`](#get_assign_value) | Get the name and value of the assignment of the given node....
[`get_const_values`](#get_const_values) | Get the value of a constant node.
[`get_assign_annotation`](#get_assign_annotation) | Get the type annotation of the assignment of the given node....
[`resolve_annotation`](#resolve_annotation) | Resolve a type annotation to a string.
[`resolve_qualname`](#resolve_qualname) | Resolve where a node is defined to get its fully qualified name....
[`get_module_all`](#get_module_all) | Get the contents of the ``__all__`` variable from a module.
[`is_decorated_with_singledispatch`](#is_decorated_with_singledispatch) | Check if the function is decorated as a singledispatch.
[`is_singledispatch_decorator`](#is_singledispatch_decorator) | Check if the decorator is a singledispatch.
[`is_decorated_as_singledispatch_register`](#is_decorated_as_singledispatch_register) | Check if the function is decorated as a singledispatch register.
[`is_decorated_with_property`](#is_decorated_with_property) | Check if the function is decorated as a property.
[`is_property_decorator`](#is_property_decorator) | Check if the decorator is a property.
[`is_decorated_with_property_setter`](#is_decorated_with_property_setter) | Check if the function is decorated as a property setter....
[`get_class_docstring`](#get_class_docstring) | Get the docstring of a node, using a parent docstring if needed.
[`is_exception`](#is_exception) | Check if a class is an exception.
[`is_decorated_with_overload`](#is_decorated_with_overload) | Check if the function is decorated as an overload definition.
[`is_overload_decorator`](#is_overload_decorator)
[`get_func_docstring`](#get_func_docstring) | Get the docstring of a node, using a parent docstring if needed.
[`get_return_annotation`](#get_return_annotation) | Get the return annotation of a node.
[`get_args_info`](#get_args_info) | Get the arguments of a function....
[`_iter_args`](#_iter_args) | Iterate over arguments.
[`_merge_annotations`](#_merge_annotations)
[`_is_ellipsis`](#_is_ellipsis)

## API

## resolve_import_alias

```python
def resolve_import_alias(name: str, import_names: list[tuple[str, str | None]]) -> str
```

Resolve a name from an aliased import to its original name.

    from the import.

**Parameters:**

- **name**: The potentially aliased name to resolve.
- **import_names**: The pairs of original names and aliases

**Returns:**

The original name.


## is_constructor

```python
def is_constructor(node: astroid.nodes.NodeNG) -> bool
```

Check if the function is a constructor.


## get_full_import_name

```python
def get_full_import_name(import_from: astroid.nodes.ImportFrom, name: str) -> str
```

Get the full path of a name from a ``from x import y`` statement.

**Returns:**

The full import path of the name.


## get_assign_value

```python
def get_assign_value(node: astroid.nodes.NodeNG) -> None | tuple[str, typing.Any]
```

Get the name and value of the assignment of the given node.

Assignments to multiple names are ignored, as per PEP 257.


    and the value assigned to the name (if it can be converted).

**Parameters:**

- **node**: The node to get the assignment value from.

**Returns:**

The name that is assigned to,


## get_const_values

```python
def get_const_values(node: astroid.nodes.NodeNG) -> typing.Any
```

Get the value of a constant node.


## get_assign_annotation

```python
def get_assign_annotation(node: astroid.nodes.Assign) -> None | str
```

Get the type annotation of the assignment of the given node.

**Returns:**

The type annotation as a string, or None if one does not exist.


## resolve_annotation

```python
def resolve_annotation(annotation: astroid.nodes.NodeNG) -> str
```

Resolve a type annotation to a string.


## resolve_qualname

```python
def resolve_qualname(node: astroid.nodes.NodeNG, basename: str) -> str
```

Resolve where a node is defined to get its fully qualified name.

**Parameters:**

- **node**: The node representing the base name.
- **basename**: The partial base name to resolve.

**Returns:**

The fully resolved base name.


## get_module_all

```python
def get_module_all(node: astroid.nodes.Module) -> None | list[str]
```

Get the contents of the ``__all__`` variable from a module.


## is_decorated_with_singledispatch

```python
def is_decorated_with_singledispatch(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
```

Check if the function is decorated as a singledispatch.


## is_singledispatch_decorator

```python
def is_singledispatch_decorator(decorator: astroid.Name) -> bool
```

Check if the decorator is a singledispatch.


## is_decorated_as_singledispatch_register

```python
def is_decorated_as_singledispatch_register(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
```

Check if the function is decorated as a singledispatch register.


## is_decorated_with_property

```python
def is_decorated_with_property(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
```

Check if the function is decorated as a property.


## is_property_decorator

```python
def is_property_decorator(decorator: astroid.Name) -> bool
```

Check if the decorator is a property.


## is_decorated_with_property_setter

```python
def is_decorated_with_property_setter(node: astroid.nodes.FunctionDef | astroid.nodes.AsyncFunctionDef) -> bool
```

Check if the function is decorated as a property setter.

**Parameters:**

- **node**: The node to check.

**Returns:**

True if the function is a property setter, False otherwise.


## get_class_docstring

```python
def get_class_docstring(node: astroid.nodes.ClassDef) -> tuple[str, str | None]
```

Get the docstring of a node, using a parent docstring if needed.


## is_exception

```python
def is_exception(node: astroid.nodes.ClassDef) -> bool
```

Check if a class is an exception.


## is_decorated_with_overload

```python
def is_decorated_with_overload(node: astroid.nodes.FunctionDef) -> bool
```

Check if the function is decorated as an overload definition.


## is_overload_decorator

```python
def is_overload_decorator(decorator: astroid.Name | astroid.Attribute) -> bool
```


## get_func_docstring

```python
def get_func_docstring(node: astroid.nodes.FunctionDef) -> tuple[str, None | str]
```

Get the docstring of a node, using a parent docstring if needed.


## get_return_annotation

```python
def get_return_annotation(node: astroid.nodes.FunctionDef) -> None | str
```

Get the return annotation of a node.


## get_args_info

```python
def get_args_info(args_node: astroid.Arguments) -> list[tuple[None | str, None | str, None | str, None | str]]
```

Get the arguments of a function.

**Returns:**

a list of (type, name, annotation, default)


## _iter_args

```python
def _iter_args(args: list[astroid.nodes.NodeNG], annotations: list[astroid.nodes.NodeNG], defaults: list[astroid.nodes.NodeNG]) -> typing.Iterable[tuple[str, None | str, str | None]]
```

Iterate over arguments.


## _merge_annotations

```python
def _merge_annotations(annotations: typing.Iterable[typing.Any], comment_annotations: typing.Iterable[typing.Any]) -> typing.Iterable[typing.Any]
```


## _is_ellipsis

```python
def _is_ellipsis(node: typing.Any) -> bool
```


### __version__
**Value**: `0.5.0`



## setup

```python
def setup(app)
```

Entrypoint for sphinx.

