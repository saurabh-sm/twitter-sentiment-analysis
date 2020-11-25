from tweepy import Stream

import keys
from listener import TwitterListener
from authenticator import TwitterAuthenticator


class Streamer():

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, hash_tag_list):
        listener = TwitterListener()
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)


def main():

    tweet_streamer = Streamer()
    hash_tag = ['Donald Trump']
    # hash_tags = ['Donald Trump', 'Joe Biden']     # returns sentiment for both trackers
    tweet_streamer.stream_tweets(hash_tag)


if __name__ == '__main__':
    main()
