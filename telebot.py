import os
from webbrowser import get

import telebot
from telebot.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
import certifi
import time
from datetime import datetime, timedelta
import operator
import psycopg2
import urllib.parse as up

#Database connection
up.uses_netloc.append("postgres")
url = up.urlparse("postgres://tahlzcju:CxBsyL_gRR_Ee1KBu-bmDOpf8_hUCGk_@satao.db.elephantsql.com/tahlzcju")
conn = psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
cursor = conn.cursor()

# Telegram Bot setup
API_KEY = '5942614858:AAHRlUVi-Y_7AOTZmYHMSaNGi29WXw66-1Q'
bot = telebot.TeleBot(API_KEY)

bot.set_my_commands([
    BotCommand('start', 'Starts the bot'),
])

#Commands
@bot.message_handler(commands=['start'])
def start(message):
    """
    Command that welcomes the user 
    """

    chat_id = message.chat.id
    chat_user = message.chat.username
    cursor.execute("SELECT FirstName FROM Persons WHERE PersonID = %s", (1234,))
    result = cursor.fetchone()
    first_name = result[0]
    cursor.close()
    conn.close()

    message_text = """ Hi @{}
                \nWelcome to Study.io's reminder bot!
                \nTo get started, please type /login [token_id] and key in your unique token_id.
                \nYou can get your token_id by clicking the <b>Telegram</b> icon under reminders on our <a href="https://study-io.herokuapp.com/">website</a>. 
                \nFor more details, check out /help!""".format(first_name)
    bot.send_message(chat_id, message_text, parse_mode= 'HTML')

# Running the bot
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)


