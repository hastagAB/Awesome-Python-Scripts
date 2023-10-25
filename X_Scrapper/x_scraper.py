#!/usr/bin/env python
# encoding: utf-8

import sys
try:
	import tweepy #https://github.com/tweepy/tweepy
except ImportError:
	print("You'll need tweepy instaled on your system.")
	sys.exit()
try:
	import csv
except ImportError:
	print("You'll need the python csv module instaled on your system.")
	sys.exit()

consumer_key = "xxx"
consumer_secret = "yyy"
access_key = "aa-zzzz"
access_secret = "bbb"

def get_all_tweets(screen_name):

	if (consumer_key == ""):
		print("You need to set up the script first. Edit it and add your keys.")
		return

	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize x, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	if (len(sys.argv) == 2):
		get_all_tweets(sys.argv[1])
	else:
	    print("Please add the x account you want to back up as an argument.")
