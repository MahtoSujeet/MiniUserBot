import asyncio
import sys

from telethon.sessions import StringSession
from telethon import events

from .logger import logging
from .client import MiniUserBotCient
from config import Config
from .constants import USERID


LOGS = logging.getLogger("MiniUserBot")
try:
    miniub = MiniUserBotCient(
        StringSession(Config.SESSION_STRING),
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
    )
except Exception as e:
    LOGS.error(e)
    sys.exit()


miniub.tgbot = tgbot = MiniUserBotCient(
    "minitgbot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
).start(bot_token=Config.BOT_TOKEN)

