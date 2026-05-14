from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[TavilyTools()],
)

agent.print_response("Use suas ferramentas para ver a temperatura hoje em Juiz de Fora-MG")
