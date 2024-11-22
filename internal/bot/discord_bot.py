import discord
from discord.ext import commands
from .bluesky_bot import post_to_bluesky
from .x_bot import post_to_x

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command()
async def post(ctx, platform: str, *, message: str):
    try:
        platform = platform.lower()
        if platform == "bsky":
            post_to_bluesky(message)
            await ctx.send("Posted successfully to Bluesky!")
        elif platform == "x":
            post_to_x(message)
            await ctx.send("Posted successfully to X/Twitter!")
        elif platform == "both":
            post_to_bluesky(message)
            post_to_x(message)
            await ctx.send("Posted successfully to X/Twitter and Bluesky!")
        else:
            await ctx.send("Invalid platform. Use 'bsky', 'x', or 'both'")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

def run_discord_bot(token):
    bot.run(token)