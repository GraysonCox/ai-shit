from functools import lru_cache

import discord
from discord.ext import commands

from . import _commands, _events


@lru_cache(maxsize=1)
def _create_bot() -> commands.Bot:
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="$", intents=intents)

    @bot.event
    async def on_ready():
        await _events.on_ready()

    @bot.event
    async def on_message(message: discord.Message):
        await _events.on_message(bot, message)

    @bot.command()
    async def search(ctx, arg):
        await _commands.search(ctx, arg)

    return bot


def run(token: str):
    _create_bot().run(token, log_handler=None)
