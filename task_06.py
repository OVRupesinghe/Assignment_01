from data_handler import DataLoader

df = DataLoader('data/recipes.json')
ingredients = df.get_column('Ingredients')
names = df.get_column('Name')

ingredients_dict = dict(zip(names, ingredients))
preferred_ingredients = ['sweet potato', 'chocolate', 'dried cranberries', 'raspberries', 'icing sugar', 'ginger',
                         'cherries', 'brandy']


def get_score(dictionary):
    for key, value in dictionary.items():
        score = 0
        for ingredient in value:
            tokens = ingredient.split(' ')
            for token in tokens:
                if token.lower() in preferred_ingredients:
                    score += 1
        if score:
            print(f'Key: {key}, Score: {score}')


get_score(ingredients_dict)
