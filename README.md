# sphinx-autodoc2-fern

Generate Fern-compatible API documentation from Python packages using static analysis.

Fork of [`sphinx-autodoc2`](https://github.com/sphinx-extensions2/sphinx-autodoc2) with [Fern](https://buildwithfern.com) output support.

## Installation

```bash
pip install sphinx-autodoc2-fern
```

## Usage

Generate Fern-compatible markdown documentation:

```bash
autodoc2 --renderer fern /path/to/your/package
```

This creates:
- Markdown files with Fern-compatible frontmatter and slugs
- `navigation.yml` for Fern docs structure
- Tables with proper linking and descriptions

## Acknowledgments

This project is a fork of the excellent [`sphinx-autodoc2`](https://github.com/sphinx-extensions2/sphinx-autodoc2) by Chris Sewell. All credit for the core functionality goes to the original project.

## Design and comparison to sphinx-autoapi

The original sphinx-autodoc2 was created with the following goals:

- Static analysis of Python code, so things like `if TYPE_CHECKING` were handled correctly
- Support for MyST docstrings (see <https://github.com/executablebooks/MyST-Parser/issues/228>)
  - Also support for transitioning from `rst` to `md`, i.e. mixing docstrings
- Make it simple and minimise the amount of configuration and rebuilds necessary
- Support for building public API via `__all__` variable

I am not looking to support other languages tha Python (at least for now).

[sphinx-autoapi](https://github.com/readthedocs/sphinx-autoapi) was a good candidate, but it had a few issues:

- It does not support MyST docstrings: <https://github.com/readthedocs/sphinx-autoapi/issues/287>
- It does not support the `__all__` very well: <https://github.com/readthedocs/sphinx-autoapi/issues/358>
- The analysis and rendering are coupled, making it difficult to test, modify and use outside of Sphinx

I've use a lot of their code, for the `astroid` static analysis, but I've made a number of "improvements":

- separating concerns: analysis and template writing
- type annotations for code base
- fixed `a | b` annotations inference
- added analysis of `functools.singledispatch` and their registers
- handling of `__all__`
- docstrings (and summaries) are now parsed with the correct source/line, i.e. warnings point to the correct location in the source file
- added `:canonical:` to `py` directives
- Moved away from using jinja templates, to using python functions
  - IMO the templates were too complex and hard to read,
    plus they do not benefit from any form of type checking, linting, etc.
  - uses `list-table`, instead of `auto-summary` directive

## Development

All configuration is mainly in `pyproject.toml`.

Use [tox](https://tox.readthedocs.io/en/latest/) to run the tests.

```bash
pipx install tox
tox -av
```

Use [pre-commit](https://pre-commit.com/) to run the linters and formatters.

```bash
pipx install pre-commit
pre-commit run --all-files
# pre-commit install
```

[flit](https://flit.readthedocs.io/en/latest/) is used to build the package.

```bash
pipx install flit
flit build
```
