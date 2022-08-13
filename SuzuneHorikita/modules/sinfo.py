import html
import re
import os
import requests
import datetime
import platform
import time

from psutil import cpu_percent, virtual_memory, disk_usage, boot_time
from platform import python_version
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events

from telegram import (
    MAX_MESSAGE_LENGTH,
    ParseMode,
    Update,
    MessageEntity,
    __version__ as ptbver,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown, mention_html

from SuzuneHorikita import (
    DEV_USERS,
    OWNER_ID,
    DRAGONS,
    DEMONS,
    TIGERS,
    WOLVES,
    INFOPIC,
    dispatcher,
    sw,
    StartTime,
    SUPPORT_CHAT,
)
from SuzuneHorikita.__main__ import STATS, TOKEN, USER_INFO
from SuzuneHorikita.modules.sql import SESSION
import SuzuneHorikita.modules.sql.userinfo_sql as sql
from horisan.modules.disable import DisableAbleCommandHandler
from SuzuneHorikita.modules.sql.global_bans_sql import is_user_gbanned
from SuzuneHorikita.modules.sql.afk_redis import is_user_afk, start_afk
from horisan.modules.sql.users_sql import get_user_num_chats
from SuzuneHorikita.modules.helper_funcs.chat_status import sudo_plus
from SuzuneHorikita.modules.helper_funcs.extraction import extract_user
from SuzuneHorikita import telethn


def sinfo(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat
    user_id = extract_user(update.effective_message, args)

    if user_id:
        user = bot.get_chat(user_id)

    elif not message.reply_to_message and not args:
        user = message.from_user

    elif not message.reply_to_message and (
        not args
        or (
            len(args) >= 1
            and not args[0].startswith("@")
            and not args[0].isdigit()
            and not message.parse_entities([MessageEntity.TEXT_MENTION])
        )
    ):
        message.reply_text("I can't extract a user from this.")
        return

    else:
        return

    rep = message.reply_text("<code>Small Intel About This User...</code>", parse_mode=ParseMode.HTML)

    text = (
        f"「<b> 【ɪɴꜰᴏ ᴏꜰ ᴛʜɪꜱ ᴜꜱᴇʀ】</b> 」\n"
        f"───────────────────\n"
        f"۞ ID: <code>{user.id}</code>"
        )

    if user.username:
        text += f"\n۞ Username: @{html.escape(user.username)}"

    text += f"\n۞ Userlink: {mention_html(user.id, 'LINK')}"

    disaster_level_present = False

    if user.id == OWNER_ID:
        text += "\n۞ Disaster : King 👑"
        disaster_level_present = True
    elif user.id in DEV_USERS:
        text += "\n۞ Disaster : Prince."
        disaster_level_present = True
    elif user.id in DRAGONS:
        text += "\n۞ Disaster : Emperor."
        disaster_level_present = True
    elif user.id in DEMONS:
        text += "\n۞ Disaster : Governer."

    disaster_level_present = True

    if INFOPIC:
        try:
            profile = context.bot.get_user_profile_photos(user.id).photos[0][-1]
            context.bot.sendChatAction(chat.id, "upload_photo")
            context.bot.send_photo(
                chat.id,
                photo=profile,
                caption=(text),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Support", url="https://t.me/ignitetechdivision"
                            ),
                            InlineKeyboardButton(
                                "Disasters", url="https://t.me/shoto_xxupdates/3"
                            ),
                        ],
                    ]
                ),
                parse_mode=ParseMode.HTML,
            )

        # Incase user don't have profile pic, send normal text
        except IndexError:
            message.reply_text(
                text,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Support", url="https://t.me/ignitetechdivision"
                            ),
                            InlineKeyboardButton(
                                "Disasters", url="https://t.me/shoto_xxupdates/3"
                            ),
                        ],
                    ]
                ),
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )

    else:
        message.reply_text(
            text,
            parse_mode=ParseMode.HTML,
        )

    rep.delete()
   
    
__help__ = """
*SINFO:*
❂ /sinfo*:* Get Your Info But In Smaller Size.
"""

INFO_HANDLER = DisableAbleCommandHandler("sinfo", sinfo, run_async=True)

dispatcher.add_handler(INFO_HANDLER)

__mod_name__ = "sɪɴꜰ】"
__command_list__ = ["info"]
__handlers__ = [
    INFO_HANDLER
    ]
    
    
    
