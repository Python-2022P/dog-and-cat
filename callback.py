import requests
import telegram
from telegram import (Update,
                      ReplyKeyboardMarkup,
                      KeyboardButton,
                      InlineKeyboardMarkup,
                      InlineKeyboardButton)
from telegram.ext import CallbackContext
from db import Db
import os
db=Db()
url_dog=""
url_cat=""
def start(update: Update, callback: CallbackContext):
    chat_id=update.message.chat.id
    chat_name=update.message.chat.full_name
    chat_user=update.message.chat.username
    db.add_user(chat_id,chat_name,chat_user)
    btn1=ReplyKeyboardMarkup([["Dog 🐶","Cat 🐈"]],resize_keyboard=True)
    

    update.message.reply_html("<b>Welcome our bot</b>\nPress one of the buttons",reply_markup=btn1)
    
    db.add_user(chat_id,chat_name,chat_user)
def dog(update: Update, collback: CallbackContext):
    
    response: str=requests.get("https://random.dog/woof.json").json()["url"]
    global url_dog
    url_dog=response    
    
    # keyboard
    btn1 = InlineKeyboardButton(text='👍', callback_data='like')
    btn2 = InlineKeyboardButton(text='👎', callback_data='dislike')
    inline_keyboard = [
        [btn1, btn2]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    (update.message.reply_photo(response,reply_markup=reply_markup).photo[-1].file_id)
    
    return response

def cat(update: Update, collback: CallbackContext):
    
    response="https://cataas.com"+requests.get("https://cataas.com/cat?json=true").json()["url"]
    global url_cat
    url_cat=response
    
    
    # keyboard
    btn1 = InlineKeyboardButton(text='👍', callback_data='like')
    btn2 = InlineKeyboardButton(text='👎', callback_data='dislike')
    inline_keyboard = [
        [btn1, btn2]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    
    update.message.reply_photo(response,reply_markup=reply_markup)


    update.message.reply_html(text=f'Saved is your photo of cat',reply_markup=ReplyKeyboardMarkup([["Dog 🐶","Cat 🐈"]],resize_keyboard=True))
def send_like_photo(update: Update, callback: CallbackContext):
    chat_id=update.callback_query.from_user.id
    data=update.callback_query.data

    if data=="like":
        db.increase_like(chat_id)
        update.callback_query.message.reply_html(db.stat(f'{chat_id}'))        
    elif data=="dislike":
        db.increase_dislike(chat_id)
        update.callback_query.message.reply_html(db.stat(chat_id))