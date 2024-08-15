from crewai import Task
from agents import linkedin_agent
# Define a task for creating a LinkedIn post
linkedin_post_task = Task(
    description=(
        "Create a LinkedIn post based on the following input: '{content}'."
        "Ensure the post is professional, engaging, and optimized for LinkedIn's audience."
        "Include relevant hashtags and a call-to-action."
    ),
    expected_output="A LinkedIn post ready to be copied and pasted, including hashtags and a call-to-action.",
    agent=linkedin_agent,
)