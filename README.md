# sphinx-autodoc-fern

`sphinx-autodoc-fern` is a Sphinx extension that automatically generates API documentation for your Python packages with **Fern documentation format support**.

This is a fork of [`sphinx-autodoc2`](https://github.com/sphinx-extensions2/sphinx-autodoc2) that adds powerful [Fern](https://buildwithfern.com) documentation generation capabilities.

## 🆕 New Fern Features

- **Fern-compatible Markdown output** - Generate documentation that works seamlessly with Fern
- **Enhanced parameter formatting** - Uses Fern's ParamField components for better API documentation
- **Smart callout handling** - Automatically converts NOTE: and WARNING: to Fern components
- **Beautiful tables** - Improved formatting for classes, functions, and module contents

Static analysis of Python code

: There is no need to install your package to generate the documentation, and `sphinx-autodoc2` will correctly handle `if TYPE_CHECKING` blocks and other typing only features.
: You can even document packages from outside the project (via `git clone`)!

Optimized for rebuilds

: Analysis of packages and file rendering are cached, so you can use `sphinx-autodoc2` in your development workflow.

Support for `__all__`

: `sphinx-autodoc2` can follow `__all__` variable, to only document the public API.

Support for both `rst` and `md` docstrings

: `sphinx-autodoc2` supports both `rst` and `md` ([MyST](https://myst-parser.readthedocs.io)) docstrings, which can be mixed within the same project.

Highly configurable

: `sphinx-autodoc-fern` is highly configurable, with many options to control the analysis and output of the documentation.

Fern Documentation Format Support

: Generate beautiful Fern-compatible documentation with enhanced formatting for parameters, callouts, and API references.

Decoupled analysis and rendering

: The analysis and rendering of the documentation are decoupled, and not dependent on Sphinx.
: This means that you can use `sphinx-autodoc-fern` to generate documentation outside of Sphinx (see the `autodoc2` command line tool).

## 🚀 Quick Start with Fern

```bash
pip install sphinx-autodoc-fern
```

To use the Fern renderer:

```python
from autodoc2.render.fern_ import FernRenderer

renderer = FernRenderer()
# Generate Fern-compatible documentation
```

Or use with the CLI:

```bash
autodoc2 --renderer fern your_package/
```

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
