# Copyright (C) 2021 JMTHON TEAM
# FILES WRITTEN BY  @RR7PP
import html

from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest

from ..Config import Config
from . import (
    ALIVE_NAME,
    AUTONAME,
    BOTLOG,
    BOTLOG_CHATID,
    DEFAULT_BIO,
    edit_delete,
    get_user_from_event,
    jmthon,
)

plugin_category = "tools"
DEFAULTUSER = str(AUTONAME) if AUTONAME else str(ALIVE_NAME)
DEFAULTUSERBIO = str(DEFAULT_BIO) if DEFAULT_BIO else "الـحمد لله عـلى كـل شـيء"


@jmthon.ar_cmd(
    pattern="انتحال(?:\s|$)([\s\S]*)",
    command=("انتحال", plugin_category),
    info={
        "header": "لعمـل نسـخ حـسـاب الشـخص الـذي تـرد عليـه ",
        "usage": "{tr}انتحال <معرف/ايدي/بالرد عليه>",
    },
)
async def _(event):
    "لعمـل نسـخ حـسـاب الشـخص الـذي تـرد عليـه"
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    pfile = await event.client.upload_file(profile_pic)
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "⌯︙تـم نسـخ الـحساب بـنجاح ✅")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#CLONED\nsuccessfully cloned [{first_name}](tg://user?id={user_id })",
        )


@jmthon.ar_cmd(
    pattern="اعادة$",
    command=("اعادة", plugin_category),
    info={
        "header": "لأرجـاع الحـساب الى وضـعه الطـبيعي مـن صـورة واسم وبـايو",
        "usage": "{tr}اعادة",
    },
)
async def _(event):
    "لأرجـاع الحسـاب الـى وضـعن الأصـلي"
    name = f"{DEFAULTUSER}"
    blank = ""
    bio = f"{DEFAULTUSERBIO}"
    await event.client(
        functions.photos.DeletePhotosRequest(
            await event.client.get_profile_photos("me", limit=1)
        )
    )
    await event.client(functions.account.UpdateProfileRequest(about=bio))
    await event.client(functions.account.UpdateProfileRequest(first_name=name))
    await event.client(functions.account.UpdateProfileRequest(last_name=blank))
    await edit_delete(event, "⌯︙تـم اعـادة الـحساب بـنجاح ✅")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, f"⌯︙تـم اعادة الـحساب الى وضـعه الاصلـي ✅"
        )
