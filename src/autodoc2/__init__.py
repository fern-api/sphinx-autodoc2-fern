"""Generate Fern documentation from Python packages using static analysis.

A simplified fork of sphinx-autodoc2 focused purely on Python → Fern markdown output.
"""

import subprocess
import os

def _get_version():
    """Get version from git tag or fallback to default."""
    try:
        if os.path.exists('.git'):
            result = subprocess.run(
                ['git', 'describe', '--tags', '--exact-match', 'HEAD'],
                capture_output=True, text=True, check=True
            )
            version = result.stdout.strip()
            return version[1:] if version.startswith('v') else version
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    # Fallback version for development
    return "0.1.2-dev"

__version__ = _get_version()
