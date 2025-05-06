from google.adk.agents import Agent

root_agent = Agent(
		name="greeting_agent",
		description="A simple agent that greets the user.",
		model="gemini-2.0-flash",
		instruction="""
		You are a helpful assistant. Your task is to greet the user and ask how you can assist them.
		Ask for their name and greeet them by name.
		""",
)