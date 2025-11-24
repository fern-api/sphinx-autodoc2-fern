"""Docstring transformation utilities for Fern renderer.

This module handles all docstring processing and transformation operations,
including converting MyST directives, bolding section headers, and transforming
docstring sections into Fern components.
"""

from __future__ import annotations

import logging
import os
import re
import typing as t

from docstring_parser import parse

logger = logging.getLogger(__name__)


class DocstringProcessor:
    """Handles docstring transformations for Fern MDX output."""

    def __init__(
        self,
        format_annotation_fn: t.Callable[[t.Any], str],
        escape_fn: t.Callable[[str], str],
        current_item: str | None = None,
    ):
        """Initialize the docstring processor.

        Args:
            format_annotation_fn: Function to format type annotations
            escape_fn: Function to escape content for Fern/MDX
            current_item: Current item being processed (for logging)
        """
        self.format_annotation = format_annotation_fn
        self.escape_content = escape_fn
        self.current_item = current_item
        # Feature flag: Set USE_REGEX_PARSER=1 to use legacy regex implementation
        self.use_docstring_parser = os.environ.get("USE_REGEX_PARSER", "0") != "1"

    def process_docstring(
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
        if not raw_docstring.strip():
            return ""

        # Use new docstring_parser implementation if feature flag is enabled
        if self.use_docstring_parser:
            # Temporarily store current_item for use in _process_docstring_with_parser
            old_item = self.current_item
            self.current_item = current_item or old_item
            result = self._process_docstring_with_parser(raw_docstring, args_info, return_annotation)
            self.current_item = old_item
            return result

        # Otherwise use original regex-based implementation
        docstring = self.convert_myst_directives(raw_docstring)
        docstring = self.bold_docstring_sections(docstring)
        docstring = self.convert_note_sections_to_components(docstring)

        if args_info:
            docstring = self.convert_args_to_paramfields(docstring, args_info)

        if return_annotation is not None:
            docstring = self.convert_returns_to_paramfield(docstring, return_annotation)

        docstring = self.format_examples_section(docstring)
        return self.escape_content(docstring)

    def convert_myst_directives(self, content: str) -> str:
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

    def bold_docstring_sections(self, content: str) -> str:
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
            pattern = rf"^(\s*)({re.escape(section)})[ \t]*$"
            replacement = r"\1**\2**\n"
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

        return content

    def dedent_lines(self, lines: list[str], base_indent: int | None = None) -> str:
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
                if len(line) >= base_indent and line[:base_indent].strip() == "":
                    dedented.append(line[base_indent:])
                else:
                    dedented.append(line.lstrip())
            else:
                # Preserve empty lines
                dedented.append("")

        return "\n".join(dedented).strip()

    def convert_args_to_paramfields(self, docstring: str, args_info: list) -> str:
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
                    "default": default,
                }

        # Pattern to match Args/Parameters/Arguments section
        # Captures all indented content (including blank lines) until we hit a non-indented line or another section
        args_pattern = r"^(\*\*(?:Args|Arguments|Parameters):\*\*)\s*$\n((?:(?:[ \t]+.*|[ \t]*)\n)*(?:[ \t]+.*)?)"

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

            for line in section_content.split("\n"):
                # Match lines like "    param_name: description" or "    param_name (type): description"
                param_match = re.match(
                    r"^([ \t]+)([a-zA-Z_][a-zA-Z0-9_]*)\s*(?:\([^)]+\))?\s*:\s*(.*)$", line
                )
                if param_match:
                    # Save previous parameter
                    if current_param:
                        # Remove common indentation from description lines
                        dedented_desc = self.dedent_lines(current_desc_lines, base_indent)
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
                dedented_desc = self.dedent_lines(current_desc_lines, base_indent)
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
                param_field += ">"

                result_lines.append(param_field)
                if description:
                    # Escape curly braces and angle brackets in description
                    escaped_desc = description.replace("{", "\\{").replace("}", "\\}")
                    escaped_desc = escaped_desc.replace("<", "\\<").replace(">", "\\>")
                    result_lines.append(f"  {escaped_desc}")
                result_lines.append("</ParamField>")
                result_lines.append("")

            return "\n".join(result_lines)

        # Replace Args sections with ParamFields
        docstring = re.sub(args_pattern, replace_args_section, docstring, flags=re.MULTILINE)

        return docstring

    def convert_returns_to_paramfield(
        self, docstring: str, return_annotation: str | None = None
    ) -> str:
        """Convert Returns/Yields section to Fern ParamField format.

        Args:
            docstring: The docstring to process
            return_annotation: The actual return type annotation from the function signature (if available)
        """
        returns_pattern = (
            r"^(\*\*(?:Returns|Return|Yields|Yield):\*\*)\s*$\n((?:[ \t]+.+(?:\n|$))*)"
        )

        def replace_returns_section(match):
            section_header = match.group(1)
            section_content = match.group(2)

            if not section_content.strip():
                return match.group(0)

            lines = section_content.split("\n")

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
                type_desc_match = re.match(r"^([^:]+?):\s*(.*)$", first_line)
                if type_desc_match:
                    # If there's a colon, the part after the colon starts the description
                    description_parts = (
                        [type_desc_match.group(2)] if type_desc_match.group(2) else []
                    )
                else:
                    # Otherwise the entire first line is the description
                    description_parts = [first_line]
            else:
                # Fallback: parse type from docstring (old behavior)
                type_desc_match = re.match(r"^([^:]+?):\s*(.*)$", first_line)

                if type_desc_match:
                    return_type = type_desc_match.group(1).strip()
                    description_parts = (
                        [type_desc_match.group(2)] if type_desc_match.group(2) else []
                    )
                else:
                    return_type = first_line.strip()
                    description_parts = []

            for line in remaining_lines:
                if line.strip():
                    description_parts.append(line.strip())

            description = " ".join(description_parts).strip() if description_parts else ""

            result_lines = ["**Returns:**", ""]

            # Build ParamField with type only (no path for return values)
            # Wrap type in backticks for inline code formatting
            param_field = f'<ParamField type="`{return_type}`">'
            result_lines.append(param_field)

            if description:
                result_lines.append(f"  {description}")

            result_lines.append("</ParamField>")
            result_lines.append("")

            return "\n".join(result_lines)

        docstring = re.sub(returns_pattern, replace_returns_section, docstring, flags=re.MULTILINE)

        return docstring

    def convert_note_sections_to_components(self, docstring: str) -> str:
        """Convert **Note:** and **Warning:** sections to Fern components."""
        # Pattern to match Note/Warning sections
        note_pattern = r"^(\*\*Note:\*\*)\s*$\n((?:(?:[ \t]+.*|[ \t]*)\n)*(?:[ \t]+.*)?)"
        warning_pattern = r"^(\*\*Warning:\*\*)\s*$\n((?:(?:[ \t]+.*|[ \t]*)\n)*(?:[ \t]+.*)?)"

        def replace_note_section(match):
            section_content = match.group(2)

            if not section_content.strip():
                return match.group(0)

            # Remove leading indentation from all lines
            lines = section_content.split("\n")
            content = self.dedent_lines(lines)

            # Build result with Note component
            return f"<Note>\n\n{content}\n\n</Note>\n"

        def replace_warning_section(match):
            section_content = match.group(2)

            if not section_content.strip():
                return match.group(0)

            # Remove leading indentation from all lines
            lines = section_content.split("\n")
            content = self.dedent_lines(lines)

            # Build result with Warning component
            return f"<Warning>\n\n{content}\n\n</Warning>\n"

        # Replace Note and Warning sections with components
        docstring = re.sub(note_pattern, replace_note_section, docstring, flags=re.MULTILINE)
        docstring = re.sub(warning_pattern, replace_warning_section, docstring, flags=re.MULTILINE)

        return docstring

    def format_examples_section(self, docstring: str) -> str:
        """Format Examples section by wrapping code in code blocks."""
        # Pattern to match Examples/Example section
        # Captures everything indented (or blank lines) until we hit a non-indented line or end of string
        examples_pattern = (
            r"^(\*\*(?:Examples?|Example):\*\*)\s*$\n((?:(?:[ \t]+.*|[ \t]*)\n)*(?:[ \t]+.*)?)"
        )

        def replace_examples_section(match):
            section_header = match.group(1)
            section_content = match.group(2)

            if not section_content.strip():
                return match.group(0)

            # Remove leading indentation from all lines
            lines = section_content.split("\n")
            code_content = self.dedent_lines(lines)

            # Check if code_content already has code block markers (from MyST directives)
            # If it starts with ```python or ```{xxx}, don't wrap it again
            if code_content.strip().startswith("```"):
                # Already has code blocks, just return with header
                result_lines = [section_header, "", code_content, ""]
            else:
                # Build result with code block
                result_lines = [section_header, "", "```python", code_content, "```", ""]

            return "\n".join(result_lines)

        # Replace Examples sections with code blocks
        docstring = re.sub(examples_pattern, replace_examples_section, docstring, flags=re.MULTILINE)

        return docstring

    def _process_docstring_with_parser(
        self,
        raw_docstring: str,
        args_info: list | None = None,
        return_annotation: str | None = None,
    ) -> str:
        """Process docstring using HYBRID approach (NEW IMPLEMENTATION).

        Uses docstring_parser for Args/Returns parsing (the complex parts),
        but keeps the existing regex for everything else (MyST, Note, Examples).

        This gives us:
        - Robust parsing of structured Args/Returns sections
        - Consistent output format (keeps existing regex behavior)
        - Support for multiple docstring styles (Google/NumPy/reStructuredText)

        Args:
            raw_docstring: The raw docstring text to process
            args_info: Optional list of (prefix, name, annotation, default) tuples for parameters
            return_annotation: Optional return type annotation string

        Returns:
            Fully processed and escaped docstring ready for MDX output
        """
        # Parse with docstring_parser to extract structured sections
        parsed = parse(raw_docstring)

        # Start with standard processing
        docstring = self.convert_myst_directives(raw_docstring)
        docstring = self.bold_docstring_sections(docstring)
        docstring = self.convert_note_sections_to_components(docstring)

        # Use parser for Args section if available (more robust than regex)
        if parsed.params and args_info:
            docstring = self._replace_args_with_parser(docstring, parsed.params, args_info)

        # Use parser for Returns/Yields section if available (more robust than regex)
        # Always convert if Returns section exists, even without signature annotation
        if parsed.returns:
            # Check if this is a Yields section (generator)
            if parsed.returns.is_generator:
                # Handle as Yields section
                docstring = self._replace_yields_with_parser(docstring, parsed.returns, return_annotation)
            else:
                # Handle as Returns section
                # Log warning if signature is missing return type annotation
                if not return_annotation:
                    item_name = self.current_item or 'function'
                    logger.warning(
                        f"Missing return type annotation: {item_name}"
                    )
                docstring = self._replace_returns_with_parser(docstring, parsed.returns, return_annotation)

        # Use parser for Raises section if available
        if parsed.raises:
            docstring = self._replace_raises_with_parser(docstring, parsed.raises)

        # Use parser for Attributes section if available (for classes)
        # Attributes are in params with args[0] == 'attribute'
        attributes = [p for p in parsed.params if p.args and p.args[0] == 'attribute']
        if attributes:
            docstring = self._replace_attributes_with_parser(docstring, attributes)

        # Keep existing regex for Examples section
        docstring = self.format_examples_section(docstring)

        return self.escape_content(docstring)

    def _replace_args_with_parser(
        self, docstring: str, params: list, args_info: list
    ) -> str:
        """Replace Args section using parsed parameters."""
        # Build the new ParamFields section
        param_fields = self._convert_params_to_paramfields(parsed_params=params, args_info=args_info)

        if not param_fields:
            return docstring

        # Remove the old Args section using regex
        args_pattern = r'\*\*(?:Args|Arguments|Parameters):\*\*\s*\n(?:(?:[ \t]+.*|[ \t]*)\n)*(?:[ \t]+.*)?'
        docstring = re.sub(args_pattern, "", docstring, flags=re.MULTILINE)

        # Find where to insert the new ParamFields (after long description, before other sections)
        lines = docstring.split("\n")
        insert_pos = len(lines)

        # Find the first section header (Returns, Raises, etc.)
        for i, line in enumerate(lines):
            if line.strip().startswith("**") and line.strip().endswith(":**"):
                insert_pos = i
                break

        # Insert the new ParamFields
        lines[insert_pos:insert_pos] = param_fields
        return "\n".join(lines)

    def _replace_returns_with_parser(
        self, docstring: str, returns, return_annotation: str | None
    ) -> str:
        """Replace Returns section using parsed returns."""
        # Build the new Returns ParamField section
        return_fields = self._convert_returns_to_paramfield_new(returns, return_annotation)

        if not return_fields:
            return docstring

        # Remove the old Returns section using regex
        returns_pattern = r'\*\*(?:Returns|Return|Yields|Yield):\*\*\s*\n(?:[ \t]+.+(?:\n|$))*'
        docstring = re.sub(returns_pattern, "", docstring, flags=re.MULTILINE)

        # Find where to insert (after Params, before Raises/Examples)
        lines = docstring.split("\n")
        insert_pos = len(lines)

        # Find position after **Parameters:** section
        for i, line in enumerate(lines):
            if line.strip() in ("**Raises:**", "**Example:**", "**Examples:**", "**Note:**", "**Warning:**"):
                insert_pos = i
                break

        # Insert the new Returns section
        lines[insert_pos:insert_pos] = return_fields
        return "\n".join(lines)

    def _convert_params_to_paramfields(
        self, parsed_params: list, args_info: list
    ) -> list[str]:
        """Convert parsed parameters to Fern ParamField components.

        Args:
            parsed_params: List of parsed DocstringParam objects
            args_info: List of (prefix, name, annotation, default) tuples from function signature

        Returns:
            List of formatted lines for ParamFields section
        """
        # Build a map of parameter info from the signature
        param_info = {}
        for prefix, name, annotation, default in args_info:
            if name and name not in ("self", "cls"):
                param_info[name] = {
                    "type": self.format_annotation(annotation) if annotation else None,
                    "default": default,
                }

        result_lines = ["**Parameters:**", ""]

        for param in parsed_params:
            param_name = param.arg_name
            if not param_name or param_name in ("self", "cls"):
                continue

            # Get type and default from signature (prefer signature over docstring)
            type_str = param_info.get(param_name, {}).get("type")
            default_val = param_info.get(param_name, {}).get("default")

            # Build ParamField
            param_field = f'<ParamField path="{param_name}"'
            if type_str:
                # Don't wrap type in backticks - Fern handles formatting
                param_field += f' type="{type_str}"'
            if default_val:
                default_str = str(default_val)
                # Handle quote escaping
                if '"' in default_str:
                    param_field += f" default='{default_str}'"
                else:
                    # Escape single quotes for HTML/JSX parsing
                    escaped_default = default_str.replace("'", "&#39;")
                    param_field += f' default="{escaped_default}"'
            param_field += '>'

            result_lines.append(param_field)

            # Add description if available
            if param.description:
                # Escape special characters in description
                escaped_desc = param.description.replace("{", "\\{").replace("}", "\\}")
                escaped_desc = escaped_desc.replace("<", "\\<").replace(">", "\\>")
                # Handle multi-line descriptions
                desc_lines = escaped_desc.strip().split("\n")
                for line in desc_lines:
                    result_lines.append(f"  {line}" if line.strip() else "")

            result_lines.append("</ParamField>")
            result_lines.append("")

        return result_lines

    def _convert_returns_to_paramfield_new(
        self, returns, return_annotation: str | None = None
    ) -> list[str]:
        """Convert parsed returns to Fern ParamField component.

        Args:
            returns: Parsed DocstringReturns object
            return_annotation: The actual return type annotation from the function signature

        Returns:
            List of formatted lines for Returns section
        """
        result_lines = ["**Returns:**", ""]

        # Use return_annotation from signature if available, otherwise use parsed type
        return_type = return_annotation if return_annotation else (returns.type_name or "Any")

        # Build ParamField with both empty path and empty type for cleaner appearance
        # The actual type will be shown in the description
        param_field = f'<ParamField path="" type="">'
        result_lines.append(param_field)

        # Show the type as the first line of the description
        result_lines.append(f"  `{return_type}`")
        result_lines.append("")

        # Add description if available
        if returns.description:
            # Escape special characters in description
            escaped_desc = returns.description.replace("{", "\\{").replace("}", "\\}")
            escaped_desc = escaped_desc.replace("<", "\\<").replace(">", "\\>")
            result_lines.append(f"  {escaped_desc}")

        result_lines.append("</ParamField>")
        result_lines.append("")

        return result_lines

    def _replace_yields_with_parser(
        self, docstring: str, yields, return_annotation: str | None
    ) -> str:
        """Replace Yields section using parsed yields (for generators).

        Args:
            docstring: The docstring to process
            yields: Parsed DocstringReturns object with is_generator=True
            return_annotation: The actual return type annotation from the function signature

        Returns:
            Docstring with Yields section replaced with ParamField
        """
        # Build the new Yields ParamField section
        yields_fields = self._convert_yields_to_paramfield(yields, return_annotation)

        if not yields_fields:
            return docstring

        # Remove the old Yields section using regex
        yields_pattern = r'\*\*(?:Yields|Yield):\*\*\s*\n(?:[ \t]+.+(?:\n|$))*'
        docstring = re.sub(yields_pattern, "", docstring, flags=re.MULTILINE)

        # Find where to insert (after Params, before Raises/Examples)
        lines = docstring.split("\n")
        insert_pos = len(lines)

        # Find position after **Parameters:** section, before Raises
        for i, line in enumerate(lines):
            if line.strip() in ("**Raises:**", "**Example:**", "**Examples:**", "**Note:**", "**Warning:**"):
                insert_pos = i
                break

        # Insert the new Yields section
        lines[insert_pos:insert_pos] = yields_fields
        return "\n".join(lines)

    def _replace_raises_with_parser(self, docstring: str, raises: list) -> str:
        """Replace Raises section using parsed exceptions.

        Args:
            docstring: The docstring to process
            raises: List of parsed DocstringRaises objects

        Returns:
            Docstring with Raises section replaced with ParamFields
        """
        # Build the new Raises ParamFields section
        raises_fields = self._convert_raises_to_paramfields(raises)

        if not raises_fields:
            return docstring

        # Remove the old Raises section using regex
        raises_pattern = r'\*\*(?:Raises|Raise):\*\*\s*\n(?:[ \t]+.+(?:\n|$))*'
        docstring = re.sub(raises_pattern, "", docstring, flags=re.MULTILINE)

        # Find where to insert (after Returns, before Examples)
        lines = docstring.split("\n")
        insert_pos = len(lines)

        # Find position after Returns/Yields sections
        for i, line in enumerate(lines):
            if line.strip() in ("**Example:**", "**Examples:**", "**Note:**", "**Warning:**"):
                insert_pos = i
                break

        # Insert the new Raises section
        lines[insert_pos:insert_pos] = raises_fields
        return "\n".join(lines)

    def _replace_attributes_with_parser(self, docstring: str, attributes: list) -> str:
        """Replace Attributes section using parsed attributes.

        Args:
            docstring: The docstring to process
            attributes: List of parsed DocstringParam objects with args[0] == 'attribute'

        Returns:
            Docstring with Attributes section replaced with ParamFields
        """
        # Build the new Attributes ParamFields section
        attr_fields = self._convert_attributes_to_paramfields(attributes)

        if not attr_fields:
            return docstring

        # Remove the old Attributes section using regex
        attrs_pattern = r'\*\*(?:Attributes|Attribute):\*\*\s*\n(?:(?:[ \t]+.*|[ \t]*)\n)*(?:[ \t]+.*)?'
        docstring = re.sub(attrs_pattern, "", docstring, flags=re.MULTILINE)

        # Find where to insert (after Parameters, before Returns)
        lines = docstring.split("\n")
        insert_pos = len(lines)

        # Find position after Parameters section, before Returns
        for i, line in enumerate(lines):
            if line.strip() in ("**Returns:**", "**Raises:**", "**Example:**", "**Examples:**", "**Note:**", "**Warning:**"):
                insert_pos = i
                break

        # Insert the new Attributes section
        lines[insert_pos:insert_pos] = attr_fields
        return "\n".join(lines)

    def _convert_raises_to_paramfields(self, raises: list) -> list[str]:
        """Convert parsed exceptions to Fern ParamField components.

        Args:
            raises: List of parsed DocstringRaises objects

        Returns:
            List of formatted lines for Raises section
        """
        result_lines = ["**Raises:**", ""]

        for exc in raises:
            exc_type = exc.type_name or "Exception"

            # Build ParamField with exception type as path
            param_field = f'<ParamField path="{exc_type}">'
            result_lines.append(param_field)

            # Add description if available
            if exc.description:
                # Escape special characters in description
                escaped_desc = exc.description.replace("{", "\\{").replace("}", "\\}")
                escaped_desc = escaped_desc.replace("<", "\\<").replace(">", "\\>")
                # Handle multi-line descriptions
                desc_lines = escaped_desc.strip().split("\n")
                for line in desc_lines:
                    result_lines.append(f"  {line}" if line.strip() else "")

            result_lines.append("</ParamField>")
            result_lines.append("")

        return result_lines

    def _convert_attributes_to_paramfields(self, attributes: list) -> list[str]:
        """Convert parsed attributes to Fern ParamField components.

        Args:
            attributes: List of parsed DocstringParam objects for class attributes

        Returns:
            List of formatted lines for Attributes section
        """
        result_lines = ["**Attributes:**", ""]

        for attr in attributes:
            attr_name = attr.arg_name
            if not attr_name:
                continue

            # Build ParamField
            param_field = f'<ParamField path="{attr_name}"'

            # Add type if available from docstring
            if attr.type_name:
                param_field += f' type="`{attr.type_name}`"'

            param_field += '>'
            result_lines.append(param_field)

            # Add description if available
            if attr.description:
                # Escape special characters in description
                escaped_desc = attr.description.replace("{", "\\{").replace("}", "\\}")
                escaped_desc = escaped_desc.replace("<", "\\<").replace(">", "\\>")
                # Handle multi-line descriptions
                desc_lines = escaped_desc.strip().split("\n")
                for line in desc_lines:
                    result_lines.append(f"  {line}" if line.strip() else "")

            result_lines.append("</ParamField>")
            result_lines.append("")

        return result_lines

    def _convert_yields_to_paramfield(
        self, yields, return_annotation: str | None = None
    ) -> list[str]:
        """Convert parsed yields to Fern ParamField component (for generators).

        Args:
            yields: Parsed DocstringReturns object with is_generator=True
            return_annotation: The actual return type annotation from the function signature

        Returns:
            List of formatted lines for Yields section
        """
        result_lines = ["**Yields:**", ""]

        # Use return_annotation from signature if available, otherwise use parsed type
        yield_type = return_annotation if return_annotation else (yields.type_name or "Any")

        # Build ParamField with both empty path and empty type for cleaner appearance
        # The actual type will be shown in the description
        param_field = f'<ParamField path="" type="">'
        result_lines.append(param_field)

        # Show the type as the first line of the description
        result_lines.append(f"  `{yield_type}`")
        result_lines.append("")

        # Add description if available
        if yields.description:
            # Escape special characters in description
            escaped_desc = yields.description.replace("{", "\\{").replace("}", "\\}")
            escaped_desc = escaped_desc.replace("<", "\\<").replace(">", "\\>")
            result_lines.append(f"  {escaped_desc}")

        result_lines.append("</ParamField>")
        result_lines.append("")

        return result_lines
