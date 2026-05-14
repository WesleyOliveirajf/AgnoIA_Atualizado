# from agno.models.openai import OpenAI
from agno.models.groq import Groq
from agno.models.message import Message

from dotenv import load_dotenv

load_dotenv() 
model = Groq(id="llama-3.3-70b-versatile")

msg = Message(
    role="user",
    content=[{"type": "text", "text": "Olá Meu nome e Wesley"}]
)

assistant_message = Message(role="assistant", content="")

response = model.invoke(messages=[msg], assistant_message=assistant_message)
print(response.content)


