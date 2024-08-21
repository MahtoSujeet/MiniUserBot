import contextlib
import os
import shutil

from telethon.errors.rpcerrorlist import MediaEmptyError

from userbot import miniub

from ..core.tg_manager import edit_or_reply
from ..utils.google_img_dl import googleimagesdownload

plugin_category = "misc"


@miniub.client_cmd(
    pattern=r"img(?: |$)(\d*)? ?([\s\S]*)",
    command=("img", plugin_category),
)
async def img_sampler(event):
    "Google image search."
    reply_to_id = await event.get_reply_message()
    if event.is_reply and not event.pattern_match.group(2):
        query = await event.get_reply_message()
        query = str(query.message)
    else:
        query = str(event.pattern_match.group(2))
    if not query:
        return await edit_or_reply(
            event, "Reply to a message or pass a query to search!"
        )
    cat = await edit_or_reply(event, "`Processing...`")
    if event.pattern_match.group(1) != "":
        lim = int(event.pattern_match.group(1))
        lim = min(lim, 10)
        if lim <= 0:
            lim = 1
    else:
        lim = 3
    response = googleimagesdownload()
    # creating list of arguments
    arguments = {
        "keywords": query.replace(",", " "),
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }
    # passing the arguments to the function
    try:
        print("before")
        paths = response.download(arguments)
        print("afer")
    except Exception as e:
        return await cat.edit(f"Error: \n`{e}`")
    lst = paths[0][query.replace(",", " ")]
    try:
        await event.client.send_file(event.chat_id, lst, reply_to=reply_to_id)
    except MediaEmptyError:
        for i in lst:
            with contextlib.suppress(MediaEmptyError):
                await event.client.send_file(event.chat_id, i, reply_to=reply_to_id)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await cat.delete()
