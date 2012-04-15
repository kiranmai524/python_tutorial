from sys import argv
import twitter
script,name = argv
user = twitter.Api()
tweets_5 = user.GetUserTimeline(name)
print " latest 5 tweets from Channel %r:"%name
for i in range(0,6,1):
		print " %r\t %s\n"%(i,tweets_5[i].text