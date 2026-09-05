import re
from collections import Counter
from preprocessing import clean_text

CATEGORIES = {
    "Placement": ["placement", "campus", "recruitment", "company", "tcs", "interview", "job"],
    "Exam": ["exam", "examination", "test", "mse", "semester", "hall ticket", "result"],
    "Internship": ["internship", "intern", "training", "summer internship"],
    "Scholarship": ["scholarship", "scholar", "fellowship", "financial aid"],
    "Event": ["event", "workshop", "seminar", "fest", "competition", "webinar"],
    "Assignment": ["assignment", "submission", "project", "report", "submit"],
}

STOPWORDS = {
    "the","is","are","a","an","and","or","of","to","in","on","for","with",
    "this","that","be","by","from","at","as","will","all","students","please",
    "you","your","has","have","must","can","may","their","eligible"
}

def detect_category(text):
    lower = text.lower()
    scores = {}
    for category, words in CATEGORIES.items():
        scores[category] = sum(1 for word in words if word in lower)
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "General Notice"

def extract_date(text):
    patterns = [
        r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',
        r'\b\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b',
        r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\b'
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0)
    return "Not detected"

def extract_time(text):
    patterns = [
        r'\b\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)\b',
        r'\b\d{1,2}\s*(?:AM|PM|am|pm)\b'
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(0)
    return "Not detected"

def detect_priority(text):
    lower = text.lower()
    high_words = ["urgent", "immediately", "last date", "deadline", "today", "tomorrow", "mandatory"]
    medium_words = ["important", "register", "registration", "submit", "apply"]
    if any(word in lower for word in high_words):
        return "HIGH"
    if any(word in lower for word in medium_words):
        return "MEDIUM"
    return "LOW"

def make_summary(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    if not sentences:
        return text.strip()
    # Simple extractive summary: first two meaningful sentences.
    meaningful = [s for s in sentences if len(s.split()) >= 5]
    return " ".join(meaningful[:2]) if meaningful else text.strip()

def extract_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    words = [w for w in words if w not in STOPWORDS]
    counts = Counter(words)
    return [word for word, _ in counts.most_common(8)]

def analyze_notice(text):
    cleaned = clean_text(text)
    return {
        "category": detect_category(text),
        "deadline": extract_date(text),
        "time": extract_time(text),
        "priority": detect_priority(text),
        "summary": make_summary(text),
        "keywords": extract_keywords(cleaned),
    }
