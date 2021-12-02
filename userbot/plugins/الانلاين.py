from telethon import Button, events

from Jmthon.razan.resources.mybot import *
#jmthon
from ..Config import Config
import asyncio
import html
import os
import re
from math import ceil
import time
import datetime
from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest
from userbot import CMD_HELP, CMD_LIST
from userbot import jmthon

CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "")
HELP_ROWS = int(os.environ.get("HELP_ROWS", 5))
HELP_COLOUMNS = int(os.environ.get("HELP_COLOUMNS", 3))
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("**•   𝙅𝙈𝙏𝙃𝙊𝙉"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© مساعدة جمثون",
                text="{}\n الملفات الحالية في سورس جمثون العربي: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        await event.answer([result] if result else None)
    @tgbot.on(
        events.callbackquery.CallbackQuery(
            data=re.compile(rb"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            await event.edit(buttons=buttons)
        else:
            reply_jmthon_alert = (
                "عذرا لا تستطيع الضغط هنا هذا الخيار ليس لك، نصب جمثون لنفسك"
            )
            await event.answer(reply_jmthon_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"reopen")))
    async def megic(event):
        if event.query.user_id == bot.uid:
            buttons = paginate_help(0, CMD_LIST, "helpme")
            await event.edit("▾∮ فتح القائمة الرئيسيية مره اخرى ", buttons=buttons)
        else:
            reply_jmthon_alert = "عذرا لا تستطيع الضغط هنا هذا الخيار ليس لك، نصب جمثون لنفسك"
            await event.answer(reply_jmthon_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzeq")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_jmthon_alert = "عذرا هذا الخيار ليس لك"
            await event.answer(reply_jmthon_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"- حسنا اذا كان لديك شيء ما لـ {MYUSER} \n عليك الأنتظار لأن مالك الحساب مشغول حاليا\n لا ترسل اي شي فقط انتظر."
            )
            tarzt = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(tarzt.user.first_name)
            jmthon = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            rozsend = f"- مرحبا {MYUSER}, [{first_name}](tg://user?id={jmthon}) يريد طلب شيء ما \n ربما يريد ان يخبرك شيء أذهب وتأكد"
            await tgbot.send_message(LOG_JMTHON, rozsend)
            
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_jmthon_alert = "عذرا هذا الخيار ليس لك"
            await event.answer(reply_jmthon_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"**- تريد الدردشة 💬**\n اكيد تستطيع لكن مالك الحساب مشغول الان الرجاء انتظار وصول المالك وانتظار رده لا تكرر الرسائل رجاءا  !"
            )
            tarzt = await event.client(GetFullUserRequest(event.query.user_id))
            jmthon = event.query.user_id
            first_name = html.escape(tarzt.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            rozsend = f"▾∮ مرحبـا {NAMERZ}\n [{first_name}](tg://user?id={jmthon}) يريد ان يراسلك ويتحدث معك **\n أذا ما عندك واهس ومفعل مود لا ترد منو جابرك -_-"
            await tgbot.send_message(LOG_JMTHON, rozsend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"jmk")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_jmthon_alert = "عذرا هذا الخيار ليس لك"
            await event.answer(reply_jmthon_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"▾∮ ما الذي تريد ان تسأله لـ {NAMERZ} اذكر ماذا تريد في رسالة واحدة فقط رجاءا الرجاء انتظار رد المالك"
            )
            tarzt = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(tarzt.user.first_name)
            jmthon = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            rozsend = f"- مرحبا {MYUSER}, [{first_name}](tg://user?id={jmthon}) يريد محادثتك\n ربما يريد ان يخبرك شيء أذهب وتأكد"
            await tgbot.send_message(LOG_JMTHON, rozsend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"elsi")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_jmthon_alert = "ماذا تفعل هذا ليس لك  ؟"
            await event.answer(reply_jmthon_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"- حسنا اذا كان لديك شيء ما لـ {MYUSER} \n عليك الأنتظار لأن مالك الحساب مشغول حاليا\n لا ترسل اي شي فقط انتظر."
            )
            tarzt = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(tarzt.user.first_name)
            jmthon = event.query.user_id
            first_name = html.escape(tarzt.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(tarzt.user.first_name)
            await tgbot.send_message(
                LOG_JMTHON,
                f"- مرحبا {MYUSER}\n[{first_name}](tg://user?id={jmthon}) يريد محادثتك\n ربما يريد ان يخبرك شيء أذهب وتأكد",
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit(
                "تم غلق القائمة", buttons=[Button.inline("• فتح القائمة •", data="reopen")]
            )
        else:
            reply_jmthon_alert = "عذرا لا تستطيع الضغط هنا هذا الخيار ليس لك، نصب جمثون لنفسك"
            await event.answer(reply_jmthon_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"statcheck")))
    async def rip(event):
        text = telestats
        await event.answer(text, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(
            data=re.compile(rb"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"
            )
            await event.edit(buttons=buttons)
        else:
            reply_jmthon_alert = "عذرا لا تستطيع الضغط هنا هذا الخيار ليس لك .  نصب جمثون لنفسك"
            await event.answer(reply_jmthon_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            help_string += f"• الأوامر المتاحة في {plugin_name} - \n"
            try:
                if plugin_name in CMD_HELP:
                    for i in CMD_HELP[plugin_name]:
                        help_string += i
                    help_string += "\n"
                else:
                    for i in CMD_LIST[plugin_name]:
                        help_string += i
                        help_string += "\n"
            except BaseException:
                pass
            if help_string == "":
                reply_jmthon_alert = "{} ليس له معلومات كثيرة.\n أرسل .مساعدة {}".format(
                    plugin_name, plugin_name
                )
            else:
                reply_jmthon_alert = help_string
            reply_jmthon_alert += "\n ارسل .مساعدة {} للعرض بالتفصيل\n\
                @jmthon".format(
                plugin_name
            )
            if len(help_string) >= 140:
                oops = "قائمة الاوامر كبيرة جدا تأكد من الرسائل المحفوظة لعرضها لك"
                await event.answer(oops, cache_time=0, alert=True)
                help_string += "\n\n- سيتم حذف هذه الرسالة تلقائيا بعد دقيقتين"
                if bot is not None and event.query.user_id == bot.uid:
                    jmthon = await bot.send_message("me", help_string)
                    await asyncio.sleep(120)
                    await jmthon.delete()
            else:
                await event.answer(reply_jmthon_alert, cache_time=0, alert=True)
        else:
            reply_jmthon_alert = "قم بتنصيب بوت جمثون بنفسك"
            await event.answer(reply_jmthon_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = HELP_ROWS
    number_of_cols = HELP_COLOUMNS
    tele = CUSTOM_HELP_EMOJI
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline(
            "{} {}".format(tele, x), data="us_plugin_{}".format(x)
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "|| السابق ||", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("اغلاق", data="close"),
                custom.Button.inline(
                    "|| التالي ||", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


async def userinfo(event):
    tarzt = await event.client(GetFullUserRequest(event.query.user_id))
    first_name = html.escape(tarzt.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    return first_name
