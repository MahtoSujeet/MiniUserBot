from userbot import miniub
from ..core.constants import USERID


@miniub.client_cmd(command="id")
async def _(event):
    reply_msg = await event.get_reply_message()
    if reply_msg:
        await event.edit(
            f"{reply_msg.sender.first_name}'s USER ID: `{reply_msg.sender_id}`"
        )

    elif event.is_group:
        await event.edit(f"My USER ID: `{USERID}`\nGroup ID: `{event.chat_id}`")

    else:
        await event.edit(f"My USER ID: `{USERID}`")
