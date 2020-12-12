import telebot
bot = telebot.TeleBot('1435977321:AAEooPYb77BHDWqWHyRJD3jN5eoFe25Q7jg')
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    print(message)
    ist = message.json["text"].split()
    for a in ist:
        bot.send_message(message.from_user.id, a)

bot.polling(none_stop=True, interval=0)