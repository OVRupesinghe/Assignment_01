import re
import nltk
import string
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
#import wordninja
from data_handler import DataLoader

df = DataLoader('data/recipes.json').get_column('Ingredients')

# Download NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize stop words and lemmatizer
stop_words = set(stopwords.words('english'))
stop_words.add("tbsp")
stop_words.add("tsp")
stop_words.add("carton")

pattern = r'\d+\s*\w*'

lemmatizer = WordNetLemmatizer()

# Function to preprocess the text
def preprocess_text(texts):
    total_words = []
    for text in texts:
        tokens = text.split(' ')
        ingredients = []
        for token in tokens:
            if token not in stop_words and not re.match(pattern, token):
                # split_words = wordninja.split(token)
                # for split_word in split_words:
                #     ingredients.append(split_word)
                ingredients.append(token)

        words = [ingredient.lower().translate(str.maketrans('', '', string.punctuation)) for ingredient in ingredients]
        words = [lemmatizer.lemmatize(word) for word in words]
        total_words += words
    return ' '.join(total_words)
# Read and preprocess the corpus
ingredients = [preprocess_text(text) for text in df]

# Compute TF-IDF scores
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(ingredients)
tfidf_scores = dict(zip(vectorizer.get_feature_names_out(), X.sum(axis=0).tolist()[0]))

# Generate and visualize a word cloud based on TF-IDF scores
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(tfidf_scores)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud based on TF-IDF scores')
plt.show()
