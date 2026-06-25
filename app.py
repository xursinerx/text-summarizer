import streamlit as st
from summarizer import summarize

st.title("Summarizer")
kw_amount = st.number_input("Change keyword amount", min_value = 1, max_value = 100, value=10)
st.write(f"Current amount is {kw_amount}")
text_input = st.text_area("Paste your text here")
paid_ver = st.toggle("Enable paid")

if paid_ver:
    st.write("Currently using OpenAI tokens.")
else:
    st.write("Currently using free version.")

if st.button("summarize", type="primary", disabled=(not text_input)):
    result = summarize(text_input, kw_amount, paid_ver)
    st.write(result)