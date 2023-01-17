from telegram.ext import Updater, MessageHandler, Filters
from tg_bot import token

def echo(update, context):
    update.message.reply_text("Я получил сообщение " + update.message.text)

updater = Updater(token, use_context=True)
dp = updater.dispatcher
text_handler = MessageHandler(Filters.text, echo)
dp.add_handler(text_handler)
updater.start_polling()
updater.idle()
