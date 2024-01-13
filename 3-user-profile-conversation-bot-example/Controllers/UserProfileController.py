from telegram import Update
from telegram.ext import filters, ConversationHandler, \
CommandHandler, MessageHandler, ContextTypes

""" Controlador con Conversation Handler """

USERNAME, INFO, PHOTO = range(3)

class UserProfileController:

    @staticmethod
    async def starting_get_info( update: Update, context: ContextTypes.DEFAULT_TYPE ):
        await update.message.reply_text("Creacion de pefil, escribe tu nombre de usuario:")
        return USERNAME

    @staticmethod
    async def get_username( update: Update, context: ContextTypes.DEFAULT_TYPE ):
        context.user_data["username"] = update.message.text
        await update.message.reply_text("Perfecto, escribe tu info:")
        return INFO

    @staticmethod
    async def get_info( update: Update, context: ContextTypes.DEFAULT_TYPE ):
        context.user_data["user_info"] = update.message.text
        await update.message.reply_text("Muchas gracias, podrias proporcionarnos una foto de perfil?")
        return PHOTO
    
    @staticmethod
    async def get_photo( update: Update, context: ContextTypes.DEFAULT_TYPE ):
        message = update.effective_message
        if message.photo: # Puede ser None
            context.user_data["user_photo"] = message.photo[-1].file_id
            await update.message.reply_photo(
                photo=context.user_data["user_photo"],
                caption=
                f"Nombre de usuario: {context.user_data['username']}\nInfo: {context.user_data['user_info']}"
            )
        else:
            await update.message.reply_text("No se proporciono una foto")
            await update.message.reply_text(
                f"Nombre de usuario: {context.user_data['username']}\nInfo: {context.user_data['user_info']}"
            )
        return ConversationHandler.END

    @staticmethod
    async def cancel_operation( update: Update, context: ContextTypes.DEFAULT_TYPE ):
        await update.message.reply_text("Operacion cancelada")
        return ConversationHandler.END
    
user_profile_controller_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("profile", UserProfileController.starting_get_info)],
    states={
        USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, UserProfileController.get_username)],
        INFO: [MessageHandler(filters.TEXT & ~filters.COMMAND, UserProfileController.get_info)],
        PHOTO: [MessageHandler(filters.ALL & ~filters.COMMAND, UserProfileController.get_photo)],
    },
    fallbacks=[MessageHandler(filters.COMMAND, UserProfileController.cancel_operation)]
)