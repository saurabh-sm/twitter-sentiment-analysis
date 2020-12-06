import json
import re

from tweepy.streaming import StreamListener
from textblob import TextBlob
from elasticsearch import Elasticsearch

class TwitterListener(StreamListener):

    def __init__(self):
        self.es = Elasticsearch()
        self.es.indices.create(index='twitter', ignore=400)


    def on_data(self, data):
        try:
            raw_tweet = json.loads(data)
            for tweet in raw_tweet:
                filtered_tweet = TextBlob(raw_tweet["text"])
                print("Text extracted from metadata:")
                print(filtered_tweet, "\n")
                processed_tweet = self.clean_tweet(str(filtered_tweet))
                print("Result after cleaning tweet:")
                print(processed_tweet, "\n")
                print("Polarity of processed tweet:")
                print(filtered_tweet.sentiment.polarity, "\n")

                if (filtered_tweet.sentiment.polarity == 0):
                    sentiment = "neutral"
                elif (filtered_tweet.sentiment.polarity > 0 and filtered_tweet.sentiment.polarity <= 0.3):
                    sentiment = "weak positive"
                elif (filtered_tweet.sentiment.polarity > 0.3 and filtered_tweet.sentiment.polarity <= 0.6):
                    sentiment = "positive"
                elif (filtered_tweet.sentiment.polarity > 0.6 and filtered_tweet.sentiment.polarity <= 1):
                    sentiment = "strong positive"
                elif (filtered_tweet.sentiment.polarity > -0.3 and filtered_tweet.sentiment.polarity <= 0):
                    sentiment = "weak negative"
                elif (filtered_tweet.sentiment.polarity > -0.6 and filtered_tweet.sentiment.polarity <= -0.3):
                    sentiment = "negative"
                else: # (filtered_tweet.sentiment.polarity > -1 and filtered_tweet.sentiment.polarity <= -0.6):
                    sentiment = "strong negative"

                print("General sentiment of processed tweet:")
                print(sentiment, "\n")

                self.es.index(
                    index = "twitter",
                    doc_type = "test-type",
                    body = {
                        "author": raw_tweet["user"]["screen_name"],
                        "date": raw_tweet["created_at"],
                        "message": raw_tweet["text"],
                        "polarity": filtered_tweet.sentiment.polarity,
                        "subjectivity": filtered_tweet.sentiment.subjectivity,
                        "sentiment": sentiment
                    })

                print('----------------------------------------------------------------------------')

            return True

        except Exception as ex:
            print("EXCEPTION:  ", str(ex))
            return False


    def on_error(self, status):
        """Repeated access after rate limit will lock developer account."""
        if status == 420:
            return False
        print(status)


    def clean_tweet(self, tweet):
        tweet = re.sub(r'@[A-Za-z0-9]+', '', tweet)     # remove @mentions
        tweet = re.sub(r'#', '', tweet)                 # remove hashtag indicator
        tweet = re.sub(r'RT[\s]+', '', tweet)           # remove retweet indicator
        tweet = re.sub(r'https?:\/\/\S+', '', tweet)    # remove hyperlink
        return tweet
