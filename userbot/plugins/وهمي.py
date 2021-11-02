import asyncio

from telethon.errors import ChatAdminRequiredError as no_admin
from telethon.tl.functions.messages import ExportChatInviteRequest

from userbot import jmthon

from ..core.managers import edit_or_reply as eod
from . import *


@jmthon.on(admin_cmd(pattern="كتابة(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع الكتابة الوهمية لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@jmthon.on(admin_cmd(pattern="صوتية(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع ارسال الصوتية الوهمية لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@jmthon.on(admin_cmd(pattern="فيد(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع ارسال الفيديو الوهمي لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@jmthon.on(admin_cmd(pattern="لعبة(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع اللعب الوهمي لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


@jmthon.on(admin_cmd(pattern="الرابط$"))
async def _(e):
    rr = await edit_or_reply(e, "**يتم جلب الرابط انتظر **")
    try:
        r = await e.client(
            ExportChatInviteRequest(e.chat_id),
        )
    except no_admin:
        return await eod(rr, "عذرا انت لست مشرف في هذه الدردشة", time=10)
    await eod(rr, f"- رابط الدردشة\n {r.link}")


@jmthon.on(admin_cmd(pattern="للكل تاك$"))
async def listall(jmthon):
    if jmthon.fwd_from:
        return
    mentions = "- هذه هي قائمة جميع الاعضاء هنا: "
    chat = await jmthon.get_input_chat()
    async for x in borg.iter_participants(chat, 2000):
        mentions += f" \n[{x.first_name}](tg://user?id={x.id})"
    await jmthon.reply(mentions)
    await jmthon.delete()


# don't kang the file your mother puusy
# code by @jmthon
