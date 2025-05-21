import asyncio
from dotenv import load_dotenv
load_dotenv()

from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from memory_agent.agent import memory_agent
from utils import call_agent_async

db_url = "sqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)

initial_state = {
    "user_name": "Kripesh Das",
    "reminders": [],
}

async def main_async():
    
    app_name = "Memory Agent"
    user_id = "krip3sh"
    
    existing_sessions = session_service.list_sessions(
        app_name = app_name,
        user_id = user_id,
        )
    
    if existing_sessions and len(existing_sessions.sessions) > 0:
        
        session_id = existing_sessions.sessions[0].session_id
        print(f"Continuing existing session: {session_id}")

    else:
        new_session = session_service.create_session(
            app_name = app_name,
            user_id = user_id,
            state = initial_state,
        )
        
        session_id = new_session.id
        print(f"Created new session: {session_id}")
        
        
        
    runner = Runner(
        agent = memory_agent,
        app_name = app_name,
        session_service = session_service,
    )
    
    
    print("\nWelcome to Memory Agent Chat!")
    print("Your reminders will be remembered across conversations.")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    while True:
        
        user_input = input("You:")
        if user_input.lower() in ["exit","quit"]:
            print("Ending conversation. Your data has been saved to the database.")
            break
        
        await call_agent_async(runner,user_id,session_id,user_input)



if __name__ == "__main__":
    asyncio.run(main_async())