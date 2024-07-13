from data_handler import DataLoader

def search_in_nested_list(nested_list, search_string):
    count = 0
    for sublist in nested_list:
        for item in sublist:
            if search_string.lower() in item.lower():
                count+=1
                break
    print(count)

file = DataLoader('data/recipes.json')
df = file.get_column_2('Method')

search_in_nested_list(df, 'saucepan')





