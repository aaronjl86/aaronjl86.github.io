# LawBot 10X

A significantly upgraded Streamlit legal-information assistant focused on:

- **Knowledge retrieval (RAG-style)** from a structured legal knowledge pack.
- **Jurisdiction-aware ranking** so answers prefer relevant state/federal context.
- **Risk signal detection** (deadlines, housing, employment, criminal indicators).
- **Draft Builder** for common legal communication templates.
- **Outcome Comparator** to compare two legal strategy options.
- **Source transparency** with surfaced authorities and knowledge entries.

> ⚠️ LawBot provides legal information, **not legal advice**.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py --server.port 8501
```

Then open: <http://localhost:8501>

## Files

- `app.py` — Main Streamlit application.
- `lawbot_knowledge.json` — Structured legal knowledge entries.
- `requirements.txt` — Runtime dependencies.
