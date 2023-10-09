from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from settings import TOKEN
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename="logs.log"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "Привет, напиши число на которое хочешь узнать расписание и свой класс."
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=text)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=number)
"""
async def echo2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    your_class = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=your_class)

"""
if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
#    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo2))

    application.run_polling()
#https://docs-python.ru/packages/biblioteka-python-telegram-bot-python/