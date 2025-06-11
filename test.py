import pandas as pd

df = pd.read_csv('captions.csv')

for id in df['id'].values:
    print(id)
    