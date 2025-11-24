"""Link generation and path utilities for Fern renderer.

This module handles all cross-reference link generation, path/slug generation,
and code block deep linking functionality.
"""

from __future__ import annotations

import re
import typing as t

if t.TYPE_CHECKING:
    from autodoc2.utils import ItemData


class LinkGenerator:
    """Handles link generation and path management for Fern docs."""

    def __init__(self, get_item_fn: t.Callable[[str], ItemData | None], extension: str = ".mdx"):
        """Initialize the link generator.

        Args:
            get_item_fn: Function to retrieve items from the database by full name
            extension: File extension for generated files (default: ".mdx")
        """
        self.get_item = get_item_fn
        self.extension = extension

    def generate_slug(self, full_name: str) -> str:
        """Generate slug from full dotted name: mypackage.utils.helpers → mypackage-utils-helpers"""
        return full_name.replace(".", "-").replace("_", "-")

    def generate_file_path(self, full_name: str) -> str:
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

    def generate_page_path(self, full_name: str) -> str:
        """Generate page path for linking (directory path without duplicate filename).

        Used for cross-page links in Fern.
        Examples:
        - mypackage → mypackage
        - mypackage.utils → mypackage/utils
        - mypackage.utils.helpers → mypackage/utils/helpers
        """
        parts = full_name.split(".")
        return "/".join(parts)

    def generate_anchor_id(self, full_name: str) -> str:
        """Generate anchor ID from full_name for use in <Anchor> components.

        Removes dots but preserves underscores to maintain uniqueness.
        For example:
        - mypackage.utils.helpers -> mypackageutilshelpers
        - mypackage.__version__ -> mypackage__version__
        """
        return full_name.replace(".", "").lower()

    def get_page_for_item(self, full_name: str) -> str:
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

    def are_on_same_page(self, item1_name: str, item2_name: str) -> bool:
        """Determine if two items are rendered on the same page."""
        item1 = self.get_item(item1_name)
        item2 = self.get_item(item2_name)

        if not item1 or not item2:
            return False

        # Each item type gets its own page, except for direct children
        item1_page = self.get_page_for_item(item1_name)
        item2_page = self.get_page_for_item(item2_name)

        return item1_page == item2_page

    def get_cross_reference_link(
        self, target_name: str, display_name: str | None = None, current_page: str | None = None
    ) -> str:
        """Generate cross-reference link to another documented object."""
        # Check if target exists in our database
        target_item = self.get_item(target_name)
        if target_item is None:
            # Return plain text if target not found
            return f"`{display_name or target_name}`"

        link_text = display_name or target_name.split(".")[-1]
        anchor_id = self.generate_anchor_id(target_name)

        # Determine if target is on same page as current page
        if current_page and self.are_on_same_page(target_name, current_page):
            # Same page - use anchor link only
            return f"[`{link_text}`](#{anchor_id})"
        else:
            # Different page - use cross-page link
            target_page = self.get_page_for_item(target_name)
            target_page_path = self.generate_file_path(target_page)
            return f"[`{link_text}`]({target_page_path}#{anchor_id})"

    def format_code_block_with_links(
        self,
        code: str,
        language: str = "python",
        current_page: str | None = None,
        current_item: str | None = None,
    ) -> str:
        """Format code block with deep linking using CodeBlock component.

        Extracts full dotted paths (e.g., mypackage.utils.helpers.MyClass) from the code
        and creates direct links to them - only when there are actual documented types to link to.

        Simple type annotations like 'input_key: str' won't generate links since 'str' is a built-in.
        Items won't link to themselves (e.g., class name in its own signature).
        """
        links = {}

        # Pattern to match Python dotted paths (e.g., mypackage.utils.helpers.MyClass)
        # Must start with a word boundary and consist of identifiers separated by dots
        dotted_path_pattern = r"\b([a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)+)\b"

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
                if current_page and self.are_on_same_page(full_path, current_page):
                    # Same page - use anchor-only link
                    anchor_id = self.generate_anchor_id(full_path)
                    links[full_path] = f"#{anchor_id}"
                else:
                    # Different page - use slug-based cross-page link
                    page_name = self.get_page_for_item(full_path)
                    page_slug = self.generate_slug(page_name)
                    anchor_id = self.generate_anchor_id(full_path)
                    links[full_path] = f"{page_slug}#{anchor_id}"

        # Only generate CodeBlock component if we found linkable types
        # Simple annotations like 'input_key: str' won't have links (str is built-in)
        if links:
            links_json = ", ".join(f'"{k}": "{v}"' for k, v in links.items())
            return f"<CodeBlock\n  links={{{{{links_json}}}}}\n>\n\n```{language}\n{code}\n```\n\n</CodeBlock>"
        else:
            # No linkable types found - use simple code block
            return f"```{language}\n{code}\n```"
