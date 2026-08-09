import logging
import os

from rich.logging import RichHandler

from .discord_stuff import bot


def _get_env(key: str, default_value: str | None = None) -> str:
    value = os.getenv(key)

    if value:
        return value

    if default_value:
        return default_value

    raise ValueError(f"{key} is a required environment variable.")


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler()],
    )

    bot.run(_get_env("DISCORD_BOT_TOKEN"))
