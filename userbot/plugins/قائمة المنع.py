import re

from telethon.utils import get_display_name

from userbot import jmthon, CMD_HELP

from ..core.managers import edit_or_reply
from ..sql_helper import blacklist_sql as sql
#
# for ~ @Jmthon ~ @RR7PP


@jmthon.ar_cmd(incoming=True, groups_only=True)
async def on_new_message(event):
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"**⌔∮ عذرًا ليست لدي صلاحية في {get_display_name(await event.get_chat())}.\nلذا سيتم إزالة الكلمات الممنوعة من هذه المجموعة**",
                )
                for word in snips:
                    sql.rm_from_blacklist(event.chat_id, word.lower())
            break


@jmthon.on(admin_cmd(pattern="منع(?:\s|$)([\s\S]*)"))
async def _(event):
    text = event.pattern_match.group(1)
    to_blacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await edit_or_reply(
        event,
        "**▾∮ تم اضافة** `{}` **الى قائمة المنع الغير مرغوب به ◛**".format(
            len(to_blacklist)
        ),
    )


@jmthon.on(admin_cmd(pattern="الغاء منع(?:\s|$)([\s\S]*)"))
async def _(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )
    successful = sum(
        bool(sql.rm_from_blacklist(event.chat_id, trigger.lower()))
        for trigger in to_unblacklist
    )
    await edit_or_reply(
        event,
        f"**▾∮ تم الغاء منع** `{successful} / {len(to_unblacklist)}` **من قائمة المنع ◙**",
    )


@jmthon.on(admin_cmd(pattern="قائمة المنع$"))
async def _(event):
    all_blacklisted = sql.get_chat_blacklist(event.chat_id)
    OUT_JM = "**▾∮ اليكَ قائمة الكلمات الممنوعة 📝 ↶\n\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_JM += f"▾☜ {trigger} \n"
    else:
        OUT_JM = "**▾∮ لم تقوم بأضافة اي كلمة الى قائمة المنع\n استخدم `.منع` **<الكلمة> ✎✓**"
    await edit_or_reply(event, OUT_JM)

CMD_HELP.update(
    {
        "قائمة المنع": ".منع <كلمة>\n الوظيفة⦂ لمنع ارسال كلمه معينه في الدردشة\
            \n\n`.القائمة السوداء`\nالوظيفة ⦂ لعرض الكلمات التي تم منعها في الدردشة.\
            \n\n`.الغاء منع` <كلمة>\nالوظيفة ⦂ للسماح في الكلمة في هذه الدردشة"
    }
)
