"""
This script fetches all tweets containing any of the hashtags that have
been posted during the period between start_time and end_time
"""
import json
import datetime, time
import TweetGrabber

start_date = datetime.datetime(2015,02,01, 20,00,0)
end_date = datetime.datetime(2015,02,02, 11,00,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

hashtags_list = ['#SB49', '#football', '#MakeSafeHappen', '#brandbowl', '#adbowl']
hashtags = ','.join(hashtags_list)


win_start = mintime	# start of time window of tweets to be crawled
def_win_sz = 500	# default window size
win_sz = def_win_sz	# Window size initially the default size

f_tweets = open('../result/tweets.txt', 'w')
f_searchlog = open('../result/searchlog.txt', 'w')

while (win_start < maxtime):
	win_end = min(win_start + win_sz, maxtime)
	grabber = TweetGrabber.TweetGrabber(hashtags, win_start, win_end)
	grabber.fetchTweet(500)	# default fetch size is 500
	results_count = grabber.countTweets()
	if (results_count < 500):
		########## Save tweets
		while True:
			nextTweet = grabber.nextTweet()
			if nextTweet is not None:
				f_tweets.write(json.dumps(nextTweet))
			else:
				break

		
		########## Save Query
		print("%s	From: %s	To: %s	No. of Results: %d" %(hashtags,
			time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(win_start)),
			time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(win_end)),
			results_count))
		f_searchlog.write("%s	From: %s	To: %s	No. of Results: %d\n" %(hashtags,
			time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(win_start)),
			time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(win_end)),
			results_count))
		########## Move window
		win_start = win_end + 1 
		
		########## Increase window size if too little results returned.
		if (results_count < 125):
			win_sz = min(def_win_sz, win_sz*2)
			print("+++ Increasing window size ! new size = %d" %win_sz)

	else:
		######### adjust window size and retry using smaller window
		win_sz = win_sz / 2
		print("--- Decreasing window size ! new size = %d" %win_sz)

f_tweets.close()
f_searchlog.close()
