from telethon.errors import ChatIdInvalidError

from userbot import miniub
from ..core.tg_manager import edit_delete
from config import Config


@miniub.client_cmd(command="psave", pattern=r"psave\s*([\da-z]+)?")
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
        msg_ids = {reply_msg.id}
        async for msg in event.client.iter_messages(reply_msg.chat_id, min_id=reply_msg.id, reverse=True):
            await msg.forward_to("me")
            print(msg.sender_id, reply_msg.sender_id)
            if msg.sender_id == reply_msg.sender_id:
                msg_ids.add(msg.id)
            else:
                break
        await event.client.forward_messages(
            Config.SAVE_GROUP_ID, msg_ids, from_peer=reply_msg.chat_id
        )
        return await edit_delete(event, f"`Saved {len(msg_ids)} messages.`")
    if no_of_msg:
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
