import streamlit as st
from summarizer import summarize

st.title("Summarizer")
kw_amount = st.number_input("Change keyword amount", min_value = 1, max_value = 100, value=10)
st.write(f"Current amount is {kw_amount}")
uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf"])
text_input = st.text_area("Or paste your text here", disabled=(uploaded_file is not None))
paid_ver = st.toggle("Enable paid")

if uploaded_file is not None:
    if uploaded_file.name.endswith(".txt"):
        text_input = uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith(".pdf"):
        from PyPDF2 import PdfReader
        reader = PdfReader(uploaded_file)
        text_input = ""
        for i in reader.pages:
            text_input += i.extract_text()

if paid_ver:
    st.write("Currently using OpenAI tokens.")
else:
    st.write("Currently using free version.")

has_input = (uploaded_file is not None) or text_input

if st.button("summarize", type="primary", disabled=(not has_input)):
    with st.spinner("Summarizing..."):
        result = summarize(text_input, kw_amount, paid_ver)
    
    st.subheader("Summary")
    st.write(result["summary"])

    st.subheader("Vocabulary")
    for word in result["vocabulary"]:
        st.write(f"- {word}")
