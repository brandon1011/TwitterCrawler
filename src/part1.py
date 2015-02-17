# Part 1
# Make API quaries for our hashtags in the specific time interval.
# Print out result as a JSON object to stdout

import json
import datetime, time
import TweetGrabber

start_date = datetime.datetime(2015,02,01, 20,00,0)
end_date = datetime.datetime(2015,02,02, 11,00,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

hashtags = ['#SB49', '#football', '#MakeSafeHappen', '#brandbowl', '#adbowl']

for hashtag in hashtags:
	grabber = TweetGrabber.TweetGrabber(hashtag, mintime, maxtime)
	grabber.fetchTweet(5)
        
	while True:
		nextTweet = grabber.nextTweet()
		if nextTweet is not None:
			print(json.dumps(nextTweet))
		else
			break

