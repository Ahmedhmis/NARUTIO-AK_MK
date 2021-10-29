import re

from telethon.utils import get_display_name

from userbot import jmthon

from ..core.managers import edit_or_reply
from ..sql_helper import blacklist_sql as sql

plugin_category = "admin"

# for ~ @Jmthon ~ @RR7PP


@jmthon.ar_cmd(incoming=True, groups_only=True)
async def on_new_message(event):
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    # catadmin = await is_admin(event.client, event.chat_id, event.client.uid)
    # if not catadmin:
    #     return
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


@jmthon.ar_cmd(
    pattern="منع(?:\s|$)([\s\S]*)",
    command=("منع", plugin_category),
    info={
        "عمل الملف": "لإضافة كلمات غير مرغوب بها إلى قاعدة البيانات",
        "وصف الملف": "ستتم إضافة الكلمة أو الكلمات المحددة إلى القائمة السوداء في تلك الدردشة المحددة إذا أرسلها أي مستخدم يتم حذف الرسالة.",
        "ملاحظة": "إذا كنت تريد اضافة اكثر من كلمة في امر واحد ، فتذكر أنه يجب إعطاء كلمة جديدة في سطر واحد ليس هكذا ( .منع مرحبا هاي ) \n انما تقوم بمثل هذا ↫ .منع مرحبا\nهاي",
        "طريقة الاستخدام": "{tr}منع <الكلمة المراد منعها>",
        "امثلة": ["{tr}منع هلو\n" "\n{tr}منع هلو\nهاي"],
    },
    # groups_only=True,
    # require_admin=True,
)
async def _(event):
    "لإضافة كلمات غير مرغوب بها إلى قاعدة البيانات"
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


@jmthon.ar_cmd(
    pattern="الغاء منع(?:\s|$)([\s\S]*)",
    command=("الغاء منع", plugin_category),
    info={
        "عمل الملف": "لازالة كلمة ممنوعة من المجموعة",
        "وصف الملف": "ستتم إزالة الكلمة أو الكلمات المعينة من قائمة المنع في المحادثة المحددة",
        "ملاحظة": "اذا كنت تريد حذف اكثر من كلمة فـ يجب عليك اعطاء اكثر من سطر مثل .الغاء منع هلو\nهاي",
        "طريقة الاستخدام": "{tr}الغاء منع <الكلمة>",
        "امثلة": ["{tr}الغاء منع هلو", "\n{tr}الغاء منع هلو\nهاي"],
    },
    # groups_only=True,
    # require_admin=True,
)
async def _(event):
    "لازالة كلمة ممنوعة من بياناتي"
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


@jmthon.ar_cmd(
    pattern="قائمة المنع$",
    command=("قائمة المنع", plugin_category),
    info={
        "عمل الملف": "لاظهار الكلمات الممنوعة في المجموعة",
        "وصف الملف": "يظهر لك الكلمات الممنوعة في المحادثة المحددة",
        "طريقة الاستخدام": "{tr}قائمة المنع",
    },
    # groups_only=True,
    # require_admin=True,
)
async def _(event):
    "لمشاهدة الكلمات الممنوعة من مجموعة محددة"
    all_blacklisted = sql.get_chat_blacklist(event.chat_id)
    OUT_STR = "**▾∮ اليكَ قائمة الكلمات الممنوعة 📝 ↶\n\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"▾☜ {trigger} \n"
    else:
        OUT_STR = "**▾∮ لم تقوم بأضافة اي كلمة الى قائمة المنع\n استخدم `.منع` **<الكلمة> ✎✓**"
    await edit_or_reply(event, OUT_STR)
