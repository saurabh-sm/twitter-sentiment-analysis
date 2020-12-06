import unittest

from app.analyzer import Analyzer
from app.client   import TwitterClient

class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.search_term = 'trump'
        self.number_of_tweets = 10
        self.analyzer = Analyzer()
        self.client   = TwitterClient()

    def test_filtered_tweets(self):
        filtered_tweets = self.client.get_tweets(self.search_term, self.number_of_tweets)
        self.assertIsNotNone(filtered_tweets)
        return filtered_tweets

    def test_clean_tweet(self):
        self.assertIsNotNone(self.analyzer.clean_tweet("This is a test string"))

    def test_get_tweets_and_analyze(self):
        filtered_tweets = self.test_filtered_tweets()
        self.assertTrue(self.analyzer.get_tweets_and_analyze(filtered_tweets, self.search_term, self.number_of_tweets))

    def test_percentage(self):
        self.assertIsNotNone(self.analyzer.percentage(2, self.number_of_tweets))

    def test_compute_average(self):
        self.assertTrue(self.analyzer.compute_average(self.number_of_tweets))

    def test_compute_avarage_exception(self):
        self.assertRaises(Exception, self.analyzer.compute_average(0))

    def test_sentiment_report(self):
        self.assertTrue(self.analyzer.sentiment_report(self.search_term, self.number_of_tweets))

    def test_plot_pie_chart(self):
        self.assertTrue(self.analyzer.plot_piechart(self.search_term, self.number_of_tweets))

    def test_create_report(self):
        filtered_tweets = self.test_filtered_tweets()
        self.assertIsNotNone(self.analyzer.create_report(self.search_term, self.number_of_tweets))

    def test_create_chart(self):
        filtered_tweets = self.test_filtered_tweets()
        self.assertIsNone(self.analyzer.create_chart(self.search_term, self.number_of_tweets))

