import pygame
import time
import random
import multitasking
import signal

class tennis:

    def __init__(self):
        pygame.init()

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.dis_width = 1200
        self.dis_height = 800

        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Tennis')

        self.clock = pygame.time.Clock()
        self.lastInp = -1
        self.score_p1 = 0
        self.score_p2 = 0

        self.speed = 15

        self.score_style = pygame.font.SysFont("bahnschrift", 25)
        self.end_font = pygame.font.SysFont("comicsansms", 35)

        self.stackKeys = []
        self.len_stack = 0
        self.key = -1

        self.start = True

        self.pos_p1 = 350
        self.pos_p2 = 350

        self.p1_change = 0
        self.p2_change = 0

        signal.signal(signal.SIGINT, multitasking.killall)

        self.gameLoop()



    def press(self, n):
        if self.lastInp != n:
            print("key Pressed " + str(n))
            self.stackKeys.append(int(n))
            self.len_stack += 1
            self.lastInp = n

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
            if self.key == 4:
                self.p1_change = -15
            elif self.key == 5:
                self.p1_change = 15
            elif self.key == 8:
                self.p2_change = -15
            elif self.key == 9:
                self.p2_change = 15

    def Your_score(self):
        return str(self.score_p2) + " - " + str(self.score_p1)

    def message(self):
        mes = self.score_style.render("score p1: "+str(self.score_p1), True, self.white)
        self.dis.blit(mes, [1075, 50])
        mes = self.score_style.render("score p2: "+str(self.score_p2), True, self.white)
        self.dis.blit(mes, [25, 50])

    @multitasking.task
    def gameLoop(self):
        quit_game = False
        self.pos_p1 = 350
        self.pos_p2 = 350
        ball_x = 600
        ball_y = 400
        mov_x = 5
        mov_y = 5

        while True:
            self.dis.fill(self.black)
            self.pos_p1 += self.p1_change
            self.pos_p2 += self.p2_change
            if self.pos_p1 <=0:
                self.pos_p1 = 0
            elif self.pos_p1 >= 700:
                self.pos_p1 = 700

            if self.pos_p2 <=0:
                self.pos_p2 = 0
            elif self.pos_p2 >= 700:
                self.pos_p2 = 700

            self.p1_change = 0
            self.p2_change = 0

            ball_x += mov_x
            ball_y += mov_y

            if (200 < ball_x < 235 and self.pos_p2 < ball_y < self.pos_p2+100):
                mov_x = 5
            if (990 <= ball_x <= 1025 and self.pos_p1 < ball_y < self.pos_p1+100):
                mov_x = -5

            if (ball_y+10 >= 800 or ball_y-10 <= 0):
                mov_y = -mov_y

            if ball_x <= 0:
                self.score_p1 += 1
                mov_x = -mov_x
                mov_y = -mov_y
                ball_x = 600
                ball_y = 400

            if ball_x >= 1200:
                self.score_p2 += 1
                mov_x = -mov_x
                mov_y = -mov_y
                ball_x = 600
                ball_y = 400

            pygame.draw.ellipse(self.dis, self.white, (570, 370, 60, 60))
            pygame.draw.ellipse(self.dis, self.black, (571, 371, 58, 58))
            pygame.draw.circle(self.dis, self.white, (600, 400), 4)
            for i in range(100):
                pygame.draw.line(self.dis, self.white, (600, i*8), (600, (i*8)+4))
            pygame.draw.line(self.dis, self.white, (150, 0), (150, 800))
            pygame.draw.line(self.dis, self.white, (1050, 0), (1050, 800))
            pygame.draw.rect(self.dis, self.white, [975, self.pos_p1, 25, 100])
            pygame.draw.rect(self.dis, self.white, [200, self.pos_p2, 25, 100])
            pygame.draw.circle(self.dis, self.white, (ball_x, ball_y), 10)
            self.message()
            pygame.display.update()
            self.keysControl()

            if self.score_p1 >= 10 or self.score_p2 >= 10:
                winner = "Player 2"
                if self.score_p1 > self.score_p2:
                    winner = "Player 1"

                while not quit_game:
                    self.dis.fill(self.black)
                    mes = self.end_font.render("Fin del juego", True, self.white)
                    self.dis.blit(mes, [400, 150])
                    mes = self.end_font.render("Ganador: "+winner, True, self.white)
                    self.dis.blit(mes, [400, 350])
                    mes = self.end_font.render("Press q -> quit | Press c -> restart", True, self.white)
                    self.dis.blit(mes, [400, 550])
                    if self.keyPress():
                        if self.key == 0:
                            quit_game = True
                        elif self.key == 1:
                            quit_game = True
                            self.gameLoop()

                    pygame.display.update()
                break


        pygame.quit()
        quit()
