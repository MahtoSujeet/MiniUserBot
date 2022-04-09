import sys
import asyncio

from telethon.sessions import StringSession

from .logger import logging
from .client import MiniUserBotCient
from config import Config


LOGS = logging.getLogger("MiniUserBot")
try:
    miniub = MiniUserBotCient(StringSession(Config.SESSION_STRING), api_id=Config.API_ID, api_hash=Config.API_HASH)
except Exception as e:
    LOGS.error(e)
    sys.exit()
