#!/usr/bin/env python3
"""
Simple CLI wrapper for generating Fern documentation using autodoc2's built-in CLI.

Usage:
    python fern_cli.py /path/to/repo [--output /path/to/output] [--module module_name]
    
This is a simpler alternative to batch_fern_docs.py for single repositories.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Generate Fern-compatible documentation using autodoc2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Process nemo-rl repository
    python fern_cli.py /tmp/nemo-rl --output /tmp/nemo-rl-docs --module nemo_rl
    
    # Auto-detect module name and use default output
    python fern_cli.py ~/code/my-package
    
    # Process with verbose output
    python fern_cli.py /path/to/repo --verbose
        """
    )
    
    parser.add_argument("repo_path", type=Path, help="Path to the repository to process")
    parser.add_argument("--output", "-o", type=Path, help="Output directory (default: {repo}/fern_docs)")
    parser.add_argument("--module", "-m", type=str, help="Module name (auto-detected if not provided)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show verbose output")
    parser.add_argument("--clean", "-c", action="store_true", help="Clean output directory first")
    
    args = parser.parse_args()
    
    # Resolve repo path
    repo_path = args.repo_path.expanduser().resolve()
    if not repo_path.exists():
        print(f"ERROR: Repository path does not exist: {repo_path}")
        return 1
    
    # Determine output directory
    output_dir = args.output
    if output_dir is None:
        output_dir = repo_path / "fern_docs"
    else:
        output_dir = output_dir.expanduser().resolve()
    
    # Determine module name
    module_name = args.module
    if module_name is None:
        # Look for Python packages in the repo
        package_dirs = [
            d for d in repo_path.iterdir() 
            if d.is_dir() and (d / "__init__.py").exists()
        ]
        if package_dirs:
            module_name = package_dirs[0].name
            print(f"Auto-detected module: {module_name}")
        else:
            module_name = repo_path.name
            print(f"No Python packages found, using repo name: {module_name}")
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    if args.clean and output_dir.exists():
        import shutil
        shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True)
    
    # Set up environment to use our FernRenderer
    env = os.environ.copy()
    autodoc2_src = Path(__file__).parent / "src"
    if "PYTHONPATH" in env:
        env["PYTHONPATH"] = f"{autodoc2_src}:{env['PYTHONPATH']}"
    else:
        env["PYTHONPATH"] = str(autodoc2_src)
    
    # Build the autodoc2 command
    cmd = [
        sys.executable, "-m", "autodoc2.cli", "write",
        str(repo_path),
        "--output", str(output_dir),
        "--module", module_name,
    ]
    
    if args.clean:
        cmd.append("--clean")
    
    print(f"🔄 Processing: {repo_path}")
    print(f"📁 Output: {output_dir}")  
    print(f"📦 Module: {module_name}")
    print(f"🔧 Command: {' '.join(cmd)}")
    print()
    
    # Unfortunately, the current autodoc2 CLI doesn't support specifying renderer
    # So we need to create a temporary config or modify the approach
    print("⚠️  NOTE: This uses the default renderer (MyST).")
    print("   For Fern output, use batch_fern_docs.py instead.")
    print("   Running with MyST renderer...")
    print()
    
    # Run the command
    try:
        result = subprocess.run(cmd, env=env, capture_output=not args.verbose)
        
        if result.returncode == 0:
            print("✅ Documentation generated successfully!")
            print(f"📂 Output directory: {output_dir}")
            
            # List generated files
            if output_dir.exists():
                md_files = list(output_dir.glob("**/*.md"))
                rst_files = list(output_dir.glob("**/*.rst"))
                all_files = md_files + rst_files
                
                if all_files:
                    print(f"📄 Generated {len(all_files)} files:")
                    for file in sorted(all_files):
                        rel_path = file.relative_to(output_dir)
                        print(f"   - {rel_path}")
                else:
                    print("⚠️  No documentation files found in output directory")
            
            return 0
        else:
            print("❌ Documentation generation failed!")
            if result.stderr:
                print("Error output:")
                print(result.stderr.decode())
            return 1
            
    except FileNotFoundError:
        print("❌ autodoc2 CLI not found. Make sure autodoc2 is installed.")
        print("   Try: pip install -e .")
        return 1
    except KeyboardInterrupt:
        print("\n⏹️ Cancelled by user")
        return 1


if __name__ == "__main__":
    sys.exit(main())
