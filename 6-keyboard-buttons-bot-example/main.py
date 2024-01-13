from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# File ID Sticker
# CAACAgQAAxkBAAICSGWeGvLgwzuR2t9zGQKSFnbOxS0eAAJECQAClA3oUkxe1gvtNZKVNAQ

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("Hola"), KeyboardButton("Hola")],
        [KeyboardButton("Adios")]
    ])
    await update.message.reply_text("Teclado enviado", reply_markup=keyboard)

async def saludar_o_despedir( update: Update, context: ContextTypes.DEFAULT_TYPE ):
    if update.message.text == "Hola":
        await update.message.reply_text("Como estas?", reply_markup=ReplyKeyboardRemove())
    if update.message.text == "Adios":
        await update.message.reply_sticker("CAACAgQAAxkBAAICSGWeGvLgwzuR2t9zGQKSFnbOxS0eAAJECQAClA3oUkxe1gvtNZKVNAQ", reply_markup=ReplyKeyboardRemove())
    pass

TOKEN = "<Insert your token>"

application = ApplicationBuilder().token(TOKEN).build()

application.add_handler( CommandHandler( "start", say_hello ) )
application.add_handler( MessageHandler( filters.ALL, saludar_o_despedir ) )

application.run_polling(allowed_updates=Update.ALL_TYPES)