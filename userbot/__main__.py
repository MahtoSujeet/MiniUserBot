from telethon import events
from config import Vars
from .core import client, logger


@client.on(events.NewMessage(outgoing=True, pattern=f"{Vars.COMMAND_HANDLER}alive"))
async def alive(client):
    await client.edit("**Bot is running successfully!**")


client.run_until_disconnected()
