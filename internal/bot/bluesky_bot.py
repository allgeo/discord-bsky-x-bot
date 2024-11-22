import os
from atproto import Client
from dotenv import load_dotenv

load_dotenv()

def post_to_bluesky(text):
    client = Client()
    client.login(
        os.getenv("BLUESKY_USERNAME"),
        os.getenv("BLUESKY_APP_PASSWORD")
    )
    
    client.send_post(text)