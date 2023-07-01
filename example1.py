## Integrate code to openAI
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key


# streamlit framework

st.title("Langchain demo with OpenAI")
input_text=st.text_input("Search for any topic you want")

# Prompt Templates 

First_input_prompt=PromptTemplate(
    
    input_variables=["name"],
    template="Tell me about {name}"
)



# OpenAI LLMS
llm=OpenAI(temperature=0.8)
chain=LLMChain(llm=llm,prompt=First_input_prompt,verbose=True)

if input_text:
    st.write(chain.run(input_text))