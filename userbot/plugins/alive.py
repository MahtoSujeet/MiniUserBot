from platform import python_version
from datetime import datetime

from telethon import __version__ as telever, events

# Relative import of ..core didnt work
# TODO find out why
from userbot.core.session import miniub
from userbot import __version__ as minibot_ver


@miniub.client_cmd(command="alive")
async def alive(client):
    print(client.sender_id)
    print(client.sender.first_name)

    start = datetime.now()
    await client.edit("`Checking!......`")
    end = datetime.now()
    ping = (end - start).microseconds / 1000

    alive_msg = f"""**☬  MiniUserBot is successfully working!  ☬**

➽  **Master**: [{client.sender.first_name}](tg://user?id={client.sender_id})
➽  **Ping**: `{ping} ms`
➽  **MiniUserBot**: `{minibot_ver}`
➽  **Telethon version**: `{telever}`
➽  **Python version**: `{python_version()}`
"""

    await client.edit(alive_msg)
