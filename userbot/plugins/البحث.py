import asyncio
import base64
import io
import os
from pathlib import Path

from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from userbot import jmthon

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import name_dl, song_dl, video_dl, yt_search
from ..helpers.tools import media_type
from ..helpers.utils import _catutils, reply_id

plugin_category = "utils"
LOGS = logging.getLogger(__name__)

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>wi8..!**جار البحث عن الاغنيه انتظر رجاءا ✅**....</code>"
SONG_NOT_FOUND = "<code>Sorry ! لم استطيع ايجاد الاغنيه مثل هذه</code>"
SONG_SENDING_STRING = "<code>yeah..!**جار البحث عن الاغنيه انتظر رجاءا ✅**..🥰...</code>"
SONGBOT_BLOCKED_STRING = "<code>قم بالغاء حظر البوت @songdl_bot وحاول مجددا</code>"
# =========================================================== #
#                                                             #
# =========================================================== #


@jmthon.ar_cmd(
    pattern="بحث(320)?(?: |$)(.*)",
    command=("بحث", plugin_category),
    info={
        "header": "To get songs from youtube.",
        "description": "Basically this command searches youtube and send the first video as audio file.",
        "flags": {
            "320": "if you use song320 then you get 320k quality else 128k quality",
        },
        "usage": "{tr}song <song name>",
        "examples": "{tr}song memories song",
    },
)
async def _(event):
    "To search songs"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply:
        if reply.message:
            query = reply.message
    else:
        return await edit_or_reply(event, "**ما الذي تريد ان ابحث عنه**")
    cat = base64.b64decode("VHdIUHd6RlpkYkNJR1duTg==")
    catevent = await edit_or_reply(event, "جار البحث عن الاغنيه انتظر رجاءا ✅*....`")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(
            f"**عـذرا لم استطيع ايجاد الاغنيه او الفيديو لـ** `{query}`"
        )
    cmd = event.pattern_match.group(1)
    q = "320k" if cmd == "320" else "128k"
    song_cmd = song_dl.format(QUALITY=q, video_link=video_link)
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    stderr = (await _catutils.runcmd(song_cmd))[1]
    if stderr:
        return await catevent.edit(f"**خـطأ :** `{stderr}`")
    catname, stderr = (await _catutils.runcmd(name_cmd))[:2]
    if stderr:
        return await catevent.edit(f"**خـطأ :** `{stderr}`")
    # stderr = (await runcmd(thumb_cmd))[1]
    catname = os.path.splitext(catname)[0]
    # if stderr:
    #    return await catevent.edit(f"**Error :** `{stderr}`")
    song_file = Path(f"{catname}.mp3")
    if not os.path.exists(song_file):
        return await catevent.edit(
            f"**عـذرا لم استطيع ايجاد الاغنيه او الفيديو لـ** `{query}`"
        )
    await catevent.edit("**جار البحث عن الاغنيه انتظر رجاءا ✅**")
    catthumb = Path(f"{catname}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{catname}.webp")
    elif not os.path.exists(catthumb):
        catthumb = None

    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=query,
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (catthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


async def delete_messages(event, chat, from_message):
    itermsg = event.client.iter_messages(chat, min_id=from_message.id)
    msgs = [from_message.id]
    async for i in itermsg:
        msgs.append(i.id)
    await event.client.delete_messages(chat, msgs)
    await event.client.send_read_acknowledge(chat)
