import os 
from callback import start,dog,cat,send_like_photo
from telegram.ext import (Updater,
                          Filters,
                          CommandHandler,
                          MessageHandler,
                          CallbackQueryHandler)
TOKEN=os.environ["TOKEN"]
def main():
    updater=Updater(TOKEN)
    dispecher=updater.dispatcher
    dispecher.add_handler(handler=CommandHandler(command="start",callback=start))
    dispecher.add_handler(handler=MessageHandler(Filters.text("Dog 🐶"),callback=dog))
    dispecher.add_handler(handler=MessageHandler(Filters.text("Cat 🐈"),callback=cat))
    dispecher.add_handler(handler=MessageHandler(Filters.text("My like photo 📸"),callback=send_like_photo))
    dispecher.add_handler(handler=CallbackQueryHandler(send_like_photo))
    
    
    
    updater.start_polling()
    updater.idle()
    
if __name__=="__main__":
    main()
    