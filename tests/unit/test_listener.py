'''
Exception handling already present in streamer.py
'''

import unittest

from app.listener import TwitterListener

class TestListener(unittest.TestCase):

    def setUp(self):
        self.listener = TwitterListener()
        self.tweet = "RT @davidhickman14: It's North London Matchday. \
                      Come on you Gunners #Arsenal #NorthLondonIsRed \
                      https://t.co/6WbJ9WJNrF"

    def test_clean_tweet(self):
        self.assertIsNotNone(self.listener.clean_tweet(self.tweet))

    def test_on_error(self):
        """Empty list is passed in search field."""
        self.assertFalse(self.listener.on_error(406))

    def test_on_data_exception(self):
        self.assertRaises(Exception, self.listener.on_data(''))
