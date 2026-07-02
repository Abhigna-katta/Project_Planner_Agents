import os
from pathlib import Path


def write_output_tool(agent_name: str, content: str) -> dict:
    """Write agent output to a dedicated outputs file.

    Args:
        agent_name (str): The name of the agent generating the content.
        content (str): The complete generated output to save.

    Returns:
        dict: Success status and file path details.
    """
    repo_root = Path(__file__).resolve().parent
    output_dir = repo_root / ".." / "outputs"
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{agent_name}_output.txt"
    output_path.write_text(content, encoding="utf-8")

    return {
        "status": "success",
        "file": str(output_path),
        "message": f"Saved output to {output_path}"
    }
