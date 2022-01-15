from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers.utils import _catutils, yaml_format

plugin_category = "tools"


@jmthon.ar_cmd(
    pattern="الملفات$",
    command=("الملفات", plugin_category),
    info={
        "header": "To list all plugins in userbot.",
        "usage": "{tr}plugins",
    },
)
async def _(event):
    "To list all plugins in userbot"
    cmd = "ls userbot/plugins"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = f"**[جـمـثـون](tg://need_update_for_some_feature/) الـمـلفـات:**\n{o}"
    await edit_or_reply(event, OUTPUT)



@jmthon.ar_cmd(
    pattern="متى$",
    command=("متى", plugin_category),
    info={
        "header": "To get date and time of message when it posted.",
        "usage": "{tr}when <reply>",
    },
)
async def _(event):
    "To get date and time of message when it posted."
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    await edit_or_reply(
        event, f"**⌯︙نـشـرت هـذه الـرسالة فـي  :** `{yaml_format(result)}`"
    )
