import urllib
import httplib
import json
import datetime, time

API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
HOST = 'api.topsy.com'
URL = '/v2/content/tweets.json'

class TweetGrabber:

	def __init__(self, hashtag, mintime, maxtime):
		self.hashtag = hashtag
		self.mintime = mintime
		self.maxtime = maxtime
		self.tweets = None

        # Added result limit parameter for our convenience.
	def fetchTweet(self, limit=500):
		########   set query parameters
		params = urllib.urlencode({'apikey' : API_KEY, 'q' :self.hashtag,
			'mintime': str(self.mintime), 'maxtime': str(self.maxtime),
			'new_only': '1', 'include_metrics':'1', 'limit': limit})
		#########   create and send HTTP request
		req_url = URL + '?' + params
		req = httplib.HTTPConnection(HOST)
		req.putrequest("GET", req_url)
		req.putheader("Host", HOST)
		req.endheaders()
		req.send('')
	
		#########   get response and print out status
		resp = req.getresponse()

		#########   extract tweets
		resp_content = resp.read()
		ret = json.loads(resp_content)
		self.tweets = ret['response']['results']['list']
		self.it = 0

	def nextTweet(self):
		if self.tweets is None or self.it >= len(self.tweets):
			return None

		tweet = self.tweets[self.it]
		self.it += 1
		return tweet
	
	def countTweets(self):
		if (self.tweets is None):
			return 0
		return len(self.tweets)

		
