from userbot import miniub
from ..core.tg_manager import edit_delete


@miniub.client_cmd(pattern=r"\++", command=None, group_only=True)
async def _(event):
    reply_msg = await event.get_reply_message()
    if reply_msg is None:
        return await edit_delete(event, "`Reply to a message to use this command`")

    reply_msg_of_reply_msg = await reply_msg.get_reply_message()
    print(f"[{reply_msg.text}](https://t.me/c/{str(event.chat_id)[4:]}/{reply_msg.id})")
    if reply_msg_of_reply_msg is None:
        return await event.edit(
            f"[{reply_msg.text}](https://t.me/c/{str(event.chat_id)[4:]}/{reply_msg.id})"
        )

    else:
        await event.delete()
        return await reply_msg_of_reply_msg.reply(
            f"[{reply_msg.text}](https://t.me/c/{str(event.chat_id)[4:]}/{reply_msg.id})"
        )
