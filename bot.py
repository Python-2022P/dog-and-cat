from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup
import os


TOKEN = os.environ.get('TOKEN')


def start(update: Update, context):
    update.message.reply_text('Hello!', reply_markup=ReplyKeyboardMarkup([['🐶']], resize_keyboard=True))


def main():
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
