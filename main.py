from langchain_ollama import OllamaLLM     #importing ollamaLLM into code
from langchain_core.prompts import ChatPromptTemplate # langchain used to deal with llms and its responces

template = """                             
answer the question below.

Here is the coversation history : {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model="gemma3:4b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 
def handle_conversation():
    context = "" 
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context":context, "question":user_input})
        print("bot :", result)
    context += f"\nUser : {user_input}\nAi : {result}"   #for updating conv history
    

   

if __name__ == "__main__":
    handle_conversation()

