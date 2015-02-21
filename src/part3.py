# Part 3
# Extracts tweet count for each of our hashtag, put into "tweet_count.txt".
#
# For the most popular two hashtags, we generate two files, "SB49_1.csv"
# and "FOOTBALL_2.csv" (here SB49 and FOOTBALL are the most popular hashtags)
# The filenames are computed rather than hard coded. Each file contains
# the sorted timestamps when a tweet with the related hashtag is published. 
#
# Then data will be useful for the second half of part3 and part5, tweet
# rate computation. This can be easily done with matlab.
#
# All output files should reside in "../result/".

import json

######################      Definitions      ######################
# For each tweet, we convert it to a structure containing the time
# when it's tweeted, and all the hashtags it contains.
class TimeAndHashtag:
	def __init__(self, time, hashtags):
		self.time = time
		self.hashtags = hashtags

# Convert a json line of tweet data into the object above
def extractTimeAndHashtag(tweetLine):
	tweetObj = json.loads(tweetLine.strip())
	time = tweetObj['firstpost_date']
	rawHashtags = tweetObj['tweet']['entities']['hashtags']
	hashtags = []
	for entry in rawHashtags:
		hashtags.append('#' + entry['text'].upper())
	return TimeAndHashtag(time, hashtags)

# Write a list into a file, one entry each line
def writeList(timeList, path):
	f = open(path,'w')
	for time in timeList:
		f.write(str(time) + '\n')
	f.close()

##################################################################

# Hashtags are case insensitive, convert to upper case for 
# easy comparison. Use unicode strings to prevent implicit conversion.
hashtags = [u'#SB49', u'#football', u'#MakeSafeHappen', u'#brandbowl', u'#adbowl']
for i in range(len(hashtags)):
	hashtags[i] = hashtags[i].upper()

resultPath = '../result/'

# Count hashtags. count[i] is the count for hashtag[i]
count = [0  for i in range(len(hashtags))]

# Each entry in this list timestampList[i] is a list of timestamps
# when a tweet with hashtags[i] is published. Not necessarily sorted.
timestampList = [[] for i in range(len(hashtags))]

# Read input and count tweets
#f = open('../result/top_tweets.txt', 'r');
f = open(resultPath + 'tweets.txt', 'r')

# We write timestamp + hashtag structs into this file
fc = open(resultPath + 'compressed_tweets.txt', 'w')

for line in f:
	metadata = extractTimeAndHashtag(line)
	for hashtag in metadata.hashtags:
		if hashtag in hashtags:
			index = hashtags.index(hashtag)
			count[index] += 1
			(timestampList[index]).append(metadata.time)
	t = (metadata.time, metadata.hashtags)
	fc.write(str(t)+'\n')

f.close()
fc.close()

# write counts out
fcount = open('../result/tweet_count.txt', 'w')
for index in range(len(hashtags)):
	line = hashtags[index] + ' ' + str(count[index]) + '\n'
	fcount.write(line)
fcount.close

# For the two most popular hashtags, write the sorted timestamp list
sortedCount = sorted(count, reverse=True)
max1 = count.index(sortedCount[0])
max2 = count.index(sortedCount[1])
file1Name = resultPath + hashtags[max1][1:] + '_1.csv'
file2Name = resultPath + hashtags[max2][1:] + '_2.csv'

#print count
#print timestampList

writeList(sorted(timestampList[max1]), file1Name)
writeList(sorted(timestampList[max2]), file2Name)

