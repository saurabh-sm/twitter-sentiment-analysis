from tweepy import API
from tweepy import Cursor

from app.authenticator import TwitterAuthenticator

class TwitterClient():

    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth, wait_on_rate_limit=True)    # obey rate limit
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_timeline_tweets(self, num_tweets):
        """
        Get tweets from a specified user's timeline if specified.
        If user is not specified, get tweets from the developer's account.
        """
        timeline_tweets = []
        if self.twitter_user:
            for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
                timeline_tweets.append(tweet)
        else:
            for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
                timeline_tweets.append(tweet)
        return timeline_tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_tweets(self, search_term, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=search_term, lang = "en").items(num_tweets):
            tweets.append(tweet)
        return tweets


def main():

    twitter_client = TwitterClient()
    print(type(twitter_client.get_twitter_client_api()))
    #print(twitter_client.get_timeline_tweets(1))
    #print('\n')
    #twitter_client.get_timeline_tweets(1)
    #print('\n')
    #print(twitter_client.get_friend_list(1))
    #print('\n')
    #print(twitter_client.get_tweets('chelsea', 1))


if __name__ == '__main__':
    main()
