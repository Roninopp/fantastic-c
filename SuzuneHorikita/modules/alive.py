import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SuzuneHorikita.events import register
from SuzuneHorikita import telethn as tbot


PHOTO = "https://telegra.ph/file/4da3edb111cf6f2e9526e.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Yo [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Shoto Todoroki** \n\n"
  TEXT += "⚪ **I'm Working Properly** \n\n"
  TEXT += f"⚪ **My Master : [𝘼𝙗𝙝𝙞𝙣𝙖𝙫 || ᏆᏀΝᏆͲᎬ](https://t.me/Redeye_Ghoul)** \n\n"
  TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
  TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here️**"
  BUTTON = [[Button.url("Updates", "https://t.me/Shoto_xxupdates"), Button.url("Support", "https://t.me/Shoto_xxsupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
