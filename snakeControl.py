import snake
import time
import RPi.GPIO as GPIO

game_1 = snake.snake()

GPIO.setmode(GPIO.BOARD)

pines = [11, 12, 13, 15, 16, 18]

for pin in pines:
    GPIO.setup(pin, GPIO.IN)

while True:
    for i in range(len(pines)):
        if GPIO.input(pines[i]) == 1:
            game_1.press(i)
