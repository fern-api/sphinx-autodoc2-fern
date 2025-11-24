"""Renderer for Fern."""

from __future__ import annotations

import re
import typing as t

from autodoc2.render.base import RendererBase
from autodoc2.render.fern_docstring import DocstringProcessor
from autodoc2.render.fern_links import LinkGenerator
from autodoc2.render.fern_navigation import NavigationGenerator

if t.TYPE_CHECKING:
    from autodoc2.utils import ItemData


# Configuration constants
MULTILINE_PARAM_THRESHOLD = 2  # Number of parameters to trigger multiline formatting
MAX_SUMMARY_LENGTH = 80  # Maximum length for summary descriptions
MAX_TABLE_DESC_LENGTH = 50  # Maximum length for table descriptions
LINE_LENGTH_THRESHOLD = 80  # Maximum line length before wrapping


class FernRenderer(RendererBase):
    """Render the documentation as Fern-compatible MDX"""

    EXTENSION = ".mdx"

    def __init__(self, *args, **kwargs):
        """Initialize renderer with helper classes."""
        super().__init__(*args, **kwargs)

        # Initialize helper classes
        self._docstring_processor = DocstringProcessor(
            format_annotation_fn=self.format_annotation,
            escape_fn=self._escape_fern_content
        )
        self._link_generator = LinkGenerator(
            get_item_fn=self.get_item,
            extension=self.EXTENSION
        )
        self._nav_generator = NavigationGenerator(
            get_by_type_fn=self._db.get_by_type,
            get_children_fn=self.get_children,
            generate_file_path_fn=self._link_generator.generate_file_path,
            extension=self.EXTENSION
        )

    def render_item(self, full_name: str) -> t.Iterable[str]:
        """Render a single item by dispatching to the appropriate method."""
        item = self.get_item(full_name)
        if item is None:
            raise ValueError(f"Item {full_name} does not exist")

        type_ = item["type"]

        # Add frontmatter for API reference pages (packages and modules)
        if type_ in ("package", "module"):
            yield "---"
            yield "layout: overview"
            slug = self._link_generator.generate_slug(full_name)
            yield f"slug: {slug}"
            yield "---"
            yield ""

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
        full_name = item["full_name"]
        show_annotations = self.show_annotations(item)

        # Add anchor for linking
        anchor_id = self._link_generator.generate_anchor_id(full_name)
        yield f'<Anchor id="{anchor_id}">'
        yield ""

        # Function signature in code block (no header - code block IS the header)
        return_annotation = (
            f" -> {self.format_annotation(item['return_annotation'])}"
            if show_annotations and item.get("return_annotation")
            else ""
        )

        # Use multiline format only if there are multiple actual parameters (excluding self)
        args_list = item.get("args", [])
        # Filter out 'self' and 'cls' to determine if there are real parameters
        real_params = [arg for arg in args_list if arg[1] not in ("self", "cls")]
        use_multiline = len(real_params) >= MULTILINE_PARAM_THRESHOLD

        if not use_multiline:
            # No/few real parameters - use inline format
            args_formatted = self.format_args(args_list, show_annotations)
            code_content = f"{full_name}({args_formatted}){return_annotation}"
        else:
            # Multiple real parameters - use multiline format
            args_formatted = self._format_args_multiline(args_list, show_annotations)
            code_lines = [f"{full_name}("]
            if args_formatted.strip():
                for line in args_formatted.split("\n"):
                    if line.strip():
                        code_lines.append(f"    {line.strip()}")
            code_lines.append(f"){return_annotation}")
            code_content = "\n".join(code_lines)

        # Use enhanced code block formatting with potential links
        # Pass the page name (parent module/package) to enable context-aware linking
        current_page = self._link_generator.get_page_for_item(full_name)
        formatted_code = self._link_generator.format_code_block_with_links(code_content, "python", current_page, current_item=full_name)
        for line in formatted_code.split("\n"):
            yield line

        yield "</Anchor>"
        yield ""

        # Wrap all function content (docstring, params, returns) in Indent
        if self.show_docstring(item):
            raw_docstring = item.get("doc", "").strip()
            if raw_docstring:
                yield "<Indent>"
                yield ""
                # Pass the actual return annotation from the function signature
                return_annotation = self.format_annotation(item["return_annotation"]) if show_annotations and item.get("return_annotation") else None
                processed_docstring = self._process_docstring(
                    raw_docstring,
                    args_info=item.get("args", []),
                    return_annotation=return_annotation,
                    current_item=full_name
                )
                yield processed_docstring
                yield ""
                yield "</Indent>"
                yield ""

    def render_module(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a module."""
        # For now, delegate to package rendering
        yield from self.render_package(item)

    def render_package(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a package."""
        full_name = item["full_name"]

        # Package header as proper title
        yield f"# {full_name}"
        yield ""

        if self.show_docstring(item):
            yield item["doc"]
            yield ""

        # Get all children organized by type
        children_by_type = {
            "package": list(self.get_children(item, {"package"})),
            "module": list(self.get_children(item, {"module"})),
            "class": list(self.get_children(item, {"class"})),
            "function": list(self.get_children(item, {"function"})),
            "data": list(self.get_children(item, {"data"})),
        }

        has_subpackages = bool(children_by_type["package"])
        has_submodules = bool(children_by_type["module"])
        has_content = any(children_by_type[t] for t in ["class", "function", "data"])

        # Show hierarchical structure if we have subpackages/modules
        if has_subpackages:
            yield from self._render_child_list(children_by_type["package"], "Subpackages")

        if has_submodules:
            yield from self._render_child_list(children_by_type["module"], "Submodules")

        # Show Module Contents summary if we have actual content (not just submodules)
        if has_content:
            yield "## Module Contents"
            yield ""

            # Classes section - proper table format with full descriptions
            if children_by_type["class"]:
                yield "### Classes"
                yield ""
                yield "| Name | Description |"
                yield "|------|-------------|"
                for child in children_by_type["class"]:
                    full_name = child["full_name"]
                    short_name = full_name.split(".")[-1]
                    # Use context-aware linking (same-page anchor vs cross-page)
                    name_link = self._link_generator.get_cross_reference_link(
                        full_name, short_name, item["full_name"]
                    )
                    # Get full description (first paragraph)
                    description = self._extract_first_paragraph(child)
                    # Escape the description for Fern compatibility
                    escaped_description = self._escape_fern_content(description)
                    yield f"| {name_link} | {escaped_description} |"
                yield ""

            # Functions section - proper table format with full descriptions
            if children_by_type["function"]:
                yield "### Functions"
                yield ""
                yield "| Name | Description |"
                yield "|------|-------------|"
                for child in children_by_type["function"]:
                    full_name = child["full_name"]
                    short_name = full_name.split(".")[-1]
                    # Use context-aware linking (same-page anchor vs cross-page)
                    name_link = self._link_generator.get_cross_reference_link(
                        full_name, short_name, item["full_name"]
                    )
                    # Get full description (first paragraph)
                    description = self._extract_first_paragraph(child)
                    # Escape the description for Fern compatibility
                    escaped_description = self._escape_fern_content(description)
                    yield f"| {name_link} | {escaped_description} |"
                yield ""

            # Data section
            if children_by_type["data"]:
                yield "### Data"
                yield ""
                for child in children_by_type["data"]:
                    full_name = child["full_name"]
                    short_name = full_name.split(".")[-1]
                    # Create anchor link to API section
                    anchor_id = self._link_generator.generate_anchor_id(full_name)
                    yield f"[`{short_name}`](#{anchor_id})"
                yield ""

        # API section with detailed documentation
        # Only render detailed content for items directly defined in this package/module
        # (NOT subpackages/submodules - they get their own separate files)
        visible_children = [
            child["full_name"]
            for child in self.get_children(item)
            if child["type"] not in ("package", "module")
        ]

        if visible_children:
            yield "### API"
            yield ""

            for name in visible_children:
                yield from self.render_item(name)

    def render_class(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a class."""
        short_name = item["full_name"].split(".")[-1]
        full_name = item["full_name"]

        # Add anchor for linking
        anchor_id = self._link_generator.generate_anchor_id(full_name)
        yield f'<Anchor id="{anchor_id}">'
        yield ""

        # Build class signature with constructor args
        constructor = self.get_item(f"{full_name}.__init__")
        if constructor and "args" in constructor:
            args_list = constructor["args"]
            show_annotations = self.show_annotations(item)

            # Filter out 'self' to determine if there are real parameters
            real_params = [arg for arg in args_list if arg[1] not in ("self", "cls")]
            use_multiline = len(real_params) >= MULTILINE_PARAM_THRESHOLD
            
            if len(real_params) == 0:
                # No real parameters - no parentheses
                code_content = f"class {full_name}"
            elif not use_multiline:
                # One real parameter - use inline format
                args_formatted = self.format_args(args_list, show_annotations)
                code_content = f"class {full_name}({args_formatted})"
            else:
                # Multiple real parameters - use multiline format
                args_formatted = self._format_args_multiline(args_list, show_annotations, ignore_self="self")
                code_lines = [f"class {full_name}("]
                if args_formatted.strip():
                    for line in args_formatted.split("\n"):
                        if line.strip():
                            code_lines.append(f"    {line.strip()}")
                code_lines.append(")")
                code_content = "\n".join(code_lines)
        else:
            code_content = f"class {full_name}"

        # Use enhanced code block formatting with potential links
        # Pass the page name (parent module/package) to enable context-aware linking
        current_page = self._link_generator.get_page_for_item(full_name)
        formatted_code = self._link_generator.format_code_block_with_links(code_content, "python", current_page, current_item=full_name)
        for line in formatted_code.split("\n"):
            yield line

        yield "</Anchor>"
        yield ""

        # Collect all class content first
        content_lines = []

        # Show inheritance if configured and available
        if item.get("bases") and self.show_class_inheritance(item):
            base_list = ", ".join(
                f"`{self.format_base(base)}`" for base in item.get("bases", [])
            )
            content_lines.append(f"**Bases**: {base_list}")
            content_lines.append("")

        if self.show_docstring(item):
            raw_docstring = item.get("doc", "").strip()
            if raw_docstring:
                # Convert Args to ParamFields using constructor args (if available)
                constructor_args = constructor.get("args", []) if constructor else []
                processed_docstring = self._process_docstring(
                    raw_docstring,
                    args_info=constructor_args,
                    return_annotation=None,  # Class docstrings don't have return types
                    current_item=full_name
                )
                content_lines.append(processed_docstring)
                content_lines.append("")

            # Add "Initialization" section if we're merging __init__ docstring
            if self.config.class_docstring == "merge":
                init_item = self.get_item(f"{full_name}.__init__")
                if init_item and init_item.get("doc", "").strip():
                    content_lines.append("**Initialization:**")
                    content_lines.append("")
                    init_docstring = init_item.get("doc", "").strip()
                    processed_init = self._process_docstring(
                        init_docstring,
                        args_info=init_item.get("args", []),
                        return_annotation=None,  # __init__ doesn't have a return type
                        current_item=f"{full_name}.__init__"
                    )
                    content_lines.append(processed_init)
                    content_lines.append("")

        # Get class members
        children = list(self.get_children(
            item, {"class", "property", "attribute", "method"}
        ))
        
        # Filter out __init__ if we merged its docstring above
        children = [
            child for child in children
            if not (
                child["full_name"].endswith(".__init__")
                and self.config.class_docstring == "merge"
            )
        ]
        
        # Wrap ALL class content (own content + members) in ONE Indent block
        has_any_content = (content_lines and any(line.strip() for line in content_lines)) or children
        
        if has_any_content:
            yield "<Indent>"
            yield ""
            
            # First, render the class's own content (bases, docstring, initialization)
            if content_lines and any(line.strip() for line in content_lines):
                for line in content_lines:
                    if line.strip():
                        # Convert NOTE: and WARNING: to Fern components
                        formatted_line = self._format_fern_callouts(line)
                        yield formatted_line
                    else:
                        yield ""
            
            # Then, render class members
            if children:
                for child in children:
                    # Render each member with short names in code blocks
                    child_item = self.get_item(child["full_name"])
                    child_lines = list(self.render_item(child["full_name"]))

                    for line in child_lines:
                        # Convert full names in code blocks to short names for nested members
                        if child["full_name"] in line and "```" not in line:
                            short_name = child["full_name"].split(".")[-1]
                            # Replace the full name with short name in the line
                            updated_line = line.replace(child["full_name"], short_name)
                            yield updated_line
                        else:
                            yield line
            
            yield "</Indent>"
            yield ""

    def render_exception(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for an exception."""
        yield from self.render_class(item)

    def render_property(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a property."""
        short_name = item["full_name"].split(".")[-1]

        # Property signature in code block (no header - code block IS the header)
        full_name = item["full_name"]
        yield "```python"
        if item.get("return_annotation"):
            yield f"{full_name}: {self.format_annotation(item['return_annotation'])}"
        else:
            yield f"{full_name}"
        yield "```"
        yield ""

        # Property content - collect it first
        content_lines = []

        # Show decorators if any
        properties = item.get("properties", [])
        if properties:
            decorator_list = []
            for prop in (
                "abstractmethod",
                "async",
                "classmethod",
                "final",
                "staticmethod",
            ):
                if prop in properties:
                    decorator_list.append(f"`@{prop}`")
            if decorator_list:
                content_lines.append(f"**Decorators**: {', '.join(decorator_list)}")
                content_lines.append("")

        # Property docstring
        if self.show_docstring(item):
            raw_docstring = item.get("doc", "").strip()
            if raw_docstring:
                processed_docstring = self._process_docstring(raw_docstring, current_item=full_name)
                content_lines.append(processed_docstring)

        # Wrap property content in Indent
        if content_lines and any(line.strip() for line in content_lines):
            yield "<Indent>"
            yield ""
            for line in content_lines:
                if line.strip():
                    # Convert NOTE: and WARNING: to Fern components
                    formatted_line = self._format_fern_callouts(line)
                    yield formatted_line
                else:
                    yield ""
            yield "</Indent>"
            yield ""
        else:
            yield ""

    def render_method(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a method."""
        yield from self.render_function(item)  # Same as function for now

    def render_attribute(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for an attribute."""
        yield from self.render_data(item)

    def render_data(self, item: ItemData) -> t.Iterable[str]:
        """Create the content for a data item."""
        full_name = item["full_name"]
        short_name = full_name.split(".")[-1]

        # Add anchor for linking
        anchor_id = self._link_generator.generate_anchor_id(full_name)
        yield f'<Anchor id="{anchor_id}">'
        yield ""

        # Check if this is a class attribute vs module-level data
        # Class attributes should be shown as code blocks, not ParamFields
        parts = full_name.split(".")
        is_class_attribute = False
        if len(parts) >= 2:
            # Check if parent is a class
            parent_name = ".".join(parts[:-1])
            parent_item = self.get_item(parent_name)
            if parent_item and parent_item["type"] == "class":
                is_class_attribute = True

        has_annotation = bool(item.get("annotation"))
        value = item.get("value")

        # Class attributes: show as simple code block with type annotation
        if is_class_attribute and has_annotation:
            type_str = self.format_annotation(item["annotation"])

            # Build simple code block: name: Type or name: Type = value
            if value is not None:
                code_line = f"{short_name}: {type_str} = {value}"
            else:
                code_line = f"{short_name}: {type_str}"

            current_page = self._link_generator.get_page_for_item(full_name)
            formatted_code = self._link_generator.format_code_block_with_links(code_line, "python", current_page, current_item=full_name)
            for line in formatted_code.split("\n"):
                yield line

            yield "</Anchor>"
            yield ""
        # Module-level data/constants: use ParamField format
        elif has_annotation:
            type_str = self.format_annotation(item["annotation"])

            # Build ParamField
            # Don't wrap type in backticks - Fern handles formatting
            param_field = f'<ParamField path="{short_name}" type="{type_str}"'

            # Add default value if present
            if value is not None:
                value_str = str(value)
                # If value contains double quotes, use single quote wrapper
                # Otherwise use double quote wrapper and escape any single quotes
                if '"' in value_str:
                    param_field += f" default='{value_str}'"
                else:
                    # Escape single quotes for HTML/JSX parsing
                    escaped_value = value_str.replace("'", "&#39;")
                    param_field += f' default="{escaped_value}"'

            param_field += '>'
            yield param_field

            # Add docstring as ParamField content
            if self.show_docstring(item):
                raw_docstring = item.get("doc", "").strip()
                if raw_docstring:
                    # Don't escape ParamField content - it's already inside a component
                    # So we process but don't use _escape_fern_content
                    processed_docstring = self._docstring_processor.convert_myst_directives(raw_docstring)
                    processed_docstring = self._docstring_processor.bold_docstring_sections(processed_docstring)
                    processed_docstring = self._docstring_processor.convert_note_sections_to_components(processed_docstring)
                    processed_docstring = self._docstring_processor.format_examples_section(processed_docstring)
                    yield f"  {processed_docstring}"

            yield "</ParamField>"
            yield ""
            yield "</Anchor>"
            yield ""
        else:
            # Data without type annotation (e.g., enum members, old-style constants)
            # Show as simple inline code block: NAME = value
            if value is not None:
                code_line = f"{short_name} = {value}"
            else:
                # No value - just show the name
                code_line = short_name

            current_page = self._link_generator.get_page_for_item(full_name)
            formatted_code = self._link_generator.format_code_block_with_links(code_line, "python", current_page, current_item=full_name)
            for line in formatted_code.split("\n"):
                yield line

            yield "</Anchor>"
            yield ""

    def _process_docstring(
        self,
        raw_docstring: str,
        args_info: list | None = None,
        return_annotation: str | None = None,
        current_item: str | None = None,
    ) -> str:
        """Process docstring through the complete transformation pipeline.

        Args:
            raw_docstring: The raw docstring text to process
            args_info: Optional list of (prefix, name, annotation, default) tuples for parameters
            return_annotation: Optional return type annotation string
            current_item: Optional name of the item being processed (for logging)

        Returns:
            Fully processed and escaped docstring ready for MDX output
        """
        return self._docstring_processor.process_docstring(
            raw_docstring, args_info, return_annotation, current_item
        )

    def _extract_first_paragraph(self, item: ItemData) -> str:
        """Extract the first paragraph from an item's docstring.

        Args:
            item: The item to extract description from

        Returns:
            The first paragraph of the docstring, or "None" if empty
        """
        doc_lines = item.get("doc", "").strip().split("\n")
        if not doc_lines or not doc_lines[0]:
            return "None"

        # Get first paragraph (until empty line or end)
        doc_summary = []
        for line in doc_lines:
            if not line.strip():
                break
            doc_summary.append(line.strip())

        return " ".join(doc_summary) if doc_summary else "None"

    def _render_child_list(self, children: list[ItemData], section_title: str) -> t.Iterable[str]:
        """Render a list of child items (subpackages or submodules) with summaries.

        Args:
            children: List of child items to render
            section_title: The section header (e.g., "Subpackages", "Submodules")

        Yields:
            Formatted markdown lines for the child list
        """
        yield f"## {section_title}"
        yield ""
        for child in children:
            name = child["full_name"].split(".")[-1]
            # Use slug for Fern routing (not file paths)
            slug = self._link_generator.generate_slug(child["full_name"])
            doc_summary = (
                child.get("doc", "").split("\n")[0][:MAX_SUMMARY_LENGTH] if child.get("doc") else ""
            )
            if len(child.get("doc", "")) > MAX_SUMMARY_LENGTH:
                doc_summary += "..."
            yield (
                f"- **[`{name}`]({slug})** - {doc_summary}"
                if doc_summary
                else f"- **[`{name}`]({slug})**"
            )
        yield ""

    def generate_summary(
        self, objects: list[ItemData], alias: dict[str, str] | None = None
    ) -> t.Iterable[str]:
        """Generate a summary table with cross-reference links."""
        alias = alias or {}

        yield "| Name | Description |"
        yield "|------|-------------|"

        for item in objects:
            full_name = item["full_name"]
            display_name = alias.get(full_name, full_name.split(".")[-1])

            # Create cross-reference link to the item
            link = self._link_generator.get_cross_reference_link(full_name, display_name)

            # Get first line of docstring for description
            doc = item.get("doc", "").strip()
            description = doc.split("\n")[0] if doc else ""
            if len(description) > MAX_TABLE_DESC_LENGTH:
                description = description[:MAX_TABLE_DESC_LENGTH - 3] + "..."

            yield f"| {link} | {description} |"

    def _format_args_multiline(
        self,
        args_info: list,
        include_annotations: bool = True,
        ignore_self: str | None = None,
    ) -> str:
        """Format function arguments with newlines for better readability."""
        if not args_info:
            return ""

        formatted_args = []

        for i, (prefix, name, annotation, default) in enumerate(args_info):
            if i == 0 and ignore_self is not None and name == ignore_self:
                continue

            annotation = self.format_annotation(annotation) if annotation else ""

            # Build the argument string
            arg_str = (prefix or "") + (name or "")
            if annotation and include_annotations:
                arg_str += f": {annotation}"
            if default:
                arg_str += f" = {default}"

            formatted_args.append(arg_str)

        # If we have many arguments or long arguments, use multiline format
        args_str = ", ".join(formatted_args)
        if len(args_str) > LINE_LENGTH_THRESHOLD or len(formatted_args) >= MULTILINE_PARAM_THRESHOLD:
            # Multi-line format: each arg on its own line
            return ",\n".join(formatted_args)
        else:
            # Single line format
            return args_str

    def _create_anchor(self, text: str) -> str:
        """Create a markdown anchor from header text, following standard markdown rules."""
        # Convert to lowercase
        anchor = text.lower()
        # Replace spaces with hyphens
        anchor = re.sub(r"\s+", "-", anchor)
        # Remove non-alphanumeric characters except hyphens and underscores
        anchor = re.sub(r"[^a-z0-9\-_]", "", anchor)
        # Remove duplicate hyphens
        anchor = re.sub(r"-+", "-", anchor)
        # Remove leading/trailing hyphens
        anchor = anchor.strip("-")
        return anchor

    def _contains_jinja_template(self, text: str) -> bool:
        """Check if text contains Jinja template syntax."""
        jinja_pattern = r"({%.*?%}|{{.*?}})"
        return re.search(jinja_pattern, text) is not None

    def _format_fern_callouts(self, line: str) -> str:
        """Convert NOTE: and WARNING: to Fern components."""
        # Convert NOTE: to Fern Note component
        note_pattern = r"^(\s*)(NOTE:\s*)(.*)"
        if match := re.match(note_pattern, line, re.IGNORECASE):
            indent, prefix, content = match.groups()
            return f"{indent}<Note> {content.strip()} </Note>"

        # Convert WARNING: to Fern Warning component
        warning_pattern = r"^(\s*)(WARNING:\s*)(.*)"
        if match := re.match(warning_pattern, line, re.IGNORECASE):
            indent, prefix, content = match.groups()
            return f"{indent}<Warning> {content.strip()} </Warning>"

        return line

    def _escape_fern_content(self, content: str) -> str:
        """Escape content for Fern/MDX compatibility - preserves code blocks and Fern components."""
        # Don't escape if it's already a Jinja template
        if self._contains_jinja_template(content):
            return content

        # Split content by:
        # 1. Code blocks (triple/single backticks)
        # 2. Fern/MDX components (ParamField, CodeBlock, Anchor, Note, Warning, etc.)
        # Preserve them all without escaping
        pattern = r"(```[\s\S]*?```|`[^`]*?`|<ParamField[\s\S]*?</ParamField>|<CodeBlock[\s\S]*?</CodeBlock>|<Anchor[\s\S]*?</Anchor>|<Note[\s\S]*?</Note>|<Warning[\s\S]*?</Warning>)"
        parts = re.split(pattern, content)

        escaped_parts = []
        for i, part in enumerate(parts):
            if i % 2 == 0:  # Regular text (not inside preserved blocks)
                # Escape HTML-like tags: <tag> -> \<tag\>
                part = part.replace("<", "\\<").replace(">", "\\>")
                # Escape curly braces: {text} -> \{text\}
                part = part.replace("{", "\\{").replace("}", "\\}")
                escaped_parts.append(part)
            else:  # Inside code blocks or Fern components - don't escape anything
                escaped_parts.append(part)

        return "".join(escaped_parts)

    def validate_all_links(self, output_dir: str = None) -> dict[str, list[str]]:
        """Validate all generated links in the output files.

        Checks:
        1. All anchor IDs are unique within each file
        2. Cross-reference links point to files that exist
        3. Cross-reference links point to anchor IDs that exist in target files

        Args:
            output_dir: Path to the output directory containing generated files

        Returns:
            Dict with 'errors' and 'warnings' keys containing lists of issues.
        """
        issues = {"errors": [], "warnings": []}

        if not output_dir:
            issues["warnings"].append("No output directory provided, skipping validation")
            return issues

        from pathlib import Path
        import re

        output_path = Path(output_dir)
        if not output_path.exists():
            issues["errors"].append(f"Output directory does not exist: {output_dir}")
            return issues

        # Step 1: Collect all anchor IDs and markdown links from all files
        file_anchors = {}  # file_path -> set of anchor IDs
        file_links = {}    # file_path -> list of (link_url, line_number) tuples

        for mdx_file in output_path.rglob("*.mdx"):
            try:
                content = mdx_file.read_text("utf8")
                lines = content.split("\n")

                # Extract anchor IDs from <Anchor id="..."> tags
                anchor_ids = set()
                anchor_pattern = r'<Anchor\s+id="([^"]+)"'
                for match in re.finditer(anchor_pattern, content):
                    anchor_id = match.group(1)
                    if anchor_id in anchor_ids:
                        rel_path = mdx_file.relative_to(output_path)
                        issues["errors"].append(
                            f"Duplicate anchor ID '{anchor_id}' in {rel_path}"
                        )
                    anchor_ids.add(anchor_id)

                file_anchors[mdx_file] = anchor_ids

                # Extract markdown links [text](url)
                links = []
                link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
                for line_num, line in enumerate(lines, 1):
                    for match in re.finditer(link_pattern, line):
                        link_url = match.group(2)
                        # Only check internal links (not external URLs)
                        if not link_url.startswith(("http://", "https://", "mailto:")):
                            links.append((link_url, line_num))

                file_links[mdx_file] = links

            except Exception as e:
                rel_path = mdx_file.relative_to(output_path)
                issues["errors"].append(f"Error reading {rel_path}: {e}")

        # Step 2: Validate cross-reference links
        for source_file, links in file_links.items():
            for link_url, line_num in links:
                # Skip anchor-only links (same page)
                if link_url.startswith("#"):
                    anchor_id = link_url[1:]
                    # Check if anchor exists in this file
                    if anchor_id not in file_anchors.get(source_file, set()):
                        rel_path = source_file.relative_to(output_path)
                        issues["errors"].append(
                            f"{rel_path}:{line_num} - Anchor '#{anchor_id}' not found in file"
                        )
                    continue

                # Skip Fern slug-based links (links without / or . that Fern routes via frontmatter slugs)
                # Examples: "clickhouse-connect-tools", "nemo-rl-metrics"
                # These are handled by Fern's routing system using the slug in frontmatter
                if "/" not in link_url and "." not in link_url and not link_url.startswith("#"):
                    # This is a slug-based link, skip validation (Fern handles it)
                    continue

                # Cross-page links with file paths: path/to/file.mdx#anchor
                if "#" in link_url:
                    file_part, anchor_part = link_url.split("#", 1)
                else:
                    file_part = link_url
                    anchor_part = None

                # Resolve the target file path
                # Links can be relative or absolute from output root
                if file_part.startswith("/"):
                    # Absolute path from output root
                    target_file = output_path / file_part.lstrip("/")
                else:
                    # Relative path from source file's directory
                    target_file = (source_file.parent / file_part).resolve()

                # Add .mdx extension if not present
                if not target_file.suffix:
                    target_file = target_file.with_suffix(".mdx")

                # Check if target file exists
                if not target_file.exists():
                    rel_source = source_file.relative_to(output_path)
                    issues["errors"].append(
                        f"{rel_source}:{line_num} - Link target does not exist: {file_part}"
                    )
                    continue

                # Check if anchor exists in target file (if anchor specified)
                if anchor_part:
                    target_anchors = file_anchors.get(target_file, set())
                    if anchor_part not in target_anchors:
                        rel_source = source_file.relative_to(output_path)
                        rel_target = target_file.relative_to(output_path)
                        issues["errors"].append(
                            f"{rel_source}:{line_num} - Anchor '#{anchor_part}' not found in {rel_target}"
                        )

        return issues

    def generate_navigation_yaml(self) -> str:
        """Generate navigation YAML for Fern docs.yml following sphinx autodoc2 toctree logic.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        """
        return self._nav_generator.generate_navigation_yaml()
