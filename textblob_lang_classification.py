"""
Finding the language of each tweet using textblob. 
It turned out to be the best solustion but if you 
don't sleep after 10 request, you'll get 'Too Many Requests'
error. I slept 3 secs but still got the error ocasionally and 
had to reinitiate the process in order to get the rest. 
It happened 3 times and thats why you see tweet_lang02 file 
and it took hours. 
"""


# - *- coding: utf- 8 - *-
from textblob import TextBlob
from time import sleep
import csv
import pandas as pd

df = pd.read_csv("cleaned_data01.csv")
texts = df['cleaned_text']

counter = 188277
remains = texts.shape[0] - 188277
req_counter = 0

#========================= textblob ==========================

with open('tweet_lang02.csv', 'a', encoding="utf-8-sig") as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['text','language'])
    for i in range(188277, texts.shape[0]):
        counter +=1
        remains -=1
        req_counter +=1
        print(counter, ' ', remains)
        t = texts[i]
        s = t.replace("#","")
        s = s.replace("_", " ")
        if req_counter == 10:
            sleep(3)
            req_counter = 0

        b = TextBlob(s)
        l = b.detect_language()
        csvWriter.writerow([t,l])

# =====================end of textblob ==============================
