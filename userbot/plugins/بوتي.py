import os
from ..utils import admin_cmd
from . import *
from userbot import jmthon

@jmthon.on(admin_cmd("بوتي$", incoming=True))
async def proz(event):
  msg = await bot.send_message(event.chat_id, str(os.environ.get("TG_BOT_USERNAME")))

#حتى هذا تخمطه  😂؟ 
