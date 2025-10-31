# py2fern

Generate [Fern](https://buildwithfern.com) API documentation from Python packages using static analysis.

Simplified fork of [`sphinx-autodoc2`](https://github.com/sphinx-extensions2/sphinx-autodoc2) focused purely on **Python → Fern markdown** output.

## Installation

```bash
pipx install py2fern
```

## Usage

Generate Fern markdown documentation:

```bash
py2fern /path/to/your/package
```

This creates:

- Markdown files with Fern-compatible frontmatter and slugs
- `navigation.yml` for Fern docs structure
- Tables with proper linking and descriptions

## Acknowledgments

This project is a fork of the excellent [`sphinx-autodoc2`](https://github.com/sphinx-extensions2/sphinx-autodoc2) by Chris Sewell. All credit for the core functionality goes to the original project.

## Features

- **Static analysis** - No need to install your package
- **Handles `TYPE_CHECKING` blocks** - Documents typing-only imports  
- **Follows `__all__`** - Only documents public API
- **Fern-ready output** - Frontmatter, slugs, ParamField components
- **Navigation generation** - Automatic `navigation.yml` for Fern docs

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
