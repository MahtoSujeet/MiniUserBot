import os
import asyncio

from .logger import logging

LOGS = logging.getLogger("EventManager")

async def edit_delete(event, text: str, time: int = 5, parse_mode = "md", link_preview= False):
    try:
        await event.edit(text, parse_mode=parse_mode, link_preview= link_preview)
        await asyncio.sleep(time)
        await event.delete()
    except Exception as e:
        LOGS.error(e)


async def edit_or_reply(
    event,
    text,
    parse_mode=None,
    link_preview=None,
    file_name=None,
    deflink=False,
    caption=None,
):  # sourcery no-metrics
    link_preview = link_preview or False
    reply_to = await event.get_reply_message()
    if len(text) < 4096 and not deflink:
        parse_mode = parse_mode or "md"
        await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)
        return event
    file_name = file_name or "output.txt"
    caption = caption or None
    with open(file_name, "w+") as output:
        output.write(text)
    if reply_to:
        await reply_to.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    await event.client.send_file(event.chat_id, file_name, caption=caption)
    await event.delete()
    os.remove(file_name)

