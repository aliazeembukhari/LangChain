from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)

outline_prompt = ChatPromptTemplate.from_template("Create a short outline for the lecture in the: {topic}")

lecture_prompt = ChatPromptTemplate.from_template("Create a detailed lecture using this outline: \n{outline}")

outline_chain = outline_prompt | llm
lecture_chain = lecture_prompt | llm

topic = 'LangChain Chains'
outline = outline_chain.invoke({'topic': topic}).content

lecture = lecture_chain.invoke({'outline': outline}).content
print("outline: \n",outline)
print("\nLecture: \n", lecture)