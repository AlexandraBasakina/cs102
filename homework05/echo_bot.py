import telebot


access_token = '1058925626:AAHxRwFgujfINd04K4B8tsY0feVccHnLeeM'
bot = telebot.TeleBot(access_token)

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
