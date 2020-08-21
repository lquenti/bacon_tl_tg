#!/usr/bin/env python

import config as c
import messages as m

from telegram.ext import Updater, CommandHandler


def start_handler(update, context):
    """
    Gets called whenever someone starts a dialogue
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=m.START_MESSAGE)


def bacon_handler(update, context):
    """
    Gets called when someone writes /bacon. Sends the bacon depending on the value of config.SEND_AS
    """
    chat_id = update.effective_chat.id
    if c.SEND_AS == c.PicMode.LINK:
        for msg in m.ALL_TWEETS_LINK:
            context.bot.send_message(chat_id, text=msg)
    elif c.SEND_AS == c.PicMode.PIC:
        for path, msg in m.ALL_TWEETS_PIC:
            context.bot.send_photo(chat_id, open(path, 'rb'), caption=msg)
    else:  # Sticker
        for sticker_id, msg in m.ALL_TWEETS_STICKER:
            context.bot.send_sticker(chat_id, sticker_id)
            context.bot.send_message(chat_id=chat_id, text=msg)


def main():
    updater = Updater(token=c.TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(CommandHandler("bacon", bacon_handler))

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
