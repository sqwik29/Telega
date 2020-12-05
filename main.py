import telebot
bot = telebot.TeleBot('1435977321:AAEooPYb77BHDWqWHyRJD3jN5eoFe25Q7jg')
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    #bot.send_message(message.from_user.id, "Hello, how can i help you?")
    if message.json["text"] == "Hello":
        bot.send_message(message.from_user.id, "Hello")
bot.polling(none_stop=True, interval=0)