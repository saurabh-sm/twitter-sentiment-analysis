import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from client import TwitterClient

class Analyzer:

    def tweet_frame(self, tweets):
        tweet_frame = pd.DataFrame(data=[tweet.text for tweet in tweets], columns = ['Tweets'])
        tweet_frame['id'] = np.array([tweet.id for tweet in tweets])
        tweet_frame['date'] = np.array([tweet.created_at for tweet in tweets])
        tweet_frame['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        tweet_frame['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        return tweet_frame


def main():

    tweet_analyzer = Analyzer()
    twitter_client = TwitterClient()

    api = twitter_client.get_twitter_client_api()
    tweets = api.user_timeline(screen_name='realdonaldtrump', count = 20)
    #print(tweets)

    df = tweet_analyzer.tweet_frame(tweets)
    print(df.head(10))
    #print(dir(tweets[0]))       # infor that can be extracted from first tweet

    # Basic Stats
    print(np.max(df['likes']))      # most liked tweet
    print(np.max(df['retweets']))   # most retweeted tweet

    '''
    # Advanced Stats: Likes
    time_likes = pd.Series(data=df['likes'].values, index=df['date'])
    time_likes.plot(figsize=(15, 5), color='red')
    plt.show()

    # Advanced Stats: Retweets
    time_retweets = pd.Series(data=df['retweets'].values, index=df['date'])
    time_retweets.plot(figsize=(15, 5), color='blue')
    plt.show()
    '''

    # Advanced Stats: Combination of likes and retweets
    time_likes = pd.Series(data=df['likes'].values, index=df['date'])
    time_likes.plot(figsize=(16, 4), label='Likes', color='red', legend=True)
    time_retweets = pd.Series(data=df['retweets'].values, index=df['date'])
    time_retweets.plot(figsize=(16, 4), label='Retweets', color='blue', legend=True)
    plt.show()


if __name__ == '__main__':
    main()
