import os
import sys
from google.adk.agents import SequentialAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from agents.task_generator.agent import task_generator_agent
from agents.sprint_planner.agent import sprint_planner_agent
from agents.risk_estimator.agent import risk_estimator_agent

root_agent = SequentialAgent(
    name="root_project_planner_agent",
    sub_agents=[task_generator_agent, sprint_planner_agent, risk_estimator_agent],
    description=load_instructions_file("agents/Root_project_planner/description.txt")
)
