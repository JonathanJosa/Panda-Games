import tennis
import snake

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


game = int(input())
if game == 1:
    snake_game()
elif game == 2:
    tennis_game()
