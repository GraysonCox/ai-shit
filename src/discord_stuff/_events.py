import logging

import discord
from discord.ext import commands

logger = logging.getLogger(__name__)


async def on_ready():
    logger.info("Ready!")


async def on_message(bot: commands.Bot, message: discord.Message):
    if message.author == bot.user:
        return

    ctx = await bot.get_context(message)
    if ctx.valid:
        await bot.process_commands(message)
        return

    if isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await message.channel.send("Fuck you.")
