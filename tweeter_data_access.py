#import sys
#import codecs
import json


from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener



consumer_key = 'xnGIk3SgfWExQuoEgCcJGqyit'
consumer_secret = 'xv7PZGjPVgaDrsPxx1nENlekd6EohJpx3NF320Tr9qmI64rM5z'
access_token = '848594493716803586-E3jwS3JUjyZTEyNol5gBqQg2tAxgorl'
access_token_secret = 'S3ztxIeAiHC03xRFTtmh5j1YnYYLSEXWcYCActaHY7bqE'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )


class PrintListener(StreamListener):
	def 	on_status(self, status):
		if not status.text[:3] == 'RT ':print(status.author.screen_name,'\n')
		#print (status.text)
		#print(status.author.screen_name, 
		#	status.created_at,
		#	status.source, 
		#'\n')

	def on_error(self, status_code):
		print("Error code: {}".format(status_code))
		return True # keep stream alive

	def on_timeout(self):
		print('Listener timed out!')
		return True # keep stream alive

def print_to_terminal():
	listener = PrintListener()
	stream = Stream(auth, listener)
	languages=('en',)
	stream.sample(languages=languages)

def pull_down_tweets(screen_name):
	api=API(auth)
	tweets = api.user_timeline(screen_name=screen_name, count=200)
	for tweet in tweets:
		print(json.dumps(tweet._json, indent=4))

if __name__=='__main__':
	# print_to_terminal()
	pull_down_tweets(auth.username)