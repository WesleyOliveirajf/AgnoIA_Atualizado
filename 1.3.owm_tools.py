import os
from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
# from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat

def celsius_to_fh (temperatura_celsius: float):
  """
    converta uma temperatura em graus Celsius para Fahrenheit.
    
    Args: 
        temperatura_celsius (float): temperatura em graus Celsius
    
    return:
        float: Temperatura convertida em graus Fahrenheit
  
  """
  return(temperatura_celsius* 9/5) + 32
    

agent = Agent(
   # model=Groq(id="llama-3.3-70b-versatile"),
  model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        TavilyTools(),
        celsius_to_fh,
        ],
)

agent.print_response("Use suas ferramentas para ver a temperatura hoje em Juiz de Fora-MG")
