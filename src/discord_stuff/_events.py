import logging

import discord
from discord.ext import commands

from . import utils

logger = logging.getLogger(__name__)


async def on_ready():
    logger.info("Ready!")


async def on_message(bot: commands.Bot, message: discord.Message):
    if utils.is_from_bot(message):
        return

    if await utils.is_command(bot, message):
        logger.debug(f"Received command: {message.content}")
        await bot.process_commands(message)
        return

    if utils.is_dm(message):
        logger.debug(f"Received DM message: {message.content}")
        async with message.channel.typing():
            await message.channel.send("Fuck you.")
