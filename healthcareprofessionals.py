########
# healthcareprofessionals.py
# 
# _Author_ : Jhanani Dhakshnamoorthy (jhananidhakshnamoorthy2013@u.northwestern.edu)
# _Date_  : 10/1/2013
# _Description_ : This module retrives twitter handles of different categories of healthcare professionals
#
# Tested on OSX 10.8.5
# Terminals running at least Python 2.5.2 to 3.3.2...
# 
# Uses Python-Twitter Api, a python wrapper for twitter api
# Throws twitter rate limit exceeded exception.
# 
# To launch this module enter the below in Terminal window:-
#
# >>> python healthcareprofessionals.py
# This module writes the twitter handles of healthcare professionals to healthcarepros.csv file
#######

import twitter
import csv
api = twitter.Api(consumer_key="whTJlHYFVtl0FT6JopL7Q",consumer_secret="XjF9Y7uva2mMhW9Ttb0Hi10p9UqOT8XmQynyNligbLY",access_token_key="1927394347-qtmdjoUditvaEBmQJlIBrenrlbXkDwFTRTvCamX",access_token_secret="8AFcMSOJgmEddrFonmMCoaNVm0ZRE9A0Pkvuz6XXwVE")
f = open("healthcarepros.csv", "w")

# Retrieves twitter handles of Pediatricians
def getPediatricians():
  prof = set()  
  additives = [" a", " the", " of", " and", " in", " I", " to", " it", " for", " you", ""]
  for a in additives:
    for p in ["pediatrician"]:
        s = api.GetUsersSearch(p+a, page=5, count=300)
        for i in s:
          prof.add(i.id)
          
  print "Pediatrician :"
  print len(prof)
  for i in prof:
    f.write(str(i)+'\r')
    print(i)
  
    
  
getPediatricians()

# Retrieves twitter handles of Pediatric Therapists
def getPediatricTherapists():
  profs = set()
  additives = [" a", " the", " of", " and", " in", " I", " to", " it", " for", " you", ""]
  for a in additives:
    for p in ["Pediatric Therapist"]:
        s = api.GetUsersSearch(p+a)
        for i in s:
          profs.add(i.id)
  
  print "Pediatric Therapists :"
  print len(profs)
  for i in profs:
    f.write(str(i)+'\r')
    print(i)
   
getPediatricTherapists()

# Retrievs twitter handles of Speech Therapists
def getSpeechTherapists():
  profs = set()
  additives = [" a", " the", " of", " and", " in", " I", " to", " it", " for", " you", ""]
  for a in additives:
    for p in ["Speech Therapist"]:
        s = api.GetUsersSearch(p+a, page=5, count=300)
        for i in s:
          profs.add(i.id)
  
  print "Speech Therapists :"
  print len(profs)
  for i in profs:
    f.write(str(i)+'\r')
    print(i)
    

getSpeechTherapists()

# Retrievs twitter handles of Physiotherapists
def getPhysiotherapists():
  profs = set()
  additives = [" a", " the", " of", " and", " in", " I", " to", " it", " for", " you", ""]
  for a in additives:
    for p in ["Physiotherapist"]:
        s = api.GetUsersSearch(p+a)
        for i in s:
          profs.add(i.id)
  
  print "Physiotherapists :"
  print len(profs)
  for i in profs:
    f.write(str(i)+'\r')
    print(i)
    

getPhysiotherapists()

# Retrievs twitter handles of PhysicalTherapists
def getPhysicalTherapists():
  profs = set()
  additives = [" a", " the", " of", " and", " in", " I", " to", " it", " for", " you", "", "that", "or"]
  for a in additives:
    for p in ["Physical Therapist"]:
        s = api.GetUsersSearch(p+a, page=5, count=300)
        for i in s:
          profs.add(i.id)
  
  print "Physical Therapists :"
  print len(profs)
  for i in profs:
    f.write(str(i)+'\r')
    print(i)
    

getPhysicalTherapists()



