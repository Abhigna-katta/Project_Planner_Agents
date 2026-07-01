import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file

sprint_planner_agent = LlmAgent(
    name="sprint_planner_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/sprint_planner/instruction.txt"),
    description=load_instructions_file("agents/sprint_planner/description.txt"),
    output_key="sprint_plan_output"
)
