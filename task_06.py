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

df = DataLoader('data/recipes.json')
ingredients = df.get_column('Ingredients')
names = df.get_column('Name')

ingredients_dict = dict(zip(names, ingredients))

for key, value in ingredients_dict.items():
    print(f'Key: {key}, Value: {value}')

# # Download NLTK data
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
#
# # Initialize stop words and lemmatizer
# stop_words = set(stopwords.words('english'))
# stop_words.add("tbsp")
# stop_words.add("tsp")
# stop_words.add("carton")
#
# pattern = r'\d+\s*\w*'
#
# lemmatizer = WordNetLemmatizer()
#
# # Function to preprocess the text
# def preprocess_text(texts):
#     score = []
#     for text in texts:
#         print(text)
#     #     tokens = text.split(' ')
#     #     ingredients = []
#     #     for token in tokens:
#     #         if token not in stop_words and not re.match(pattern, token):
#     #             # split_words = wordninja.split(token)
#     #             # for split_word in split_words:
#     #             #     ingredients.append(split_word)
#     #             ingredients.append(token)
#     #
#     #     words = [ingredient.lower().translate(str.maketrans('', '', string.punctuation)) for ingredient in ingredients]
#     #     words = [lemmatizer.lemmatize(word) for word in words]
#     #     total_words += words
#     # return ' '.join(total_words)
#
# # Read and preprocess the corpus
# preferred_ingredients = ['sweet potato', 'chocolate', 'dried cranberries', 'raspberries', 'icing sugar', 'ginger', 'cherries', 'brandy']
# ingredients = [preprocess_text(text) for text in df]


