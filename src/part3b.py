import datetime, time
from TweetParser import *

start_date = datetime.datetime(2015,2,1, 20,0,0)
end_date = datetime.datetime(2015,2,2, 11,0,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

searchtag = 'SB49'
binsize = 10

frequency = [0]*((maxtime-mintime)/binsize + 1)
parser = TweetParser('../result/tweets.txt')
parser.load()

print len(frequency)
while parser.nextTweet() is not -1:
	if parser.hasTag(searchtag):
		index = (parser.getTime() - mintime)/binsize
		#print index
		frequency[index] = frequency[index] + 1

f = open('freqresults2.csv', 'w')

for i in range(len(frequency)):
	timestamp = i*binsize + mintime
	f.write(str(timestamp) + ',' + str(frequency[i]/binsize) + '\n')

