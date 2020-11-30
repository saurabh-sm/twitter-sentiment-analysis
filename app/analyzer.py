import re

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


    def get_tweets_and_analyze(self, filtered_tweets, searchTerm, NoOfTerms):
        self.tweets = filtered_tweets
        for tweet in self.tweets:
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
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


    def cleanTweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())


    def compute_average(self, searchTerm, NoOfTerms):
        self.positive = self.percentage(self.positive, NoOfTerms)
        self.wpositive = self.percentage(self.wpositive, NoOfTerms)
        self.spositive = self.percentage(self.spositive, NoOfTerms)
        self.negative = self.percentage(self.negative, NoOfTerms)
        self.wnegative = self.percentage(self.wnegative, NoOfTerms)
        self.snegative = self.percentage(self.snegative, NoOfTerms)
        self.neutral = self.percentage(self.neutral, NoOfTerms)
        self.polarity = self.polarity / NoOfTerms


    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')


    def sentiment_report(self, searchTerm, NoOfTerms):
        print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
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
        print(str(self.negative) + "% people thought it was negative")
        print(str(self.wnegative) + "% people thought it was weakly negative")
        print(str(self.snegative) + "% people thought it was strongly negative")
        print(str(self.neutral) + "% people thought it was neutral")

        self.plotPieChart(self.positive, self.wpositive, self.spositive,
            self.negative, self.wnegative, self.snegative, self.neutral,
            searchTerm, NoOfTerms)


    def plotPieChart(self, positive, wpositive, spositive, negative,
                wnegative, snegative, neutral, searchTerm, noOfSearchTerms):

        labels = ['positive [' + str(positive) + '%]', 'Weakly positive ['
                  + str(wpositive) + '%]','Strongly positive [' + str(spositive)
                  + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative ['
                  + str(negative) + '%]', 'Weakly Negative [' + str(wnegative)
                  + '%]', 'Strongly Negative [' + str(snegative) + '%]']

        sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]

        colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']

        patches, texts = plt.pie(sizes, colors=colors, startangle=90)

        plt.legend(patches, labels, loc="best")

        plt.title('How people are reacting on ' + searchTerm + ' by analyzing '
            + str(noOfSearchTerms) + ' Tweets.')

        plt.axis('equal')

        plt.tight_layout()

        plt.show()



def main():

    tweet_analyzer = Analyzer()

    twitter_client = TwitterClient()
    twitter_api = twitter_client.get_twitter_client_api()

    search_term = 'trump'
    number_of_searches = 20

    filtered_tweets = twitter_client.get_tweets(search_term, number_of_searches)
    tweet_analyzer.get_tweets_and_analyze(filtered_tweets, search_term, number_of_searches)
    tweet_analyzer.compute_average(search_term, number_of_searches)
    tweet_analyzer.sentiment_report(search_term, number_of_searches)


if __name__ == '__main__':
    main()
