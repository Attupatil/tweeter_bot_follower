import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user =api.me()

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)


#Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	if follower.followers_count >= 100 : #you can change the 100 to any other number
		follower.follow()
	break
