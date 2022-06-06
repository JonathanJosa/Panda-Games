import sys, pygame
from pygame.constants import *
import time
import serial

class obj:
    def __init__(self):
        pygame.init()

        self.dis = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Magic control')

        self.con = serial.Serial(port='/dev/ttyACM0', baudrate = 9600)
        self.clock = pygame.time.Clock()

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.loop()


    def loop(self):
        val = ""
        px = 400
        py = 400
        while True:
            self.dis.fill(self.black)
            for e in pygame.event.get():
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    sys.exit()

            x = self.con.read()
            if x == "b''":
                continue
            elif x == b'\r' or x == b'\n':
                if val != "":
                    v = int(val)
                    if v >= 41:
                        py = (v-41) * 10
                    else:
                        px = v * 10
                val = ""
            else:
                val += str(int(x,16))

            pygame.draw.rect(self.dis, self.white, [900 - (px//2), 400 - (py//2), px, py])
            pygame.draw.rect(self.dis, self.white, [300 - (py//2), 400 - (px//2), py, px])
            pygame.display.update()
