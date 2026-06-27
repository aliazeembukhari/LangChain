from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")
result = llm.invoke("Which is the National Animal of Pakistan")
print(result.content)

print()

result2 = llm.invoke("Name the colors in Rainbow")
print(result2.content)