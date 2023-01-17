import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, Update
from fake_useragent import UserAgent
from tokens import tokens

bot_token = tokens["telegram_bot"]
weather_token = tokens["api_yandex_weather"]
geocoder_token = tokens["geocoder"]

command_1 = "\U00002604 Погода на сегодня"
command_2 = "\U00002604 Погода на неделю"
command_3 = "\U0001F4F0 Новости"
command_4 = "\U0001F195 Сменить город"
user_city = ""
prevAns = ""

weather_keyboard = [
    [command_1, command_2],
    [command_3, command_4]
]

markup = ReplyKeyboardMarkup(
    weather_keyboard, one_time_keyboard=False, resize_keyboard=True)


def get_pos(city: str):
    response = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey={geocoder_token}&geocode={city}&format=json")
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"].split()
    return toponym_coodrinates


def change_city(update: Update, context: CallbackContext):
    global prevAns, user_city
    prevAns = ""
    user_city = update.message.text


def yandex_weather_today(latitude: str, longitude: str):
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}&[lang=ru_RU]"
    response = requests.get(url, headers={"X-Yandex-API-Key": weather_token})
    conditions = {"clear": "ясно \U00002600", "partly-cloudy": "малооблачно \U0001F324", "cloudy": "облачно с прояснениями \U000026C5",
                  "overcast": "пасмурно \U0001F327", "drizzle": "морось \U0001F326", "light-rain": "небольшой дождь \U0001F327",
                  "rain": "дождь \U0001F327", "moderate-rain": "умеренно сильный дождь \U0001F327", "heavy-rain": "сильный дождь \U0001F327",
                  "continuous-heavy-rain": "длительный сильный дождь \U0001F327", "showers": "ливень \U0001F327",
                  "wet-snow": "дождь со снегом \U0001F328", "light-snow": "небольшой снег \U0001F328", "snow": "снег \U0001F328",
                  "snow-showers": "снегопад \U0001F328", "hail": "град \U000026C8", "thunderstorm": "гроза \U0001F329",
                  "thunderstorm-with-rain": "дождь с грозой \U000026C8", "thunderstorm-with-hail": "гроза с градом \U000026C8"
                  }
    wind_dir = {"nw": "северо-западный", "n": "северный", "ne": "северо-восточный", "e": "восточный",
                "se": "юго-восточный", "s": "южный", "sw": "юго-западный", "w": "западный", "с": "штиль"}
    yandex_json = response.json()
    

    yandex_json["fact"]["condition"] = conditions[yandex_json["fact"]["condition"]]
    yandex_json["fact"]["wind_dir"] = wind_dir[yandex_json["fact"]["wind_dir"]]
    for part in yandex_json["forecasts"][0]["parts"]:
        yandex_json["forecasts"][0]["parts"][part]["condition"] = conditions[yandex_json["forecasts"]
                                                                             [0]["parts"][part]["condition"]]
        yandex_json["forecasts"][0]["parts"][part]["wind_dir"] = wind_dir[yandex_json["forecasts"]
                                                                          [0]["parts"][part]["wind_dir"]]

    weather = dict()
    params = ["condition", "wind_speed", "wind_dir", "pressure_mm", "humidity"]

    for part in yandex_json["forecasts"][0]["parts"]:
        if "short" not in part:
            weather[part] = dict()
            weather[part]["temp"] = yandex_json["forecasts"][0]["parts"][part]["temp_avg"]
            for param in params:
                weather[part][param] = yandex_json["forecasts"][0]["parts"][part][param]

    weather["fact"] = dict()
    weather["fact"]["temp"] = yandex_json["fact"]["temp"]
    for param in params:
        weather["fact"][param] = yandex_json["fact"][param]

    weather["link"] = yandex_json["info"]["url"]

    return weather

