import asyncio

from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from ..sql_helper import antiflood_sql as sql
from ..utils import is_admin
from . import edit_or_reply, jmthon, CMD_HELP
#
plugin_category = "admin"
CHAT_FLOOD = sql.__load_flood_settings()

ANTI_FLOOD_WARN_MODE = ChatBannedRights(
    until_date=None, view_messages=None, send_messages=True
)


@jmthon.ar_cmd(incoming=True, groups_only=True)
async def _(event):
    if not CHAT_FLOOD:
        return
    catadmin = await is_admin(event.client, event.chat_id, event.client.uid)
    if not catadmin:
        return
    if str(event.chat_id) not in CHAT_FLOOD:
        return
    should_ban = sql.update_flood(event.chat_id, event.message.sender_id)
    if not should_ban:
        return
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id, event.message.sender_id, ANTI_FLOOD_WARN_MODE
            )
        )
    except Exception:
        no_admin_privilege_message = await event.client.send_message(
            entity=event.chat_id,
            message=f"**⌔∮ تنبيه التكرار للادمنية ⚠️**\n\n**▾∮ الى** @admin **المجموعة!**\n**▾∮ قام↫** [المستخدم](tg://user?id={event.message.sender_id})\n**▾∮بتكرار رسائله في المجموعة**\n",
            reply_to=event.message.id,
        )
        await asyncio.sleep(4)
        await no_admin_privilege_message.edit(
            "**⌔∮هذا هو الشخص الذي قام بالتكرار \n توقف يا رجل لكي لا تًطرد 📵**"
        )
    else:
        await event.client.send_message(
            entity=event.chat_id,
            message=f"**⌔∮ عملية التقيد التلقائي للتكرار ⚠️**\n\n**▾ قام ↫**[المستخدم ](tg://user?id={event.message.sender_id})\n**▾∮تم تقييده تلقائيًا بسبب عبوره حد السماح بالتكرار في هذه المجموعة**",
            reply_to=event.message.id,
        )


@jmthon.on(admin_cmd(pattern="ضع تكرار(?: |$)(.*)"))
async def _(event):
    "لوضع عدد تكرار الرسائل في المجموعة"
    input_str = event.pattern_match.group(1)
    event = await edit_or_reply(event, "**▾∮ يتم وضع عدد التكرار الجديد ... ♻️**")
    await asyncio.sleep(2)
    try:
        sql.set_flood(event.chat_id, input_str)
        sql.__load_flood_settings()
        await event.edit(f"**▾∮ عدد التكرار في المجموعة الان** ↫`┆{input_str}┆` 📊")
    except Exception as e:
        await event.edit(str(e))


@jmthon.on(admin_cmd(pattern="ضع تكرار(?: |$)(.*)"))
@jmthon.on(sudo_cmd(pattern="ضع تكرار(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    event = await edit_or_reply(event, "**جـارِ تحديث حد التكـرار...**")
    try:
        sql.set_flood(event.chat_id, input_str)
        sql.__load_flood_settings()
        await eor(
            "**تم وضـع حد التكـرار الى {} في هذه الدردشه...**".format(input_str)
        )
    except Exception as e:
        await eor(str(e))


CMD_HELP.update(
    {
        "مضاد التكرار": "**`.ضع تكرار <عدد>`\
\n الوظيفة : لتقييد الشخص تلقائيا بعد تحذيره ... \
"
    }
)ذ
