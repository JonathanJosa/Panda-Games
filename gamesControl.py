import tennis
import snake

import time
import RPi.GPIO as GPIO

def snake_game():
    game_1 = snake.snake()
    keep = True
    while keep:
        for i in range(len(pines)):
            if GPIO.input(pines[i]) == 1:
                if not game_1.press(i):
                    keep = False

def tennis_game():
    game_1 = tennis.tennis()
    keep = True
    while keep:
        for i in range(len(pines)):
            if GPIO.input(pines[i]) == 1:
                if not game_1.press(i):
                    keep = False


GPIO.setmode(GPIO.BOARD)

pines = [11, 12, 13, 15, 16, 18, 19, 21, 22, 23]

for pin in pines:
    GPIO.setup(pin, GPIO.IN)


game = int(input())
if game == 1:
    snake_game()
elif game == 2:
    tennis_game()
