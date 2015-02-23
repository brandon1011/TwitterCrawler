setwd("C:\\Users\\datd\\Desktop")

library('ggplot2') 
library('scales')

tweet = scan('tweets.txt',what=character(),sep="\n")
tweet = gsub ( '(\\\\|")','',tweet) 

hashtags = c('#SB49', '#football', 
			'#MakeSafeHappen', '#brandbowl', '#adbowl')

retweetCount = regexpr ( '(retweet_count: [0-9]+)',tweet) # location of 'retweet_count
retweetCount = regmatches ( tweet,retweetCount ) # extract the retweet_count. 
retweetCount = gsub ( 'retweet_count: ','',retweetCount )

count = table(retweetCount)
RETWEET = data.frame(count)
RETWEET[,1:2] = apply(RETWEET[,1:2],2,as.numeric)

	
p = ggplot(data=RETWEET,aes(x=retweetCount ,y=Freq)) + 
		geom_point(shape=16, alpha=3/4,size=4) + 
			ggtitle("Retweet Count") + 
		theme(plot.title = element_text(lineheight=.8, face="bold"))+
		scale_y_continuous(name="Number of Tweets") + 
		scale_x_continuous(name="Retweet Count") + 
		geom_smooth(method=lm, se=TRUE, size=1, color='royalblue',alpha=1/2,fill = "lightsteelblue1") + # Add linear regression line          
		theme_bw()
p

windows()
pLog = ggplot(data=log(RETWEET[-1,]),aes(x=retweetCount ,y=Freq)) + 
		geom_point(shape=16, alpha=3/4,size=4) + 
			ggtitle("Retweet Count (Log scale)") + 
		theme(plot.title = element_text(lineheight=.8, face="bold"))+
		scale_y_continuous(name="Log(Number of Tweets)") + 
		scale_x_continuous(name="Log(Retweet Count)") + 
		geom_smooth(method=lm, se=TRUE, size=1, color='royalblue',alpha=1/2,fill = "lightsteelblue1") + # Add linear regression line          
		theme_bw()
pLog


RETWEET = NULL
for ( hash in hashtags) {

	tweetHash = grep(hash,tweet,ignore.case=TRUE,value = TRUE); 
	if (length(tweetHash) == 0) { 
		next; 
	} 
	retweetCount = regexpr ( '(retweet_count: [0-9]+)',tweetHash) # location of 'retweet_count
	retweetCount = regmatches ( tweetHash,retweetCount ) # extract the retweet_count. 
	retweetCount = gsub ( 'retweet_count: ','',retweetCount )

	count = table(retweetCount)
	count = data.frame(count,hash)
	
	RETWEET = rbind(RETWEET,count)
}
RETWEET[,1:2] = apply(RETWEET[,1:2],2,as.numeric)

pSep = ggplot(data=RETWEET,aes(x=retweetCount ,y=Freq)) + 
		geom_point(aes(colour=hash),shape=16, alpha=1/2,size=2) + 
			ggtitle("Retweet Count") + 
		theme(plot.title = element_text(lineheight=.8, face="bold"))+
		scale_y_continuous(name="Number of Tweets") + 
		scale_x_continuous(name="Retweet Count") + 
		geom_smooth(aes(colour=hash),method=lm, se=FALSE, size=1) +  # Add linear regression line   
		geom_smooth(method=lm, se=FALSE, size=2, color='royalblue') +
		theme_bw()		
pSep

p = ggplot(data=RETWEET,aes(x=retweetCount ,y=Freq)) + 
		geom_point(aes(colour=hash),shape=16, alpha=1/2,size=2) + 
			ggtitle("Retweet Count") + 
		theme(plot.title = element_text(lineheight=.8, face="bold"))+
		scale_y_continuous(name="Number of Tweets") + 
		scale_x_continuous(name="Retweet Count") + 
		geom_smooth(method=lm, se=TRUE, size=1, color='royalblue',alpha=1/2,fill = "lightsteelblue1") + # Add linear regression line          
		theme_bw()
p


pLog = ggplot() + 
		geom_point(data=count,aes(x=retweetCount ,y=Freq),shape=16, alpha=1/2) + 
		ggtitle("Retweet Count") + 
		theme(plot.title = element_text(lineheight=.8, face="bold"))+
		scale_y_continuous(name="Number of Tweets") + 
		scale_x_log(name="Retweet Count",breaks = trans_breaks("log10", function(x) 10^x),
                     labels = trans_format("log10", math_format(10^.x)))
pLog
