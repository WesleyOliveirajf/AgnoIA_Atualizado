import os
from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat

agent = Agent(
    name="teste_cotacao",
    model=OpenAIChat(id="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")),
    tools=[YFinanceTools()],
    instructions="Retorne apenas a tabela com a cotação",
    add_history_to_context=False,
)

# Teste com símbolo correto
print("=== Testando PETR4.SA ===")
agent.print_response("Qual é a cotação atual de PETR4.SA?")

print("\n=== Testando VALE3.SA ===")
agent.print_response("Qual é a cotação atual de VALE3.SA?")
