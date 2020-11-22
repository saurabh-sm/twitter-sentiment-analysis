from tweepy import Stream

import keys
from listener import TwitterListener
from authenticator import TwitterAuthenticator

class Streamer():

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)


def main():

    hash_tags = ['Donald Trump', 'Joe Biden']
    tweets_file = 'live_tweets.json'

    tweet_streamer = Streamer()
    tweet_streamer.stream_tweets(tweets_file, hash_tags)


if __name__ == '__main__':
    main()
