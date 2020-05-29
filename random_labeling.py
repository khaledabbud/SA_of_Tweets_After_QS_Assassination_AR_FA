"""
Here I randomly selected 1000 tweets and checked the accuracy of the language labeling
and also labeled the sentiment manually to use as a training set for ML sentiment analysis.
"""


# - *- coding: utf- 8 - *-
import pandas as pd
import random

df = pd.read_csv("tweets_lang_added.csv")
df_ar = df[df['language'] == 'fa']
df_ar = df_ar.reset_index()
df_ar = df_ar.drop(['index'], axis = 1)

nums = random.sample(range(df_ar.shape[0]-1), 1000)
counter = 0
remains = 1000

for i in nums:
    print(df_ar.loc[i]['cleaned_text'])
    print("")
    lang = input("lang: ")
    df_ar.at[i, 'language'] = lang
    sentiment = input("sentiment: ")
    df_ar.at[i, 'sentiment'] = sentiment
    hate = input("hate: ")
    df_ar.at[i, 'hate'] = hate
    print("")
    counter += 1
    remains -= 1
    print(counter, ' ', remains)
    print("")
    print("================================================================================================================")
    print("")
    print("")

df_ar.to_csv("tweets_sent_fa.csv")

print("======== Done ==========")
