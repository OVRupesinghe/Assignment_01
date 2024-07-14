import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from data_handler import DataLoader

# Get the author column
authors = DataLoader('data/recipes.json').get_column('Author')
# Remove rows that doesn't indicate and author
authors = [author for author in authors if author != "Unknown"]
# Count the number of recipes by each author
author_counts = Counter(authors)

# Convert the counter to a dataFrame
author_counts_df = pd.DataFrame.from_dict(author_counts, orient='index', columns=['Recipe Count'])

# Plot the bar graph
plt.figure(figsize=(10, 6))
author_counts_df.sort_values('Recipe Count', ascending=False).plot(kind='bar', legend=False)
plt.title('Number of Recipes by Each Author')
plt.xlabel('Author')
plt.ylabel('Number of Recipes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()