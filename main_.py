from fasthtml.fastapp import *
from dotenv import load_dotenv
import os
import openai
from crewai import Crew, Process
from agents import linkedin_agent
from tasks import linkedin_post_task

# Load environment variables and set up OpenAI API key
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app, rt = fast_app()

@rt("/")
def get():
    # Define the crew with the agent and task
    crew = Crew(
        agents=[linkedin_agent],
        tasks=[linkedin_post_task],
        process=Process.sequential,
        verbose=True
    )

    # Run the crew with the input content
    try:
        result = crew.kickoff(inputs={'content': 'Announcing our new AI-powered content generation tool!'})
    except Exception as e:
        result = f"An error occurred: {e}"

    return Titled("Agent", 
        Main(
            H1("Welcome to Agent"),
            P("This is a minimal FastHTML web app for the Agent project."),
            H1("Crew Result:"),
            P(result),
            cls="container"
        )
    )

serve()