import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import SuzuneHorikita.modules.slapstrings as slapstrings
from SuzuneHorikita import dispatcher
from SuzuneHorikita.modules.disable import DisableAbleCommandHandler
from SuzuneHorikita.modules.helper_funcs.chat_status import (is_user_admin)
from SuzuneHorikita.modules.helper_funcs.extraction import extract_user

@run_async
def slap(update: Update, context: CallbackContext):

    bot = context.bot

    args = context.args

    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)

    user_id = extract_user(message, args)

    if user_id:

        abhinavgae = bot.get_chat(user_id)

        user1 = curr_user

        user2 = html.escape(abhinavgae.first_name)

    else:

        user1 = bot.first_name

        user2 = curr_user

    slap_type = random.choice(("Text", "Gif"))

    if slap_type == "Gif":

        try:

            temp = random.choice(slapstrings.SLAP_GIFS)

            reply_to.reply_animation(temp)

        except BadRequest:

            slap_type = "Text"

    if slap_type == "Text":

        temp = random.choice(slapstrings.SLAP_TEXT)

        reply = temp.format(user1=user1, user2=user2)

        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


SLAP_HANDLER = DisableAbleCommandHandler("slap", slap)

dispatcher.add_handler(SLAP_HANDLER)

__command_list__ = [

       "slap"

]

__handlers__ = [

       SLAP_HANDLER

]
