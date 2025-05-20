from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

def get_curr_time(format: str = "%Y-%m-%d %H:%M:%S") -> dict:
  """
  Get the current date and time in the format of YYYY-MM-DD and HH:MM:SS respectively
  """
  return {
    "current_time": datetime.datetime.now().strftime(format)
  }
  
  
root_agent = Agent(
    name = "tools_agent",
    model = "gemini-2.0-flash",
    description = "Tool Agent",
    instruction = """
                    You are a helpful assistant that uses the following tools:
                    1. Google_Search
                    2. Custom Tools use the get_curr_time func  
                  """,
    tools = [get_curr_time],
  # tools = [get_curr_time],
  )