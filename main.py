import telebot
import wikipediaapi

wiki_api = wikipediaapi.Wikipedia('en')
bot_token = 'токен'
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Вітаю! Введіть запит щоб знайти статтю на Wiki')
@bot.message_handler(func=lambda message: True)
def search_wikipedia(message):
    query = message.text
    page = wiki_api.page(query)
    if page.exists():
        summary = page.summary[:1000]
        bot.reply_to(message, summary)
    else:
        bot.reply_to(message, 'Такої статті немає')
bot.polling()