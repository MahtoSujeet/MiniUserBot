from telethon.errors import ChatIdInvalidError

from userbot import miniub
from ..core.tg_manager import edit_delete
from config import Config


@miniub.client_cmd(command="psave", pattern=r"psave\s*([(\d|a-z)+])?")
async def _(event):
    if Config.SAVE_GROUP_ID is None:
        return await edit_delete(
            event, "Please add `SAVE_GROUP_ID` variable in order to use this command."
        )

    reply_msg = await event.get_reply_message()
    if reply_msg is None:
        return await edit_delete(event, "`Reply to a message to save it.`")

    no_of_msg = event.pattern_match.group(1)
    if no_of_msg == "all":
        msg_ids = list()
        for msg in event.client.iter_messages(reply_msg.chat_id, min_id=reply_msg.id):
            if msg.id == reply_msg.id:
                msg_ids.append(msg.id)
            else:
                break
        return await event.client.forward_messages(
            Config.SAVE_GROUP_ID, msg_ids, from_peer=reply_msg.chat_id
        )

    try:
        no_of_msg = int(no_of_msg)
    except ValueError:
        return await edit_delete(event, "`Please provide a valid argument`")

    if not (reply_msg.photo or reply_msg.video or reply_msg.document):
        return await edit_delete(
            event, "`Save some nice vidoes bhai, message dekhake hilaega kya!`", 10
        )

    try:
        if no_of_msg:
            await event.client.forward_messages(
                Config.SAVE_GROUP_ID,
                [msg_id for msg_id in range(reply_msg.id, reply_msg.id + no_of_msg)],
                from_peer=reply_msg.chat_id,
            )
            return await edit_delete(event, f"`Saved {no_of_msg} messages.`")

        await reply_msg.forward_to(Config.SAVE_GROUP_ID)
        return await edit_delete(event, "`Save the message.`")
    except ChatIdInvalidError:
        return await edit_delete(
            event,
            "Either you provided invalid `SAVE_GROUP_ID` or you aren't in the group.",
        )
