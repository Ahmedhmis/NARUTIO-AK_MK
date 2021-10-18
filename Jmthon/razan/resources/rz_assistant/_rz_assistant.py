import asyncio

from Jmthon.razan.resources.assistant import RBOT, ROZA, SetAbt, Stdec, StJms
from userbot import LOGS, bot


async def rz_assistant():
    try:
        jmthon = await bot.get_entity(RBOT)
        if jmthon.photo == None:
            LOGS.info(StJms[0])
            RO = RBOT
            if bot.me.username == None:
                first_name = bot.me.first_name
            else:
                first_name = f"@{bot.me.username}"
            await bot.send_message(ROZA, StJms[0])
            await asyncio.sleep(1)
            await bot.send_message("@botfather", "/cancel")
            await asyncio.sleep(1)
            await bot.send_message("@botfather", "/start")
            await asyncio.sleep(1)
            await bot.send_message("@botfather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@botfather", RO)
            await asyncio.sleep(1)
            await bot.send_file(
                "@botfather", "Jmthon/razan/resources/assistant/razan.jpeg"
            )
            await asyncio.sleep(2)
            await bot.send_message("@botfather", "/setabouttext")
            await asyncio.sleep(1)
            await bot.send_message("@botfather", RO)
            await asyncio.sleep(1)
            await bot.send_message("@botfather", SetAbt.format(first_name))
            await asyncio.sleep(2)
            await bot.send_message("@botfather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@botfather", RO)
            await asyncio.sleep(1)
            await bot.send_message("@botfather", Stdec.format(first_name))
            await asyncio.sleep(2)
            await bot.send_message("@botfather", "/start")
            await asyncio.sleep(1)
            await bot.send_message(ROZA, StJms[1])
            LOGS.info(StJms[2])
    except Exception as e:
        LOGS.info(str(e))


# For Jmthon userbot don't kang   !!
