from telegram.ext import MessageHandler, CommandHandler, filters, Updater, Application, ApplicationBuilder, _application


def start(bot, update):
    update.message.bot_text("Привет, напиши число на которое хочешь узнать расписание и свой класс.")


def echo(bot, update):
    update.message.bot_text("sdfdsf" + update.message.text)

updater = ApplicationBuilder().token('6572797075:AAFH_zY6uLZYKLEiGHZTRG8Jdm-ud4tYoDs').build()

#updater = Updater.update_queue('6572797075:AAFH_zY6uLZYKLEiGHZTRG8Jdm-ud4tYoDs')

#TOKEN = '6572797075:AAFH_zY6uLZYKLEiGHZTRG8Jdm-ud4tYoDs'

#updater = Updater(token=TOKEN, use_context=True)

#dp = updater.dispatcher
_application.add_handler(CommandHandler('start', start))

#dp.add_handler(CommandHandler("start", start))

#text_handler = MessageHandler(filters.TEXT, echo)

#dp.add_handler(text_handler)
_application.run_polling(1.0)

#updater.start_polling()

#updater.idle()
