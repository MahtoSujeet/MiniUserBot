from userbot import miniub
from ..core.tg_manager import edit_delete


@miniub.client_cmd(command="del")
async def _(event):
    reply_msg = await event.get_reply_message()
    if reply_msg is None:
        return await edit_delete(event, "`Reply to any message to delete it`", 5)

    await event.delete()
    await reply_msg.delete()


@miniub.client_cmd(command="purge")
async def _(event):
    reply_msg = await event.get_reply_message()
    if reply_msg is None:
        return await edit_delete(event, "`Reply to any message to purge from there`", 5)

    entity = event.to_id
    start_id = reply_msg.id
    end_id = event.id  # excluding purge msg

    del_msges = (
        await event.client.delete_messages(entity, list(range(start_id, end_id)))
    )[0]

    await edit_delete(event, f"`Plurged {del_msges.pts_count} messages.`", 3)
