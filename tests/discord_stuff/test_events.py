from unittest.mock import AsyncMock, MagicMock, patch

import discord
import pytest
from discord.ext import commands

from src.discord_stuff import _events


@pytest.fixture(autouse=True)
def mock_utils():
    with patch.object(_events, "utils") as mock:
        mock.is_command = AsyncMock()
        yield mock


@pytest.fixture(autouse=True)
def mock_bot():
    yield MagicMock(spec=commands.Bot)


@pytest.fixture(autouse=True)
def mock_message():
    mock = MagicMock(spec=discord.Message)
    mock.channel = AsyncMock()
    mock.channel.typing = MagicMock()
    mock.channel.typing.return_value.__enter__.return_value = MagicMock()
    yield mock


@pytest.mark.asyncio
async def test_on_ready(mock_bot: MagicMock):
    await _events.on_ready()


@pytest.mark.asyncio
async def test_on_message_when_message_is_from_bot(
    mock_utils: MagicMock,
    mock_bot: MagicMock,
    mock_message: MagicMock,
):
    mock_utils.is_from_bot.side_effect = lambda m: m == mock_message
    mock_utils.is_command.return_value = False
    mock_utils.is_dm.return_value = False

    await _events.on_message(mock_bot, mock_message)

    mock_bot.process_commands.assert_not_called()
    mock_message.channel.send.assert_not_called()


@pytest.mark.asyncio
async def test_on_message_when_message_is_command(
    mock_utils: MagicMock,
    mock_bot: MagicMock,
    mock_message: MagicMock,
):
    mock_utils.is_from_bot.return_value = False
    mock_utils.is_command.return_value = True
    mock_utils.is_dm.return_value = False

    await _events.on_message(mock_bot, mock_message)

    mock_bot.process_commands.assert_called_once_with(mock_message)


@pytest.mark.asyncio
async def test_on_message_when_message_is_not_command(
    mock_utils: MagicMock,
    mock_bot: MagicMock,
    mock_message: MagicMock,
):
    mock_utils.is_from_bot.return_value = False
    mock_utils.is_command.return_value = False
    mock_utils.is_dm.side_effect = lambda m: m == mock_message

    await _events.on_message(mock_bot, mock_message)

    mock_message.channel.send.assert_called_once_with("Fuck you.")
