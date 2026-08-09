import logging

from discord.ext import commands

logger = logging.getLogger(__name__)


async def search(ctx: commands.Context, arg: str):
    await ctx.send(f"Searching for {arg} ...")
