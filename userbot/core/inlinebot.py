from telethon import Button, events

from Jmthon.razan.resources.mybot import *

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
import json
import math
import os
import random
import re
import time
from uuid import uuid4

from telethon import Button, types
from telethon.errors import QueryIdInvalidError
from telethon.events import CallbackQuery, InlineQuery
from youtubesearchpython import VideosSearch

from userbot import jmthon

from ..Config import Config
from ..helpers.functions import rand_key
from ..helpers.functions.utube import (
    download_button,
    get_yt_video_id,
    get_ytthumb,
    result_formatter,
    ytsearch_data,
)
from ..plugins import mention
from ..sql_helper.globals import gvarstatus
from . import CMD_INFO, GRP_INFO, PLG_INFO, check_owner
from .logger import logging

CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "")
HELP_ROWS = int(os.environ.get("HELP_ROWS", 5))
HELP_COLOUMNS = int(os.environ.get("HELP_COLOUMNS", 3))
LOGS = logging.getLogger(__name__)
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
CATLOGO = "https://telegra.ph/file/88f00e9c84c0a01207adb.jpg"
tr = Config.COMMAND_HAND_LER
def getkey(val):
    for key, value in GRP_INFO.items():
        for plugin in value:
            if val == plugin:
                return key
    return None

def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb

