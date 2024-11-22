import os
import tweepy
from dotenv import load_dotenv
import re

load_dotenv()

def post_to_x(text):
    client = tweepy.Client(
        consumer_key=os.getenv("X_API_KEY"),
        consumer_secret=os.getenv("X_API_SECRET"),
        access_token=os.getenv("X_ACCESS_TOKEN"),
        access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
    )
    
    # ensure the text is within the character limit
    if len(text) > 280:
        text = text[:280]
    
    client.create_tweet(text=text)