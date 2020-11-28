import unittest

import tweepy

from app.authenticator import TwitterAuthenticator

class TestTwitterAuthenticator(unittest.TestCase):

    def setUp(self):
        self.authenticator = TwitterAuthenticator()

    def test_not_none(self):
        self.assertIsNotNone(self.authenticator.authenticate_twitter_app())

    def test_auth_object(self):
        self.assertIsInstance(self.authenticator.authenticate_twitter_app(),
                              tweepy.auth.OAuthHandler)

if __name__ == '__main__':
    main()
