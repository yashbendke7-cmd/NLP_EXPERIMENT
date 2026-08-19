import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

text = "Natural Language Processing is very interesting and useful!"

# Lowercase
text = text.lower()

# Tokenization
words = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

print("Original Text:", text)
print("Tokens:", words)
print("After Stopword Removal:", filtered_words)
print("After Stemming:", stemmed_words)
