import re
from userbot import jmthon
from . import BOTLOG, BOTLOG_CHATID
from userbot.sql_helper.filter_sql import (
    add_filter,
    get_filters,
    remove_all_filters,
    remove_filter,
)


@jmthon.on(admin_cmd(incoming=True))
async def filter_incoming_handler(handler):
    try:
        if (
            not (await handler.get_sender()).bot
            and (handler.sender_id) != handler.client.uid
        ):
            name = handler.raw_text
            filters = get_filters(handler.chat_id)
            if not filters:
                return
            for trigger in filters:
                pattern = r"( |^|[^\w])" + re.escape(trigger.keyword) + r"( |$|[^\w])"
                if re.search(pattern, name, flags=re.IGNORECASE):
                    if trigger.f_mesg_id:
                        msg_o = await handler.client.get_messages(
                            entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id)
                        )
                        await handler.reply(msg_o.message, file=msg_o.media)
                    elif trigger.reply:
                        await handler.reply(trigger.reply)
    except AttributeError:
        pass


@jmthon.on(admin_cmd(pattern="اضف رد (.*)"))
@jmthon.on(sudo_cmd(pattern="اضف رد (.*)", allow_sudo=True))
async def add_new_filter(new_handler):
    if new_handler.fwd_from:
        return
    keyword = new_handler.pattern_match.group(1)
    string = new_handler.text.partition(keyword)[2]
    msg = await new_handler.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG:
            await new_handler.client.send_message(
                BOTLOG_CHATID,
                f"⌔∮ الردود\
            \n- ايدي الدردشه: {new_handler.chat_id}\
            \n- الرد: {keyword}\
            \n- يتم حفظ الرسالة التالية كبيانات رد على المستخدمين في الدردشه ، يرجى عدم حذفها !!",
            )
            msg_o = await new_handler.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=new_handler.chat_id,
                silent=True,
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                new_handler,
                "`يتطلب حفظ الوسائط كردود تعيين فار BOTLOG_CHATID",
            )
            return
    elif new_handler.reply_to_msg_id and not string:
        rep_msg = await new_handler.get_reply_message()
        string = rep_msg.text
    success = "- الرد **{}** تم {} بنجاح "
    if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(new_handler, success.format(keyword, "اضافته"))
    remove_filter(str(new_handler.chat_id), keyword)
    if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(new_handler, success.format(keyword, "تحديثه"))
    await edit_or_reply(new_handler, f"خطأ أثناء تعيين الـرد لـ {keyword}")


@jmthon.on(admin_cmd(pattern="الردود$"))
@jmthon.on(sudo_cmd(pattern="الردود$", allow_sudo=True))
async def on_snip_list(event):
    if event.fwd_from:
        return
    OUT_STR = "**⌔∮ لاتوجـد ردود في هذه الدردشة**"
    filters = get_filters(event.chat_id)
    for filt in filters:
        if OUT_STR == "**⌔∮ لاتوجـد ردود في هذه الدردشة**":
            OUT_STR = "**- قائمـه الـردود في هذه الدردشـه : **\n"
        OUT_STR += "- {}  \n".format(filt.keyword)
    await edit_or_reply(
        event,
        OUT_STR,
        caption="**- الردود المضـافه في هذه الدردشة**",
        file_name="filters.text",
    )


@jmthon.on(admin_cmd(pattern="حذف رد (.*)"))
@jmthon.on(sudo_cmd(pattern="حذف رد (.*)", allow_sudo=True))
async def remove_a_filter(r_handler):
    if r_handler.fwd_from:
        return
    filt = r_handler.pattern_match.group(1)
    if not remove_filter(r_handler.chat_id, filt):
        await r_handler.edit("- الرد **{}** غير موجود ".format(filt))
    else:
        await r_handler.edit("- الرد **{}** تم حذفه بنجاح  ✓".format(filt))


@jmthon.on(admin_cmd(pattern="حذف الردود$"))
@jmthon.on(sudo_cmd(pattern="حذف الردود$", allow_sudo=True))
async def on_all_snip_delete(event):
    if event.fwd_from:
        return
    filters = get_filters(event.chat_id)
    if filters:
        remove_all_filters(event.chat_id)
        await edit_or_reply(
            event,
            f"**- تم حذف جـميع الردود في هذه الدردشة بنجاح ✓**",
        )
    else:
        await edit_or_reply(event, f"**- لا توجد ردود في هذه المجموعه **")


CMD_HELP.update(
    {
        "الردود": "**الامـر :** `.الردود`\
    \n  •  **الأستخدام: **لعرض جميع الردود المضافة في الدردشة\
    \n\n  •  **الامـر :** `.اضف رد`  بالرد على الرسالة بـ .اضف رد <كلمة>\
    \n  •  **الأستخدام: **لحفظ الرسالة التي عملت لها رد كـرد للكلمة\
    \n\n  •  **الامـر :** `.حذف رد <كلمة>`\
    \n  •  **الأستخدام: ** لحذف رد معين من الدردشة.\
    \n\n  •  **الامـر :** `.حذف الردود` \
    \n  •  **الأستخدام: ** لحذف جميع الردود المضافة في الدردشة"
    }
)
