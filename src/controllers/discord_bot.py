import logging

import discord

logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    logger.info(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    logger.info(message)
    if message.author == client.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await message.channel.send("Fuck you.")


def run(discord_token: str):
    client.run(discord_token, log_handler=None)
