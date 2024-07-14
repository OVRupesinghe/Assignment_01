from data_handler import DataLoader
import matplotlib.pyplot as plt

# Load data
df = DataLoader('data/recipes.json')
ingredients = df.get_column('Ingredients')
names = df.get_column('Name')
ingredients_dict = dict(zip(names, ingredients))
preferred_ingredients = ['sweet potato', 'chocolate', 'dried cranberries', 'raspberries', 'icing sugar', 'ginger',
                         'cherries', 'brandy']

preferred_set = set(preferred_ingredients)

# The score is calculated according to the number of occurrences of the preferred_ingredients in the ingredients
# column of the particular recipe
def get_score(dictionary):
    scores = {}
    for key, value in dictionary.items():
        score = 0
        for ingredient in value:
            # Tokenize the ingredient string
            ingredient_tokens = set(map(str.lower, ingredient.split()))
            # Check for exact matches in the preferred ingredients
            for pref_ing in preferred_ingredients:
                # Tokenize the preferred ingredient
                pref_ing_tokens = set(pref_ing.split())
                # Check if the preferred ingredient tokens are a subset of the ingredient tokens
                if pref_ing_tokens.issubset(ingredient_tokens) or pref_ing in ingredient.lower():
                    score += 1
        if score > 0:
            scores[key] = score
    return scores


# Get scores for the recipes
recipe_scores = get_score(ingredients_dict)

# Sort recipes by score in descending order
sorted_recipes = sorted(recipe_scores.items(), key=lambda item: item[1], reverse=True)

# Get the top 12 recipes
top_recipes = sorted_recipes[:12]

# Display the top 12 recipes and their scores
for recipe, score in top_recipes:
    print(f'Recipe: {recipe}, Score: {score}')


# Plotting the top 12 recipes
def plot_recommendations(recipes):
    names, scores = zip(*recipes)
    plt.figure(figsize=(12, 6))
    plt.barh(names, scores, color='green')
    plt.xlabel('Score')
    plt.ylabel('Recipe')
    plt.title('Top 12 Recommended Foods for Customer A')
    plt.gca().invert_yaxis()
    plt.show()


plot_recommendations(top_recipes)
