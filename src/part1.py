# Part 1
# Make API quaries for our hashtags in the specific time interval.
# Print out result as a JSON object to stdout

import json
import datetime, time
import TweetGrabber

def writeTweetsToFile(grabber, f):
	while True:
		nextTweet = grabber.nextTweet()
		if nextTweet is not None:
			f.write(json.dumps(nextTweet)+ '\n')
		else:
			break

f_tweets = open('../result/top_tweets.txt', 'w')

start_date = datetime.datetime(2015,02,01, 20,00,0)
end_date = datetime.datetime(2015,02,02, 11,00,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

hashtags = ['#SB49', '#football', '#MakeSafeHappen', '#brandbowl', '#adbowl']

# Let's only search for the first hashtag #SB49
hashtag = hashtags[0]
grabber = TweetGrabber.TweetGrabber(hashtag, mintime, maxtime)
grabber.fetchTweet(5)
        
writeTweetsToFile(grabber, f_tweets)

f_tweets.close()
