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

def huggingface_summary(text, kw_num):
    result = summarizer(text)
    summary = result[0]["summary_text"]
    keywords = kw_model.extract_keywords(text, top_n=kw_num)
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