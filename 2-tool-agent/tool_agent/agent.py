from google.adk.agents import Agent
from google.adk.tools import google_search

from tool_agent.tools import get_current_time

root_agent = Agent(
		name="tool_agent",
		description="A simple agent that uses Google search.",
		model="gemini-2.0-flash",
		instruction="""
		You are a helpful assistant that can use the following tools:
		- google_search
		""",
		tools=[google_search],
)