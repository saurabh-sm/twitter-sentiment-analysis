from tweepy.streaming import StreamListener

class Listener(StreamListener):
    '''
    Stream filtered tweets to the standard output and JSON file.
    '''
    def __init__(self, tweets_file):
        self.tweets_file = tweets_file

    def on_data(self, data):
        try:
            print(data)
            with open(self.tweets_file, 'a') as tweets_file:
                tweets_file.write(data)
            return True
        except BaseException as ex:
            print("Data Error: %s", str(ex))
        return False

    def on_error(self, status):
        print(status)
        return False
