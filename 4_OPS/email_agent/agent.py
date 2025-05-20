from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()

# -----OUTPUT SCHEMA------
class EmailContent(BaseModel):
    
    subject: str = Field(
      description = "This is the subject line. Should be concise and descriptive"
    )
    
    body: str = Field(
      description = "The main content of the email body should be here with good amounts of paras and formatting punctuations, greetings and signatures"
    )  
 

root_agent = LlmAgent(
  
  name = "email_agent",
  model = "gemini-2.0-flash",
  instruction = """
  
                You are an email generation assistant.
                Your task is to generate a professional email with respective to the users request,
                
                GUIDELINES:
                1. Create an appropriate subject line which is concise and to the point
                2. Write a well structured email body while keeping in mind
                  *Professional Greeting 
                  *Clear concise main content
                  *Appropriate Closing 
                  *Your name as signature
                3. Suggest relevant attachments if required (else keep it an empty list)
                4. Email tone should be match the purpose(e.g. formal, friendly, professional)
                
                **************************************************************
                
                IMPORTANT All the outputs should be in JSON matching this structure:
                {
                  "subject": "Subject line should be here",
                  "body": "Email's body with proper paras and formatting",
                }
                
                NOTE: No useless explanations or additional text outside the JSON format
                
                """,
                
  description = "Generate professional emails with structured subject and body",
  output_schema = EmailContent,
  output_key = "email",
  
  
  )

