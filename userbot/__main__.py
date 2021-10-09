import sys

import userbot
from userbot import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import jmthon
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("JMTHON")

print(userbot.__copyright__)
print("Licensed under the terms of the " + userbot.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("Starting Userbot")
    jmthon.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()


class CatCheck:
    def __init__(self):
        self.sucess = True


Catcheck = CatCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        Catcheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("⌯︙بـوت جـمثون يعـمل بـنجاح ")
    print(
        f"يجـب تفـعيل وضع الأنلايـن ثم أرسـل {cmdhr}فحص لـرؤيـة اذا كـان البوت شـغال\
        \nللمسـاعدة تواصـل  https://t.me/jmthon"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    try:
        await bot(JoinChannelRequest("@JMTHON"))
    except BaseException:
        pass
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
    try:
        await bot(JoinChannelRequest("@RR7PP"))
    except BaseException:
         pass
     return

jmthon.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    jmthon.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        jmthon.run_until_disconnected()
    except ConnectionError:
        pass
