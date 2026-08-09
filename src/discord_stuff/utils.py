import discord
from discord.ext import commands


def is_from_bot(message: discord.Message) -> bool:
    return message.author.bot


async def is_command(bot: commands.Bot, message: discord.Message) -> bool:
    return (await bot.get_context(message)).valid


def is_dm(message: discord.Message) -> bool:
    return isinstance(message.channel, discord.DMChannel)
