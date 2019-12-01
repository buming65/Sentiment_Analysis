from tweepy import OAuthHandler
from tweepy import Stream
from   tweepy.streaming import StreamListener
import time
import json
import csv



APIkey = "JsLfvl8gYTbAjozeRvBP5SL9t" #API key
APIsecret = "PnLhX1F5Lnv4jyMm2bWxjp6jIleUDEKuZVumjqsjer924ZURrO" #API scret
atoken = "743234403669684227-9d6jzlupZ9k0DfVONXjdswMsJ0sieTq" # access token
asecret = "wbgftRYRCFnckpTl1jOZjFOKAZLVtheiSbSPeJAEbP4tC" #access secret


class SListener(StreamListener):

    def on_data(self, data):
        try:

            csvFile = open('data.csv',
                           'a')

            csvWriter = csv.writer(csvFile)
            jsonStr = json.loads(data)

            tweetText = jsonStr["text"] if jsonStr["text"] else "None"

            location = jsonStr["user"]["location"] if jsonStr["user"]["location"] else "None"

            csvWriter.writerow([tweetText.encode('utf-8'), location])

            return True
        except:
            print("Exception encountered while processing tweets.")
            time.sleep(900)

    def on_status(self, status):
        if status.retweeted:
            return True

if __name__=="__main__":

    # instantiate OAuthHandler and initialize it with your credentials
    auth = OAuthHandler(APIkey,APIsecret)
    auth.set_access_token(atoken,asecret)

    # instantiate an instance of the new SListener class
    myListener = SListener()
    twitterStream = Stream(auth,myListener)
    twitterStream.filter(locations=[-124.7625, 24.5210, -66.9326, 49.3845], languages= ["en"])