import os

import streamlit as st
from streamlit import set_page_config
from langchain.llm import OpenAI



#os.environ['OPENAI_API_key']=apikey
st.title('Lesson Plan gpt creator')

prompt= st.text_input('Enter the grade')

prompt= st.text_input('Enter the course/ subject')
prompt= st.text_input('specific board if any')

llm= OpenAI(temperature=0.9)
if prompt:
  response=llm(prompt)
  st.write(response)
