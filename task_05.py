import google.generativeai as genai
from data_handler import DataLoader
from google.api_core.exceptions import ResourceExhausted

GOOGLE_API_KEY = "AIzaSyCR6gH1aUIS_SWATJzFBcyaHQEhTs3hLVU"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro-latest')

def callGemini(description):
    prompt = [f"Is this recipe description suitable for making with kids? \"{description}\" Answer with 'Yes' or 'No'."]
    response = model.generate_content(prompt)
    return response.text.strip()

# Load data
data_loader = DataLoader('data/recipes.json')

# Remove rows with "No description available"
data_loader.data = data_loader.data[data_loader.data['Description'] != "No description available"]

# Extract relevant columns
names = data_loader.get_column('Name')
descriptions = data_loader.get_column('Description')

recommended_recipes = []
try:
    for name, description in zip(names, descriptions):
        result = callGemini(description)
        if result and result.lower() == 'yes':
            recommended_recipes.append(name)
except ResourceExhausted:
    print("Resource exhausted. Returning processed responses so far.")

# Print the names of recommended recipes
print("Recipes recommended to make with kids:")
for recipe in recommended_recipes:
    print(recipe)