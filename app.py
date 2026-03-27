import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

import streamlit as st

DATA_PATH = Path(__file__).parent / "lawbot_knowledge.json"

STOPWORDS = {
    "the",
    "a",
    "an",
    "and",
    "or",
    "to",
    "of",
    "in",
    "on",
    "for",
    "with",
    "by",
    "is",
    "are",
    "be",
    "as",
    "at",
    "that",
    "this",
    "it",
    "from",
    "your",
    "you",
    "can",
    "should",
    "will",
}

RISK_PATTERNS = {
    "deadline": r"\b(deadline|statute of limitations|within \d+ days|expires?)\b",
    "money": r"\b(damages|fine|penalty|fees?|costs?|owed|debt)\b",
    "criminal": r"\b(arrest|charge|criminal|misdemeanor|felony|probation)\b",
    "employment": r"\b(fired|terminated|retaliation|discrimination|harassment|wage)\b",
    "housing": r"\b(evict|landlord|tenant|lease|rent|security deposit)\b",
}


@dataclass
class KnowledgeDoc:
    id: str
    title: str
    jurisdiction: str
    topic: str
    summary: str
    key_points: List[str]
    citations: List[str]
    tokens: Counter


def tokenize(text: str) -> List[str]:
    words = re.findall(r"[a-zA-Z][a-zA-Z\-']+", text.lower())
    return [w for w in words if w not in STOPWORDS and len(w) > 2]


def build_index(rows: List[Dict]) -> Tuple[List[KnowledgeDoc], Dict[str, float]]:
    docs: List[KnowledgeDoc] = []
    doc_freq = Counter()

    for row in rows:
        corpus = " ".join([row["title"], row["summary"], " ".join(row["key_points"])])
        tokens = Counter(tokenize(corpus))
        docs.append(
            KnowledgeDoc(
                id=row["id"],
                title=row["title"],
                jurisdiction=row["jurisdiction"],
                topic=row["topic"],
                summary=row["summary"],
                key_points=row["key_points"],
                citations=row["citations"],
                tokens=tokens,
            )
        )
        for term in tokens:
            doc_freq[term] += 1

    n = max(len(docs), 1)
    idf = {term: math.log((n + 1) / (df + 1)) + 1 for term, df in doc_freq.items()}
    return docs, idf


def score(query: str, docs: List[KnowledgeDoc], idf: Dict[str, float], jurisdiction: str) -> List[Tuple[float, KnowledgeDoc]]:
    q_terms = Counter(tokenize(query))
    if not q_terms:
        return []

    ranked: List[Tuple[float, KnowledgeDoc]] = []
    for doc in docs:
        s = 0.0
        for term, q_count in q_terms.items():
            if term in doc.tokens:
                s += (1 + math.log(doc.tokens[term])) * idf.get(term, 1.0) * q_count

        if jurisdiction != "All" and doc.jurisdiction != jurisdiction:
            s *= 0.65
        if s > 0:
            ranked.append((s, doc))

    return sorted(ranked, key=lambda t: t[0], reverse=True)


def detect_risks(user_input: str) -> List[str]:
    findings = []
    for label, pattern in RISK_PATTERNS.items():
        if re.search(pattern, user_input.lower()):
            findings.append(label)
    return findings


def generate_answer(query: str, top_docs: List[KnowledgeDoc], mode: str, risks: List[str]) -> str:
    date_stamp = datetime.now(timezone.utc).strftime("%B %d, %Y")
    style = {
        "Concise": "Keep it brief and action-oriented.",
        "Standard": "Use practical plain language and explain each step.",
        "Deep Analysis": "Provide a structured analysis with options and tradeoffs.",
    }[mode]

    if not top_docs:
        return (
            "I couldn't find a close match in the current LawBot knowledge pack. "
            "Try adding details like jurisdiction, timeline, and key documents."
        )

    top = top_docs[0]
    bullets = "\n".join([f"- {point}" for point in top.key_points[:4]])
    risk_text = "None detected" if not risks else ", ".join(risks)

    return (
        f"As of {date_stamp}, here's a practical legal information briefing (not legal advice).\n\n"
        f"**Likely relevant area:** {top.topic} ({top.jurisdiction})\n"
        f"**Why this likely applies:** {top.summary}\n\n"
        f"**Key points to consider**\n{bullets}\n\n"
        f"**Risk flags detected from your question:** {risk_text}\n\n"
        f"**Recommended next actions**\n"
        "1. Organize documents and dates in a timeline.\n"
        "2. Preserve written evidence (emails, notices, contracts, receipts).\n"
        "3. Validate local rules with a licensed attorney or official court/self-help source.\n"
        f"4. {style}\n"
    )


