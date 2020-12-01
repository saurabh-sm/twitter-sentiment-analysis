import re

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from textblob import TextBlob

from app.client import TwitterClient

class Analyzer:

    def __init__(self):
        self.tweets = []
        self.tweetText = []
        self.polarity = 0
        self.positive = 0
        self.wpositive = 0
        self.spositive = 0
        self.negative = 0
        self.wnegative = 0
        self.snegative = 0
        self.neutral = 0


    def get_tweets_and_analyze(self, filtered_tweets, searchTerm, num_tweets):
        try:
            self.tweets = filtered_tweets
            for tweet in self.tweets:
                self.tweetText.append(self.clean_tweet(tweet.text).encode('utf-8'))
                analysis = TextBlob(tweet.text)
                self.polarity += analysis.sentiment.polarity

                if (analysis.sentiment.polarity == 0):
                    self.neutral += 1
                elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                    self.wpositive += 1
                elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                    self.positive += 1
                elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                    self.spositive += 1
                elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                    self.wnegative += 1
                elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                    self.negative += 1
                elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                    self.snegative += 1

            return True

        except Exception as ex:
            print("EXCEPTION: %s", str(ex))
        return False


    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())


    def compute_average(self, num_tweets):
        try:
            self.positive = self.percentage(self.positive, num_tweets)
            self.wpositive = self.percentage(self.wpositive, num_tweets)
            self.spositive = self.percentage(self.spositive, num_tweets)
            self.negative = self.percentage(self.negative, num_tweets)
            self.wnegative = self.percentage(self.wnegative, num_tweets)
            self.snegative = self.percentage(self.snegative, num_tweets)
            self.neutral = self.percentage(self.neutral, num_tweets)
            self.polarity = self.polarity / num_tweets

            return True

        except Exception as ex:
            print("EXCEPTION: %s", str(ex))
        return False


    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')


    def sentiment_report(self, searchTerm, num_tweets):
        try:
            print('Analyzing ' + str(num_tweets) + ' tweets from people reacting on term: ' + searchTerm)
            print()
            print("General Report: ")

            if (self.polarity == 0):
                print("Neutral")
            elif (self.polarity > 0 and self.polarity <= 0.3):
                print("Weakly positive")
            elif (self.polarity > 0.3 and self.polarity <= 0.6):
                print("Positive")
            elif (self.polarity > 0.6 and self.polarity <= 1):
                print("Strongly positive")
            elif (self.polarity > -0.3 and self.polarity <= 0):
                print("Weakly Negative")
            elif (self.polarity > -0.6 and self.polarity <= -0.3):
                print("Negative")
            elif (self.polarity > -1 and self.polarity <= -0.6):
                print("Strongly Negative")

            print()
            print("Detailed Report: ")
            print(str(self.positive) + "% people thought it was positive")
            print(str(self.wpositive) + "% people thought it was weakly positive")
            print(str(self.spositive) + "% people thought it was strongly positive")
            print(str(self.neutral) + "% people thought it was neutral")
            print(str(self.negative) + "% people thought it was negative")
            print(str(self.wnegative) + "% people thought it was weakly negative")
            print(str(self.snegative) + "% people thought it was strongly negative")

            return True

        except Exception as ex:
            print("EXCEPTION: %s", str(ex))
        return False


    def plot_piechart(self, searchTerm, noOfSearchTerms):
        try:
            labels = ['positive [' + str(self.positive) + '%]', 'Weakly positive [' + str(self.wpositive) + '%]',
                      'Strongly positive [' + str(self.spositive) + '%]', 'Neutral [' + str(self.neutral) + '%]',
                      'Negative [' + str(self.negative) + '%]', 'Weakly Negative [' + str(self.wnegative) + '%]',
                      'Strongly Negative [' + str(self.snegative) + '%]']

            sizes = [self.positive, self.wpositive, self.spositive, self.neutral, self.negative, self.wnegative, self.snegative]
            colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']
            patches, texts = plt.pie(sizes, colors=colors, startangle=90)
            plt.legend(labels, loc="best")
            plt.title('Analyzing ' + str(noOfSearchTerms) + ' tweets from people reacting on term: ' + searchTerm)
            plt.axis('equal')
            plt.tight_layout()
            # plt.show()
            plt.savefig('app/static/images/piechart.png')

            return True

        except Exception as ex:
            print("EXCEPTION: %s", str(ex))
        return False


    def create_report(self, search_term, number_of_searches):
        twitter_client = TwitterClient()
        filtered_tweets = twitter_client.get_tweets(search_term, number_of_searches)
        self.get_tweets_and_analyze(filtered_tweets, search_term, number_of_searches)
        self.compute_average(number_of_searches)
        self.sentiment_report(search_term, number_of_searches)


    def create_chart(self, search_term, number_of_searches):
        twitter_client = TwitterClient()
        filtered_tweets = twitter_client.get_tweets(search_term, number_of_searches)
        self.get_tweets_and_analyze(filtered_tweets, search_term, number_of_searches)
        self.compute_average(number_of_searches)
        self.plot_piechart(search_term, number_of_searches)


'''
def main():

    tweet_analyzer = Analyzer()
    twitter_client = TwitterClient()

    search_term = 'trump'
    number_of_searches = 10

    filtered_tweets = twitter_client.get_tweets(search_term, number_of_searches)
    tweet_analyzer.get_tweets_and_analyze(filtered_tweets, search_term, number_of_searches)
    tweet_analyzer.compute_average(number_of_searches)
    tweet_analyzer.sentiment_report(search_term, number_of_searches)
    tweet_analyzer.plot_piechart(search_term, number_of_searches)


if __name__ == '__main__':
    main()
'''
