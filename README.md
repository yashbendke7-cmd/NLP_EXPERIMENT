# 🎓 AI College Notice Analyzer

A small NLP/AI project that analyzes college notices and extracts useful information automatically.

## Features

- 📌 Notice category detection
- 📅 Deadline/date extraction
- ⏰ Time extraction
- ⚠️ Priority detection
- 📝 Simple extractive summary
- 🔑 Important keyword extraction
- 🌐 Streamlit web interface

## Categories

The analyzer can identify notices related to:
- Placement
- Exam
- Internship
- Scholarship
- Event
- Assignment
- General Notice

## Technologies Used

- Python
- NLP concepts
- Regular Expressions
- Streamlit

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
streamlit run app.py
```

## Example Input

TCS campus placement registration is open for eligible students. Last date is 15 September 2026 at 5:00 PM.

## Example Output

- Category: Placement
- Priority: HIGH
- Deadline: 15 September 2026
- Time: 5:00 PM
- Keywords: placement, registration, tcs, campus

## Project Structure

```text
AI_College_Notice_Analyzer/
├── app.py
├── notice_analyzer.py
├── preprocessing.py
├── requirements.txt
├── README.md
└── sample_notices/
    └── placement_notice.txt
```
