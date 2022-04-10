import os

from userbot import miniub
from userbot.utils.plugin_manager import PluginManager as pm
from userbot.core.tg_manager import edit_delete


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
        # second para is to make plugins_path to root
        # TODO fix this plugin path shit
        pm.install_plugin("file", "")
    except Exception as e:
        return await event.edit(f"`Install failed! {e}`")
    os.remove("file.py")
    return await event.edit("`Plugin install successfully!`")
