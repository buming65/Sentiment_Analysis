import tweepy
import sklearn
import csv

consumer_key = "lfUerIde4jKMzSYuwTHmfgNpw"
consumer_secret = "duv7Fk7ijTOYBzSzyPzgaO7kupQ3FcNWdzp4gWD3vyT3pyp1JB"
access_token = "1185943912998817792-lPF001dtXR2HZyf9vIeFyhN0huBXL1"
access_token_secret = "ISlaAmnjvsdXIIERV1WnoWB5kbepKvWuvUvBoryX2Mabo"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
# csvFile = open('tweetsData.csv', 'a')
csvFile = open('data12-2.csv', 'a')

#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,
    q="key word",
    # since="2019-11-02",
    # until="2019-11-03",
    since="2019-11-03",
    until="2019-11-04",
    #startSince = '2015-11-25 00:00:00',
    #endUntil = '2015-11-25 23:59:59',
    lang="en").items():
    #print tweet.created_at, tweet.text, tweet.place, tweet.coordinates
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.place,tweet.coordinates])
