import streamlit as st
from openai import OpenAI
import os

### Load your API Key
my_secret_key = st.secret.get['MyOpenAIKey']
os.environ["OPENAI_API_KEY"] = my_secret_key

### Request the answer to the question "Damascus is a"
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": "Damascus is a"}
  ],
  seed = BUID,
  n=10,
  max_tokens=20
)

### Print all 10 completions:
for i in range(10):
    st.write(response.choices[i].message.content)
  ##print(response.choices[i].message.content)
    
st.title("🎈 My latest app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
