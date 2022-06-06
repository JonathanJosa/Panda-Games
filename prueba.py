import sys, pygame
from pygame.constants import *

class prueba:
    def __init__(self):
        pygame.init()

        self.dis = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Magic control')

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

    def loop(self):
        pos_x = 0
        mov = 1
        while True:
            self.dis.fill(self.black)

            for e in pygame.event.get():
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    sys.exit()

            pos_x += mov
            if pos_x >= 600 or pos_x <= 0:
                mov = -mov
            pygame.draw.rect(self.dis, self.white, [100+pos_x, 200, 400, 400])

            pygame.display.update()



if __name__ == "__main__":
    init = prueba()
    init.loop()
