from tweepy import OAuthHandler
from tweepy import Stream

import keys
from listener import Listener

class Streamer():
    '''
    Stream tweets based on hash tags.
    '''
    def stream_tweets(self, tweets_file, hash_tags):
        listener = Listener(tweets_file)

        auth = OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
        auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)
        stream.filter(track=hash_tags)

def main():
    hash_tags = ['Donald Trump', 'Joe Biden']
    tweets_file = 'live_tweets.json'

    tweet_streamer = Streamer()
    tweet_streamer.stream_tweets(tweets_file, hash_tags)


if __name__ == '__main__':
    main()
