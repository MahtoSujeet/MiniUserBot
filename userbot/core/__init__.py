from telethon.client import TelegramClient
from telethon.sessions import StringSession
from config import Vars
from .logger import logging

LOGS = logging.getLogger("MiniBot")

minibot = TelegramClient(
    StringSession(Vars.SESSION_STRING), Vars.API_ID, Vars.API_HASH
)


