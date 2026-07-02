import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from utils.write_output_tool import write_output_tool

task_generator_agent = LlmAgent(
    name="task_generator_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/task_generator/instruction.txt"),
    description=load_instructions_file("agents/task_generator/description.txt"),
    tools=[write_output_tool],
    output_key="task_list_output"
)