def yandex_weather_week(latitude: str, longitude: str):
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}&[lang=ru_RU]&[limit=7]"
    response = requests.get(url, headers={"X-Yandex-API-Key": weather_token})
    conditions = {"clear": "ясно \U00002600", "partly-cloudy": "малооблачно \U0001F324", "cloudy": "облачно с прояснениями \U000026C5",
                  "overcast": "пасмурно \U0001F327", "drizzle": "морось \U0001F326", "light-rain": "небольшой дождь \U0001F327",
                  "rain": "дождь \U0001F327", "moderate-rain": "умеренно сильный дождь \U0001F327", "heavy-rain": "сильный дождь \U0001F327",
                  "continuous-heavy-rain": "длительный сильный дождь \U0001F327", "showers": "ливень \U0001F327",
                  "wet-snow": "дождь со снегом \U0001F328", "light-snow": "небольшой снег \U0001F328", "snow": "снег \U0001F328",
                  "snow-showers": "снегопад \U0001F328", "hail": "град \U000026C8", "thunderstorm": "гроза \U0001F329",
                  "thunderstorm-with-rain": "дождь с грозой \U000026C8", "thunderstorm-with-hail": "гроза с градом \U000026C8"
                  }
    wind_dir = {"nw": "северо-западный", "n": "северный", "ne": "северо-восточный", "e": "восточный",
                "se": "юго-восточный", "s": "южный", "sw": "юго-западный", "w": "западный", "с": "штиль"}
    yandex_json = response.json()
    for day in range(7):
        for part in yandex_json["forecasts"][day]["parts"]:
            yandex_json["forecasts"][day]["parts"][part]["condition"] = conditions[yandex_json["forecasts"][day]["parts"][part]["condition"]]
            yandex_json["forecasts"][day]["parts"][part]["wind_dir"] = wind_dir[yandex_json["forecasts"][day]["parts"][part]["wind_dir"]]

    weather = dict()
    params = ["condition", "wind_speed", "wind_dir", "pressure_mm", "humidity"]

    for day in range(7):
        weather[day] = dict()
        weather[day]["date"] = yandex_json["forecasts"][day]["date"]
        weather[day]["day_short"] = dict()
        weather[day]["day_short"]["temp"] = yandex_json["forecasts"][day]["parts"]["day_short"]["temp"]
        for param in params:
            weather[day]["day_short"][param] = yandex_json["forecasts"][day]["parts"]["day_short"][param]
    return weather


def get_news():
    global user_city
    url = "https://yandex.ru/news/region/"
    translit_user_city = ""
    replace_user_city = ""

    replace_table = {
        "й": "y", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
        "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "",
        "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
        "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
        "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "",
        "б": "b", "ю": "ju", "ё": "jo", " ": "_", "-": "-"
    }
    for letter in user_city:
        if letter.lower() in replace_table:
            translit_user_city += replace_table[letter.lower()]

    if user_city.lower() == "москва":
        replace_user_city += "moscow"
    elif user_city.lower() == "нижний новгород":
        replace_user_city += "nizhny_novgorod"
    elif user_city.lower() == "великий новгород":
        replace_user_city += "veliky_novgorod"
    elif user_city.lower() == "санкт-петербург":
        replace_user_city += "saint_petersburg"
        
    
    news_list = []
    if replace_user_city != "":
        url += replace_user_city
    else:
        url += translit_user_city
        
    ua = UserAgent()
    header = {"User-Agent": str(ua.random)}
    response = requests.get(url, headers=header)
    if (response.status_code != 200):
        return news_list
    soup = BeautifulSoup(response.text, 'html.parser')
    for news in soup.find_all("a", class_="mg-card__link"):
        text = news.text
        link = news.get("href").replace("https://", "")
        news_list.append((link, text))
    return news_list



