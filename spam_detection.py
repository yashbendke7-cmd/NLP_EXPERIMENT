from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

messages = [
    "Congratulations you won a lottery",
    "You have won 10000 rupees",
    "Free gift available click now",
    "Meeting is scheduled at 10 AM",
    "Please send me the notes",
    "Can you call me tonight?"
]

labels = [
    "Spam",
    "Spam",
    "Spam",
    "Not Spam",
    "Not Spam",
    "Not Spam"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

model = MultinomialNB()
model.fit(X, labels)

message = input("Enter a message: ")

test = vectorizer.transform([message])
prediction = model.predict(test)

print("Prediction:", prediction[0])
