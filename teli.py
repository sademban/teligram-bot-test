import schedule
import telebot
from telebot import types
import time
import threading
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variable
token = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(token)

# Initialize flag as a global variable
flag = False
idd = None  # This will hold the user ID

@bot.message_handler(commands=['start'])
def start_handler(message):
    global idd
    idd = message.from_user.id
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('yes', callback_data='yes')
    btn2 = types.InlineKeyboardButton('no', callback_data='no')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'spam', reply_markup=markup)

def spam():
    if idd is not None and flag:  # Ensure flag is checked before sending
        bot.send_message(idd, 'testtest')

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global flag
    if callback.data == 'yes':
        flag = True
        schedule.every().second.do(spam)
    elif callback.data == 'no':
        flag = False
        schedule.clear()  # Clear the scheduled jobs

# Start the schedule in a separate thread
threading.Thread(target=run_schedule, daemon=True).start()

# Start the bot
bot.infinity_polling()
