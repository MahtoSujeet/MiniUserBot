from telethon.client import TelegramClient
from telethon.sessions import StringSession
from config import Vars
from .logger import logging

LOGS = logging.getLogger("MiniBot")

client = TelegramClient(
    StringSession(Vars.SESSION_STRING), Vars.API_ID, Vars.API_HASH
)


client.start()
LOGS.info("Bot started successfully!")
