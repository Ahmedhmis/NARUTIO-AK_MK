# @Jmthon - < https://t.me/Jmthon >
# Copyright (C) 2021 - JMTHON-AR
# All rights reserved.
#
# This file is a part of < https://github.com/JMTHON-AR/JMTHON-AR >
# Please read the GNU Affero General Public License in;
# < https://github.com/JMTHON-AR/JMTHON-AR/blob/master/LICENSE 
# ===============================================================import threading
#
import re

from userbot import bot
from userbot.utils import admin_cmd
from userbot import CMD_HELP

@borg.on(admin_cmd(pattern="اكس او$"))
# كتابة وتعديل فريق جمثون  #@RR7PP
async def gamez(event):
    if event.fwd_from:
        return
    jmusername = "@xobot"
    uunzz = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(jmusername, uunzz)
    await tap[0].click(event.chat_id)
    await event.delete()

CMD_HELP.update(
  {
   "اكس او": ".اكس او \n اكتب الامر لبدء لعبة اكس او"
  }
    )
