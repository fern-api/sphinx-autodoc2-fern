"""Renderer for Fern."""

from __future__ import annotations

import re
import typing as t

from autodoc2.render.base import RendererBase

if t.TYPE_CHECKING:
    from autodoc2.utils import ItemData


_RE_DELIMS = re.compile(r"(\s*[\[\]\(\),]\s*)")


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

        # Use multiline format only if there are actual parameters (excluding self)
        args_list = item.get("args", [])
        # Filter out 'self' and 'cls' to determine if there are real parameters
        real_params = [arg for arg in args_list if arg[1] not in ("self", "cls")]
        has_real_params = len(real_params) > 0

        if not has_real_params:
            # No real parameters (empty or only self/cls) - use inline format
            args_formatted = self.format_args(args_list, show_annotations)
            code_content = f"{full_name}({args_formatted}){return_annotation}"
        else:
            # Has real parameters - use multiline format
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

        if self.show_docstring(item):
            raw_docstring = item.get("doc", "").strip()
            if raw_docstring:
                processed_docstring = self._convert_myst_directives(raw_docstring)
                processed_docstring = self._bold_docstring_sections(processed_docstring)
                processed_docstring = self._convert_args_to_paramfields(processed_docstring, item.get("args", []))
                processed_docstring = self._convert_returns_to_list(processed_docstring)
                escaped_docstring = self._escape_fern_content(processed_docstring)
                yield escaped_docstring

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
            yield "## Subpackages"
            yield ""
            for child in children_by_type["package"]:
                name = child["full_name"].split(".")[-1]
                # Create link using nested file path
                file_path = self._generate_file_path(child["full_name"])
                doc_summary = (
                    child.get("doc", "").split("\n")[0][:80] if child.get("doc") else ""
                )
                if len(child.get("doc", "")) > 80:
                    doc_summary += "..."
                yield (
                    f"- **[`{name}`]({file_path})** - {doc_summary}"
                    if doc_summary
                    else f"- **[`{name}`]({file_path})**"
                )
            yield ""

        if has_submodules:
            yield "## Submodules"
            yield ""
            for child in children_by_type["module"]:
                name = child["full_name"].split(".")[-1]
                # Create link using nested file path
                file_path = self._generate_file_path(child["full_name"])
                doc_summary = (
                    child.get("doc", "").split("\n")[0][:80] if child.get("doc") else ""
                )
                if len(child.get("doc", "")) > 80:
                    doc_summary += "..."
                yield (
                    f"- **[`{name}`]({file_path})** - {doc_summary}"
                    if doc_summary
                    else f"- **[`{name}`]({file_path})**"
                )
            yield ""

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
                    # Get full description (first paragraph, not truncated)
                    doc_lines = child.get("doc", "").strip().split("\n")
                    if doc_lines and doc_lines[0]:
                        # Get first paragraph (until empty line or end)
                        doc_summary = []
                        for line in doc_lines:
                            if not line.strip():
                                break
                            doc_summary.append(line.strip())
                        description = " ".join(doc_summary) if doc_summary else "None"
                    else:
                        description = "None"
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
                    # Get full description (first paragraph, not truncated)
                    doc_lines = child.get("doc", "").strip().split("\n")
                    if doc_lines and doc_lines[0]:
                        # Get first paragraph (until empty line or end)
                        doc_summary = []
                        for line in doc_lines:
                            if not line.strip():
                                break
                            doc_summary.append(line.strip())
                        description = " ".join(doc_summary) if doc_summary else "None"
                    else:
                        description = "None"
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
            args = self.format_args(
                constructor["args"], self.show_annotations(item), ignore_self="self"
            )
            if args.strip():
                code_content = f"class {full_name}({args})"
            else:
                code_content = f"class {full_name}"
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

        # Class content (wrapped in HTML div for proper indentation)
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
                processed_docstring = self._convert_myst_directives(raw_docstring)
                processed_docstring = self._bold_docstring_sections(processed_docstring)
                processed_docstring = self._convert_returns_to_list(processed_docstring)
                escaped_docstring = self._escape_fern_content(processed_docstring)
                content_lines.append(escaped_docstring)
                content_lines.append("")
            
            # Add "Initialization" section if we're merging __init__ docstring
            if self.config.class_docstring == "merge":
                init_item = self.get_item(f"{full_name}.__init__")
                if init_item and init_item.get("doc", "").strip():
                    content_lines.append("#### Initialization")
                    content_lines.append("")
                    init_docstring = init_item.get("doc", "").strip()
                    processed_init = self._convert_myst_directives(init_docstring)
                    processed_init = self._bold_docstring_sections(processed_init)
                    escaped_init = self._escape_fern_content(processed_init)
                    content_lines.append(escaped_init)
                    content_lines.append("")

        if content_lines and any(line.strip() for line in content_lines):
            for line in content_lines:
                if line.strip():
                    # Convert NOTE: and WARNING: to Fern components
                    formatted_line = self._format_fern_callouts(line)
                    yield formatted_line
                else:
                    yield ""

        # Render class members (methods, properties, attributes)
        for child in self.get_children(
            item, {"class", "property", "attribute", "method"}
        ):
            # Skip __init__ if we merged its docstring above
            if (
                child["full_name"].endswith(".__init__")
                and self.config.class_docstring == "merge"
            ):
                continue

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

        # Property content (wrapped in HTML div for proper indentation)
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

        # Property docstring - simple approach like MyST
        if self.show_docstring(item):
            raw_docstring = item.get("doc", "").strip()
            if raw_docstring:
                processed_docstring = self._convert_myst_directives(raw_docstring)
                processed_docstring = self._bold_docstring_sections(processed_docstring)
                escaped_docstring = self._escape_fern_content(processed_docstring)
                content_lines.append(escaped_docstring)

        if content_lines and any(line.strip() for line in content_lines):
            for line in content_lines:
                if line.strip():
                    # Convert NOTE: and WARNING: to Fern components
                    formatted_line = self._format_fern_callouts(line)
                    yield formatted_line
                else:
                    yield ""
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
            param_field = f'<ParamField path="{short_name}" type="{type_str}"'
            
            # Add default value if present
            if value is not None:
                value_str = str(value)
                # Escape quotes in the value
                escaped_value = value_str.replace('"', '\\"')
                param_field += f' default="{escaped_value}"'
            
            param_field += '>'
            yield param_field
            
            # Add docstring as ParamField content
            if self.show_docstring(item):
                raw_docstring = item.get("doc", "").strip()
                if raw_docstring:
                    processed_docstring = self._convert_myst_directives(raw_docstring)
                    processed_docstring = self._bold_docstring_sections(processed_docstring)
                    # Don't escape ParamField content - it's already inside a component
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
            
            # Show value for non-annotated data
            if value is not None:
                value_str = str(value)
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
                    processed_docstring = self._convert_myst_directives(raw_docstring)
                    processed_docstring = self._bold_docstring_sections(processed_docstring)
                    escaped_docstring = self._escape_fern_content(processed_docstring)
                    yield escaped_docstring
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
            if len(description) > 50:
                description = description[:47] + "..."

            yield f"| {link} | {description} |"

    def _format_args_multiline(
        self,
        args_info,
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
        if len(args_str) > 80 or len(formatted_args) >= 3:
            # Multi-line format: each arg on its own line
            return ",\n".join(formatted_args)
        else:
            # Single line format
            return args_str

    def _create_anchor(self, text: str) -> str:
        """Create a markdown anchor from header text, following standard markdown rules."""
        import re

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
        import re

        jinja_pattern = r"({%.*?%}|{{.*?}})"
        return re.search(jinja_pattern, text) is not None

    def _format_fern_callouts(self, line: str) -> str:
        """Convert NOTE: and WARNING: to Fern components."""
        import re

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
        import re

        # Don't escape if it's already a Jinja template
        if self._contains_jinja_template(content):
            return content

        # Split content by:
        # 1. Code blocks (triple/single backticks)
        # 2. Fern/MDX components (ParamField, CodeBlock, Anchor, etc.)
        # Preserve them all without escaping
        pattern = r"(```[\s\S]*?```|`[^`]*?`|<ParamField[\s\S]*?</ParamField>|<CodeBlock[\s\S]*?</CodeBlock>|<Anchor[\s\S]*?</Anchor>)"
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
        import re

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
        import re
        
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
            pattern = rf'^(\s*)({re.escape(section)})(\s*)$'
            content = re.sub(pattern, r'\1**\2**\3', content, flags=re.MULTILINE)
        
        return content

    def _convert_args_to_paramfields(self, docstring: str, args_info: list) -> str:
        """Convert Args/Parameters section in docstring to Fern ParamField components.
        
        Args:
            docstring: The docstring content
            args_info: List of (prefix, name, annotation, default) tuples from function signature
        """
        import re
        
        # Build a map of parameter info from the signature
        param_info = {}
        for prefix, name, annotation, default in args_info:
            if name and name not in ("self", "cls"):
                param_info[name] = {
                    "type": self.format_annotation(annotation) if annotation else None,
                    "default": default
                }
        
        # Pattern to match Args/Parameters/Arguments section
        args_pattern = r'^(\*\*(?:Args|Arguments|Parameters):\*\*)\s*$\n((?:[ \t]+.+(?:\n|$))*)'
        
        def replace_args_section(match):
            section_header = match.group(1)
            section_content = match.group(2)
            
            if not section_content.strip():
                return match.group(0)
            
            # Parse parameter descriptions from docstring
            param_descriptions = {}
            current_param = None
            current_desc_lines = []
            
            for line in section_content.split('\n'):
                # Match lines like "    param_name: description" or "    param_name (type): description"
                param_match = re.match(r'^[ \t]+([a-zA-Z_][a-zA-Z0-9_]*)\s*(?:\([^)]+\))?\s*:\s*(.*)$', line)
                if param_match:
                    # Save previous parameter
                    if current_param:
                        param_descriptions[current_param] = '\n'.join(current_desc_lines).strip()
                    current_param = param_match.group(1)
                    current_desc_lines = [param_match.group(2)] if param_match.group(2) else []
                elif current_param and line.strip():
                    # Continuation of description
                    current_desc_lines.append(line.strip())
            
            # Save last parameter
            if current_param:
                param_descriptions[current_param] = '\n'.join(current_desc_lines).strip()
            
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
                    param_field += f' type="{type_str}"'
                if default_val:
                    # Escape quotes in default value
                    escaped_default = str(default_val).replace('"', '\\"')
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

    def _convert_returns_to_list(self, docstring: str) -> str:
        """Convert Returns section to clean list format."""
        import re
        
        returns_pattern = r'^(\*\*(?:Returns|Return):\*\*)\s*$\n((?:[ \t]+.+(?:\n|$))*)'
        
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
            
            result_lines = ["**Returns:**"]
            
            if description:
                result_lines.append(f"- **{return_type}**: {description}")
            else:
                result_lines.append(f"- **{return_type}**")
            
            result_lines.append("")
            
            return '\n'.join(result_lines)
        
        docstring = re.sub(returns_pattern, replace_returns_section, docstring, flags=re.MULTILINE)
        
        return docstring

    def _generate_slug(self, full_name: str) -> str:
        """Generate slug from full dotted name: mypackage.utils.helpers → mypackage-utils-helpers"""
        return full_name.replace(".", "-").replace("_", "-")

    def _generate_file_path(self, full_name: str) -> str:
        """Generate nested file path from full dotted name.
        
        Every item gets its own folder.
        Examples:
        - mypackage → mypackage/mypackage/mypackage
        - mypackage.utils → mypackage/utils/utils
        - mypackage.utils.helpers → mypackage/utils/helpers/helpers
        """
        parts = full_name.split(".")
        # All parts as directories + last part as filename
        return "/".join(parts) + "/" + parts[-1]

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
        import re
        
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

    def _convert_py_obj_references(self, text: str) -> str:
        """Convert MyST {py:obj} references to Fern cross-reference links."""
        import re

        # Pattern to match {py:obj}`target_name` or {py:obj}`display_text <target_name>`
        pattern = r"\{py:obj\}`([^<>`]+)(?:\s*<([^>]+)>)?\`"

        def replace_ref(match):
            content = match.group(1)
            target = match.group(2)

            if target:
                # Format: {py:obj}`display_text <target_name>`
                display_text = content.strip()
                target_name = target.strip()
            else:
                # Format: {py:obj}`target_name`
                target_name = content.strip()
                display_text = None

            return self._get_cross_reference_link(target_name, display_text)

        return re.sub(pattern, replace_ref, text)

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
