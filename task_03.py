from data_handler import DataLoader


# Search for the keyword "saucepan" in the method column
def search_list(list, search_string):
    count = 0
    for sublist in list:
        for item in sublist:
            if search_string.lower() in item.lower():
                count += 1
                break
    print(count)


file = DataLoader('data/recipes.json')
df = file.get_column('Method')

search_list(df, 'saucepan')
