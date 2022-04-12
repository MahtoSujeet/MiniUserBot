from datetime import datetime

from userbot import miniub


@miniub.client_cmd(command="ping")
async def _(event):
    start = datetime.now()
    await event.edit("**♛ Pong**")
    await event.edit(f"**♛ Ping : **`{(datetime.now() - start).microseconds / 1000} ms`")
