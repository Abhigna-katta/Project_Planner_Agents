import datetime
from pathlib import Path


def write_report_to_file(content: str) -> dict:
    """
    Writes the project plan report (tasks, sprints, risks) to a timestamped Markdown file.

    Args:
        content (str): Full Markdown report content to be saved to disk.

    Returns:
        dict: A dictionary containing the status and generated filename.
    """
    repo_root = Path(__file__).resolve().parent.parent
    output_dir = repo_root / "output"
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    output_path = output_dir / f"{timestamp}_project_plan.md"
    output_path.write_text(content, encoding="utf-8")

    return {
        "status": "success",
        "file": str(output_path)
    }
