from telebot import TeleBot
import multitasking
import signal
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

bot = TeleBot(__name__)

def iniciar():
    signal.signal(signal.SIGINT, multitasking.killall)
    global queue_msg
    global users
    users = {0: "Raspi"}
    queue_msg = []
    start_bot()

@multitasking.task
def start_bot():
    bot.config['api_key'] = "5159291527:AAECemDgi7fT9VkN2YA3opmTS0GbRnCTZSA"
    bot.poll(debug=True)

@bot.route('/name ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    name = message['text'][6:]
    if name == "":
        name = "user#"+str(len(users)+1)
    users[chat_dest] = name
    bot.send_message(chat_dest, "Connected to server, actual users: "+str(len(users)))
    bot.send_message(chat_dest, "Welcome to server: " + name)


@bot.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']
    if users.get(chat_dest) == None:
        users[chat_dest] = "user#" + str(len(users))
    msg = users[chat_dest] + ": " + user_msg
    queue_msg.append(msg)
    for hash_user in list(users.keys()):
        if hash_user != chat_dest:
            bot.send_message(hash_user, msg)



def screen(MainWindow):
    MainWindow.resize(600, 800)
    widgets = QtWidgets.QWidget(MainWindow)

    global input
    input = QtWidgets.QLineEdit(widgets)
    input.setGeometry(QtCore.QRect(75, 700, 375, 40))
    input.returnPressed.connect(detectData_2)

    analizar = QtWidgets.QPushButton(widgets)
    analizar.setGeometry(QtCore.QRect(460, 700, 65, 40))
    analizar.setText(">")
    analizar.clicked.connect(detectData)
    analizar.setAutoDefault(True)

    global box
    box = QtWidgets.QTextBrowser(widgets)
    box.setGeometry(QtCore.QRect(75, 60, 450, 630))

    MainWindow.setCentralWidget(widgets)


def refreshDataBox():
    box.setText(''.join([ i+"\n" for i in queue_msg[-30:][::-1] ]))

def detectData(_):
    txt = input.text()
    if txt != "":
        msg = "Raspi: " + txt
        input.setText("")
        queue_msg.append(msg)
        for hash_user in users:
            bot.send_message(hash_user, msg)

def detectData_2():
    txt = input.text()
    if txt != "":
        msg = "Raspi: " + txt
        input.setText("")
        queue_msg.append(msg)
        for hash_user in users:
            bot.send_message(hash_user, msg)

def interface():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    screen(MainWindow)
    MainWindow.show()
    timer = QtCore.QTimer()
    timer.setInterval(300)
    timer.timeout.connect(refreshDataBox)
    timer.start()
    app.exec_()
