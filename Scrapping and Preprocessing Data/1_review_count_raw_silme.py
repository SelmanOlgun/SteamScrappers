import pandas as pd

df = pd.read_csv('0_1000pageoutput.csv')

df = df.drop(columns=['review_count_raw'])

df.to_csv('1review_count_raw_silinmis.csv', index=False)
