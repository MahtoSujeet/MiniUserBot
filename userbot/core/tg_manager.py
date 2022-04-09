
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
