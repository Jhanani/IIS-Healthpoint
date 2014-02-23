from __future__ import division
import datagetter
import twitter
import random
import time
import operator
import pickle
api = twitter.Api("whTJlHYFVtl0FT6JopL7Q", "XjF9Y7uva2mMhW9Ttb0Hi10p9UqOT8XmQynyNligbLY", "1927394347-qtmdjoUditvaEBmQJlIBrenrlbXkDwFTRTvCamX", "8AFcMSOJgmEddrFonmMCoaNVm0ZRE9A0Pkvuz6XXwVE")
parents = datagetter.getKnownParents2()

def getHashtags(users):
  testtweets = datagetter.getMoreParentTweets([], [u for u in users])
  pickle.dump(testtweets, open("testtweets", "w"))
  testdict = datagetter.makeDict(testtweets)
  controltweets = pickle.load(open("utweets"))
  controldict = datagetter.makeDict(controltweets)
  wordprobs = datagetter.makeWordProbDict(testdict, controldict, mincount=50)
  hashtags = datagetter.getBestHashtags(wordprobs)
  return hashtags


getHashtags(parents)