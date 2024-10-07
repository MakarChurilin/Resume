import telebot
from googletrans import Translator, LANGUAGES

TOKEN = '7863623614:AAFpPQ6oYYa8YloYrih1dLsEnTwshM0Z9R8'
bot = telebot.TeleBot(TOKEN)

translator = Translator()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я бот-переводчик. Используй команду /translate')

@bot.message_handler(commands=['translate'])
def handle_translate(message):
    try:
        command, *args = message.text.split()

        if len(args) < 2:
            bot.reply_to(message, 'Пожалуйста, укажите язык и текст для перевода. Пример: /translate en Привет мир')
            return

        language = args[0]
        text = ' '.join(args[1:])

        translated = translator.translate(text, dest=language).text

        bot.reply_to(message, translated)
    except Exception as e:
        bot.reply_to(message, f'Произошла ошибка: {e}')

@bot.message_handler(commands=['languages'])
def handle_languages(message):
    languages_list = "\n".join([f"{key}: {value}" for key, value in LANGUAGES.items()])
    bot.reply_to(message, f'Поддерживаемые языки:\n{languages_list}')

bot.polling(timeout=60)