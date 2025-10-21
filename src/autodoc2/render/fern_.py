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

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize the renderer with navigation tracking."""
        super().__init__(*args, **kwargs)
        self._navigation_items: list[dict[str, t.Any]] = []

    def render_item(self, full_name: str) -> t.Iterable[str]:
        """Render a single item by dispatching to the appropriate method."""
        item = self.get_item(full_name)
        if item is None:
            raise ValueError(f"Item {full_name} does not exist")
        
        type_ = item["type"]
        
        # Track this item for navigation generation (only packages and modules)
        if type_ in ("package", "module"):
            self._track_navigation_item(item)
        
        # Add frontmatter for API reference pages (packages and modules)
        if type_ in ("package", "module"):
            yield "---"
            yield "layout: overview"
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
        full_name = item["full_name"]
        show_annotations = self.show_annotations(item)
        
        # Function signature in code block (no header - code block IS the header)
        yield "```python"
        
        # Check if we should use inline or multiline formatting
        # Count non-self parameters
        non_self_args = [arg for arg in item.get('args', []) if arg[1] != 'self']
        use_inline = len(non_self_args) <= 1
        
        return_annotation = f" -> {self.format_annotation(item['return_annotation'])}" if show_annotations and item.get("return_annotation") else ""
        
        if use_inline:
            # Single parameter or no parameters - use inline format
            args_formatted = self.format_args(item['args'], show_annotations)
            yield f"{full_name}({args_formatted}){return_annotation}"
        else:
            # Multiple parameters - use multiline format
            args_formatted = self._format_args_multiline(item['args'], show_annotations)
            yield f"{full_name}("
            if args_formatted.strip():
                for line in args_formatted.split('\n'):
                    if line.strip():
                        yield f"    {line.strip()}"
            yield f"){return_annotation}"
        
        yield "```"
        yield ""
        
        # Function docstring
        if self.show_docstring(item):
            docstring_lines = list(self._format_docstring_sections(item['doc'], item))
            if any(line.strip() for line in docstring_lines):
                for line in docstring_lines:
                    if line.strip():
                        # Convert NOTE: and WARNING: to Fern components
                        formatted_line = self._format_fern_callouts(line)
                        yield formatted_line
                    else:
                        yield ""
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
            yield item['doc']
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
                link_path = child["full_name"].replace('.', '_')
                doc_summary = child.get('doc', '').split('\n')[0][:80] if child.get('doc') else ""
                if len(child.get('doc', '')) > 80:
                    doc_summary += "..."
                yield f"- **[`{name}`]({link_path})** - {doc_summary}" if doc_summary else f"- **[`{name}`]({link_path})**"
            yield ""
            
        if has_submodules:
            yield "## Submodules" 
            yield ""
            for child in children_by_type["module"]:
                name = child["full_name"].split(".")[-1]
                link_path = child["full_name"].replace('.', '_')
                doc_summary = child.get('doc', '').split('\n')[0][:80] if child.get('doc') else ""
                if len(child.get('doc', '')) > 80:
                    doc_summary += "..."
                yield f"- **[`{name}`]({link_path})** - {doc_summary}" if doc_summary else f"- **[`{name}`]({link_path})**"
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
                    short_name = full_name.split('.')[-1]
                    # Create anchor that matches auto-generated markdown anchors from headers
                    anchor = self._create_anchor(full_name)
                    name_link = f"[`{short_name}`](#{anchor})"
                    # Get full description (first paragraph, not truncated)
                    doc_lines = child.get('doc', '').strip().split('\n')
                    if doc_lines and doc_lines[0]:
                        # Get first paragraph (until empty line or end)
                        class_doc_summary: list[str] = []
                        for line in doc_lines:
                            if not line.strip():
                                break
                            class_doc_summary.append(line.strip())
                        description = ' '.join(class_doc_summary) if class_doc_summary else "None"
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
                    short_name = full_name.split('.')[-1]
                    # Create proper anchor that matches the header (use full name for anchor)
                    anchor = self._create_anchor(full_name)
                    name_link = f"[`{short_name}`](#{anchor})"
                    # Get full description (first paragraph, not truncated)
                    doc_lines = child.get('doc', '').strip().split('\n')
                    if doc_lines and doc_lines[0]:
                        # Get first paragraph (until empty line or end)
                        func_doc_summary: list[str] = []
                        for line in doc_lines:
                            if not line.strip():
                                break
                            func_doc_summary.append(line.strip())
                        description = ' '.join(func_doc_summary) if func_doc_summary else "None"
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
                    name = child["full_name"].split(".")[-1]
                    yield f"`{name}`"
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
        
        # Build class signature with constructor args
        constructor = self.get_item(f"{item['full_name']}.__init__")
        sig = short_name
        if constructor and "args" in constructor:
            args = self.format_args(
                constructor["args"], self.show_annotations(item), ignore_self="self"
            )
            sig += f"({args})"

        yield "```python"
        if constructor and "args" in constructor and args.strip():
            yield f"class {item['full_name']}({args})"
        else:
            yield f"class {item['full_name']}"
        yield "```"
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

        # Class docstring
        if self.show_docstring(item):
            content_lines.extend(self._format_docstring_sections(item['doc']))

            # Optionally merge __init__ docstring
            if self.config.class_docstring == "merge":
                init_item = self.get_item(f"{item['full_name']}.__init__")
                if init_item and init_item.get('doc'):
                    content_lines.append("### Initialization")
                    content_lines.append("")
                    content_lines.extend(self._format_docstring_sections(init_item['doc']))
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
            decorator_list = [f"`@{prop}`" for prop in ("abstractmethod", "classmethod") if prop in properties]
            if decorator_list:
                content_lines.append(f"**Decorators**: {', '.join(decorator_list)}")
                content_lines.append("")
        
        # Property docstring
        if self.show_docstring(item):
            content_lines.extend(self._format_docstring_sections(item['doc']))

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
        
        # Data signature in code block (no header - code block IS the header)
        yield "```python"
        if item.get("annotation"):
            yield f"{full_name}: {self.format_annotation(item['annotation'])}"
        else:
            yield f"{full_name}"
        yield "```"
        yield ""
        
        # Data content (wrapped in HTML div for proper indentation)
        content_lines = []
        value = item.get("value")
        if value is not None:
            value_str = str(value)
            
            # Handle Jinja templates like MyST does - use <Multiline-String> for complex templates
            if self._contains_jinja_template(value_str):
                if len(value_str.splitlines()) > 1 or len(value_str) > 100:
                    content_lines.append("**Value**: `<Multiline-String>`")
                else:
                    # Short templates - wrap in code block
                    content_lines.append("**Value**:")
                    content_lines.append("```jinja2")
                    content_lines.append(value_str)
                    content_lines.append("```")
            else:
                # Regular values - escape and wrap normally
                escaped_value = self._escape_fern_content(value_str)
                content_lines.append(f"**Value**: `{escaped_value}`")
        else:
            # Show None values explicitly like in HTML output
            content_lines.append("**Value**: `None`")
        
        if self.show_docstring(item):
            if content_lines:
                content_lines.append("")
            content_lines.extend(self._format_docstring_sections(item['doc']))
            
        if content_lines and any(line.strip() for line in content_lines):
            for line in content_lines:
                if line.strip():
                    # Convert NOTE: and WARNING: to Fern components
                    formatted_line = self._format_fern_callouts(line)
                    yield formatted_line
                else:
                    yield ""
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

    def _format_docstring_sections(self, docstring: str, item: ItemData | None = None) -> t.Iterable[str]:
        """Parse docstring into structured sections like Parameters, Returns, etc."""
        if not docstring.strip():
            return
            
        lines = docstring.strip().split('\n')
        
        # Parse into sections
        sections: dict[str, list[str]] = {"description": [], "parameters": [], "returns": [], "raises": []}
        current_section = "description"
        
        i = 0
        while i < len(lines):
            line = lines[i]
            line_stripped = line.strip()
            line_lower = line_stripped.lower()
            
            # Check for section headers (Google/Numpy style)
            if line_lower in ('args:', 'arguments:', 'parameters:', 'params:'):
                current_section = "parameters"
                i += 1
                continue
            elif line_lower in ('returns:', 'return:', 'yields:', 'yield:'):
                current_section = "returns"
                i += 1
                continue
            elif line_lower in ('raises:', 'raise:', 'except:', 'exceptions:'):
                current_section = "raises"
                i += 1
                continue
            
            # Check for RST-style parameters
            elif line_stripped.startswith(':param '):
                if ':' in line_stripped[7:]:
                    param_part = line_stripped[7:]
                    if ':' in param_part:
                        name, desc = param_part.split(':', 1)
                        sections["parameters"].append(f"**{name.strip()}**: {desc.strip()}")
                i += 1
                continue
                
            elif line_stripped.startswith((':return:', ':returns:', ':rtype:')):
                if ':' in line_stripped:
                    parts = line_stripped.split(':', 2)
                    if len(parts) >= 3:
                        sections["returns"].append(parts[2].strip())
                i += 1
                continue
            
            # Add line to current section
            sections[current_section].append(line)
            i += 1
        
        # Output formatted sections
        # Description first
        if sections["description"]:
            desc_text = '\n'.join(sections["description"]).strip()
            if desc_text:
                yield self._escape_fern_content(desc_text)
                yield ""
        
        # Parameters section
        if sections["parameters"]:
            yield "**Parameters:**"
            yield ""
            # If we have function item data, use ParamField components
            if item and item.get("args"):
                # Build parameter info map from function signature
                param_info: dict[str, dict[str, t.Any]] = {}
                for _prefix, name, annotation, default in item["args"]:  # type: ignore[assignment]
                    if name:
                        param_info[name] = {
                            "type": annotation,
                            "default": default
                        }
                
                # Render each parameter as ParamField
                for line in sections["parameters"]:
                    if line.strip() and ':' in line:
                        param_line = line.strip()
                        if ':' in param_line:
                            name, desc = param_line.split(':', 1)
                            param_name = name.strip()
                            escaped_desc = self._escape_fern_content(desc.strip())
                            
                            # Get type and default from function signature
                            if param_name in param_info:
                                param_type = param_info[param_name]["type"]
                                param_default = param_info[param_name]["default"]
                                
                                # Build ParamField component
                                param_field = f'<ParamField path="{param_name}"'
                                if param_type:
                                    param_field += f' type="{param_type}"'
                                if param_default is not None and param_default != "None":
                                    param_field += f' default="{param_default}"'
                                param_field += '>'
                                
                                yield param_field
                                if escaped_desc:
                                    yield f"  {escaped_desc}"
                                yield "</ParamField>"
                                yield ""
            else:
                # Fallback to old markdown format
                yield "**Parameters:**"
                yield ""
                for line in sections["parameters"]:
                    if line.strip():
                        # Google style: "    param_name: description"
                        if line.strip() and ':' in line:
                            # Remove leading whitespace and parse
                            param_line = line.strip()
                            if ':' in param_line:
                                name, desc = param_line.split(':', 1)
                                escaped_name = self._escape_fern_content(name.strip())
                                escaped_desc = self._escape_fern_content(desc.strip())
                                yield f"- **{escaped_name}**: {escaped_desc}"
                            else:
                                escaped_param = self._escape_fern_content(param_line)
                                yield f"- {escaped_param}"
                        elif line.strip():
                            # Continuation line
                            escaped_line = self._escape_fern_content(line.strip())
                            yield f"  {escaped_line}"
                yield ""
            
        # Returns section
        if sections["returns"]:
            yield "**Returns:**"
            yield ""
            for line in sections["returns"]:
                if line.strip():
                    yield self._escape_fern_content(line.strip())
            yield ""
            
        # Raises section
        if sections["raises"]:
            yield "**Raises:**"
            yield ""
            for line in sections["raises"]:
                if line.strip():
                    yield self._escape_fern_content(line.strip())
            yield ""

    def _format_args_multiline(self, args_info: t.Any, include_annotations: bool = True, ignore_self: str | None = None) -> str:
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
        anchor = re.sub(r'\s+', '-', anchor)
        # Remove non-alphanumeric characters except hyphens and underscores
        anchor = re.sub(r'[^a-z0-9\-_]', '', anchor)
        # Remove duplicate hyphens
        anchor = re.sub(r'-+', '-', anchor)
        # Remove leading/trailing hyphens
        anchor = anchor.strip('-')
        return anchor
    
    def _contains_jinja_template(self, text: str) -> bool:
        """Check if text contains Jinja template syntax."""
        import re
        jinja_pattern = r'({%.*?%}|{{.*?}})'
        return re.search(jinja_pattern, text) is not None
    
    def _format_fern_callouts(self, line: str) -> str:
        """Convert NOTE: and WARNING: to Fern components."""
        import re
        
        # Convert NOTE: to Fern Note component
        note_pattern = r'^(\s*)(NOTE:\s*)(.*)'
        if match := re.match(note_pattern, line, re.IGNORECASE):
            indent, _prefix, content = match.groups()
            return f"{indent}<Note> {content.strip()} </Note>"
            
        # Convert WARNING: to Fern Warning component  
        warning_pattern = r'^(\s*)(WARNING:\s*)(.*)'
        if match := re.match(warning_pattern, line, re.IGNORECASE):
            indent, _prefix, content = match.groups()
            return f"{indent}<Warning> {content.strip()} </Warning>"
            
        return line
    
    def _escape_fern_content(self, content: str) -> str:
        """Escape content for Fern compatibility (braces and HTML tags)."""
        import re
        
        # Don't escape if it's already a Jinja template 
        if self._contains_jinja_template(content):
            return content
        
        # First, find and temporarily replace HTML-like tags (including those with braces)
        # Pattern matches: <tag>, <{tag}>, <{answer_tag}>, </think>, etc.
        tag_pattern = r'<[^<>]*(?:\\?\{[^}]*\\?\}[^<>]*)*[^<>]*>'
        tags: list[str] = []
        def replace_tag(match: t.Any) -> str:
            tag = match.group(0)
            placeholder = f"__FERN_TAG_{len(tags)}__"
            tags.append(tag)
            return placeholder
        
        temp_content = re.sub(tag_pattern, replace_tag, content)
        
        # Now escape curly braces in the remaining content
        escaped_content = temp_content.replace('{', '\\{').replace('}', '\\}')
        
        # Restore tags wrapped in backticks
        for i, tag in enumerate(tags):
            placeholder = f"__FERN_TAG_{i}__"
            # Escape any braces inside the tag itself for consistency
            escaped_tag = tag.replace('{', '\\{').replace('}', '\\}')
            escaped_content = escaped_content.replace(placeholder, f'`{escaped_tag}`')
        
        return escaped_content

    def _track_navigation_item(self, item: ItemData) -> None:
        """Track an item for navigation generation.
        
        :param item: The item to track (should be a package or module)
        """
        full_name = item["full_name"]
        type_ = item["type"]
        
        doc = item.get('doc', '').strip()
        description = doc.split('\n')[0] if doc else ""
        
        nav_item = {
            "full_name": full_name,
            "type": type_,
            "description": description,
            "file_path": self._get_file_path_for_item(full_name),
        }
        self._navigation_items.append(nav_item)

    def _get_file_path_for_item(self, full_name: str) -> str:
        """Get the relative file path for an item.
        
        This generates the path that will be used in the navigation YAML.
        Converts dots to underscores, keeping existing underscores.
        For example: 'my_package.submodule' -> './my_package_submodule.md'
        
        :param full_name: The fully qualified name of the item
        :return: The relative file path
        """
        filename = full_name.replace('.', '_')
        return f"./{filename}{self.EXTENSION}"

    def build_navigation_tree(self) -> list[dict[str, t.Any]]:
        """Build a hierarchical navigation tree from tracked items.
        
        This creates a nested structure that matches Fern's navigation format:
        - Top-level packages become sections
        - Subpackages and modules become nested sections or pages
        
        :return: A list of navigation items in Fern format
        """
        if not self._navigation_items:
            return []
        
        tree: dict[str, dict[str, t.Any]] = {}
        
        for item in self._navigation_items:
            full_name = item["full_name"]
            parts = full_name.split(".")
            
            current = tree
            for i, part in enumerate(parts):
                if part not in current:
                    current[part] = {
                        "_item": None,
                        "_children": {}
                    }
                
                if i == len(parts) - 1:
                    current[part]["_item"] = item
                
                current = current[part]["_children"]
        
        # Convert tree to Fern navigation format
        def tree_to_nav(node_dict: dict[str, dict[str, t.Any]], parent_name: str = "") -> list[dict[str, t.Any]]:
            """Convert tree structure to Fern navigation format."""
            nav_items = []
            
            for name in sorted(node_dict.keys()):
                node = node_dict[name]
                item = node["_item"]
                children = node["_children"]
                
                if item is None:
                    continue
                
                full_name = item["full_name"]
                
                if children:
                    section_item = {
                        "section": full_name,
                        "contents": []
                    }
                    
                    section_item["contents"].append({
                        "page": full_name,
                        "path": item["file_path"]
                    })
                    
                    child_nav = tree_to_nav(children, full_name)
                    section_item["contents"].extend(child_nav)
                    
                    nav_items.append(section_item)
                else:
                    page_item = {
                        "page": full_name,
                        "path": item["file_path"]
                    }
                    nav_items.append(page_item)
            
            return nav_items
        
        return tree_to_nav(tree)

    def generate_navigation_yaml(self) -> str:
        """Generate a YAML string for Fern navigation.
        
        This creates a navigation structure that can be saved to a file
        and included in a Fern docs.yml file.
        
        :return: YAML string representing the navigation structure
        """
        import yaml
        
        nav_tree = self.build_navigation_tree()
        
        if not nav_tree:
            return ""
        
        navigation_structure = {
            "navigation": nav_tree
        }
        
        # Generate YAML with proper formatting
        return yaml.dump(
            navigation_structure,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True
        )
