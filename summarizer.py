# ABOUTME: A small project that is supposed to summarize given text, output as summary + vocabulary
# ABOUTME: Two possibilities for the user, free and paid version
from transformers import pipeline
from keybert import KeyBERT
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
kw_model = KeyBERT()
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def text_splitter(text):
    sentences = text.split(". ")
    split_text = []
    current_chunk = ""

    for s in sentences:
        if len(current_chunk) + len(s) > 900:
            split_text.append(current_chunk)
            current_chunk = s
        else:
            current_chunk += ". " + s
    
    split_text.append(current_chunk)
    return split_text

def huggingface_summary(text, kw_num):
    original_text = text
    while len(text) > 1400:
        split_text = text_splitter(text)
        to_summarize = []
        for i in split_text:
            to_summarize.append(summarizer(i, truncation=True)[0]["summary_text"])
        text = " ".join(to_summarize)
    
    result = summarizer(text, truncation=True)
    summary = result[0]["summary_text"]

    keywords = kw_model.extract_keywords(original_text, top_n=kw_num)
    top10_kw = [kw[0] for kw in keywords]
    return {"summary": summary, "vocabulary": top10_kw}

def openai_summary(text, kw_num):
    client = OpenAI()
    prompt =(f"Summarize this text and give the top {kw_num} keywords. "
          f"Respond with JSON only: {{\"summary\": \"...\", \"vocabulary\": [\"word1\", \"word2\"]}}"
          f"\n\nText:\n{text}")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    answer = response.choices[0].message.content
    return json.loads(answer)

def summarize(text, kw_num, paid=False):
    if paid:
        return openai_summary(text, kw_num)
    else:
        return huggingface_summary(text, kw_num)
