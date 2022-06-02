import oledClass
import snake
import tennis

import time
import RPi.GPIO as GPIO

def snake_game():
    try:
        game_1 = snake.snake()
        while True:
            for i in range(len(pines)):
                if GPIO.input(pines[i]) == 1:
                    game_1.press(i)
    except:
        print("end snake game")

def tennis_game():
    try:
        game_1 = tennis.tennis()
        while True:
            for i in range(len(pines)):
                if GPIO.input(pines[i]) == 1:
                    game_1.press(i)
    except:
        print("end tennis game")

GPIO.setmode(GPIO.BOARD)

pines = [11, 12, 13, 15, 16, 18]

for pin in pines:
    GPIO.setup(pin, GPIO.IN)

oled = oledClass.display()
while True:
    oled.bienvenida()
    oled.menu()

    selected = False
    game = 1

    while selected:
        if GPIO.input(16) == 1:
            game += 1
            if game == 3:
                game = 1
        if GPIO.input(18) == 1:
            game -= 1
            if game == 0:
                game = 2
        if GPIO.input(12) == 1:
            selected = True


    if game == 1:
        snake_game()
    elif game == 1:
        tennis_game()
