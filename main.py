from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


def manage_conversation():
    context = ''
    print("\n\nYou are Chatting with the Llama3.1\n Type Bye to quit.\n\n\n")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ('exit', 'bye', 'quit'):
            break

        res = chain.invoke({"context": context, "text": user_input})

        context+=f"\nUser:{user_input}\nAI Response:{res}"

        print("\nAI Bot: ",res)



template = """
    Reply to the below text.

    This is the conversation history: {context}

    Text: {text}

    Answer: 
"""

model  = OllamaLLM(model='llama3.1')
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


if __name__ == '__main__':
    manage_conversation()