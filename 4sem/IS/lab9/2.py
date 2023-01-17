from http.cookiejar import Cookie
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from tg_bot import token
import datetime

def echo(update, context):
    update.message.reply_text("Я получил сообщение " + update.message.text)

def com_time(update, context):
    now = datetime.datetime.now()
    hours = str(now.hour)
    minutes = str(now.minute)
    seconds = str(now.second)
    update.message.reply_text(hours + ":" + minutes + ":" + seconds)

def com_date(update, context):
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    update.message.reply_text(day + "/" + month + "/" + year)

updater = Updater(token, use_context=True)
dp = updater.dispatcher


text_handler = MessageHandler(Filters.text, echo)
dp.add_handler(CommandHandler("time", com_time))
dp.add_handler(CommandHandler("date", com_date))
dp.add_handler(text_handler)
updater.start_polling()
updater.idle()