import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import multitasking
import signal

class bot:

    def __init__(self):
        updater = Updater("5563154280:AAHZUhvE9AjZAIacDlGxfxXEJS7cN48unoM", use_context=True)
        dp = updater.dispatcher


        #signal.signal(signal.SIGINT, multitasking.killall)

        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(CommandHandler("help", self.help))
        dp.add_handler(MessageHandler(Filters.text, self.echo))

        updater.start_polling()
        updater.idle()

    #@multitasking.task
    def start(self, update, context):
        update.message.reply_text("Conexion establecida")
        while True:
            txt = input()
            if txt == "":
                txt = "Error al enviar mensaje"
            self.msg.append("Rasp: "+txt)
            update.message.reply_text(txt)

    def help(self, update, context):
        update.message.reply_text('Help!')

    def echo(self, update, context):
        self.msg.append("User: "+update.message.text)
        print(update.message.text)
        #update.message.reply_text(update.message.text)
