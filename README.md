# Social Media Cross-Poster Discord Bot

A Discord bot that allows users to post messages to X (Twitter) and Bluesky simultaneously through simple commands.

## Features

- Post to X (Twitter)
- Post to Bluesky
- Post to both platforms simultaneously
- Simple Discord command interface

## Prerequisites

- Python 3.8 or higher
- Discord bot token
- X (Twitter) API credentials
- Bluesky account credentials

## Installation

1. Clone the repository:

```bash
git clone https://github.com/allgeo/discord-bsky-x-bot.git
cd discord-bsky-x-bot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file based on the `.example.env` template and fill in your credentials:

```bash
cp .example.env .env
```

## Usage

The bot responds to the following commands:

- `!post x [message]` - Post to X (Twitter)
- `!post bsky [message]` - Post to Bluesky
- `!post both [message]` - Post to both platforms

Examples:

```bash
!post x "Hello, X/Twitter!"
!post bsky "Hello, Bluesky!"
!post both "Hello, X/Twitter and Bluesky!"
```

## Configuration

### Discord Bot Setup

1. Create a new application at [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a bot for your application
3. Enable message content intent in the bot settings
4. Copy the bot token to your `.env` file

### Bluesky Setup

1. Create a Bluesky account
2. Generate an app password
3. Add your username and app password to the `.env` file

### X (Twitter) Setup

1. Refer to [Twitter Developer Platform](https://developer.twitter.com/) for instructions on how to create an app and generate API keys and tokens

## Contributing

Contributions are welcome. This is an ongoing project and will be updated with more features over time.
