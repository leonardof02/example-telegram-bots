from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, ApplicationBuilder, MessageHandler, ConversationHandler, filters

from Controllers.UserProfileController import user_profile_controller_conversation_handler

TOKEN = "<Insert your token>"

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler( user_profile_controller_conversation_handler )

application.run_polling(allowed_updates=Update.ALL_TYPES)