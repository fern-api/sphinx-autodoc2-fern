"""Generate Fern documentation from Python packages using static analysis.

A simplified fork of sphinx-autodoc2 focused purely on Python → Fern markdown output.
"""

import subprocess
import sys
from pathlib import Path

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata  # type: ignore


def _get_version() -> str:
    """Get version from package metadata, git tag, or fallback to default."""
    # Try package metadata first (works for installed packages)
    try:
        return metadata.version("py2fern")
    except metadata.PackageNotFoundError:
        pass

    # Try git tags (works for development from git repo)
    try:
        if Path(".git").exists():
            result = subprocess.run(
                ["git", "describe", "--tags", "--exact-match", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
            )
            version = result.stdout.strip()
            return version[1:] if version.startswith("v") else version
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # Fallback version for development
    return "0.1.2-dev"


__version__ = _get_version()
