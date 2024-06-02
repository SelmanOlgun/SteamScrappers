import pandas as pd

df = pd.read_csv('2review_count_integer_yapilmis.csv')

df['review_percentage'] = df['review_percentage'].str.rstrip('%')

df.to_csv('3review_percentage_yuzde_silinmis.csv', index=False)
