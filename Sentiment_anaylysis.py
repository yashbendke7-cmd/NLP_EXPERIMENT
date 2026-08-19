from textblob import TextBlob

text = input("Enter a sentence: ")

analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

print("\nSentence:", text)
print("Polarity:", polarity)

if polarity > 0:
    print("Sentiment: Positive 😊")
elif polarity < 0:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")
