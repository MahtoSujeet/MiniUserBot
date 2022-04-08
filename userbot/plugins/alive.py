from userbot.core import minibot
from telethon import events
from config import Vars

print("alive")

@minibot.on(
    events.NewMessage(outgoing=True, pattern=f"{Vars.COMMAND_HANDLER}alive")
)
async def alive(client):
    await client.edit("**Bot is running successfully!**")
