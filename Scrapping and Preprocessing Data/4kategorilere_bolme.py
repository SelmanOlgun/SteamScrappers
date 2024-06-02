import os
import pandas as pd

df = pd.read_csv('3review_percentage_yuzde_silinmis.csv')
df['price'] = df['price'].replace('Free', 0)
df['price'] = pd.to_numeric(df['price'].str.replace('$', '').str.replace(',', ''))
df = df[df['price'] < 100]
bins = [0, 250, 500, 1000, 5000, 25000, 100000, float('inf')]
labels = ['0-250', '250-500', '500-1000', '1000-5000', '5000-25000', '25000-100000', '+100000']

df['Review_Category'] = pd.cut(df['review_count'], bins=bins, labels=labels, right=False)

category_dfs = {category: df[df['Review_Category'] == category] for category in labels}

for category, category_df in category_dfs.items():
    folder_name = f'{category}_reviews'
    os.makedirs(folder_name, exist_ok=True)
    
    file_name = os.path.join(folder_name, f'{category}_reviews.csv')
    category_df.to_csv(file_name, index=False)
