from userbot.core import minibot
from telethon import events
from config import Vars

from userbot import __version__ as minibot_ver
from platform import python_version
from telethon import __version__ as telever
from datetime import datetime


@minibot.on(events.NewMessage(outgoing=True, pattern=f"{Vars.COMMAND_HANDLER}alive"))
async def alive(client):

    start = datetime.now()
    await client.edit("`Checking!......`")
    end = datetime.now()
    ping = (end - start).microseconds / 1000

    alive_msg = f"""**I am running!**
Master: **Sujeet**
Ping: `{ping} ms`
MiniUserBot: `{minibot_ver}`
Telethon version: `{telever}`
Python version: `{python_version()}
"""

    await client.edit(alive_msg)
