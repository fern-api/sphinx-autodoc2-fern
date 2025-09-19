"""Analyse a python project and create documentation for it.

This is a fork of sphinx-autodoc2 with added support for Fern documentation format.
"""

__version__ = "0.1.0"


def setup(app):  # type: ignore
    """Entrypoint for sphinx."""
    from .sphinx.extension import setup as _setup

    return _setup(app)