def make_draft(template: str, facts: str, tone: str) -> str:
    header_map = {
        "Demand Letter": "Subject: Formal Demand and Notice",
        "Landlord Notice": "Subject: Notice Concerning Lease Compliance",
        "HR Complaint": "Subject: Workplace Complaint and Request for Investigation",
        "Small Claims Outline": "Subject: Small Claims Case Outline",
    }
    return (
        f"{header_map[template]}\n\n"
        f"Tone: {tone}\n\n"
        "To Whom It May Concern,\n\n"
        "I am writing to document the following facts and request resolution:\n"
        f"{facts.strip()}\n\n"
        "Requested resolution:\n"
        "- Confirm receipt of this notice in writing.\n"
        "- Provide a response within the applicable legal timeframe.\n"
        "- Preserve relevant records related to this matter.\n\n"
        "This letter is sent for resolution purposes and to preserve my rights.\n\n"
        "Sincerely,\n[Your Name]"
    )


def load_data() -> List[Dict]:
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    st.set_page_config(page_title="LawBot 10X", page_icon="⚖️", layout="wide")
    st.title("⚖️ LawBot 10X")
    st.caption("Advanced legal information assistant with retrieval, risk spotting, and legal drafting workflows.")

    rows = load_data()
    docs, idf = build_index(rows)
    jurisdictions = ["All"] + sorted({d.jurisdiction for d in docs})

    with st.sidebar:
        st.header("Configuration")
        jurisdiction = st.selectbox("Jurisdiction focus", jurisdictions)
        analysis_mode = st.radio("Answer depth", ["Concise", "Standard", "Deep Analysis"], index=1)
        st.markdown("---")
        st.info(
            "LawBot provides legal information, not legal advice. Always verify with licensed counsel."
        )

    ask_tab, draft_tab, compare_tab, sources_tab = st.tabs(
        ["Ask LawBot", "Draft Builder", "Outcome Compare", "Knowledge Sources"]
    )

    with ask_tab:
        user_query = st.text_area(
            "Describe your legal issue",
            placeholder="Example: My landlord kept my security deposit after I moved out in California...",
            height=140,
        )
        if st.button("Analyze", type="primary"):
            ranked = score(user_query, docs, idf, jurisdiction)
            top_docs = [d for _, d in ranked[:3]]
            risks = detect_risks(user_query)
            answer = generate_answer(user_query, top_docs, analysis_mode, risks)
            st.markdown(answer)

            if top_docs:
                with st.expander("Top retrieved references"):
                    for i, doc in enumerate(top_docs, 1):
                        st.markdown(f"**{i}. {doc.title}** ({doc.jurisdiction})")
                        for cite in doc.citations:
                            st.markdown(f"- {cite}")

    with draft_tab:
        template = st.selectbox(
            "Template",
            ["Demand Letter", "Landlord Notice", "HR Complaint", "Small Claims Outline"],
        )
        tone = st.select_slider("Tone", ["Neutral", "Firm", "Assertive"])
        facts = st.text_area("Your facts", height=180)
        if st.button("Generate Draft"):
            st.code(make_draft(template, facts, tone))

    with compare_tab:
        st.subheader("Scenario Comparator")
        col1, col2 = st.columns(2)
        with col1:
            option_a = st.text_area("Option A", height=140, placeholder="Negotiate directly with employer")
        with col2:
            option_b = st.text_area("Option B", height=140, placeholder="File agency complaint first")

        if st.button("Compare options"):
            def score_option(text: str) -> Dict[str, int]:
                t = text.lower()
                return {
                    "speed": 8 if "direct" in t or "negot" in t else 5,
                    "cost": 7 if "self" in t or "direct" in t else 4,
                    "evidence_strength": 8 if "document" in t or "written" in t else 5,
                    "enforcement": 8 if "agency" in t or "court" in t else 4,
                }

            a = score_option(option_a)
            b = score_option(option_b)
            st.write("### Weighted comparison (heuristic)")
            st.table({"Option A": a, "Option B": b})

    with sources_tab:
        st.subheader("Knowledge pack loaded")
        st.write(f"{len(docs)} legal knowledge entries available.")
        for doc in docs:
            st.markdown(f"- **{doc.title}** — {doc.topic} ({doc.jurisdiction})")


if __name__ == "__main__":
    main()
