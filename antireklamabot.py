import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Bot tokeningizni kiriting
TOKEN = 'token'

# Reklama so'zlari va linklar ro'yxati
BAD_WORDS = ['reklama', 'link', 'promo', 'sale']
BAD_LINKS = ['http://', 'https://', 'www.']

# Xabarlarni tekshirish va o'chirish uchun funksiya
def filter_messages(update: Update, context: CallbackContext):
    message = update.message.text.lower()

    # So'zlar bo'yicha tekshirish
    if any(word in message for word in BAD_WORDS) or any(link in message for link in BAD_LINKS):
        update.message.delete()

# Start komandasi
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom! Men reklama va linklarni guruhda cheklayman.")

# Botni ishga tushirish
def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    # Start komandasi
    dp.add_handler(CommandHandler("start", start))

    # Xabarlar filtrini qo'shish
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, filter_messages))

    # Botni doimiy ishlashini ta'minlash
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
