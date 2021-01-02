try:
	import http.cookiejar as cookielib
except ImportError:
	import cookielib

import urllib, json, re, datetime, sys
import pandas as pd
import numpy as np
from pyquery import PyQuery

class TweetCriteria:
	def __init__(self):
		self.maxTweets = 0

	def setUsername(self, username):
		self.username = username
		return self

	def setSince(self, since):
		self.since = since
		return self

	def setUntil(self, until):
		self.until = until
		return self

	def setQuerySearch(self, querySearch):
		self.querySearch = querySearch
		return self

	def setMaxTweets(self, maxTweets):
		self.maxTweets = maxTweets
		return self

	def setLang(self, Lang):
		self.lang = Lang
		return self

	def setTopTweets(self, topTweets):
		self.topTweets = topTweets
		return self


class Tweet:
	def __init__(self):
		pass


class TweetManager:
	def __init__(self):
		pass

	@staticmethod
	def getTweets(tweetCriteria,
	              receiveBuffer=None,
	              bufferLength=100,
	              proxy=None):
		"""Return the list of tweets retrieved by using an instance of TwitterCriteria"""
		refreshCursor = ''
		results = []
		resultsAux = []
		cookieJar = cookielib.CookieJar()

		if hasattr(
		    tweetCriteria,
		    'username') and (tweetCriteria.username.startswith("\'")
		                     or tweetCriteria.username.startswith("\"")) and (
		                         tweetCriteria.username.endswith("\'")
		                         or tweetCriteria.username.endswith("\"")):
			tweetCriteria.username = tweetCriteria.username[1:-1]

		active = True

		while active:
			json = TweetManager.getJsonReponse(tweetCriteria, refreshCursor,
			                                   cookieJar, proxy)
			if len(json['items_html'].strip()) == 0:
				break

			refreshCursor = json['min_position']
			scrapedTweets = PyQuery(json['items_html'])
			#Remove incomplete tweets withheld by Twitter Guidelines
			scrapedTweets.remove('div.withheld-tweet')
			tweets = scrapedTweets('div.js-stream-tweet')

			if len(tweets) == 0:
				break

			for tweetHTML in tweets:
				tweetPQ = PyQuery(tweetHTML)
				tweet = Tweet()

				usernameTweet = tweetPQ("span:first.username.u-dir b").text()
				txt = re.sub(r"\s+", " ",
				             tweetPQ("p.js-tweet-text").text().replace(
				                 '# ', '#').replace('@ ', '@'))
				retweets = int(
				    tweetPQ(
				        "span.ProfileTweet-action--retweet span.ProfileTweet-actionCount"
				    ).attr("data-tweet-stat-count").replace(",", ""))
				favorites = int(
				    tweetPQ(
				        "span.ProfileTweet-action--favorite span.ProfileTweet-actionCount"
				    ).attr("data-tweet-stat-count").replace(",", ""))
				dateSec = int(
				    tweetPQ("small.time span.js-short-timestamp").attr(
				        "data-time"))
				id = tweetPQ.attr("data-tweet-id")
				permalink = tweetPQ.attr("data-permalink-path")

				geo = ''
				geoSpan = tweetPQ('span.Tweet-geo')
				if len(geoSpan) > 0:
					geo = geoSpan.attr('title')

				tweet.id = id
				tweet.permalink = 'https://twitter.com' + permalink
				tweet.username = usernameTweet
				tweet.text = txt
				tweet.date = datetime.datetime.fromtimestamp(dateSec)
				tweet.retweets = retweets
				tweet.favorites = favorites
				tweet.mentions = " ".join(
				    re.compile('(@\\w*)').findall(tweet.text))
				tweet.hashtags = " ".join(
				    re.compile('(#\\w*)').findall(tweet.text))
				tweet.geo = geo

				results.append(tweet)
				resultsAux.append(tweet)

				if receiveBuffer and len(resultsAux) >= bufferLength:
					receiveBuffer(resultsAux)
					resultsAux = []

				if tweetCriteria.maxTweets > 0 and len(
				    results) >= tweetCriteria.maxTweets:
					active = False
					break

		if receiveBuffer and len(resultsAux) > 0:
			receiveBuffer(resultsAux)

		return results

	@staticmethod
	def getJsonReponse(tweetCriteria, refreshCursor, cookieJar, proxy):
		"""Actually obtains the tweets and returns an object that can be read"""
		url = "https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&max_position=%s"

		urlGetData = ''

		if hasattr(tweetCriteria, 'username'):
			urlGetData += ' from:' + tweetCriteria.username

		if hasattr(tweetCriteria, 'querySearch'):
			urlGetData += ' ' + tweetCriteria.querySearch

		if hasattr(tweetCriteria, 'near'):
			urlGetData += "&near:" + tweetCriteria.near + " within:" + tweetCriteria.within

		if hasattr(tweetCriteria, 'since'):
			urlGetData += ' since:' + tweetCriteria.since

		if hasattr(tweetCriteria, 'until'):
			urlGetData += ' until:' + tweetCriteria.until

		if hasattr(tweetCriteria, 'topTweets'):
			if tweetCriteria.topTweets:
				url = "https://twitter.com/i/search/timeline?q=%s&src=typd&max_position=%s"
		url = url % (urllib.parse.quote(urlGetData), refreshCursor)

		headers = [('Host', "twitter.com"),
		           ('User-Agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"),
		           ('Accept',
		            "application/json, text/javascript, */*; q=0.01"),
		           ('Accept-Language', "de,en-US;q=0.7,en;q=0.3"),
		           ('X-Requested-With',
		            "XMLHttpRequest"), ('Referer', url), ('Connection',
		                                                  "keep-alive")]
		if proxy:
			opener = urllib.request.build_opener(
			    urllib.request.ProxyHandler({
			        'http': proxy,
			        'https': proxy
			    }), urllib.HTTPCookieProcessor(cookieJar))
		else:
			opener = urllib.request.build_opener(
			    urllib.request.HTTPCookieProcessor(cookieJar))
		opener.addheaders = headers

		try:
			response = opener.open(url)
			jsonResponse = response.read()
		except:
			print(
			    "Twitter weird response. Try to see on browser: https://twitter.com/search?q=%s&src=typd"
			    % urllib.parse.quote(urlGetData))
			sys.exit()
			return
		dataJson = json.loads(jsonResponse)

		return dataJson


class TweetObtain:
	def __init__(self):
		pass
	def TweetObtain_function(self,videogame):
		"""Returns a clean dataframe for analysis using TweetCriteria and TweetManager"""
		print(videogame)
		tweet_date = []
		tweet_text = []
		tweetCriteria = TweetCriteria().setQuerySearch(videogame[0]). \
		setSince(videogame[1]).setUntil(videogame[2]).setMaxTweets(1000)
		tweets = TweetManager().getTweets(tweetCriteria)
		for tweet in tweets:
			tweet_date.append(tweet.date)
			tweet_text.append(tweet.text)
		df = pd.DataFrame(np.column_stack((tweet_date, tweet_text)))
		df['name'] = videogame[0]
		df['start_date'] = videogame[1]
		df['end_date'] = videogame[2]
		return df
