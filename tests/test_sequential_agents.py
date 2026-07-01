import asyncio
import os
import tempfile
import unittest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_report_to_file


class SequentialAgentsPathTests(unittest.TestCase):
    def test_load_instructions_file_supports_repo_relative_paths(self):
        content = load_instructions_file("agents/task_generator/instruction.txt")

        self.assertIn("Task Generator Agent", content)
        self.assertIn("Your output will be consumed by the next agent", content)

    def test_write_report_to_file_uses_repo_output_directory(self):
        temp_dir = tempfile.mkdtemp()
        previous_cwd = os.getcwd()
        os.chdir(temp_dir)

        try:
            result = write_report_to_file("# test report")
        finally:
            os.chdir(previous_cwd)

        output_path = Path(result["file"])
        self.assertTrue(output_path.exists())
        self.assertIn("output", str(output_path))
        output_path.unlink(missing_ok=True)

    def test_risk_estimator_agent_includes_write_report_tool(self):
        from agents.risk_estimator.agent import risk_estimator_agent

        tools = asyncio.run(risk_estimator_agent.canonical_tools(None))
        tool_names = {tool.name for tool in tools}

        self.assertIn("write_report_to_file", tool_names)


if __name__ == "__main__":
    unittest.main()
