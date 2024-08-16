from openai import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA

import streamlit as st
st.title("🦜🔗 Praveen build his first App")



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
def generate_response(input_text):

    chain = prompt | client | StrOutputParser()
    context = ""
    for txt in chain.stream({"input": input_text}):
        context += str(txt)
    st.info(context)



def handle_conversion():

    with st.form("my_form"):
        text = st.text_area(
            "Enter text:",
            "Your query here!!!",
        )
        submitted = st.form_submit_button("Submit")
        if submitted:
            generate_response(text)


if __name__ == "__main__":
    handle_conversion()