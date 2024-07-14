import google.generativeai as genai
from data_handler import DataLoader
from google.api_core.exceptions import ResourceExhausted

# Enter your google api key here, api keys can be obtained from : https://aistudio.google.com/app/apikey
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Configure model, selected latest model for best results
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Call the gemini model by send the description along with the prompt and obtain response
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

# If using free-tier the resources might exceed before all the rows are computed, therefore the already processed
# results are displayed.
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