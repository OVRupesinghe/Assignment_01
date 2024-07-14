import os
import nltk
import string
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud

# Download NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize stop words and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Function to read text files and create a corpus
def read_files(filenames):
    corpus = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            corpus.append(file.read())
    return corpus

# Function to preprocess the text
def preprocess_text(text):
    # Tokenize text
    tokens = text.split()
    # Remove punctuation and convert to lowercase
    tokens = [word.lower().translate(str.maketrans('', '', string.punctuation)) for word in tokens]
    # Remove stop words and lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Filenames of the text files
filenames = ['data/text1.txt', 'data/text2.txt', 'data/text3.txt']

# Read and preprocess the corpus
corpus = read_files(filenames)
corpus = [preprocess_text(text) for text in corpus]
print(corpus)

# # Compute TF-IDF scores
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(corpus)
# tfidf_scores = dict(zip(vectorizer.get_feature_names_out(), X.sum(axis=0).tolist()[0]))

# # Generate and visualize a word cloud based on TF-IDF scores
# wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(tfidf_scores)

# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.title('Word Cloud based on TF-IDF scores')
# plt.show()