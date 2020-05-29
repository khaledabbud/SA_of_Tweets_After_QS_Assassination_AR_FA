# Sentiment Analysis of Arabic and Persian Tweets Following the Assassination of Qasem Soleimani

#### On the 3rd of January 2020, a United States drone strike near Baghdad International Airport targeted and killed Iranian major general [Qasem Soleimani](https://edition.cnn.com/2020/01/03/asia/soleimani-profile-intl-hnk/index.html) of Iran's Islamic Revolutionary Guard Corps (IRGC) along with [Abu Mahdi al-Muhandis](https://www.theguardian.com/world/2020/jan/03/abu-mahdi-al-muhandis-iraq-iran-militias-suleimani), a very important figure in the Popular Mobilization Committee (Al-Hashd Al-Sha'abi). Soleimani was commander of the Quds Force and was considered the second most powerful person in Iran, subordinate only to the Supreme Leader Ali Khamenei. This Assassination caused a [massive escalation of tensions between the United States and Iran]((https://www.dw.com/en/qassem-soleimani-timeline-of-events-following-iranian-generals-assassination/a-51910195)).
#### In this study I analyzed the sentiments of Arabic and Persian-language tweets that used the hashtag "#قاسم_سليماني" (Qasem Soleimani in Arabic/Persian) between January 3rd, the date of assassination and January 31st. The aim of my study was to analyze the change in sentiments over time, and how they were affected by major news and events. 


## Repositories I forked to use in this project:  
1. [**Optimized-modified-GetOldTweets3-OMGOT**](https://github.com/marquisvictor/Optimized-Modified-GetOldTweets3-OMGOT)  
In my quest to find a library or a piece of code that could assist me in downloading tweets that are older than 7 days, I found this project.  It is the only one that ran accurately and gave me the expected data. However, I had to add in a sleep time of 3 seconds after downloading 10 tweets in order to avoid receiving "too many requests" errors.
2. [**Persian Stop Words List**](https://github.com/kharazi/persian-stopwords): I used this project because NLTK does not have Persian stop words. 

## The approach I took:  
After spending two weeks trying to find a way to obtain old tweets, I finally got them using [Optimized-modified-GetOldTweets3-OMGOT](https://github.com/marquisvictor/Optimized-Modified-GetOldTweets3-OMGOT) project. After this, the next issue was determining the language of the tweets, since both Persian and Arabic tweets used the same hashtag. After trying many algorithms and solutions to determine the language of the tweets, I found that [textblob](https://pypi.org/project/textblob/) library has the highest accuracy, but the downside was that to avoid "too many request" error, I had to sleep after 10 tweets. Once the languages of the tweets were identified, I randomly selected and labeled 1000 tweets from each language and ran some NLTK algorithms to determine the sentiment of the Arabic tweets only, using the codes taught by Harrison Kinsley on his amazing [website](https://pythonprogramming.net/text-classification-nltk-tutorial/). It turned out that the training data was not sufficient, so the result was highly inaccurate and inconsistent. Finally I realized, because the topic of the tweets is very specific, I could easily find some keywords that determined the sentiments of the tweets for both languages. The result was satisfying, consistent and computationally cheap. 

## Here are the files of the project. To reproduce the result, you must run the files in the order specified below. However, because labeling and determining the language of the tweets are not easily reproducible, I recommend running the last 3 or 4 files only. 

## code:  
* preprocessingData.ipynb: Cleaning the tweets and extracting mentions and hashtags.
* textblob_lang_classification.py: Using [textblob](https://pypi.org/project/textblob/) library to determine the language of the tweets. 
* addingLanguage.ipynb: Adding the language as a column to the main data.
* random_labeling.py: Labeling 1000 randomly selected tweets from each language.
* arabic_full_analysis.ipynb: running some NLTK sentiment analysis algorithms on Arabic tweets. 
* noMLar.ipynb: Classifying Arabic tweets without using ML Algorithms. 
* noMLfa.ipynb: Classifying Persian tweets without using ML Algorithms.
* tweets_visualization.ipynb: Visualizing the tweets' sentiments.

## Data:
* concatenated_data.csv: Raw data
* cleaned_data.csv: Pre-processed data
* tweets_lang_added.csv: The language column added. 
* tweets_sent_fa.csv: Persian tweets from which 1000 are labeled. Ready for Sentiment analysis.
* tweets_sent_ar.csv: Arabic tweets from which 1000 are labeled. Ready for Sentiment analysis.


