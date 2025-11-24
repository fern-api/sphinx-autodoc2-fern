"""Navigation YAML generation for Fern renderer.

DEPRECATED: This module is planned for deprecation and will be removed in a future version.
The navigation generation functionality may be replaced or removed entirely.

This module handles generation of navigation.yml files for Fern documentation,
following sphinx autodoc2 toctree logic.
"""

from __future__ import annotations

import typing as t
import warnings

import yaml

if t.TYPE_CHECKING:
    from autodoc2.utils import ItemData


warnings.warn(
    "fern_navigation module is deprecated and will be removed in a future version",
    DeprecationWarning,
    stacklevel=2,
)


class NavigationGenerator:
    """Generates navigation YAML for Fern docs.yml.

    DEPRECATED: This class and its methods are planned for removal.
    """

    def __init__(
        self,
        get_by_type_fn: t.Callable[[str], t.Iterable[ItemData]],
        get_children_fn: t.Callable[[ItemData, set[str] | None], t.Iterable[ItemData]],
        generate_file_path_fn: t.Callable[[str], str],
        extension: str = ".mdx",
    ):
        """Initialize the navigation generator.

        Args:
            get_by_type_fn: Function to get items by type from database
            get_children_fn: Function to get children of an item
            generate_file_path_fn: Function to generate file paths
            extension: File extension for generated files
        """
        self.get_by_type = get_by_type_fn
        self.get_children = get_children_fn
        self.generate_file_path = generate_file_path_fn
        self.extension = extension

    def generate_navigation_yaml(self) -> str:
        """Generate navigation YAML for Fern docs.yml following sphinx autodoc2 toctree logic.

        DEPRECATED: This method will be removed in a future version.
        """
        # Find root packages (no dots in name)
        root_packages = []
        for item in self.get_by_type("package"):
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
        """Build navigation item recursively following sphinx autodoc2 toctree logic.

        DEPRECATED: This method will be removed in a future version.
        """
        full_name = item["full_name"]
        file_path = self.generate_file_path(full_name)

        # Get children (same logic as sphinx toctrees)
        subpackages = list(self.get_children(item, {"package"}))
        submodules = list(self.get_children(item, {"module"}))

        if subpackages or submodules:
            # This has children - make it a section with skip-slug
            section_item = {
                "section": full_name.split(".")[-1],  # Use short name for section
                "skip-slug": True,
                "path": f"{file_path}{self.extension}",
                "contents": [],
            }

            # Add subpackages recursively (maxdepth: 3 like sphinx)
            for child in sorted(subpackages, key=lambda x: x["full_name"]):
                child_nav = self._build_nav_item_recursive(child)
                if child_nav:
                    section_item["contents"].append(child_nav)

            # Add submodules as pages (maxdepth: 1 like sphinx)
            for child in sorted(submodules, key=lambda x: x["full_name"]):
                child_file_path = self.generate_file_path(child["full_name"])
                section_item["contents"].append(
                    {
                        "page": child["full_name"].split(".")[-1],  # Use short name
                        "path": f"{child_file_path}{self.extension}",
                    }
                )

            return section_item
        else:
            # Leaf item - just a page
            return {
                "page": full_name.split(".")[-1],  # Use short name
                "path": f"{file_path}{self.extension}",
            }
