import os
from dotenv import load_dotenv
from internal.bot.discord_bot import run_discord_bot

load_dotenv()  # Load environment variables from .env file

if __name__ == "__main__":
    discord_token = os.getenv("DISCORD_TOKEN")
    run_discord_bot(discord_token)