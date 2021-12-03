from userbot import jmthon 
from userbot import CMD_HELP


@jmthon.on(admin_cmd(pattern=r"كول (.*)"))
@jmthon.on(sudo_cmd(pattern=r"كول ( .*)", allow_sudo=True))
async def _(event):
    bxt = Config.TG_BOT_USERNAME
    try:
        tex = str(event.text[6:])
        await tgbot.send_message(event.chat_id, tex)
        await event.delete()
    except BaseException:
        await event.client.send_message(event.chat_id, f"**- يجب عليك اضافة {bxt} هنا اولا**")
        await event.delete()


CMD_HELP.update(
    {
        "كول": ".كول <الرسالة>\nامر كول اولا ضيف البوت في المجموعه و اكتب الامر وكلمه وسيرسلها البوت "
    }
)
