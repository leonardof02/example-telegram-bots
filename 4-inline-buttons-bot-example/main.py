from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, \
CommandHandler, ContextTypes, CallbackContext, CallbackQueryHandler

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Decir Hola", callback_data="Hola"),
            InlineKeyboardButton(text="Decir Feo", callback_data="Feo"),
            InlineKeyboardButton(text="Decir Uff", callback_data="Temazooo"),
        ],
        [InlineKeyboardButton(text="Wikipedia", url="www.wikipedia.com")],    
    ])

    await update.message.reply_text("Hello World!", reply_markup=keyboard)

async def button_controller( update: Update, context: CallbackContext ):

    data = update.callback_query.data
    if( data == "Hola" ):
        await update.callback_query.message.edit_text("Hola Hola Hola", reply_markup=None)
        return
    
    await update.callback_query.answer( text=data,show_alert=True )
    await update.callback_query.message.reply_text(data)


async def send_link( update: Update, context: ContextTypes.DEFAULT_TYPE ):
    button_name = context.args[0]
    link = context.args[1]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(button_name,url=link)]])
    await update.message.reply_text("Ve a este sitio!!!", reply_markup=keyboard)
    pass
    

TOKEN = "<Insert your token>"
application = ApplicationBuilder().token(TOKEN).build()

application.add_handler( CommandHandler( "start", say_hello ) )
application.add_handler( CommandHandler("link", send_link) )
application.add_handler( CallbackQueryHandler(button_controller) )

application.run_polling(allowed_updates=Update.ALL_TYPES)