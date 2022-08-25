from cgitb import text
from email.mime import image
from tkinter import font
from urllib import request, response
import tweepy

# authenticate to twiiter

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_SECRET")
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")
#
access_token=""
access_token_secret=""
API_key=""
API_secret_key=""