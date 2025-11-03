"""Tests for the rendering."""

from pathlib import Path
from textwrap import dedent

from autodoc2.analysis import analyse_module
from autodoc2.config import Config
from autodoc2.db import InMemoryDb
from autodoc2.render.fern_ import FernRenderer
from autodoc2.utils import yield_modules
import pytest


def test_basic(tmp_path: Path, file_regression):
    """Test basic rendering."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)
    content = "\n".join(FernRenderer(db, Config()).render_item(package.name))
    file_regression.check(content, extension=".md")


def test_config_options(tmp_path: Path, file_regression):
    """Test basic rendering."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)
    config = Config(no_index=True)
    content = "\n".join(FernRenderer(db, config).render_item(package.name + ".func"))
    file_regression.check(content, extension=".md")




def build_package(tmp_path: Path) -> Path:
    """Build a simple package for testing."""
    package = tmp_path / "package"
    package.mkdir()
    package.joinpath("__init__.py").write_text(
        dedent(
            """\
        '''This is a test package.'''
        from package.a import a1
        from package.a.c import ac1 as alias
        __all__ = ['p', 'a1', 'alias']
        p = 1
        '''p can be documented here.'''

        def func(a: str, b: int) -> alias:
            '''This is a function.'''

        class Class:
            '''This is a class.'''

            x: int = 1
            '''x can be documented here.'''

            def method(self, a: str, b: int) -> ...:
                '''This is a method.'''

            @property
            def prop(self) -> alias | None:
                '''This is a property.'''

            class Nested:
                '''This is a nested class.'''
        """
        ),
        "utf-8",
    )
    package.joinpath("a").mkdir()
    package.joinpath("a", "__init__.py").write_text(
        dedent(
            """\
        '''This is a test module.'''
        from .c import *
        from .d import *
        __all__ = ['a1', 'ac1', 'ad1', 'ade1', 'adf1']
        a1 = 1
        '''a1 can be documented here.'''
        """
        ),
        "utf-8",
    )
    package.joinpath("a", "c.py").write_text(
        dedent(
            """\
        '''This is also a test module.'''
        __all__ = ['ac1']
        ac1 = 1
        """
        ),
        "utf-8",
    )
    return package
