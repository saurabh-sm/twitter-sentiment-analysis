import json

from tweepy.streaming import StreamListener
from textblob import TextBlob
from elasticsearch import Elasticsearch

class TwitterListener(StreamListener):

    def __init__(self):
        self.es = Elasticsearch()
        self.es.indices.create(index='twitter', ignore=400)

    def on_data(self, data):
        try:
            dict_data = json.loads(data)
            tweet = TextBlob(dict_data["text"])
            print(tweet.sentiment.polarity)

            if tweet.sentiment.polarity < 0:
                sentiment = "negative"
            elif tweet.sentiment.polarity == 0:
                sentiment = "neutral"
            else:
                sentiment = "positive"

            print(sentiment)

            self.es.index(
                index = "twitter-sentiment",
                doc_type = "test-type",
                body = {
                    "author": dict_data["user"]["screen_name"],
                    "date": dict_data["created_at"],
                    "message": dict_data["text"],
                    "polarity": tweet.sentiment.polarity,
                    "subjectivity": tweet.sentiment.subjectivity,
                    "sentiment": sentiment
                })

            return True

        except Exception as e:
            print("Data Error: %s", str(e))
        return False

    def on_error(self, status):
        if status == 420:   # repeated access with incorrect stuff / rate limit will lock the developer account
            return False
        print(status)
