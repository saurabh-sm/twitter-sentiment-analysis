from tweepy import Stream

from app import keys

from app.listener import TwitterListener
from app.authenticator import TwitterAuthenticator


class Streamer():

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, hash_tag_list):
        """Hashtag list can have one more more terms."""
        listener = TwitterListener()
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        return stream.filter(track=hash_tag_list)
