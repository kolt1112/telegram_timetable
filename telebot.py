from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler

from errors import WorksheetDoesNotExist
from parser import get_schedule
from settings import TOKEN
import logging


formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler("./logs/logs.log")
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(formatter)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

DATA_SELECT, CLASS_NAME = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Привет, напиши число на которое хочешь узнать расписание и свой класс.")
    return DATA_SELECT


async def data_select(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['select_data'] = update.message.text
    await update.message.reply_text("Введите класс")
    return CLASS_NAME


async def class_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['class_name'] = update.message.text
    try:
        answer = get_schedule(context.user_data['select_data'],
                              context.user_data['class_name'])
    except WorksheetDoesNotExist:
        await update.message.reply_text('Вы ввели несуществующую дату')

    text = '<code>' + '\n'.join(f'№{row[0]} ⏰: {row[1]} 📖: {row[2]}' for row in answer) + '</code>'
    await update.message.reply_text(text, parse_mode=ParseMode.HTML)
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Пока и удачи!")
    return ConversationHandler.END


def main():
    application = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            DATA_SELECT: [MessageHandler(filters.TEXT & ~filters.COMMAND, data_select)],
            CLASS_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, class_name)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
