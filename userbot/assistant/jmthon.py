#    جميع الحقوق لمطوري سورس جمثون حصريا لهم فقط
#    اذا تخمط الملف اذك الحقوق وكاتبيه ومطوريه لا تحذف الحقوق وتصير فاشل 👍
#    كتابة محمد الزهيري
import io
import re

from telethon import *
from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from Jmthon.razan.resources.assistant import *

# Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
from userbot import bot
from userbot.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)

# Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
from . import *


# start
@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    razan = await tgbot.get_me()
    bot_id = razan.first_name
    razan.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    starttext = f"**مـرحبا {firstname} ! انـا هـو {bot_id}, بـوت مساعـد بسيـط 🧸🤍 \n\n- [مـالك البـوت](tg://user?id={bot.uid}) \nيمكـنك مراسلـة المـالك عبـر هذا البـوت . \n\nاذا كـنت تـريد تنـصيب بـوت خـاص بـك تـاكد من الازرار بالأسفل**"
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            vent,
            message=f"**اهلا بك مطـوري 🤍**\n**اختر احد الاوامر في الاسفل**\n\n**⍣ⵧⵧⵧⵧⵧᴊᴍᴛʜᴏɴⵧⵧⵧⵧⵧ⍣**\n𝙅𝙈𝙏𝙃𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🧸♥",
            buttons=[
                [
                    Button.url("المطـور ", "https://t.me/RR7PP"),
                    Button.inline("اوامر السورس", data="rzhelp"),
                ],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tgbot.send_message(
            event.chat_id,
            message=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("تنـصيب جمثـون  🐍", data="deploy")],
                [Button.url("تحتاج مسـاعدة ❓", "https://t.me/GroupJmthon")],
            ],
        )


# Data

# Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="**لتـنصيب البـوت الخاص بك اتبـع الخطـوات في الاسفـل وحاول واذا لم تستطيع تفضل الى مجموعة المساعدة ليساعدوك 🧸♥**.",
            buttons=[
                [Button.url("شرح التنصيب 📺", "https://youtu.be/9VJ1HYtGbJU")],
                [Button.url("كروب المساعدة ❓", "https://t.me/GroupJmthon")],
            ],
        )


# Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "- قـائمة مستخـدمين البـوت  : \n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "razan.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="مجموع مستخدمـين بوتـك",
                allow_cache=False,
            )
    else:
        pass


# Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    rorza = "**▾∮ قائـمه اوامر المطور **\n* تستخدم في ↫ `{botusername} ` فقط! `\n**⍣ⵧⵧⵧⵧⵧᴊᴍᴛʜᴏɴⵧⵧⵧⵧⵧ⍣**\n\n*الامر  ( اذاعة  ) \n- لعمل اذاعة لمستخدمي البوت ◛ ↶\n**⋆ قم بالرد ع الرسالة لاذاعتها للمستخدمين ↸**\n\n*الامر ( معلومات ) \n- لمعرفة الملصقات المرسلة ↶\n**⋆ بالرد ع المستخدم لجلب معلوماتة **\n\n*الامر ( حظر + سبب )\n- لحظر مستخدم من البوت \n**⋆ بالرد ع المستخدم مع سبب مثل **\n**حظر @RR9R7 قمت بازعاجي**\n\n* الامر ( الغاء حظر ) \n لالغاء حظر المستخدم من البوت √\n**⋆ الامر والمعرف والسبب (اختياري) مثل **\n**الغاء حظر @RR9R7 + السبب اختياري**\n\n**⋆ الامر ( المحظورين )\n- لمعرفة المحظورين من البوت  **\n\n**⋆ امر ( المستخدمين ) \n- لمعرفة مستخدمين بوتك  **\n\n**⋆ الاوامر ( التكرار + تفعيل / تعطيل ) \n- تشغيل وايقاف التكرار (في البوت) ↶**\n* عند التشغيل يحظر المزعجين تلقائيًا ⊝\n\n\n**⍣ⵧⵧⵧⵧⵧᴊᴍᴛʜᴏɴⵧⵧⵧⵧⵧ⍣**\n𝙅𝙈𝙏𝙃𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🧸♥"
    await tgbot.send_message(event.chat_id, rorza)


# Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
@tgbot.on(events.NewMessage(pattern="^/help", func=lambda e: e.sender_id == bot.uid))
async def starkislub(event):
    rorza = "**قـائمـة اوامـر البـوت الخاصـة بك**:\n- **جميع هذه الاوامر تستخدم بعد اضافة البوت في مجموعة ورفعه مشـرف مع بعض الصلاحيـات**\n• /start \n ( للـتأكد من حالـة البـوت) \n• /ping \n ( امـر بنـك )  \n• /broadcast \n ( لعمـل اذاعـة لجميـع المستخدمين في البـوت )  \n• /id \n  ( لعـرض ايدي المسـتخدم ) \n• /alive \n- ( لـرؤية معلومات البـوت ) \n• /bun \n-  ( تعمل في المجموعات لحظر شخص )\n• /unbun  \n-  ( تعمل في المجموعات لالغاء حظر مستخدم )  \n• /prumote  \n-  ( لرفـع شخص مشـرف )\n• /demute  \n-  ( لتنزيل الشخص من رتبة الاشراف ) \n• /pin  \n-  ( لتثبيـت رسالة في المجموعـة )  \n• /stats  \n-  ( لعرض مستخدمين البوت )  \n• /purge  \n-  ( بالرد على رسالة ليقوم بحذف ما تحتها من رسائل ) \n• /del  \n-  ( بالـرد على الرسالـة لحـذفها )"
    await event.reply(rorza)


# Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE


@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def starkislub(event):
    razan = "**𝘑𝘔𝘛𝘏𝘖𝘕 𝘜𝘚𝘌𝘙𝘉𝘖𝘛**\n•━═━═━═━═━━═━═━═━═━•‌‌\n**- حالة البوت **  يعمـل بنجـاح\n**- اصدار التليثون  **: 1.23.0\n**- اصدار البايثون **: 3.9.6\n**- يوزرك ** {mention}\n**- CH : @JMTHON\n•━═━═━═━═━━═━═━═━═━•‌‌\n"
    await event.reply(razan)


""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """
"""  حقوقي شرفك تغير شي تلعب بشرفك """

# بـسـم الله الـرحمن الـرحيم  🤍


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzhelp")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            "**▾∮  اختر احد خيارات الاوامر : **",
            buttons=[
                [
                    Button.inline("اوامر الادمن ", data="rzadmin"),
                    Button.inline(" جديد جمثون", data="jdedjm"),
                ],
            ],
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام البوت احصل على بوتك من @JMTHON", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"jdedjm")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            "**▾∮ اختر احد الخيارات الاتيه. **",
            buttons=[
                [
                    Button.inline("ايميل وهمي ", data="rzfk"),
                    Button.inline("حالتي ", data="rzhala"),
                ],
                [
                    Button.inline("قراءة الملفات", data="rzred"),
                    Button.inline("ارسال خاص", data="rzprv"),
                ],
                [
                    Button.inline("حساب العمر", data="rzage"),
                ],
                [
                    Button.inline("║ رجوع ║ ⁦⁩", data="rzhelp"),
                ],
            ],
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام البوت احصل على بوتك من @JMTHON", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzage")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, ROZAGE, buttons=[[Button.inline("║ رجوع ║", data="jdedjm")]]
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzfk")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, ROZFK, buttons=[[Button.inline("║ رجوع ║", data="jdedjm")]]
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzhala")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, ROZHALA, buttons=[[Button.inline("║ رجوع ║", data="jdedjm")]]
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzred")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, ROZREAD, buttons=[[Button.inline("║ رجوع ║", data="jdedjm")]]
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzprv")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, ROZPRV, buttons=[[Button.inline("║ رجوع ║", data="jdedjm")]]
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzadmin")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            "**▾∮ اختر احد الخيارات الاتيه. **",
            buttons=[
                [
                    Button.inline("وضع التكرار", data="rztkrar"),
                    Button.inline("الـتحذيرات", data="rpwarn"),
                ],
                [
                    Button.inline("منع كلمات", data="rzmn3"),
                    Button.inline("الكتم", data="pomute"),
                ],
                [
                    Button.inline("اوامر المجموعة", data="rzgroup"),
                ],
                [
                    Button.inline("║ رجوع ║ ⁦⁩", data="rzhelp"),
                ],
            ],
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام البوت احصل على بوتك من @JMTHON", alert=True
        )


""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rztkrar")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, ROZKRR, buttons=[[Button.inline("║ رجوع ║", data="rzadmin")]]
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rpwarn")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, ROZHDR, buttons=[[Button.inline("║ رجوع ║", data="rzadmin")]]
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzmn3")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, ROZMN3, buttons=[[Button.inline("║ رجوع ║", data="rzadmin")]]
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzgroup")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            "**▾∮  اختر احد اوامر المجموعة في الاسفل : **",
            buttons=[
                [
                    Button.inline("المغادرة", data="rzkick"),
                    Button.inline("حذف المحظورين", data="rzunban"),
                ],
                [
                    Button.inline("التفليش", data="rzflsh"),
                    Button.inline("المحذوفين", data="rzzomb"),
                ],
                [
                    Button.inline("التثبيت", data="rzthbt"),
                    Button.inline("الحظر", data="rzban"),
                ],
                [
                    Button.inline("احصائيات الاعضاء", data="rzikuck"),
                    Button.inline("║ رجوع ║", data="rzadmin"),
                ],
            ],
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام البوت احصل على بوتك من @JMTHON", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzkick")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            ROZKICK,
            buttons=[[Button.inline("║ رجوع ║", data="rzgroup")]],
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzunban")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            ROZUNBAN,
            buttons=[[Button.inline("║ رجوع ║", data="rzgroup")]],
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzflsh")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            ROZFLSH,
            buttons=[[Button.inline("║ رجوع ║", data="rzgroup")]],
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzzomb")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            ROZZOMB,
            buttons=[[Button.inline("║ رجوع ║", data="rzgroup")]],
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzikuck")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            ROZIKUCK,
            buttons=[[Button.inline("║ رجوع ║", data="rzgroup")]],
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzthbt")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, ROZPIN, buttons=[[Button.inline("║ رجوع ║", data="rzgroup")]]
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzban")))
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, ROZBAN, buttons=[[Button.inline("║ رجوع ║", data="rzgroup")]]
        )
    else:
        await event.answer(
            "انت لا تستطيع استخدام هذا البوت نصب جمثون بنفسك", alert=True
        )


""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """
""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """
""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """
""" Telegram  :  @Jmthon  - @RR7PP   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """
