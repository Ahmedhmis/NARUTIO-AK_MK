import asyncio

from userbot import CMD_HELP, jmthon
from userbot.utils import admin_cmd

#
@jmthon.on(admin_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "تهكير":

        await event.edit(input_str)

        animation_chars = [
            "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "█████████████████████▒▒▒▒ `",
            "█████████████████████████ `",
            "- تم اختراق الضيحه وارسال جميع معلوماته في الرسائل المحفوظة\n\n فحبيبي اذا تحب اذا تبقى تكمز كل شي يمي\n\n#ترفيه",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


CMD_HELP.update({"تهكير": ".تهكير \nفقط ارسل الامر الترفيه"})

#  قبل لا تفكر تخمط هذا الملف ترا الملف متعوب عليه لا تخمط واني حذرتك
# حسب قوانين موقع github https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
# تنص على انه اي شخص ياخذ الملف بدون ذكر حقوق طبع والنشر سيتم حذف حسابه من قبل صاحب الملف اقتضى التنوي
# Copyright ©️ 2021 RR9R7 . All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits -  (  @RR7PP  - @JMTHON  )
