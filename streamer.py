import os
from dotenv import load_dotenv, find_dotenv

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

class TweetListener(StreamListener):
    '''
    Stream filtered tweets to the standard output
    '''
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    listener = TweetListener()

    auth = OAuthHandler(os.environ.get("CONSUMER_KEY"),
                        os.environ.get("CONSUMER_SECRET"))

    auth.set_access_token(os.environ.get("ACCESS_TOKEN"),
                          os.environ.get("ACCESS_TOKEN_SECRET"))

    stream = Stream(auth, listener)

    stream.filter(track=['Donald Trump', 'Joe Biden'])
