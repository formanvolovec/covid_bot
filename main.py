import telebot
from telebot import types
import COVID19Py

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1227263304:AAHlmuYYa6LJdXFBYDreNAV-yAgQPz6WxDo')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('Сша')
    btn3 = types.KeyboardButton('Россия')
    btn4 = types.KeyboardButton('Беларусь')
    btn5 = types.KeyboardButton('Украина')
    btn6 = types.KeyboardButton('Италия')
    btn7 = types.KeyboardButton('Испания')
    btn8 = types.KeyboardButton('Германия')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные про коронавируса " \
                   f"напишите название страны.\n"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "испания":
        location = covid19.getLocationByCountryCode("ES")
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode("DE")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
