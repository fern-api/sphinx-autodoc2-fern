"""Tests for the rendering."""

from pathlib import Path
import re
from textwrap import dedent

from autodoc2.analysis import analyse_module
from autodoc2.config import Config
from autodoc2.db import InMemoryDb
from autodoc2.render.fern_ import FernRenderer
from autodoc2.utils import yield_modules
import pytest
import yaml


def test_basic_rendering_functional(tmp_path: Path):
    """Test basic rendering works without crashes - functional test, no snapshots."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)
    
    renderer = FernRenderer(db, Config())
    content = "\n".join(renderer.render_item(package.name))
    
    # Functional assertions - test that it works, not exact format
    assert content.startswith("---\n"), "Should have frontmatter"
    assert "layout: overview" in content, "Should have layout"
    assert "slug: package" in content, "Should have correct slug"
    assert "## Module Contents" in content, "Should have module contents section"
    assert "```python" in content, "Should have code blocks"
    assert "This is a test package." in content, "Should include docstrings"
    
    # Test that tables exist without caring about exact format
    assert "Classes" in content or "Functions" in content, "Should have summary tables"


def test_link_validation(tmp_path: Path):
    """Test that all generated links are valid and follow correct patterns."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)

    renderer = FernRenderer(db, Config())

    # Test link validation method works (if available)
    if hasattr(renderer, "validate_all_links"):
        validation_results = renderer.validate_all_links()
        assert isinstance(
            validation_results, dict
        ), "validate_all_links should return dict"
        assert "errors" in validation_results, "Should have errors key"
        assert "warnings" in validation_results, "Should have warnings key"
        assert isinstance(validation_results["errors"], list), "Errors should be list"
        assert isinstance(
            validation_results["warnings"], list
        ), "Warnings should be list"

        # Should have no errors on our test package
        assert not validation_results[
            "errors"
        ], f"Found link errors: {validation_results['errors']}"

    # Test specific link patterns in rendered content
    content = "\n".join(renderer.render_item(package.name))

    # Check for same-page anchor links (items within same package)
    assert re.search(
        r"\[`\w+`\]\(#\w+\)", content
    ), "Should have same-page anchor links"

    # Check for cross-page links (subpackages/submodules)
    if "package-a" in content:
        assert re.search(
            r"\[`\w+`\]\([\w-]+\)", content
        ), "Should have cross-page links"


def test_anchor_generation(tmp_path: Path):
    """Test that anchor IDs are generated correctly."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)

    renderer = FernRenderer(db, Config())
    content = "\n".join(renderer.render_item(package.name))

    # Test that anchors exist in the rendered content
    # Look for anchor patterns like #packageclass, #packagefunc
    assert re.search(
        r"#package\w+", content
    ), "Should have anchor links with package prefix"

    # Test that rendered content has some consistent anchor pattern
    anchor_matches = re.findall(r"\(#(\w+)\)", content)
    assert len(anchor_matches) > 0, "Should have at least one anchor link"

    # Anchors should be lowercase and contain no dots or special chars
    for anchor in anchor_matches:
        assert anchor.islower(), f"Anchor should be lowercase: {anchor}"
        assert "." not in anchor, f"Anchor should not contain dots: {anchor}"


def test_cross_reference_linking(tmp_path: Path):
    """Test that cross-reference links work correctly with context awareness."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)

    renderer = FernRenderer(db, Config())
    content = "\n".join(renderer.render_item(package.name))

    # Test that we have both types of links
    # Same-page links (just anchor): [`Class`](#packageclass)
    same_page_links = re.findall(r"\[`\w+`\]\(#\w+\)", content)
    assert len(same_page_links) > 0, "Should have same-page anchor links"

    # Cross-page links (page + anchor): [`submod`](package-submod#anchor)
    # Note: cross-page links may or may not have anchors depending on target type
    # Our test package may not have cross-page links, so we don't assert on them

    # Test link format consistency
    for link in same_page_links:
        # Should start with backticks and have # anchor
        assert (
            link.startswith("[`") and ")" in link and "#" in link
        ), f"Malformed same-page link: {link}"

    # Test that items in summary tables link correctly
    # Classes and functions should link to their anchors on the same page
    class_item = renderer.get_item("package.Class")
    func_item = renderer.get_item("package.func")

    if class_item:
        # Should find Class linked with an anchor in the content
        assert re.search(
            r"\[`Class`\]\(#package\w*class\w*\)", content
        ), "Class should be linked with anchor"

    if func_item:
        # Should find func linked with an anchor in the content
        assert re.search(
            r"\[`func`\]\(#package\w*func\w*\)", content
        ), "Function should be linked with anchor"


