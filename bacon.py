#!/usr/bin/env python

import config as c
import messages as m

import telegram.bot
from telegram.ext import messagequeue as mq
from telegram.ext import CommandHandler
from telegram.utils.request import Request
from telegram.ext.updater import Updater


class MQBot(telegram.bot.Bot):
    '''
    A subclass of Bot which delegates send method handling to MQ
    Extended from: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Avoiding-flood-limits
    '''

    def __init__(self, *args, is_queued_def=True, mqueue=None, **kwargs):
        super(MQBot, self).__init__(*args, **kwargs)
        # below 2 attributes should be provided for decorator usage
        self._is_messages_queued_default = is_queued_def
        self._msg_queue = mqueue or mq.MessageQueue()

    def __del__(self):
        try:
            self._msg_queue.stop()
        except:
            pass

    @mq.queuedmessage
    def send_message(self, *args, **kwargs):
        '''Wrapped method would accept new `queued` and `isgroup`
        OPTIONAL arguments'''
        return super(MQBot, self).send_message(*args, **kwargs)

    @mq.queuedmessage
    def send_sticker(self, *args, **kwargs):
        '''Again, just needed for the decorator'''
        return super(MQBot, self).send_sticker(*args, **kwargs)


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
    # The limit is 30/s, but we'll keep it safe because we don't have that much traffic anyways
    q = mq.MessageQueue(all_burst_limit=25, all_time_limit_ms=1017)

    request = Request(con_pool_size=8)
    testbot = MQBot(c.TOKEN, request=request, mqueue=q)
    updater = Updater(bot=testbot, use_context=True)
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
