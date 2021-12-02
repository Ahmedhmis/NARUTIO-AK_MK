# @Jmthon - < https://t.me/Jmthon >
# Copyright (C) 2021 - JMTHON-AR
# All rights reserved.
#
# This file is a part of < https://github.com/JMTHON-AR/Jmthon >
# Please read the GNU Affero General Public License in;
# < https://github.com/JMTHON-AR/Jmthon/blob/master/LICENSE 
# =================================#==============================

import os

from userbot import CMD_HELP, CMD_LIST
from userbot import Config, jmthon

NAME = Config.ALIVE_NAME
CMD_HNDLR = Config.COMMAND_HAND_LER

DEFAULTUSER = str(NAME) if NAME else "jmthon"
CMD_HNDLR = Config.COMMAND_HAND_LER
CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "•")

if CMD_HNDLR is None:
    CMD_HNDLR = "."


@jmthon.on(admin_cmd(pattern="مساعدة ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        tgbotusername = Config.TG_BOT_USERNAME
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_HELP:
                string += CUSTOM_HELP_EMOJI + " " + i + " " + CUSTOM_HELP_EMOJI + "\n"
                for iter_list in CMD_HELP[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                with io.BytesIO(str.encode(string)) as out_file:
                    out_file.name = "cmd.txt"
                    await tgbot.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption="الأوامر",
                        reply_to=reply_to_id,
                    )
                    await event.delete()
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "الأوامر المتاحة فـي:  {}** \n\n".format(input_str)
                if input_str in CMD_HELP:
                    for i in CMD_HELP[input_str]:
                        string += i
                    string += "\n\n**@jmthon**"
                    await event.edit(string)
                else:
                    for i in CMD_LIST[input_str]:
                        string += "    " + i
                        string += "\n"
                    string += "\n**@jmthon**"
                    await event.edit(string)
            else:
                await event.edit(input_str + " ليس في قائمة الاوامر تاكد جيدا من الامر")
        else:
            help_string = f"""**•   𝙅𝙈𝙏𝙃𝙊𝙉 𝘽𝙊𝙏 - قائمـة الأوامـر ** •\n╼──────────────────╾\n- اهلا بك في قائمة الاوامر  . \n- من هنا يمكنك العثور على جميع اوامر السورس\n\n**╮•❐ ارسل**  `.مساعدة واسم الاضافة`\n       لأضهار شرح مفصل للأمر\n\n** الاضافة يعني الاسماء التحت باللستة**"""
            try:
                results = await bot.inline_query(  # pylint:disable=E0602
                    tgbotusername, help_string
                )
                await results[0].click(
                    event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
                )
                await event.delete()
            except BaseException:
                await event.edit(
                    f"- عذرا يجب عليك تفعيل وضع الانلاين لأستخدام هذا الامر"
                )
