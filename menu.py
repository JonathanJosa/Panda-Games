import pygame
import time
import random
import multitasking
import signal

class menu:

    def __init__(self):
        pygame.init()

        self.games = ["Snake", "Tennis", "Telegram", "Nothing....Yet"]

        self.activeGame = True

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.dis_width = 1200
        self.dis_height = 800

        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Juegos')

        self.clock = pygame.time.Clock()

        self.score_style = pygame.font.SysFont("bahnschrift", 25)
        self.end_font = pygame.font.SysFont("comicsansms", 35)

        self.stackKeys = []
        self.len_stack = 0
        self.key = -1
        self.lastInp = -1

        self.selected = 0
        self.ended = True

        signal.signal(signal.SIGINT, multitasking.killall)

        self.gameLoop()

    def press(self, n):
        if self.lastInp != n:
            print("key Pressed " + str(n))
            self.stackKeys.append(int(n))
            self.len_stack += 1
            self.lastInp = n
        return self.activeGame

    def keyPress(self):
        if(self.len_stack == 0):
            self.key = -1
            return False
        self.key = self.stackKeys.pop(0)
        self.len_stack -= 1
        self.lastInp = -1
        return True

    def keysControl(self):
        if self.len_stack != 0:
            self.keyPress()
            if self.key == 3:
                self.selected += 1
                self.selected = self.selected % 4
            elif self.key == 2:
                self.selected -= 1
                if self.selected < 0:
                    self.selected = 3
            elif self.key == 1:
                self.ended = False

    def select(self):
        return self.selected

    @multitasking.task
    def gameLoop(self):
        self.selected = 0

        img = [pygame.image.load('data/snake.jpg'), pygame.image.load('data/pingpong.png'), pygame.image.load('data/telegram.jpg'), pygame.image.load('data/hands.jpg')]

        while self.ended:
            self.dis.fill(self.black)
            mes = self.score_style.render("Seleccionado: "+str(self.games[self.selected]), True, self.white)
            self.dis.blit(mes, [500, 50])
            ([
                lambda _ : pygame.draw.rect(self.dis, self.white, [150, 150, 200, 500]),
                lambda _ : pygame.draw.rect(self.dis, self.white, [400, 150, 200, 500]),
                lambda _ : pygame.draw.rect(self.dis, self.white, [650, 150, 200, 500]),
                lambda _ : pygame.draw.rect(self.dis, self.white, [900, 150, 200, 500])
            ][self.selected])(True)

            self.dis.blit(img[0], (160, 160), (60, 0, 180, 480))
            self.dis.blit(img[1], (410, 160), (200, 70, 180, 480))
            self.dis.blit(img[2], (660, 160), (216, 66, 180, 480))
            self.dis.blit(img[3], (910, 160), (190, 0, 180, 480))

            pygame.display.update()
            self.keysControl()

        self.activeGame = False