def send_weather_info_today(update: Update, context: CallbackContext, weather_dict: dict):
    day_time = {"night": "Ночь", "morning": "Утро",
           "day": "День", "evening": "Вечер", "fact": "Сейчас"}
    update.message.reply_text(f"\U0001FA90 Погода в городе {user_city}")
    for time in weather_dict.keys():
        if time != "link":
            time_day = day_time[time]
            update.message.reply_text(f"<b><i>{time_day}:</i></b>\n"
                                      f"\t\t \U0001F321 <b>Температура:</b> {weather_dict[time]['temp']} \U00002103 \n"
                                      f"\t\t \U00002601 <b>Погодные условия:</b> {weather_dict[time]['condition']} \n"
                                      f"\t\t \U0001F32A <b>Ветер:</b> {weather_dict[time]['wind_speed']} м/с ({weather_dict[time]['wind_dir']}) \n"
                                      f"\t\t \U0001F4A7 <b>Влажность:</b> {weather_dict[time]['humidity']}% \n"
                                      f"\t\t \U0001F300 <b>Давление:</b> {weather_dict[time]['pressure_mm']} мм.рт.ст \n", parse_mode="HTML")
    update.message.reply_text(
        f"Ссылка на более подробный прогноз: {weather_dict['link']}")

def send_weather_info_week(update: Update, context: CallbackContext, weather_dict: dict):
    update.message.reply_text(f"\U0001FA90 Погода на неделю в городе {user_city}")
    for day in range(7):
        date = weather_dict[day]['date']
        update.message.reply_text(f"<b><i>\U0001F4C5 {date}</i></b>", parse_mode="HTML")
        update.message.reply_text(f"\t\t \U0001F321 <b>Температура:</b> {weather_dict[day]['day_short']['temp']} \U00002103 \n"
                                    f"\t\t \U00002601 <b>Погодные условия:</b> {weather_dict[day]['day_short']['condition']} \n"
                                    f"\t\t \U0001F32A <b>Ветер:</b> {weather_dict[day]['day_short']['wind_speed']} м/с ({weather_dict[day]['day_short']['wind_dir']}) \n"
                                    f"\t\t \U0001F4A7 <b>Влажность:</b> {weather_dict[day]['day_short']['humidity']}% \n"
                                    f"\t\t \U0001F300 <b>Давление:</b> {weather_dict[day]['day_short']['pressure_mm']} мм.рт.ст \n", parse_mode="HTML")

def send_news_info(update: Update, context: CallbackContext, news_list: list):
    if not news_list:
        update.message.reply_text("Извините, не удалось найти новости в вашем городе \U00002639"
                                    "Попробуйте выбрать столицу вашего региона")
        return
    message = ""
    for i in range(5):
        message += "<b>" + str(i+1) + f". <a href='{news_list[i][0]}'>" + news_list[i][1] + "</a></b>\n" 
    update.message.reply_text(f"\U0001F4F0 Новости в регионе города {user_city}")
    update.message.reply_text(message, parse_mode="HTML")


def start(update, context):
    update.message.reply_text(
        f"Приятно познакомится, {update.message.chat.first_name} \U0000270C! Я бот для сообщения информации о погоде и новостях \U00002600." 
        "Введи название своего города ('Мой город ...'), чтобы я мог помочь тебе узнать погоду и новости в твоем городе")


def get_message(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if update.message.text.lower()[:9] == "мой город":
        global user_city
        user_city = update.message.text[10:]
        update.message.reply_text(
            f"Теперь я знаю твой город! Твой город {user_city}! Могу подсказать погоду)", reply_markup=markup)
    if user_city != "":
        if update.message.text == command_1:
            try:
                coords = get_pos(user_city)
                send_weather_info_today(update, context, yandex_weather_today(coords[1], coords[0]))
            except: 
                context.bot.send_message(chat_id=chat_id, text="Извини, я не смог найти у себя такого города") 
        elif update.message.text == command_2:
            coords = get_pos(user_city)
            send_weather_info_week(update, context, yandex_weather_week(coords[1], coords[0]))
        elif update.message.text == command_3:
            send_news_info(update, context, get_news())
        elif update.message.text == command_4:
            global prevAns
            context.bot.send_message(chat_id=chat_id, text="Введите название своего города:")
            prevAns = update.message.text
        elif prevAns == command_4:
            change_city(update, context)


updater = Updater(bot_token, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, get_message))

updater.start_polling()
updater.idle()
