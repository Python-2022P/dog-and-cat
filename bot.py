from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import os
import requests


TOKEN = os.environ.get('TOKEN')


def start(update: Update, context):
    print(update.message.from_user.full_name, 'start')
    update.message.reply_text('Hello!', reply_markup=ReplyKeyboardMarkup([['🐶']], resize_keyboard=True))

def send_dog(update: Update, context):
    response = requests.get('https://random.dog/woof.json')
    url = response.json()['url']
    
    update.message.reply_photo(url, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton('👍', callback_data='like'), InlineKeyboardButton('👎', callback_data='dislike')]]))

def inline_query(update: Update, context):
    data = update.callback_query.data
    if data == 'like':
        update.callback_query.answer('like')
    elif data == 'dislike':
        update.callback_query.answer('dislike')
    


def main():
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('🐶'), send_dog))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_query))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
