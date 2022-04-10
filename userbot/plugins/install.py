import os

from userbot import miniub
from userbot.utils import plugin_manager as pm
from ..core.tg_manager import edit_delete


@miniub.client_cmd(command="install")
async def _(event):
    reply_msg = await event.get_reply_message()

    # TODO there must be any better way to do this if statement, checkout later
    if reply_msg is None:
        return await edit_delete(event, "`Reply to a plugin in order to install it.`")
    elif reply_msg.document is None:
        return await edit_delete(event, "`Reply to a plugin in order to install it.`")

    await event.edit("`Downloading file...`")
    with open("file.py", "wb") as file:
        try:
            await event.client.download_file(reply_msg.document, file)
        except Exception as e:
            return await event.edit(f"`Download failed! {e}`")

    try:
        pm.load_module("file")
    except ImportError as e:
        return await event.edit(f"`Install failed! {e}`")
    os.remove("file.py")
    return await event.edit("`Plugin install successfully!`")
