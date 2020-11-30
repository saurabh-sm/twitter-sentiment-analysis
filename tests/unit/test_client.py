import unittest

import tweepy

from app.client import TwitterClient

class TestTwitterClient(unittest.TestCase):

    def setUp(self):
        self.default_user = TwitterClient()
        self.custom_user = TwitterClient('chelseafc')

    def test_default_client_api(self):
        self.assertIsNotNone(self.default_user)

    def test_custom_client_api(self):
        self.assertIsNotNone(self.custom_user)

    def test_default_user_present(self):
        self.assertTrue(self.default_user)

    def test_custom_user_present(self):
        self.assertTrue(self.custom_user)

    def test_default_user_timeline(self):
        self.assertIsNotNone(self.default_user.get_timeline_tweets(1))

    def test_custom_user_timeline(self):
        self.assertIsNotNone(self.custom_user.get_timeline_tweets(1))

    def test_default_timeline_type(self):
        self.assertIsInstance(self.default_user.get_timeline_tweets(1), list)

    def test_custom_timeline_type(self):
        self.assertIsInstance(self.custom_user.get_timeline_tweets(1), list)

    def test_default_user_friends(self):
        self.assertIsNotNone(self.default_user.get_friend_list(1))

    def test_custom_user_friends(self):
        self.assertIsNotNone(self.custom_user.get_friend_list(1))

    def test_default_user_friends_type(self):
        self.assertIsInstance(self.default_user.get_friend_list(1), list)

    def test_custom_user_friends_type(self):
        self.assertIsInstance(self.custom_user.get_friend_list(1), list)

    def test_get_tweets(self):
        self.assertIsNotNone(self.default_user.get_tweets('chelsea', 1))

    def test_get_tweets_type(self):
        self.assertIsInstance(self.default_user.get_tweets('chelsea', 1), list)


if __name__ == '__main__':
    main()
