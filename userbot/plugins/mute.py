import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, get_user_from_event

plugin_category = "admin"

# =================== الكـــــــــــــــتم  ===================  #


@jmthon.ar_cmd(
    pattern="كتم(?:\s|$)([\s\S]*)",
    command=("كتم", plugin_category),
    info={
        "header": " لكـتم الشخـص في جميـع المجموعات.",
        "description": "لعمل كتم وحذف جميع رسائل المستخدم في جميع المجموعات يتطلب صلاحيات حذف",
        "الأستـخدام": " {tr}كتم <ايدي/معرف/بالرد>",
    },
)
async def startgmute(event):
    "لكـتم وحـذف جميـع رسـائل المستخـدم في جميع المجموعـات التـي فيهـا مشـرف"
    if event.is_private:
        await event.edit("**... قـد تحـدث بعـض المـشاكـل أو الأخـطاء ...**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == jmthon.uid:
            return await edit_or_reply(
                event, "**𖡛... . لمـاذا تࢪيـد كتم نفسـك؟  ...𖡛**"
            )
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "**𖡛... غيـر قـادر عـلى جـلب مـعلومات الـشخص ...𖡛**"
        )
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"**𖡛... هـذا الشـخص مكـتوم بـنجاح ...𖡛**",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خـطأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"** تـم كـتم الـمستخـدم بـنجاح  ،🔕 **",
            )
        else:
            await edit_or_reply(
                event,
                f"** تـم كـتم الـمستخـدم بـنجاح  ،🔕 **",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                " الـكتم\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**السبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                " الـكتم\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


# =================== الغـــــــــــــاء الكـــــــــــــــتم  ===================  #


@jmthon.ar_cmd(
    pattern="الغاء كتم(?:\s|$)([\s\S]*)",
    command=("الغاء كتم", plugin_category),
    info={
        "header": "لألـغاء كـتم الشخـص في جميـع المجموعات.",
        "description": "يستخدم هذا الامر عندما تكتم شخص فقـط ",
        "usage": "{tr}الغاء كتم <معرف/ايدي>",
    },
)
async def endgmute(event):
    "لألـغاء كتـم الشـخص 📮."
    if event.is_private:
        await event.edit("**... قـد تحـدث بعـض المـشاكـل أو الأخـطاء ...**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == jmthon.uid:
            return await edit_or_reply(event, "**... لمـاذا تࢪيـد كتم نفسـك؟ ...**")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "**... غيـࢪ قـادࢪ عـلى جـلب مـعلومات الـشخص ...**"
        )
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, f"**... هـذا الشـخص غيـࢪ مكـتوم اصلا  ...**")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خطـأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"** تـم الغـاء كـتم الـمستخـدم بـنجاح  🔔، **",
            )
        else:
            await edit_or_reply(
                event,
                f"** تـم الـغاء كتـم  الـمستخـدم بـنجاح  🔔، **",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "، الغـاء الـكتم\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**السبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                " الغـاء الـكتم \n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )


# ===================================== #


@jmthon.ar_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


# =====================================  #