@jmthon.tgbot.on(InlineQuery)
async def inline_handler(event):  
    builder = event.builder
    result = None
    query = event.text
    string = query.lower()
    query.split(" ", 2)
    str_y = query.split(" ", 1)
    string.split()
    query_user_id = event.query.user_id
    if query_user_id == Config.OWNER_ID or query_user_id in Config.SUDO_USERS:
        hmm = re.compile("همسة (.*) (.*)")
        match = re.findall(hmm, query)
        if query.startswith("**JMTHON"):
            buttons = [
                (
                    Button.inline("السورس", data="stats"),
                    Button.url("ch", "t.me/jmthon"),
                )
            ]
            ALIVE_PIC = gvarstatus("ALIVE_PIC")
            IALIVE_PIC = gvarstatus("IALIVE_PIC")
            if IALIVE_PIC:
                CAT = [x for x in IALIVE_PIC.split()]
                PIC = list(CAT)
                I_IMG = random.choice(PIC)
            if not IALIVE_PIC and ALIVE_PIC:
                CAT = [x for x in ALIVE_PIC.split()]
                PIC = list(CAT)
                I_IMG = random.choice(PIC)
            elif not IALIVE_PIC:
                I_IMG = None
            if I_IMG and I_IMG.endswith((".jpg", ".png")):
                result = builder.photo(
                    I_IMG,
                    text=query,
                    buttons=buttons,
                )
            elif I_IMG:
                result = builder.document(
                    I_IMG,
                    title="Alive cat",
                    text=query,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="Alive cat",
                    text=query,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)
        elif query.startswith("Inline buttons"):
            markdown_note = query[14:]
            prev = 0
            note_data = ""
            buttons = []
            for match in BTN_URL_REGEX.finditer(markdown_note):
                n_escapes = 0
                to_check = match.start(1) - 1
                while to_check > 0 and markdown_note[to_check] == "\\":
                    n_escapes += 1
                    to_check -= 1
                if n_escapes % 2 == 0:
                    buttons.append(
                        (match.group(2), match.group(3), bool(match.group(4)))
                    )
                    note_data += markdown_note[prev : match.start(1)]
                    prev = match.end(1)
                elif n_escapes % 2 == 1:
                    note_data += markdown_note[prev:to_check]
                    prev = match.start(1) - 1
                else:
                    break
            else:
                note_data += markdown_note[prev:]
            message_text = note_data.strip()
            tl_ib_buttons = ibuild_keyboard(buttons)
            result = builder.article(
                title="Inline creator",
                text=message_text,
                buttons=tl_ib_buttons,
                link_preview=False,
            )
            await event.answer([result] if result else None)
        elif match:
            query = query[7:]
            user, txct = query.split(" ", 1)
            builder = event.builder
            secret = os.path.join("./userbot", "secrets.txt")
            try:
                jsondata = json.load(open(secret))
            except Exception:
                jsondata = False
            try:
                # if u is user id
                u = int(user)
                try:
                    u = await event.client.get_entity(u)
                    if u.username:
                        sandy = f"@{u.username}"
                    else:
                        sandy = f"[{u.first_name}](tg://user?id={u.id})"
                except ValueError:
                    sandy = f"[user](tg://user?id={u})"
            except ValueError:
                try:
                    u = await event.client.get_entity(user)
                except ValueError:
                    return
                if u.username:
                    sandy = f"@{u.username}"
                else:
                    sandy = f"[{u.first_name}](tg://user?id={u.id})"
                u = int(u.id)
            except Exception:
                return
            timestamp = int(time.time() * 2)
            newsecret = {str(timestamp): {"userid": u, "text": txct}}

            buttons = [Button.inline("عرض الهمسة ", data=f"secret_{timestamp}")]
            result = builder.article(
                title="همسة سرية",
                text=f" الهمسة السرية لـ {sandy} هو فقط من يمكنه عرضها.",
                buttons=buttons,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(newsecret)
                json.dump(jsondata, open(secret, "w"))
            else:
                json.dump(newsecret, open(secret, "w"))
        elif str_y[0].lower() == "ytdl" and len(str_y) == 2:
            link = get_yt_video_id(str_y[1].strip())
            found_ = True
            if link is None:
                search = VideosSearch(str_y[1].strip(), limit=15)
                resp = (search.result()).get("result")
                if len(resp) == 0:
                    found_ = False
                else:
                    outdata = await result_formatter(resp)
                    key_ = rand_key()
                    ytsearch_data.store_(key_, outdata)
                    buttons = [
                        Button.inline(
                            f"1 / {len(outdata)}",
                            data=f"ytdl_next_{key_}_1",
                        ),
                        Button.inline(
                            "📜  List all",
                            data=f"ytdl_listall_{key_}_1",
                        ),
                        Button.inline(
                            "⬇️  Download",
                            data=f'ytdl_download_{outdata[1]["video_id"]}_0',
                        ),
                    ]
                    caption = outdata[1]["message"]
                    photo = await get_ytthumb(outdata[1]["video_id"])
            else:
                caption, buttons = await download_button(link, body=True)
                photo = await get_ytthumb(link)
            if found_:
                markup = event.client.build_reply_markup(buttons)
                photo = types.InputWebDocument(
                    url=photo, size=0, mime_type="image/jpeg", attributes=[]
                )
                text, msg_entities = await event.client._parse_message_text(
                    caption, "html"
                )
                result = types.InputBotInlineResult(
                    id=str(uuid4()),
                    type="photo",
                    title=link,
                    description="⬇️ Click to Download",
                    thumb=photo,
                    content=photo,
                    send_message=types.InputBotInlineMessageMediaAuto(
                        reply_markup=markup, message=text, entities=msg_entities
                    ),
                )
            else:
                result = builder.article(
                    title="Not Found",
                    text=f"No Results found for `{str_y[1]}`",
                    description="INVALID",
                )
            try:
                await event.answer([result] if result else None)
            except QueryIdInvalidError:
                await event.answer(
                    [
                        builder.article(
                            title="Not Found",
                            text=f"No Results found for `{str_y[1]}`",
                            description="INVALID",
                        )
                    ]
                )
        elif string == "pmpermit":
            buttons = [
                Button.inline(text="اضهار الخيارات", data="show_pmpermit_options"),
            ]
            PM_PIC = gvarstatus("pmpermit_pic")
            if PM_PIC:
                CAT = [x for x in PM_PIC.split()]
                PIC = list(CAT)
                CAT_IMG = random.choice(PIC)
            else:
                CAT_IMG = None
            query = gvarstatus("pmpermit_text")
            if CAT_IMG and CAT_IMG.endswith((".jpg", ".jpeg", ".png")):
                result = builder.photo(
                    CAT_IMG,
                    # title="Alive cat",
                    text=query,
                    buttons=buttons,
                )
            elif CAT_IMG:
                result = builder.document(
                    CAT_IMG,
                    title="Alive cat",
                    text=query,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="Alive cat",
                    text=query,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)
    else:
        buttons = [
            (
                Button.url("Source code", "https://t.me/jmthon"),
                Button.url(
                    "Deploy",
                    "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMr-confused%2Fcatpack&template=https%3A%2F%2Fgithub.com%2FMr-confused%2Fcatpack",
                ),
            )
        ]
        markup = event.client.build_reply_markup(buttons)
        photo = types.InputWebDocument(
            url=CATLOGO, size=0, mime_type="image/jpeg", attributes=[]
        )
        text, msg_entities = await event.client._parse_message_text(
            "jmthon.", "md"
        )
        result = types.InputBotInlineResult(
            id=str(uuid4()),
            type="photo",
            title="jmthon",
            description="نصب لنفسك",
            url="https://dashboard.heroku.com/new?template=https://github.com/JMTHON-AR/JMTHON-PACK",
            thumb=photo,
            content=photo,
            send_message=types.InputBotInlineMessageMediaAuto(
                reply_markup=markup, message=text, entities=msg_entities
            ),
        )
        await event.answer([result] if result else None)
        
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
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="بوت",
                text=f"**- حالة بوت جمثون للمستخدم [{DEFAULTUSER}](tg://user?id={myid})**\n\n- البوت يعمل بنجاح يا صاح\n\n@Jmthon ",
                buttons=[
                    [custom.Button.inline("الحالة", data="statcheck")],
                    [Button.url("تنصيب جمثون", "https://heroku.com/deploy?template=https://github.com/JMTHON-AR/Jmthon")],
                ],
            )
        elif event.query.user_id == bot.uid and query == "alive":
            ALIVE = ALV_TXT
            if ALIVE_PIC and ALIVE_PIC.endswith((".jpg", ".png")):
               result = builder.photo(
                 ALIVE_PIC,
                 text = ALIVE,
              
                 buttons = [
                   [
                     Button.url("قناة جمثون", "https://t.me/Jmthon"),
                     Button.url("كروب جمثون", "https://t.me/GroupJmthon")
                   ],
                   [
                     Button.inline("• حول مالكي •", data="master")
                   ],
                ],
              )
            else:
              result = builder.document(
                 text = ALIVE,
                 title = "Jmthon",
                 file = ALIVE_PIC,
                 buttons = [
                   [
                     Button.url("قناة جمثون", "https://t.me/Jmthon"),
                     Button.url("كروب جمثون", "https://t.me/GroupJmthon")
                   ],
                   [
                     Button.inline("• حول مالكي •", data="master")
                   ],
                ],
              )
                
        elif event.query.user_id == bot.uid and query.startswith("**احم"):
            JMTHONBT = USER_BOT_NO_WARN.format(DEFAULTUSER, myid, MESAG)
            result = builder.photo(
                file=JMTHON_PIC,
                text=JMTHONBT,
                buttons=[
                    [
                        custom.Button.inline("• لطلب شي •", data="rzeq"),
                        custom.Button.inline("• للسؤال •", data="jmk")
                    ],
                    [
                        custom.Button.inline("• للدردشة •", data="chat"),
                        custom.Button.inline("• شي اخر •", data="elsi")],
                ],
            )
        elif event.query.user_id == bot.uid and query == "paste":
              ok = event.text.split("-")[1]
              link = "https://spaceb.in/" + ok
              raw = f"https://spaceb.in/api/v1/documents/{ok}/raw"
              result = builder.article(
                   title= "Paste",
                   text = "لصق الكود في المحرر",
                   buttons=[
            [
                Button.url("الكود ", url=link),
                Button.url("النص️", url=raw),
            ],
        ],
    )
        else:
            result = builder.article(
                "سورس جمثون  - الافضل في الشرق الاوسط",
                text="**مرحبا بك في سورس جمثون**\n\n اضغط في الاسفل لعرض معلومات اكثر",
                buttons=[
                    [custom.Button.url("المطور", "https://t.me/rr9r7")],
                    [
                        custom.Button.url(
                            "السورس", "https://t.me/Jmthon"
                        ),
                        custom.Button.url(
                            "تنصيب ",
                            "https://heroku.com/deploy?template=https://github.com/JMTHON-AR/Jmthon",
                             ),
                    ],
                    [
                        custom.Button.url(
                            "مجموعة جمثون", "https://t.me/GroupJMTHON"
                        )
                    ],
                ],
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
            reply_jmthon_alert += "\n ارسل .انلود {} لحذف هذا الملف\n\
                فريق جثمون™".format(
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
