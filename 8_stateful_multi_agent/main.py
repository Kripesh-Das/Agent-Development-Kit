import asyncio

from customer_service_agent.agent import customer_service_agent
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from utils import add_user_query_to_history, call_agent_async

load_dotenv()

session_service = InMemorySessionService()

initial_state = {
    "username": "Kripesh Das",
    "purchased_courses": [],
    "interaction_istory": [],
    
}

async def main_async():
    
    app_name = "Customer Service Agent"
    user_id = "itskripesh"
    
    new_session = session_service.create_session(
        app_name = app_name,
        user_id = user_id,
        state = initial_state,
    )
    
    session_id = new_session.id
    print(f"Created Session ID:{session_id}")
    
    runner = Runner(
        agent = customer_service_agent,
        app_name = app_name,
        session_service = session_service,
    )
    
    print("\nWELCOME TO THE CUSTOMER SERVICE CHAT")
    print("Type EXIT to end the chat if you want to\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Thank You for having a conversation !!!")
            break
        
        add_user_query_to_history(session_service,app_name,user_id,session_id,user_input)
        
        await call_agent_async(runner,user_id,session_id,user_input)
        
    
    final_session = session_service.get_session(
        app_name = app_name,
        user_id = user_id,
        session_id = session_id,
        )
    
    
    print("\nFinal Session State:")
    for key, value in final_session.state.items():
        print(f"{key}: {value}")
    
        
    def main():
        asyncio.run(main_async())
    
        
    if __name__ == "__main__":
        main()
        
        
        