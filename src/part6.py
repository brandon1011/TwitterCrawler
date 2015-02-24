"""Part 6

Reads a tweet from a line containing a json tweet object; prints 
post date, text, number of retweets, and user.

"""
import json
import time
import datetime as dt

# Printing can be turned off
def dumpTweetMetadata(tweetLine, printing=True):
	tweetObj = json.loads(tweetLine.strip())
	
	postDateInt = tweetObj['firstpost_date']

        # We can make date human-redable: "yyyy-mm-dd hh:mm:ss" 
        postDate = str(dt.datetime.fromtimestamp(postDateInt))

        text = (tweetObj['title'])
        retweet = (tweetObj['tweet']['retweet_count'])

        # It's not sure whether to use user's 'real' name or nickname. We just use nickname for now.
        user = (tweetObj['author']['nick'])

	printDict = {'Post date': postDate, 'Text': text, 'Number of retweets': retweet, 'User': user}
	if printing:
        	print(json.dumps(printDict))

	workDict = printDict
	workDict['Post date'] = postDateInt

	return workDict

def main():
	f = open('../result/top_tweets.txt', 'r')
	l = 1
	for line in f:
		tweet = dumpTweetMetadata(line, printing=False)
		print('**** Tweet ' + str(l) + ':')
		print('Text: ' + tweet['Text'])
		print('User: ' + tweet['User'])
		print('Date: ' + str(dt.datetime.fromtimestamp(tweet['Post date'])))
		print('')
		l += 1

if __name__ == '__main__':
	main()


