import os
import random
from dotenv import load_dotenv

load_dotenv()
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
  model="",
  api_key=os.getenv("ROUTER_KEY"),
)
    

def get_dad_joke(): 
  jokes = ["","",""]
  
  return random.choices(jokes)

root_agent = Agent(
  name = "joke_agent",
  model = model,
  description = "Dad Joke Agent",
  instruction = "You are an assistant that tells dad joke via the help of the custom get_dad_joke func"
  )