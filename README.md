IIS-Healthpoint
===============
Overview

The goal of Baby Steps is to help improve the outreach of pathways, a non-profit organization that empower health professionals and parents with knowledge of early detection and early intervention for children’s health. Our tool accumulates information from two different channels twitter and online communities. This project is developed in python. It uses twitter REST API and python-twitter library for retrieving twitter handles and hash tags.  

Installation

•	You need python 2.7.5 and above to run this application. Install python from http://www.python.org/getit/
•	Download python-twitter api from github https://github.com/bear/python-twitter 
•	Install python-twitter by typing python setup.py install in command prompt or terminal by redirecting into proper directory
•	Install beautiful soup

Description

•	Datagetter.py 

Creates a sample group for each class by searching Twitter profiles for words and phrases that indicated membership in that particular class, such as “parent,” or “my baby” for the parent group

•	Hashtags.py 

Gets the most-more-proportionally-used hash tags by the twitter users in each class of users, which is a list of user ids. It will compare these to a control group of tweets, which it will generate automatically. It stores the control group’s tweets in a pickled file called “controltweets”. It stores the hash tags most used by parents in a file called “parent-hashtags” and hash tags used by healthcare professionals in a file called “healthcarepros-hashtags”

•	Healthcareprofessionals.py 

Based on ad-hoc analysis of followers of pathways, it uses a list of search terms to identify the healthcare professionals. It searches for twitter profiles for terms and phrases, which indicate them as a healthcare professional, such as “pediatrician”, “speech therapist”

•	Mailblast.py

This module is responsible for encapsulating the information retrieved from twitter and online communities. It reads the hash tags used by each class of users and embeds them in html. It also encapsulates the URL links of the threads that are relevant to pathways from online parenting forums. It uses SMTP library in python to send out an email newsletter. The message is sent using a local SMTP server, and the delivery model currently uses an existing email provider to send out the newsletter

Usage

•	Run healthcareprofessionals.py to get twitter handles of healthcare professionals. The twitter handles are stored in healthcarepros.csv file
•	Run datagetter.py to get the list of user ids of known parents
•	Run hashtags.py to get relevant hash tags used by parents and healthcare professionals. This script writes the hash tags in separate files
•	Once you have hash tags in separate output files, run mailblast.py to send newsletter containing hash tags and posts in online communities to the desired recipients

Configuration
	
	This tool can be configured to include multiple recipients to receive email newsletter by adding the desired email addresses to mailblast.py. It can also configured to search twitter and online forums for other category of users and provide hash tags and posts relevant to that class of users.
	
