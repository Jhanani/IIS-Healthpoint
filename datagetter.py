from __future__ import division
import twitter
import random
import time
import operator
api = twitter.Api("whTJlHYFVtl0FT6JopL7Q", "XjF9Y7uva2mMhW9Ttb0Hi10p9UqOT8XmQynyNligbLY", "1927394347-qtmdjoUditvaEBmQJlIBrenrlbXkDwFTRTvCamX", "8AFcMSOJgmEddrFonmMCoaNVm0ZRE9A0Pkvuz6XXwVE")

def getKnownParents():
  parents = set()
  maxid = 0
  while len(parents) < 5000:
    search = api.GetSearch("\"my son\"", count=200, max_id = maxid, include_rts = False)
    search += api.GetSearch("\"my daughter\"", count=200, max_id = maxid, include_rts = False)
    print len(search)
    maxid = min([t.id for t in search])
    for t in search:
      parents.add(t.user) 
  return parents

def getKnownParents2():
  parents = set()
  additives = [" a", " the", " of", " and", " in", " I", " to", " it", " for", " you", ""]
  adjectives = ["devoted ", "loving ", ""]
  for a in additives:
    for p in ["father", "mother"]:
      for adj in adjectives:
        s = api.GetUsersSearch(adj+p+a)
        for i in s:
          parents.add(i)
  rents = set()
  for p in parents:
    d = p.description
    if "mother" in d or "father" in d or "Mother" in d or "Father" in d:
      rents.add(p)
  return rents

def getTokens(tweet):
  return tweet.replace(".", "").replace(",", "").split(" ")

def getTweets(userid):
  print userid
  try:
    tweets = api.GetUserTimeline(userid, count = 200)
    return tweets
  except:
    return "error"

def getTweetTokens(userid):
  tweets = getTweets(userid)
  tweettokens = []
  for t in tweets:
     if t != "error":
       try:
         tweettokens.append(getTokens(t.text))
       except:
         return "error"
  return tweettokens

def getParentTokens():
  parents = getKnownParents()
  tweets = []
  for p in parents:
    tweets.append(getTweets(p.id))
  return tweets 

def getSomeUserTokens(lb, ub, rents):
  tweets = []
  for i in range(lb, ub):
    tweets.append([t for t in getTweetTokens(rents[i].id)])
  return tweets

def countTokens(tweets):
  tokens = {}
  for t in tweets:
    for tok in t:
      if tok in tokens:
        tokens[tok] += 1
      else:
        tokens[tok] = 1
  return tokens

def getUnlabeledTweets():
  tweets = []
  i = 0
  straightfails = 0
  while straightfails < 15:
    print i
    try:
      tweets.append(getTweetTokens(random.randint(10000, 15000)))
      straightfails = 0
      i += 1
    except:
      print "failed"
      straightfails += 1
  return tweets
 
def makeDict(tweets):
  tweetlist = []
  for t in tweets:
    for tl in t:
      tweetlist.append(tl)
  dict = {}
  for t in tweetlist:
    for to in t:
      if to in dict:
        dict[to] += 1
      else:
        dict[to] = 1
  return dict

def getMoreParentTweets(parenttweets, rents):
  lb = len(parenttweets)
  mypts = parenttweets
  conserrors = 0
  while lb < len(rents): #and conserrors < 5:
    ts = getTweetTokens(rents[lb])
    #ts = getTweetTokens(rents[lb].id)
    if ts == "error":
      print ts
      conserrors += 1
      mypts.append(ts)
    else:
      conserrors = 0
      mypts.append(ts)
    lb += 1
    if conserrors >= 5:
      print "Rate-limited by Twitter at", time.time(), "seconds."
      print "Going to sleep for exactly 15 minutes -- 900 seconds."
      time.sleep(900)
  return mypts[:len(mypts)-5]  

def getProb(word, pdict, udict):
  pcount = max(pdict.get(word), 1)
  ucount = max(udict.get(word), 1)
  return pcount/(pcount + ucount)

def makeWordProbDict(pdict, udict, mincount=50):
  wpdict = {}
  for w in pdict:
    if max(pdict.get(w), 1) + max(udict.get(w), 1) >= mincount:
      wpdict[w] = getProb(w, pdict, udict)
  for w in udict:
    if w not in wpdict:
      if max(pdict.get(w), 0) + max(udict.get(w), 0) >= mincount:
        wpdict[w] = getProb(w, pdict, udict)
  wpdict.pop('')
  return wpdict

def getBestHashtags(wpdict):
  wplist = [(w, wpdict[w]) for w in wpdict if w[0] == '#']
  hlist = sorted(wplist, key = lambda(x): x[1])
  hlist.reverse()
  return hlist

def getFollowers(user):
  followers = api.GetFollowers(screen_name = user)
  return followers
