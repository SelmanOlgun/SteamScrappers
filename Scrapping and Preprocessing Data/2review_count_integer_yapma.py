import pandas as pd

df = pd.read_csv('1review_count_raw_silinmis.csv')

df['review_count'] = df['review_count'].fillna(0)
df['review_percentage'] = df['review_percentage'].fillna(0)

df['review_count'] = df['review_count'].astype(int)

df_filtered = df[df['review_count'] != 0]
df_filtered = df[df['review_percentage'] != 0]

df_filtered.to_csv('2review_count_integer_yapilmis.csv', index=False)