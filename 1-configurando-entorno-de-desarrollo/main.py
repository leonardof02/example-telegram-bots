from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World!")

application = ApplicationBuilder().token("<INSERT YOUR TOKEN>").build()

application.add_handler( CommandHandler( "start", say_hello ) )

application.run_polling(allowed_updates=Update.ALL_TYPES)