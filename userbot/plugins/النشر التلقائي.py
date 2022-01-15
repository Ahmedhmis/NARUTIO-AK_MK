from telethon import *
from userbot import jmthon
from userbot.sql_helper.autopost_sql import add_post, get_all_post, is_post, remove_post
from . import *

@jmthon.on(admin_cmd(pattern="نشر_تلقائي ?(.*)"))
async def _(event):
    if (event.is_private or event.is_group):
        return await edit_or_reply(event, "**- النشر التلقائي فقط للقنوات .")
    trz_ = event.pattern_match.group(1)
    if str(trz_).startswith("-100"):
        jm = str(trz_).replace("-100", "")
    else:
        jm = trz_
    if not jm.isdigit():
        return await edit_or_reply(event, "**يجب عليك وضع ايدي القناه اولا**")
    if is_post(jm , event.chat_id):
        return await edit_or_reply(event, "- تم تفعيل النشر لهذه القناه هنا بنجاح ✓")
    add_post(jm, event.chat_id)
    await edit_or_reply(event, f"**- يتم بدء النشر التلقائي من ** `{trz_}`")


@jmthon.on(admin_cmd(pattern="ايقاف_النشر ?(.*)"))
async def _(event):
    if (event.is_private or event.is_group):
        return await edit_or_reply(event, "النشر التلقائي فقط للقنوات.")
    trz_ = event.pattern_match.group(1)
    if str(trz_).startswith("-100"):
        jm = str(trz_).replace("-100", "")
    else:
        jm = trz_
    if not jm.isdigit():
        return await edit_or_reply(event, "**جب عليك وضع ايدي القناه اولا**")
    if not is_post(jm, event.chat_id):
        return await edit_or_reply(event, "- تم تعطيل النشر لهذه القناه هن بنجاح ✓.")
    remove_post(jm, event.chat_id)
    await edit_or_reply(event, f"**- تم ايقاف النشر من ** `{trz_}`")


@jmthon.ar_cmd(incoming=True)
async def _(event):
    if event.is_private:
        return
    chat_id = str(event.chat_id).replace("-100", "")
    channels_set  = get_all_post(chat_id)
    if channels_set == []:
        return
    for chat in channels_set:
        if event.media:
            await event.client.send_file(int(chat), event.media, caption=event.text)
        elif not event.media:
            await bot.send_message(int(chat), event.message)
