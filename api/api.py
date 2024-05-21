from langchain_community.llms import Ollama

from fastapi import FastAPI

app = FastAPI()


@app.get("/basic/chat")
def basic_chat(input_text:str):
    llm = Ollama(model="llama3:8b-instruct-q4_K_M")
    return llm.invoke(input_text)

