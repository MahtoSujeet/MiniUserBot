from platform import python_version
from datetime import datetime

from telethon import __version__ as telever

# Relative import of ..core didnt work
# TODO find out why
from userbot.core.session import miniub
from userbot import __version__ as minibot_ver
from ..core.constants import USERID, ALIVE_NAME


@miniub.client_cmd(command="alive")
async def _(client):
    start = datetime.now()
    await client.edit("`Checking!......`")
    end = datetime.now()
    ping = (end - start).microseconds / 1000

    alive_msg = f"""**☬  MiniUserBot is successfully working!  ☬**

➽  **Master**: [{ALIVE_NAME}](tg://user?id={USERID})
➽  **Ping**: `{ping} ms`
➽  **MiniUserBot**: `{minibot_ver}`
➽  **Telethon version**: `{telever}`
➽  **Python version**: `{python_version()}`
"""

    await client.edit(alive_msg)
