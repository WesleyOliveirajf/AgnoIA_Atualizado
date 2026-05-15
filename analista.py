from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
import os

from dotenv import load_dotenv
load_dotenv()


# Inicializa banco de dados SQLite para armazenar histórico
db = SqliteDb(db_file="tmp/data.db")

# Cria agente financeiro para análise de cotações de ações
agent = Agent(
    name="analista_financeiro",
    model=OpenAIChat(id="gpt-5-nano", api_key=os.getenv("OPENAI_API_KEY")),
    tools=[YFinanceTools()],
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto.",
    db=db,
    add_history_to_context=True,
    num_history_runs=3
)
# Carrega as variáveis de ambiente do arquivo .env
# Já feito acima com load_dotenv(), então nada extra é necessário aqui

# Inicializa o banco de dados SQLite definindo o arquivo como "tmp/data.db"
# (Já feito logo acima com db = SqliteDb(db_file="tmp/data.db"))

# Cria o agente financeiro para análise das cotações de ações
# (Já feito acima na criação do objeto agent)

# Fim da configuração inicial. O agente está pronto para responder perguntas sobre ações!


agent.print_response("Qual é a cotação da Petrobras usando o símbolo PETR4.SA?")
agent.print_response("Qual é a cotação da Vale usando o símbolo VALE3.SA?")
agent.print_response("Quais empresas já consultamos a cotação?")