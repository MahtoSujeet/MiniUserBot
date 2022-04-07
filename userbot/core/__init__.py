from telethon.client import TelegramClient
from telethon.sessions import StringSession
from config import Vars
from .logger import LOG

print("creating client")
client = TelegramClient(StringSession(Vars.SESSION_STRING), Vars.API_ID, Vars.API_HASH)



print("Starting bot!")
client.start()

print("after start")
