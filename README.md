# Smart Study & Homework Summarizer

Upload a long article or textbook chapter and get a concise summary plus a list of key vocabulary terms.

## Features

- Two backends: free (local Hugging Face distilBART + KeyBERT) or paid (OpenAI GPT-4o-mini)
- Toggle between backends in the UI
- Handles long texts by automatically chunking and summarizing in passes
- Upload .txt or .pdf files, or paste text directly
- Configurable number of keywords to extract

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For the paid version, create a `.env` file:
```
OPENAI_API_KEY=your-key-here
```

Note: use `transformers<5` in requirements.txt (v5 removed the summarization pipeline).

## Usage

Run the web interface:
```bash
streamlit run app.py
```

Or test from the command line:
```bash
python test_summarizer.py
```

## Requirements

- Python 3.10+
- See requirements.txt for dependencies
