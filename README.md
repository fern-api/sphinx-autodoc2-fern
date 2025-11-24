# py2fern

Generate [Fern](https://buildwithfern.com) API documentation from Python packages using static analysis.

Simplified fork of [`sphinx-autodoc2`](https://github.com/sphinx-extensions2/sphinx-autodoc2) focused purely on **Python → Fern markdown** output.

## Installation

```bash
pipx install py2fern
```

## Upgrading

To upgrade to the latest version:

```bash
pipx upgrade py2fern
```

Or if installed with pip:

```bash
pip install --upgrade py2fern
```

Check your current version:

```bash
py2fern --version
```

## Usage

Generate Fern markdown documentation:

```bash
py2fern write /path/to/your/package
```

Specify output directory:

```bash
py2fern write /path/to/your/package --output ./docs/api
```

### Debug Mode

Show warnings for functions missing return type annotations:

```bash
py2fern write /path/to/your/package --output ./docs/api --debug
```

Warnings appear in yellow and help identify functions that should have type annotations added.

### Legacy Parser Mode

Use the old regex-based parser instead of the default `docstring_parser`:

```bash
USE_REGEX_PARSER=1 py2fern write /path/to/your/package --output ./docs/api
```

### Output

This creates:
- **MDX files** with Fern-compatible frontmatter and slugs
- **`navigation.yml`** for Fern docs structure
- **Consistent ParamFields** for all Parameters and Returns sections

## Acknowledgments

This project is a fork of the excellent [`sphinx-autodoc2`](https://github.com/sphinx-extensions2/sphinx-autodoc2) by Chris Sewell. All credit for the core functionality goes to the original project.

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
