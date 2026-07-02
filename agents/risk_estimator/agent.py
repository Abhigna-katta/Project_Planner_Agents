import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from utils.write_output_tool import write_output_tool

risk_estimator_agent = LlmAgent(
    name="risk_estimator_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/risk_estimator/instruction.txt"),
    description=load_instructions_file("agents/risk_estimator/description.txt"),
    tools=[write_output_tool],
    output_key="risk_estimation_output"
)


