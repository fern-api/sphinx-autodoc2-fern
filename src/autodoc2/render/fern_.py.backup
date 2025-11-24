"""Renderer for Fern."""

from __future__ import annotations

import re
import typing as t

from autodoc2.render.base import RendererBase

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
            slug = self._generate_slug(full_name)
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
        anchor_id = self._generate_anchor_id(full_name)
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
        current_page = self._get_page_for_item(full_name)
        formatted_code = self._format_code_block_with_links(code_content, "python", current_page, current_item=full_name)
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
                    return_annotation=return_annotation
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
                    name_link = self._get_cross_reference_link(
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
                    name_link = self._get_cross_reference_link(
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
                    anchor_id = self._generate_anchor_id(full_name)
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
        anchor_id = self._generate_anchor_id(full_name)
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
        current_page = self._get_page_for_item(full_name)
        formatted_code = self._format_code_block_with_links(code_content, "python", current_page, current_item=full_name)
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
                    return_annotation=None  # Class docstrings don't have return types
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
                        return_annotation=None  # __init__ doesn't have a return type
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
                processed_docstring = self._process_docstring(raw_docstring)
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
        anchor_id = self._generate_anchor_id(full_name)
        yield f'<Anchor id="{anchor_id}">'
        yield ""

        # Check if this is a simple attribute (has annotation, might have value)
        has_annotation = bool(item.get("annotation"))
        value = item.get("value")
        
        # Use ParamField for attributes with type annotations
        if has_annotation:
            type_str = self.format_annotation(item["annotation"])
            
            # Build ParamField
            # Wrap type in backticks for inline code formatting
            param_field = f'<ParamField path="{short_name}" type="`{type_str}`"'
            
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
                    processed_docstring = self._convert_myst_directives(raw_docstring)
                    processed_docstring = self._bold_docstring_sections(processed_docstring)
                    processed_docstring = self._convert_note_sections_to_components(processed_docstring)
                    processed_docstring = self._format_examples_section(processed_docstring)
                    yield f"  {processed_docstring}"
            
            yield "</ParamField>"
            yield ""
            yield "</Anchor>"
            yield ""
        else:
            code_content = f"{full_name}"
            current_page = self._get_page_for_item(full_name)
            formatted_code = self._format_code_block_with_links(code_content, "python", current_page, current_item=full_name)
            for line in formatted_code.split("\n"):
                yield line
            
            yield "</Anchor>"
            yield ""
            
            # Always wrap data content in Indent (we always show value, even if None)
            yield "<Indent>"
            yield ""
            
            # Always show value (even if None) for consistency
            value_str = str(value) if value is not None else "None"
            if self._contains_jinja_template(value_str):
                if len(value_str.splitlines()) > 1 or len(value_str) > 100:
                    yield "**Value**: `<Multiline-String>`"
                else:
                    yield "**Value**:"
                    yield "```jinja2"
                    yield value_str
                    yield "```"
            else:
                escaped_value = self._escape_fern_content(value_str)
                yield f"**Value**: `{escaped_value}`"
            yield ""
            
            # Show docstring
            if self.show_docstring(item):
                raw_docstring = item.get("doc", "").strip()
                if raw_docstring:
                    processed_docstring = self._process_docstring(raw_docstring)
                    yield processed_docstring
                    yield ""
            
            yield "</Indent>"
            yield ""

    def _process_docstring(
        self,
        raw_docstring: str,
        args_info: list | None = None,
        return_annotation: str | None = None,
    ) -> str:
        """Process docstring through the complete transformation pipeline.

        Args:
            raw_docstring: The raw docstring text to process
            args_info: Optional list of (prefix, name, annotation, default) tuples for parameters
            return_annotation: Optional return type annotation string

        Returns:
            Fully processed and escaped docstring ready for MDX output
        """
        if not raw_docstring.strip():
            return ""

        docstring = self._convert_myst_directives(raw_docstring)
        docstring = self._bold_docstring_sections(docstring)
        docstring = self._convert_note_sections_to_components(docstring)

        if args_info:
            docstring = self._convert_args_to_paramfields(docstring, args_info)

        if return_annotation is not None:
            docstring = self._convert_returns_to_paramfield(docstring, return_annotation)

        docstring = self._format_examples_section(docstring)
        return self._escape_fern_content(docstring)

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
            slug = self._generate_slug(child["full_name"])
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
            link = self._get_cross_reference_link(full_name, display_name)

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

    def _convert_myst_directives(self, content: str) -> str:
        """Convert MyST directives to Fern format."""
        # Simple approach: Just replace {doctest} with python, don't mess with closing backticks
        content = content.replace("```{doctest}", "```python")

        # Also fix malformed python blocks that are missing closing backticks
        # Look for ```python at start of line that doesn't have a matching closing ```
        lines = content.split("\n")
        in_code_block = False
        result_lines = []

        for line in lines:
            if line.strip().startswith("```python"):
                in_code_block = True
                result_lines.append(line)
            elif line.strip() == "```" and in_code_block:
                in_code_block = False
                result_lines.append(line)
            else:
                result_lines.append(line)

        # If we ended still in a code block, add closing backticks
        if in_code_block:
            result_lines.append("```")

        content = "\n".join(result_lines)

        # Handle other common MyST directives
        directive_replacements = {
            r"\{note\}": "<Note>",
            r"\{warning\}": "<Warning>",
            r"\{tip\}": "<Tip>",
            r"\{important\}": "<Important>",
        }

        for pattern, replacement in directive_replacements.items():
            content = re.sub(pattern, replacement, content)

        return content

    def _bold_docstring_sections(self, content: str) -> str:
        """Bold common docstring section headers like Args:, Returns:, Raises:"""
        # Bold section headers that appear at the start of a line (with optional whitespace)
        # Match: Args:, Returns:, Raises:, Parameters:, Yields:, Note:, Examples:, etc.
        sections_to_bold = [
            "Args:",
            "Arguments:",
            "Parameters:",
            "Returns:",
            "Return:",
            "Yields:",
            "Yield:",
            "Raises:",
            "Raise:",
            "Throws:",
            "Throw:",
            "Note:",
            "Notes:",
            "Example:",
            "Examples:",
            "See Also:",
            "Attributes:",
            "Attribute:",
        ]
        
        for section in sections_to_bold:
            # Match section header at start of line (with optional whitespace before)
            # Ensure there's a blank line after the header
            pattern = rf'^(\s*)({re.escape(section)})[ \t]*$'
            replacement = r'\1**\2**\n'
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        
        return content

    def _dedent_lines(self, lines: list[str], base_indent: int | None = None) -> str:
        """Remove common indentation from lines while preserving structure.
        
        Args:
            lines: List of lines to dedent
            base_indent: Base indentation level to remove (if None, calculates minimum)
        
        Returns:
            Dedented text with preserved relative indentation
        """
        if not lines:
            return ""
        
        # If base_indent not provided, find minimum indentation
        if base_indent is None:
            min_indent = None
            for line in lines:
                if line.strip():  # Only consider non-empty lines
                    indent = len(line) - len(line.lstrip())
                    min_indent = indent if min_indent is None else min(min_indent, indent)
            base_indent = min_indent if min_indent is not None else 0
        
        # Remove base indentation from all lines
        dedented = []
        for line in lines:
            if line.strip():  # Non-empty line
                # Remove base_indent characters, but preserve additional indentation
                if len(line) >= base_indent and line[:base_indent].strip() == '':
                    dedented.append(line[base_indent:])
                else:
                    dedented.append(line.lstrip())
            else:
                # Preserve empty lines
                dedented.append('')
        
        return '\n'.join(dedented).strip()
    
    def _convert_args_to_paramfields(self, docstring: str, args_info: list) -> str:
        """Convert Args/Parameters section in docstring to Fern ParamField components.

        Args:
            docstring: The docstring content
            args_info: List of (prefix, name, annotation, default) tuples from function signature
        """
        # Build a map of parameter info from the signature
        param_info = {}
        for prefix, name, annotation, default in args_info:
            if name and name not in ("self", "cls"):
                param_info[name] = {
                    "type": self.format_annotation(annotation) if annotation else None,
                    "default": default
                }
        
        # Pattern to match Args/Parameters/Arguments section
        # Captures all indented content (including blank lines) until we hit a non-indented line or another section
        args_pattern = r'^(\*\*(?:Args|Arguments|Parameters):\*\*)\s*$\n((?:(?:[ \t]+.*|[ \t]*)\n)*(?:[ \t]+.*)?)'
        
        def replace_args_section(match):
            section_header = match.group(1)
            section_content = match.group(2)
            
            if not section_content.strip():
                return match.group(0)
            
            # Parse parameter descriptions from docstring
            param_descriptions = {}
            current_param = None
            current_desc_lines = []
            base_indent = None
            
            for line in section_content.split('\n'):
                # Match lines like "    param_name: description" or "    param_name (type): description"
                param_match = re.match(r'^([ \t]+)([a-zA-Z_][a-zA-Z0-9_]*)\s*(?:\([^)]+\))?\s*:\s*(.*)$', line)
                if param_match:
                    # Save previous parameter
                    if current_param:
                        # Remove common indentation from description lines
                        dedented_desc = self._dedent_lines(current_desc_lines, base_indent)
                        param_descriptions[current_param] = dedented_desc
                    
                    # Start new parameter
                    base_indent = len(param_match.group(1))
                    current_param = param_match.group(2)
                    first_line = param_match.group(3)
                    current_desc_lines = [first_line] if first_line else []
                elif current_param and line:
                    # Continuation line (including empty lines within the param)
                    current_desc_lines.append(line)
                elif current_param and not line.strip():
                    # Blank line - include it to preserve structure
                    current_desc_lines.append(line)
            
            # Save last parameter
            if current_param:
                dedented_desc = self._dedent_lines(current_desc_lines, base_indent)
                param_descriptions[current_param] = dedented_desc
            
            if not param_descriptions:
                # No parseable parameters, return original
                return match.group(0)
            
            # Build ParamFields
            result_lines = ["**Parameters:**", ""]
            
            for param_name, description in param_descriptions.items():
                type_str = None
                default_val = None
                
                # Get type and default from signature if available
                if param_name in param_info:
                    type_str = param_info[param_name]["type"]
                    default_val = param_info[param_name]["default"]
                
                # Build ParamField
                param_field = f'<ParamField path="{param_name}"'
                if type_str:
                    # Wrap type in backticks for inline code formatting
                    param_field += f' type="`{type_str}`"'
                if default_val:
                    default_str = str(default_val)
                    # If default contains double quotes, use single quote wrapper
                    # Otherwise use double quote wrapper and escape any single quotes
                    if '"' in default_str:
                        param_field += f" default='{default_str}'"
                    else:
                        # Escape single quotes for HTML/JSX parsing
                        escaped_default = default_str.replace("'", "&#39;")
                        param_field += f' default="{escaped_default}"'
                param_field += '>'
                
                result_lines.append(param_field)
                if description:
                    # Escape curly braces and angle brackets in description
                    escaped_desc = description.replace("{", "\\{").replace("}", "\\}")
                    escaped_desc = escaped_desc.replace("<", "\\<").replace(">", "\\>")
                    result_lines.append(f"  {escaped_desc}")
                result_lines.append("</ParamField>")
                result_lines.append("")
            
            return '\n'.join(result_lines)
        
        # Replace Args sections with ParamFields
        docstring = re.sub(args_pattern, replace_args_section, docstring, flags=re.MULTILINE)
        
        return docstring

    def _convert_returns_to_paramfield(self, docstring: str, return_annotation: str | None = None) -> str:
        """Convert Returns/Yields section to Fern ParamField format.

        Args:
            docstring: The docstring to process
            return_annotation: The actual return type annotation from the function signature (if available)
        """
        returns_pattern = r'^(\*\*(?:Returns|Return|Yields|Yield):\*\*)\s*$\n((?:[ \t]+.+(?:\n|$))*)'
        
        def replace_returns_section(match):
            section_header = match.group(1)
            section_content = match.group(2)
            
            if not section_content.strip():
                return match.group(0)
            
            lines = section_content.split('\n')
            
            first_line = None
            remaining_lines = []
            found_first = False
            
            for line in lines:
                if not found_first and line.strip():
                    first_line = line.strip()
                    found_first = True
                elif found_first:
                    remaining_lines.append(line)
            
            if not first_line:
                return match.group(0)
            
            # If we have an actual return annotation from the signature, use it as the type
            # and treat the docstring content as the description
            if return_annotation:
                return_type = return_annotation
                # The entire docstring content (including first line) becomes the description
                type_desc_match = re.match(r'^([^:]+?):\s*(.*)$', first_line)
                if type_desc_match:
                    # If there's a colon, the part after the colon starts the description
                    description_parts = [type_desc_match.group(2)] if type_desc_match.group(2) else []
                else:
                    # Otherwise the entire first line is the description
                    description_parts = [first_line]
            else:
                # Fallback: parse type from docstring (old behavior)
                type_desc_match = re.match(r'^([^:]+?):\s*(.*)$', first_line)
                
                if type_desc_match:
                    return_type = type_desc_match.group(1).strip()
                    description_parts = [type_desc_match.group(2)] if type_desc_match.group(2) else []
                else:
                    return_type = first_line.strip()
                    description_parts = []
            
            for line in remaining_lines:
                if line.strip():
                    description_parts.append(line.strip())
            
            description = ' '.join(description_parts).strip() if description_parts else ''
            
            result_lines = ["**Returns:**", ""]
            
            # Build ParamField with type only (no path for return values)
            # Wrap type in backticks for inline code formatting
            param_field = f'<ParamField type="`{return_type}`">'
            result_lines.append(param_field)
            
            if description:
                result_lines.append(f"  {description}")
            
            result_lines.append("</ParamField>")
            result_lines.append("")
            
            return '\n'.join(result_lines)
        
        docstring = re.sub(returns_pattern, replace_returns_section, docstring, flags=re.MULTILINE)
        
        return docstring

    def _convert_note_sections_to_components(self, docstring: str) -> str:
        """Convert **Note:** and **Warning:** sections to Fern components."""
        # Pattern to match Note/Warning sections
        note_pattern = r'^(\*\*Note:\*\*)\s*$\n((?:(?:[ \t]+.*|[ \t]*)\n)*(?:[ \t]+.*)?)'
        warning_pattern = r'^(\*\*Warning:\*\*)\s*$\n((?:(?:[ \t]+.*|[ \t]*)\n)*(?:[ \t]+.*)?)'
        
        def replace_note_section(match):
            section_content = match.group(2)
            
            if not section_content.strip():
                return match.group(0)

            # Remove leading indentation from all lines
            lines = section_content.split('\n')
            content = self._dedent_lines(lines)
            
            # Build result with Note component
            return f'<Note>\n\n{content}\n\n</Note>\n'
        
        def replace_warning_section(match):
            section_content = match.group(2)
            
            if not section_content.strip():
                return match.group(0)

            # Remove leading indentation from all lines
            lines = section_content.split('\n')
            content = self._dedent_lines(lines)
            
            # Build result with Warning component
            return f'<Warning>\n\n{content}\n\n</Warning>\n'
        
        # Replace Note and Warning sections with components
        docstring = re.sub(note_pattern, replace_note_section, docstring, flags=re.MULTILINE)
        docstring = re.sub(warning_pattern, replace_warning_section, docstring, flags=re.MULTILINE)
        
        return docstring

    def _format_examples_section(self, docstring: str) -> str:
        """Format Examples section by wrapping code in code blocks."""
        # Pattern to match Examples/Example section
        # Captures everything indented (or blank lines) until we hit a non-indented line or end of string
        examples_pattern = r'^(\*\*(?:Examples?|Example):\*\*)\s*$\n((?:(?:[ \t]+.*|[ \t]*)\n)*(?:[ \t]+.*)?)'
        
        def replace_examples_section(match):
            section_header = match.group(1)
            section_content = match.group(2)
            
            if not section_content.strip():
                return match.group(0)

            # Remove leading indentation from all lines
            lines = section_content.split('\n')
            code_content = self._dedent_lines(lines)
            
            # Build result with code block
            result_lines = [section_header, "", "```python", code_content, "```", ""]
            
            return '\n'.join(result_lines)
        
        # Replace Examples sections with code blocks
        docstring = re.sub(examples_pattern, replace_examples_section, docstring, flags=re.MULTILINE)
        
        return docstring

    def _generate_slug(self, full_name: str) -> str:
        """Generate slug from full dotted name: mypackage.utils.helpers → mypackage-utils-helpers"""
        return full_name.replace(".", "-").replace("_", "-")

    def _generate_file_path(self, full_name: str) -> str:
        """Generate nested file path from full dotted name.
        
        Every item gets its own folder.
        Examples:
        - mypackage → mypackage/mypackage
        - mypackage.utils → mypackage/utils/utils
        - mypackage.utils.helpers → mypackage/utils/helpers/helpers
        """
        parts = full_name.split(".")
        # All parts as directories + last part as filename
        return "/".join(parts) + "/" + parts[-1]
    
    def _generate_page_path(self, full_name: str) -> str:
        """Generate page path for linking (directory path without duplicate filename).
        
        Used for cross-page links in Fern.
        Examples:
        - mypackage → mypackage
        - mypackage.utils → mypackage/utils
        - mypackage.utils.helpers → mypackage/utils/helpers
        """
        parts = full_name.split(".")
        return "/".join(parts)
    
    def _generate_relative_file_path(self, from_full_name: str, to_full_name: str) -> str:
        """Generate relative file path between two items.
        
        Args:
            from_full_name: The full name of the current item (where the link is)
            to_full_name: The full name of the target item (what we're linking to)
        
        Returns:
            Relative path from current item to target item (just the directory path)
        
        Examples:
            from nemo_rl.converters to nemo_rl.converters.huggingface → huggingface
            from nemo_rl to nemo_rl.converters → converters
        
        Note: Returns just the directory name, not the full file path with duplication.
        The actual file is at huggingface/huggingface.mdx but we link to just "huggingface"
        """
        from_parts = from_full_name.split(".")
        to_parts = to_full_name.split(".")
        
        # Find common prefix
        common_length = 0
        for i, (f, t) in enumerate(zip(from_parts, to_parts)):
            if f == t:
                common_length = i + 1
            else:
                break
        
        # Get the unique parts of the target path (after the common prefix)
        unique_to_parts = to_parts[common_length:]
        
        # Build the relative path: just the unique parts WITHOUT the file duplication
        # File is at: unique_parts/last_part.mdx
        # But we link to: unique_parts (directory only)
        if unique_to_parts:
            # Return just the directory path (all unique parts)
            return "/".join(unique_to_parts)
        else:
            # They're the same, shouldn't happen but handle gracefully
            return to_parts[-1]

    def _generate_anchor_id(self, full_name: str) -> str:
        """Generate anchor ID from full_name for use in <Anchor> components."""
        return full_name.replace(".", "").replace("_", "").lower()

    def _are_on_same_page(self, item1_name: str, item2_name: str) -> bool:
        """Determine if two items are rendered on the same page."""
        item1 = self.get_item(item1_name)
        item2 = self.get_item(item2_name)

        if not item1 or not item2:
            return False

        # Each item type gets its own page, except for direct children
        item1_page = self._get_page_for_item(item1_name)
        item2_page = self._get_page_for_item(item2_name)

        return item1_page == item2_page

    def _get_page_for_item(self, full_name: str) -> str:
        """Get the page where this item is rendered.

        Based on CLI logic: only packages and modules get their own files.
        All other items (classes, functions, methods, etc.) are rendered
        on their parent module/package page.
        """
        item = self.get_item(full_name)
        if not item:
            return full_name

        item_type = item["type"]
        parts = full_name.split(".")

        # Only packages and modules get their own dedicated pages/files
        if item_type in ("package", "module"):
            return full_name

        # All other items (classes, functions, methods, properties, attributes, data)
        # are rendered on their parent module/package page
        else:
            # Find the parent module or package
            for i in range(len(parts) - 1, 0, -1):
                parent_name = ".".join(parts[:i])
                parent_item = self.get_item(parent_name)
                if parent_item and parent_item["type"] in ("package", "module"):
                    return parent_name

            # Fallback - shouldn't happen, but return the root module
            return parts[0] if parts else full_name

    def _get_cross_reference_link(
        self, target_name: str, display_name: str = None, current_page: str = None
    ) -> str:
        """Generate cross-reference link to another documented object."""
        # Check if target exists in our database
        target_item = self.get_item(target_name)
        if target_item is None:
            # Return plain text if target not found
            return f"`{display_name or target_name}`"

        link_text = display_name or target_name.split(".")[-1]
        anchor_id = self._generate_anchor_id(target_name)

        # Determine if target is on same page as current page
        if current_page and self._are_on_same_page(target_name, current_page):
            # Same page - use anchor link only
            return f"[`{link_text}`](#{anchor_id})"
        else:
            # Different page - use cross-page link
            target_page = self._get_page_for_item(target_name)
            target_page_path = self._generate_file_path(target_page)
            return f"[`{link_text}`]({target_page_path}#{anchor_id})"

    def _format_code_block_with_links(self, code: str, language: str = "python", current_page: str = None, current_item: str = None) -> str:
        """Format code block with deep linking using CodeBlock component.

        Extracts full dotted paths (e.g., mypackage.utils.helpers.MyClass) from the code
        and creates direct links to them - only when there are actual documented types to link to.

        Simple type annotations like 'input_key: str' won't generate links since 'str' is a built-in.
        Items won't link to themselves (e.g., class name in its own signature).
        """
        links = {}
        
        # Pattern to match Python dotted paths (e.g., mypackage.utils.helpers.MyClass)
        # Must start with a word boundary and consist of identifiers separated by dots
        dotted_path_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)+)\b'
        
        # Find all dotted paths in the code
        for match in re.finditer(dotted_path_pattern, code):
            full_path = match.group(1)
            
            # Skip if this is the item linking to itself
            if current_item and full_path == current_item:
                continue
            
            # Try to find this exact path in our database
            item = self.get_item(full_path)
            if item:
                # Found it! Create a link using the exact text in the code (full_path)
                # This ensures we link to the right thing even if multiple items have same short name
                
                # Check if this item is on the same page as the code block
                if current_page and self._are_on_same_page(full_path, current_page):
                    # Same page - use anchor-only link
                    anchor_id = self._generate_anchor_id(full_path)
                    links[full_path] = f"#{anchor_id}"
                else:
                    # Different page - use full cross-page link
                    page_name = self._get_page_for_item(full_path)
                    page_path = self._generate_file_path(page_name)
                    anchor_id = self._generate_anchor_id(full_path)
                    links[full_path] = f"{page_path}#{anchor_id}"

        # Only generate CodeBlock component if we found linkable types
        # Simple annotations like 'input_key: str' won't have links (str is built-in)
        if links:
            links_json = ", ".join(f'"{k}": "{v}"' for k, v in links.items())
            return f"<CodeBlock\n  links={{{{{links_json}}}}}\n>\n\n```{language}\n{code}\n```\n\n</CodeBlock>"
        else:
            # No linkable types found - use simple code block
            return f"```{language}\n{code}\n```"

    def validate_all_links(self, output_dir: str = None) -> dict[str, list[str]]:
        """Validate all generated links and return any issues found.

        Fast lightweight validation focusing on core link integrity.

        Returns:
            Dict with 'errors' and 'warnings' keys containing lists of issues.
        """
        issues = {"errors": [], "warnings": []}

        # Sample a few items to validate the core logic works
        sample_items = []
        for item_type in ("package", "module", "class", "function"):
            type_items = list(self._db.get_by_type(item_type))
            if type_items:
                sample_items.append(type_items[0])  # Just take first item of each type

        for item in sample_items:
            full_name = item["full_name"]

            # Validate that we can determine the correct page for this item
            try:
                page_name = self._get_page_for_item(full_name)
                anchor_id = self._generate_anchor_id(full_name)

                if not anchor_id:
                    issues["errors"].append(
                        f"Empty anchor ID generated for {full_name}"
                    )

                # Test cross-reference link generation
                test_link = self._get_cross_reference_link(
                    full_name, None, "test.module"
                )
                if not test_link or test_link == full_name:
                    issues["warnings"].append(
                        f"Link generation may have issues for {full_name}"
                    )

            except Exception as e:
                issues["errors"].append(f"Error processing {full_name}: {e}")

        # Quick check: verify some common patterns
        packages = list(self._db.get_by_type("package"))
        modules = list(self._db.get_by_type("module"))

        if not packages and not modules:
            issues["errors"].append("No packages or modules found - this seems wrong")

        return issues

    def generate_navigation_yaml(self) -> str:
        """Generate navigation YAML for Fern docs.yml following sphinx autodoc2 toctree logic."""
        import yaml

        # Find root packages (no dots in name)
        root_packages = []
        for item in self._db.get_by_type("package"):
            full_name = item["full_name"]
            if "." not in full_name:  # Root packages only
                root_packages.append(item)

        if not root_packages:
            return ""

        # Build navigation structure recursively
        nav_contents = []
        for root_pkg in sorted(root_packages, key=lambda x: x["full_name"]):
            nav_item = self._build_nav_item_recursive(root_pkg)
            if nav_item:
                nav_contents.append(nav_item)

        # Create the final navigation structure
        navigation = {
            "navigation": [
                {
                    "section": "API Reference",
                    "skip-slug": True,
                    "contents": nav_contents,
                }
            ]
        }

        return yaml.dump(
            navigation, default_flow_style=False, sort_keys=False, allow_unicode=True
        )

    def _build_nav_item_recursive(self, item: ItemData) -> dict[str, t.Any] | None:
        """Build navigation item recursively following sphinx autodoc2 toctree logic."""
        full_name = item["full_name"]
        file_path = self._generate_file_path(full_name)

        # Get children (same logic as sphinx toctrees)
        subpackages = list(self.get_children(item, {"package"}))
        submodules = list(self.get_children(item, {"module"}))

        if subpackages or submodules:
            # This has children - make it a section with skip-slug
            section_item = {
                "section": full_name.split(".")[-1],  # Use short name for section
                "skip-slug": True,
                "path": f"{file_path}{self.EXTENSION}",
                "contents": [],
            }

            # Add subpackages recursively (maxdepth: 3 like sphinx)
            for child in sorted(subpackages, key=lambda x: x["full_name"]):
                child_nav = self._build_nav_item_recursive(child)
                if child_nav:
                    section_item["contents"].append(child_nav)

            # Add submodules as pages (maxdepth: 1 like sphinx)
            for child in sorted(submodules, key=lambda x: x["full_name"]):
                child_file_path = self._generate_file_path(child["full_name"])
                section_item["contents"].append(
                    {
                        "page": child["full_name"].split(".")[-1],  # Use short name
                        "path": f"{child_file_path}{self.EXTENSION}",
                    }
                )

            return section_item
        else:
            # Leaf item - just a page
            return {
                "page": full_name.split(".")[-1],  # Use short name
                "path": f"{file_path}{self.EXTENSION}",
            }
