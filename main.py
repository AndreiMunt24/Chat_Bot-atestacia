from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers import schedule, start, donate, button_handler, inline_buttons
from config import TOKEN

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("schedule", schedule))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("donate", donate))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))

    application.run_polling()

if __name__ == "__main__":
    main()
