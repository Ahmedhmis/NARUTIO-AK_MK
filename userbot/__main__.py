from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils.pluginmanager import load_module, start_assistant
from pathlib import Path
import asyncio
import telethon.utils
os.system("pip install -U telethon")
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
l2= Config.SUDO_COMMAND_HAND_LER
JMTHON_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/cd2a3965eadd7529b8e94.jpg"
cmdhr = Config.COMMAND_HAND_LER
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP

LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)    
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"JMTHON_STRING - {str(e)}")
        sys.exit()
        
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Config.TG_BOT_USERNAME is not None:
        print("يتم اعداد وضع الانلاين للبوت")
        bot.tgbot = TelegramClient(
            "BOT_TOKEN",
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH
        ).start(bot_token=Config.TG_BOT_TOKEN)
        print("اكتمل تشغيل الانلاين بنجاح ")
        print("يتم تشغيل البوت")
        bot.loop.run_until_complete(add_bot(Config.TG_BOT_USERNAME))
        print("أكتمل التشغيل")
    else:
        bot.start()
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
if LOAD_ASSISTANT == True:
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                start_assistant(shortname.replace(".py", ""))
            except Exception as er:
                print(er)
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
print(f""""➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
اكتمل تنصيب بوت جمثون بنجاح وبدون اخطاء
الان ارسل  .الاوامر او .السورس للتاكد من ان البوت يعمل بنجاح
قناة السورس https://t.me/JMTHON
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
)
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
async def jmthon_is_on():
    try:
        if Config.PM_LOGGER_GROUP_ID != 0:
            await bot.send_file(
                Config.PM_LOGGER_GROUP_ID,
                JMTHON_PIC,
                caption=f"**▾∮ اكتمل التنصيب بنجاح ✅**\n\nلعرض قائمة اوامر البوت فقط ارسل `{cmdhr}الاوامر`  \n\n - اشترك [قناة جمثون](t.me/JMTHON) \n [مجموعة المساعدة](t.me/GROUPJMTHON)",
            )
    except Exception as e:
        print(str(e))
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
#  اشتراك اجباري 
    try:
        await bot(JoinChannelRequest("@JMTHON"))
    except BaseException:
        pass
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
    try:
        await bot(JoinChannelRequest("@RR7PP"))
    except BaseException:
         pass
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
#𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
bot.loop.create_task(jmthon_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
    
    
                #𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @Jmthon  ~ @RR7PP
