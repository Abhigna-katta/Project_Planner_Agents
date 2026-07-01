import os
from pathlib import Path


def _resolve_repo_path(filename: str) -> Path:
    """Resolve a path relative to the repository root when possible."""
    path = Path(filename)
    if path.is_absolute():
        return path

    repo_root = Path(__file__).resolve().parent.parent
    candidate = repo_root / path
    if candidate.exists():
        return candidate

    return path


def load_instructions_file(filename: str, default: str = "") -> str:
    """
    Loads instruction or description text from a given file path.

    Args:
        filename (str): Path to the file to read (relative or absolute).
        default (str): Default string to return if the file is not found or fails to load.

    Returns:
        str: The file contents if successful, or the fallback default string.
    """
    try:
        resolved_path = _resolve_repo_path(filename)
        with open(resolved_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[WARNING] File not found: {filename}. Using default.")
    except Exception as e:
        print(f"[ERROR] Failed to load {filename}: {e}")
    return default
