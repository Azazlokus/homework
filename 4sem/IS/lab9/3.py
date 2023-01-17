from random import randint
from telegram.ext import Updater, Dispatcher, CommandHandler, Filters, MessageHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from tg_bot import token

reply_keyboard = [
    ['/dice', '/timer']
]

dice_keyboard = [
    ["кинуть 1 шестигранный кубик", "кинуть 2 шестигранных кубика одновременно"],
    ["кинуть 20-гранный кубик", "вернуться назад"]
]

timer_keyboard = [
    ["30 секунд", "1 минута"],
    ["5 минут", "вернуться назад"]
]

close_keyboard = [
    ["/close"]
]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
markup_dice = ReplyKeyboardMarkup(dice_keyboard, one_time_keyboard=False, resize_keyboard=True)
markup_timer = ReplyKeyboardMarkup(timer_keyboard, one_time_keyboard=False, resize_keyboard=True)
markup_close = ReplyKeyboardMarkup(close_keyboard, one_time_keyboard=False, resize_keyboard=True)

def start(update, context):
    update.message.reply_text("start", reply_markup=markup)

def dice(update, context):
    update.message.reply_text("dice", reply_markup=markup_dice)

def timer(update, context):
    update.message.reply_text("timer", reply_markup=markup_timer)

def roll_cube(faces, count):
    nums = [randint(1, int(faces)) for _ in range(count)]
    return nums

def set_timer(update, context, time):
    chat_id = update.message.chat_id
    try:
        due = int(time)
        
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(task, due, context=chat_id)
        context.chat_data['job'] = new_job
        update.message.reply_text(f'Засек {due} секунд', reply_markup=markup_close)

    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set <секунд>')


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Указанное время истекло')

def unset_timer(update, context):
    if 'job' not in context.chat_data:
        update.message.reply_text('Нет активного таймера', reply_markup=markup_timer)
        return
    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']
    update.message.reply_text('Сбрасываю таймер', reply_markup=markup_timer)


def ans(update, context):
    if update.message.text == "кинуть 1 шестигранный кубик":
        num = roll_cube(6, 1)
        update.message.reply_text(*num)
    elif update.message.text == "кинуть 2 шестигранных кубика одновременно":
        nums = list(map(str, roll_cube(6, 2)))
        str_nums = str(nums[0]) + ", " + str(nums[1]) 
        update.message.reply_text(str_nums)
    elif update.message.text == "кинуть 20-гранный кубик":
        num = roll_cube(20, 1)
        update.message.reply_text(*num)
    elif update.message.text == "30 секунд":
        set_timer(update, context, 30)
    elif update.message.text == "1 минута":
        set_timer(update, context, 60)
    elif update.message.text == "5 минут":
        set_timer(update, context, 300)
    elif update.message.text == "вернуться назад":
        update.message.reply_text("вернуться назад", reply_markup=markup)       
    
    
updater = Updater(token, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("dice", dice))
dp.add_handler(CommandHandler("timer", timer))
dp.add_handler(CommandHandler("close", unset_timer))
dp.add_handler(MessageHandler(Filters.text, ans))

updater.start_polling()
updater.idle()
