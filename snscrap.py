import pandas as pd
import snscrape.modules.twitter as sntwitter
import time
from datetime import datetime

# Define the search query
search_words = '("covid-19" OR "coronavirus" OR "pandemic" OR "covid" OR "corona") AND ("e-learning" OR "e learning" OR "distance learning" OR "education" OR "online learning" OR "online education" OR "distance education" OR "distance learning" OR "online learning" OR "Onlineclasses" OR "Distance-Learning" OR "Online-Classes" OR "virtual learning" OR "Remote-Learning" OR "covidneducation" OR "online teaching")'

# Define the date range for the tweets to scrape
since_date = '2019-01-01'
until_date = '2022-05-05'

# Define the number of tweets to scrape
max_tweets = 200000

# Define the list to hold the tweets
tweets_list = []



while(True): #Infinite Loop
    try:
        # Iterate through the tweets and append them to the list
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{search_words} since:{since_date} until:{until_date}').get_items()):
            if i >= max_tweets:
                break
            # Check if the tweet is already in the list, to remove duplicates
            if tweet.id not in [t[1] for t in tweets_list]:
                tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        
        # Create a Pandas dataframe from the tweets list
        tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
        
        # Save the dataframe to a CSV file
        tweets_df.to_csv('snscrap_tweets.csv', index=False)
    except Exception as e:
        print("---------------------------------------------------------------------------")
        print("Error: ", str(e))
        print("Error Type: ", type(e))
        print("---------------------------------------------------------------------------")
        
        error_occured_at = datetime.now()
        print("Error occured at: ", error_occured_at)

        print("wait for 5 seconds....")
        
        time.sleep(5)
        print("continue....")
        print(len(tweets_list))
        
        
        continue
    
