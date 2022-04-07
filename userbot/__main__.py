from telethon import events
from config import Vars
from .core import client, logger


print("running main file too")
@client.on(events.NewMessage(outgoing=True, pattern=f"{Vars.COMMAND_HANDLER}alive"))
async def alive(client):
    await client.reply("hey")


client.run_until_disconnected()
