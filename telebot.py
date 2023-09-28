from telegram.ext import Updater, MessageHandler, CommandHandler


def start(bot, update):
    update.message.bot_text("Привет, напиши число на которое хочешь узнать расписание и свой класс.")


updater = Updater('6572797075:AAFH_zY6uLZYKLEiGHZTRG8Jdm-ud4tYoDs')
#bot.polling(none_stop=True)