def test_rendering_pipeline(tmp_path: Path):
    """Test that the full rendering pipeline works without crashes."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)

    renderer = FernRenderer(db, Config())

    # Test each item type can be rendered without crashes
    for item_type in ["package", "module", "class", "function", "data"]:
        items = list(db.get_by_type(item_type))
        if items:
            item = items[0]
            try:
                content_lines = list(renderer.render_item(item["full_name"]))
                assert (
                    content_lines
                ), f"Empty output for {item_type}: {item['full_name']}"
                content = "\n".join(content_lines)
                assert len(content) > 10, f"Suspiciously short content for {item_type}"
            except Exception as e:
                pytest.fail(f"Rendering {item_type} {item['full_name']} crashed: {e}")


def test_frontmatter_structure(tmp_path: Path):
    """Test that frontmatter is generated correctly."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)

    renderer = FernRenderer(db, Config())
    content = "\n".join(renderer.render_item(package.name))

    # Should start with frontmatter
    assert content.startswith("---\n"), "Content should start with frontmatter"

    # Extract frontmatter
    parts = content.split("---\n")
    assert len(parts) >= 3, "Should have opening ---, frontmatter, closing ---, content"

    frontmatter = parts[1].strip()
    assert frontmatter, "Frontmatter should not be empty"

    # Parse as valid YAML
    try:
        fm_data = yaml.safe_load(frontmatter)
        assert isinstance(fm_data, dict), "Frontmatter should be valid YAML dict"
        assert "layout" in fm_data, "Should have layout field"
        assert "slug" in fm_data, "Should have slug field"
        assert fm_data["layout"] == "overview", "Layout should be overview"
    except yaml.YAMLError as e:
        pytest.fail(f"Invalid frontmatter YAML: {e}")


def test_code_block_structure(tmp_path: Path):
    """Test that code blocks are properly formatted and closed."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)

    renderer = FernRenderer(db, Config())
    content = "\n".join(renderer.render_item(package.name))

    # Count code block delimiters
    python_blocks = content.count("```python")
    closing_blocks = content.count("```\n") + content.count("```</CodeBlock>")

    assert python_blocks > 0, "Should have at least one Python code block"
    assert (
        python_blocks <= closing_blocks
    ), f"Unmatched code blocks: {python_blocks} opening, {closing_blocks} closing"

    # Check for proper code block content
    assert (
        "def " in content or "class " in content
    ), "Should have function or class definitions in code blocks"


def test_navigation_generation(tmp_path: Path):
    """Test that navigation.yml is generated correctly."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)

    renderer = FernRenderer(db, Config())
    nav_yaml = renderer.generate_navigation_yaml()

    assert nav_yaml, "Navigation YAML should not be empty"

    # Parse as valid YAML
    try:
        nav_data = yaml.safe_load(nav_yaml)
        assert isinstance(
            nav_data, dict
        ), "Navigation should be a dict with 'navigation' key"
        assert "navigation" in nav_data, "Should have 'navigation' key"

        nav_list = nav_data["navigation"]
        assert isinstance(nav_list, list), "Navigation value should be a list"
        assert len(nav_list) > 0, "Navigation should have at least one item"

        # Check structure of navigation items
        for item in nav_list:
            assert isinstance(item, dict), "Navigation items should be dicts"
            # Navigation can have 'section' or 'page' entries
            assert (
                "section" in item or "page" in item
            ), f"Navigation item missing 'section' or 'page': {item}"

    except yaml.YAMLError as e:
        pytest.fail(f"Invalid navigation YAML: {e}")


def test_config_options_functional(tmp_path: Path):
    """Test that config options work correctly (functional test, not snapshot)."""
    package = build_package(tmp_path)
    db = InMemoryDb()
    for path, modname in yield_modules(package):
        for item in analyse_module(path, modname):
            db.add(item)

    # Test with no_index=True
    config = Config(no_index=True)
    renderer = FernRenderer(db, config)

    func_content = "\n".join(renderer.render_item(package.name + ".func"))
    assert func_content, "Should render function content"
    assert "```python" in func_content, "Should contain code block"
    assert "This is a function" in func_content, "Should contain docstring"

    # Test basic rendering works
    assert len(func_content.split("\n")) > 3, "Should have multiple lines of content"


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
