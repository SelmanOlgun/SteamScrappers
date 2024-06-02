import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

all_categories = [category.strip() for sublist in data['game_tags'].str.split(',').tolist() for category in sublist]

category_counts = pd.Series(all_categories).value_counts()

top_categories = category_counts.head(15)

plt.figure(figsize=(10, 8))
plt.pie(top_categories, labels=top_categories.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Distribution of Game Categories')
plt.show()
