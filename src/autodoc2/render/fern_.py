"""Renderer for Fern."""

from __future__ import annotations

import re
import typing as t

from autodoc2.render.base import RendererBase

if t.TYPE_CHECKING:
    from autodoc2.utils import ItemData


_RE_DELIMS = re.compile(r"(\s*[\[\]\(\),]\s*)")


class FernRenderer(RendererBase):
    """Render the documentation as Fern-compatible Markdown."""

    EXTENSION = ".md"

    def render_item(self, full_name: str) -> t.Iterable[str]:
        """Render a single item by dispatching to the appropriate method."""
        item = self.get_item(full_name)
        if item is None:
            raise ValueError(f"Item {full_name} does not exist")
        
        type_ = item["type"]
        if type_ == "package":
            yield from self.render_package(item)
        elif type_ == "module":
            yield from self.render_module(item)
        elif type_ == "function":
            yield from self.render_function(item)
        elif type_ == "class":
            yield from self.render_class(item)
        elif type_ == "exception":
            yield from self.render_exception(item)
        elif type_ == "property":
            yield from self.render_property(item)
        elif type_ == "method":
            yield from self.render_method(item)
        elif type_ == "attribute":
            yield from self.render_attribute(item)
        elif type_ == "data":
            yield from self.render_data(item)
        else:
            self.warn(f"Unknown item type {type_!r} for {full_name!r}")

    def render_function(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a function."""
        short_name = item["full_name"].split(".")[-1]
        show_annotations = self.show_annotations(item)
        
        # Build signature
        sig = f"{short_name}({self.format_args(item['args'], show_annotations)})"
        if show_annotations and item.get("return_annotation"):
            sig += f" -> {self.format_annotation(item['return_annotation'])}"

        # Fern-style output (starting simple)
        yield f"## {sig}"
        yield ""
        
        if self.show_docstring(item):
            yield item['doc']  # Direct docstring - no directives!
        yield ""

    def render_module(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a module."""
        # For now, delegate to package rendering
        yield from self.render_package(item)

    def render_package(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a package."""
        full_name = item["full_name"]
        yield f"# {full_name}"
        yield ""
        
        if self.show_docstring(item):
            yield item['doc']
            yield ""

        # Get visible children
        visible_children = [
            i["full_name"]
            for i in self.get_children(item)
            if i["type"] not in ("package", "module")
        ]

        for name in visible_children:
            yield from self.render_item(name)

    # Placeholder methods - we'll implement these later
    def render_class(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a class."""
        yield f"## {item['full_name'].split('.')[-1]} (class)"
        yield "TODO: Implement class rendering"
        yield ""

    def render_exception(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for an exception."""
        yield from self.render_class(item)

    def render_property(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a property."""
        yield f"### {item['full_name'].split('.')[-1]} (property)"
        yield "TODO: Implement property rendering"
        yield ""

    def render_method(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a method."""
        yield from self.render_function(item)  # Same as function for now

    def render_attribute(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for an attribute."""
        yield from self.render_data(item)

    def render_data(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a data item."""
        short_name = item["full_name"].split(".")[-1]
        yield f"### {short_name}"
        
        if item.get("annotation"):
            yield f"**Type**: `{self.format_annotation(item['annotation'])}`"
        
        value = item.get("value")
        if value is not None:
            yield f"**Value**: `{value}`"
        
        if self.show_docstring(item):
            yield ""
            yield item['doc']
        yield ""

    def generate_summary(
        self, objects: list[ItemData], alias: dict[str, str] | None = None
    ) -> t.Iterable[str]:
        """Generate a summary of the objects."""
        alias = alias or {}
        
        yield "| Name | Description |"
        yield "|------|-------------|"
        
        for item in objects:
            full_name = item["full_name"]
            display_name = alias.get(full_name, full_name.split(".")[-1])
            
            # Get first line of docstring for description
            doc = item.get('doc', '').strip()
            description = doc.split('\n')[0] if doc else ""
            if len(description) > 50:
                description = description[:47] + "..."
            
            yield f"| `{display_name}` | {description} |"