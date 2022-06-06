import tennis
import snake
import chat
import object
import menu
import pygame
import time
import RPi.GPIO as GPIO

def menuControl():
    init = menu.menu()
    global game
    keep = True
    while keep:
        for i in range(len(pines)):
            if GPIO.input(pines[i]) == 1:
                if not init.press(i):
                    keep = False
                game = init.select()

def snake_game():
    init = snake.snake()
    keep = True
    while keep:
        for i in range(len(pines)):
            if GPIO.input(pines[i]) == 1:
                if not init.press(i):
                    keep = False

def tennis_game():
    init = tennis.tennis()
    keep = True
    while keep:
        for i in range(len(pines)):
            if GPIO.input(pines[i]) == 1:
                if not init.press(i):
                    keep = False

def chat_telegram():
    chat.iniciar()
    chat.interface()
    return

def magicControl():
    object.obj()

GPIO.setmode(GPIO.BOARD)

pines = [11, 12, 13, 15, 16, 18, 19, 21, 22, 23]

for pin in pines:
    GPIO.setup(pin, GPIO.IN)

game = 0
while True:
    menuControl()
    ([
        lambda _ : snake_game(),
        lambda _ : tennis_game(),
        lambda _ : chat_telegram(),
        lambda _ : magicControl()
    ][game])(True)
