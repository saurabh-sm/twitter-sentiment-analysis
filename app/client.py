from tweepy import API
from tweepy import Cursor

from authenticator import TwitterAuthenticator

class TwitterClient():

    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user  # if no user is specified, timeline content will be from your twitter handle

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_tweets(self, searchTerm, NoOfTerms):
        tweets = []
        #for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
        for tweet in Cursor(self.twitter_client.search, q=searchTerm, lang = "en").items(NoOfTerms):
            tweets.append(tweet)
        return tweets

def main():

    twitter_client = TwitterClient()                # optional specify @ handle
    print(twitter_client.get_user_timeline_tweets(1))       # get 'n' most recent stuff from your timeline
    print()
    print(twitter_client.get_friend_list(1))
    print()
    print(twitter_client.get_home_timeline_tweets(1))


if __name__ == '__main__':
    main()
