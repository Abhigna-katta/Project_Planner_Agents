import asyncio
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils.file_loader import load_instructions_file
from utils.write_output_tool import write_output_tool


class SequentialAgentsPathTests(unittest.TestCase):
    def test_load_instructions_file_supports_repo_relative_paths(self):
        content = load_instructions_file("agents/task_generator/instruction.txt")

        self.assertIn("Task Generator Agent", content)
        self.assertIn("Your output will be consumed by the next agent", content)

    def test_write_output_tool_uses_repo_outputs_directory(self):
        temp_dir = tempfile.mkdtemp()
        previous_cwd = os.getcwd()
        os.chdir(temp_dir)

        try:
            with patch("pathlib.Path.write_text") as mocked_write_text:
                result = write_output_tool("test_agent", "# test report")

            mocked_write_text.assert_called_once()
        finally:
            os.chdir(previous_cwd)

        output_path = Path(result["file"])
        self.assertIn("outputs", str(output_path))
        self.assertTrue(str(output_path).endswith("test_agent_output.txt"))

    def test_risk_estimator_agent_includes_write_output_tool(self):
        from agents.risk_estimator.agent import risk_estimator_agent

        tools = asyncio.run(risk_estimator_agent.canonical_tools(None))
        tool_names = {tool.name for tool in tools}

        self.assertIn("write_output_tool", tool_names)


if __name__ == "__main__":
    unittest.main()
