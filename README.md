# Smart Study & Homework Summarizer

Upload a long article or textbook chapter and get a concise summary plus a list of key vocabulary terms.

Supports two backends:
- Free: runs locally using Hugging Face (distilBART + KeyBERT)
- Paid: uses OpenAI API (GPT-4o-mini)

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
