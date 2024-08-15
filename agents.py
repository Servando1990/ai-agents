from crewai import Agent



# Define a simple LinkedIn content creation agent
linkedin_agent = Agent(
    role="LinkedIn Content Creator",
    goal="Create a professional LinkedIn post based on provided input",
    backstory="You are skilled at crafting engaging and professional LinkedIn posts that resonate with audiences."
)
