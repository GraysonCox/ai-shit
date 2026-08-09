import logging
import os

from rich.logging import RichHandler

from .discord_stuff import bot


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler()],
    )
    discord_token = os.getenv("DISCORD_BOT_TOKEN")
    if not discord_token:
        raise ValueError("DISCORD_BOT_TOKEN is a required environment variable.")
    bot.run(discord_token)
