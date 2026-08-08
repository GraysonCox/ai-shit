import logging
import os

from .controllers import discord_bot


def main():
    logging.basicConfig(level=logging.INFO)
    discord_token = os.getenv("DISCORD_TOKEN")
    if not discord_token:
        raise ValueError("DISCORD_TOKEN is a required environment variable.")
    discord_bot.run(discord_token)


if __name__ == "__main__":
    main()
