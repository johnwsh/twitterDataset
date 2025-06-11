import pandas as pd
import os

def main():
    df = pd.read_csv('captions.csv')
    base = pd.read_csv('ground_truth\\twitter_three_agrees.txt', sep=" ",header=None)

    alvo = {'id':[], 'text':[], 'sentiment':[]}

    for index, row in base.iterrows():
        id = row[0][:-4]
        id = 'images/' + id

        text = df[df['id'] == id]['caption'].values[0]

        sentiment = row[1]

        alvo['id'].append(id)
        alvo['text'].append(text)
        alvo['sentiment'].append(sentiment)

    df = pd.DataFrame(alvo)
    df.to_csv('captions_alpha3.csv', index=False, quoting=1)

main()