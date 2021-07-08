import tweepy
import csv

consumer_key = "QInxmsmS9s66g5r77Ulhj7iNz"
consumer_secret = "BnHcPC24CNhpUvZqlXhotNcUCfiNet54FZ7E7Ge1JoWpWJZmC7"
access_token = "1057089181569040384-8TWNBaG4aJaqkYqWYgP5EQacTsOFeM"
access_token_secret = "x62pG5nOKpVAfBCgHqxYXrssHNGvAXRBD39wND5jMaDyx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('coba6.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#vaksincovid-19, berita vaksin",count=15000,
                           lang="id",
                           since="2020-02-14").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])