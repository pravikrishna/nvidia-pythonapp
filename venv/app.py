from openai import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

completion = client.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",
    messages=[{"role": "user", "content": "list the SUV cars in India."}],
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
    stream=True
)

# for chunk in completion:
#  if chunk.choices[0].delta.content is not None:
#   print(chunk.choices[0].delta.content, end="")

client = ChatNVIDIA(
    model="meta/llama-3.1-8b-instruct",
    api_key="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",
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
)
prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful AI assistant named Fred."), ("user", "{input}")]
)


def handle_conversion():
    context = ""
    print("Welcome to the Chatbot. enter 'exit' to exit the chatbot")
    while True:
        user_input = input("\nYou: ")
        if user_input == "exit":
            break
        chain = prompt | client | StrOutputParser()

        for txt in chain.stream({"input": user_input}):
            context += f"\nUser: {user_input}\n AI :{str(txt)}"
            print(txt, end="")


if __name__ == "__main__":
    handle_conversion()




