# Tweets_Tool

Twitter Official API has limitations on how many tweets you can search for at a time and for the length of time (7 days/10 days). If I wanted to some historical tweets matching a certain criteria, I would have to either buy the Enterprise API or get GNIP, which both cost moneys. 

## Prerequisites
Since Python 2.x will be deprecated, this package assumes Python 3.x.
Expected package dependencies are listed in the "requirements.txt" file for PIP, you need to run the following command to get dependencies:
pip install -r requirements.txt

## Components
**Tweet**: Model class to give some informations about a specific tweet.  
* id (str)  
* permalink (str)  
* username (str)  
* text (str)  
* date (date)  
* retweets (int)  
* favorites (int)  
* mentions (str)  
* hashtags (str)  
* geo (str)  

**TweetManager:** A manager class to help getting tweets in Tweet's model  
* getTweets: Return the list of tweets retrieved by using an instance of TwitterCriteria  
* getJsonReponse: Actually obtains the tweets and returns an object that can be read    
 
**TwitterCriteria:** A collection of search parameters to be used together with TweetManager   
* setUsername (str): An optional specific username from a twitter account. Without "@" 
* setSince (str. "yyyy-mm-dd"): A lower bound date to restrict search  
* setUntil (str. "yyyy-mm-dd"): An upper bound date to restrist search  
* setQuerySearch (str): A query text to be matched   
* setTopTweets (bool): If True only the Top Tweets will be retrieved    
* setNear(str): A reference location area from where tweets were generated   
* setWithin (str): A distance radius from "near" location (e.g. 15mi)  
* setMaxTweets (int): The maximum number of tweets to be retrieved. If this number is unsetted or lower than 1 all possible tweets will be retrieved.    

**TweetObtain:** Returns a clean dataframe for analysis using TweetCriteria and TweetManager
* TweetObtain_function: Returns a clean dataframe for analysis using TweetCriteria and TweetManager 

## Simple examples of python usage

* Get tweets by username
``` python
	tweetCriteria = Tool.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
	tweet = Tool.TweetManager.getTweets(tweetCriteria)[0]
	tweets = pd.read_csv('tweets.csv')
	print(tweets)
```    
* Get tweets by query search
``` python
	tweetCriteria = Tool.TweetCriteria().setQuerySearch('europe refugees').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(1)
	tweet = Tool.TweetManager.getTweets(tweetCriteria)[0]
	tweets = pd.read_csv('tweets.csv')
	print(tweets)
```    
* Get tweets by username and bound dates
``` python
	tweetCriteria = Tool.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	tweet = Tool.TweetManager.getTweets(tweetCriteria)[0]
	tweets = pd.read_csv('tweets.csv')
	print(tweets)
```
* Get the last 10 top tweets by username
``` python
	tweetCriteria = Tool.TweetCriteria().setUsername("barackobama").setTopTweets(True).setMaxTweets(10)
	# first one
	tweet = Tool.TweetManager.getTweets(tweetCriteria)[0]
	tweets = pd.read_csv('tweets.csv')
	print(tweets)
```

