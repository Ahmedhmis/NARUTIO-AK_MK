from userbot import jmthon
from telethon import events
import asyncio
from userbot import jmthon
from ..core.managers import edit_or_reply
from . import *

plugin_category = "utils"

@jmthon.on(admin_cmd(pattern="وجه ?(.*)"))
async def srzo(event):
    if not event.is_reply:
        return await event.edit('- يجـب الرد على الرسـالة اولا')
    
    surze = event.pattern_match.group(1)
    if (surze == ''):
        surze = 1.5
    else:
        try:
            surze = float(surze)
        except:
            surze = 1.5
    await event.edit(f'**{surze} مـن الثواني**')
    mrzo = await event.get_reply_message()
    await event.edit('يتـم التعـرف عـلى المجمـوعات')
    muhgr = await event.client.get_dialogs()
    await event.edit(f'{len(muhgr)} تم العثور على الدردشات يتم تحديد المجموعات.')
    
    i = 0
    for grup in muhgr:
        if grup.is_group:
            await event.edit(f'{grup.name}  يتـم ارسـال الرسـالة الخـاصة بـك انتـظر...')
            try:
                await grup.send_message(mrzo)
            except:
                await event.edit(f'- لا يمكن إرسال رسالتك الى **{grup.name}** ')
                await asyncio.sleep(surze)
                continue
            i += 1
            await event.edit(f'- يتم الارسال الى {grup.name}')
            await asyncio.sleep(surze)
    await event.edit(f'تم الارسال بنجاح الى {i} من المجموعات بنجاح ✓')

@jmthon.ar_cmd(
    pattern="حول ?(.*)$",
    command=("حول", plugin_category),
)
async def gucast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "هـذا الامـر مقـيد للسـودو")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "** ⌯︙يجـب وضـع نـص مع الامـر للتوجيـه**")
    tt = event.text
    msg = tt[7:]
    await edit_or_reply(event, "** ⌯︙يتـم الـتوجيـة للخـاص انتـظر قليلا**")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await event.edit(
        f"تـم بنـجـاح فـي {done} من الـدردشـات , خطـأ فـي {er} من الـدردشـات"
    )
