import asyncio
import re

from userbot import miniub
from . import stripe_chk
from ..core.tg_manager import edit_delete



@miniub.client_cmd(command="chk")
async def _(event):
    msg = await event.edit("`Checking....`")
    card = re.findall(r"\d+", event.raw_text)
    try:
        ccn, month, year, cvc = card
    except ValueError:
        return await edit_delete(msg, "**Please provide valid input.**\n\n`cc|month|year|cvc`")
    result = await stripe_chk.check(ccn, month, year, cvc)

    await msg.edit(
        f"""**Card:** `{card}`
**Result:** `{result}`"""
    )
