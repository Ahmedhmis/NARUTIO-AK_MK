import asyncio

from userbot import jmthon


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
