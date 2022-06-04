import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import multitasking
import signal
import time

class chat:
    def __init__(self):
        self.queueText = []
        self.msg = []
        self.queueLen = 0

    def screen(self, MainWindow):
        MainWindow.resize(600, 800)
        self.widgets = QtWidgets.QWidget(MainWindow)

        self.input = QtWidgets.QLineEdit(self.widgets)
        self.input.setGeometry(QtCore.QRect(75, 700, 375, 40))

        self.analizar = QtWidgets.QPushButton(self.widgets)
        self.analizar.setGeometry(QtCore.QRect(460, 700, 65, 40))
        self.analizar.setText(">")
        self.analizar.clicked.connect(self.detectData)

        self.box = QtWidgets.QTextBrowser(self.widgets)
        self.box.setGeometry(QtCore.QRect(75, 60, 450, 630))

        MainWindow.setCentralWidget(self.widgets)

    def detectData(self, _):
        txt = self.input.text()
        self.msg.append("-> Rasp: "+txt)
        self.input.setText("")
        self.refreshDataBox()

    def refreshDataBox(self):
        self.box.setText(''.join([ i+"\n" for i in self.msg[-30:][::-1] ]))

    def chatBot(self):
        self.updater = Updater("5159291527:AAECemDgi7fT9VkN2YA3opmTS0GbRnCTZSA", use_context=True)
        dp = self.updater.dispatcher

        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(MessageHandler(Filters.text, self.echo))

        self.updater.start_polling()
        print("init chat")
        self.updater.idle()

    def start(self, update, context):
        update.message.reply_text("Conexion establecida")

    def echo(self, update, context):
        self.msg.append("-> User: "+update.message.text)
        self.refreshDataBox()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, multitasking.killall)
    ui = chat()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui.screen(MainWindow)
    MainWindow.show()
    ui.chatBot()
