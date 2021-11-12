import os

from userbot import jmthon

from ..utils import admin_cmd
from . import *


@jmthon.on(admin_cmd("بوتي$", incoming=True))
async def proz(event):
    await bot.send_message(event.chat_id, str(os.environ.get("TG_BOT_USERNAME")))


# حتى هذا تخمطه  😂؟
