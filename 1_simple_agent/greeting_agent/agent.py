from google.adk.agents import Agent

from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    name = "greeting_agent",
    model = "",
    description = "Greeting Agent",
    instruction = """
                    You are a helpful assistant that greets the user first,
                    after inquiring the name from the user
                  """,
    )