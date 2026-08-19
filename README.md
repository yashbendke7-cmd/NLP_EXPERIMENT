NLP Experiments

Small Natural Language Processing experiments using Python.

About

This repository contains three basic Natural Language Processing experiments implemented using Python.

Technologies Used

- Python
- NLTK
- TextBlob
- Scikit-learn

Experiments

1. Text Preprocessing

Aim: To preprocess text using basic NLP techniques.

Techniques used:

- Lowercase conversion
- Tokenization
- Stop-word removal
- Stemming

File: "Text_preprocessing.py"

---

2. Sentiment Analysis

Aim: To identify whether a sentence is Positive, Negative, or Neutral.

Method: TextBlob is used to calculate the sentiment polarity of the given text.

File: "Sentiment_analysis.py"

Example:

Input:

I love this movie

Output:

Sentiment: Positive

---

3. Spam Message Detection

Aim: To classify a message as Spam or Not Spam.

Method:

- Count Vectorization
- Multinomial Naive Bayes

File: "spam_detection.py"

Example:

Input:

Congratulations you won a lottery

Output:

Prediction: Spam

Requirements

Install the required libraries:

pip install nltk textblob scikit-learn

Repository Structure

NLP_EXPERIMENT/
│
├── Text_preprocessing.py
├── Sentiment_analysis.py
├── spam_detection.py
├── README.md
└── .gitignore

Learning Outcomes

- Understand basic NLP concepts
- Perform text preprocessing
- Perform sentiment analysis
- Perform text classification
- Use Python NLP libraries

Conclusion

These experiments provide a basic understanding of Natural Language Processing and demonstrate how Python can be used to process and analyze human language.
