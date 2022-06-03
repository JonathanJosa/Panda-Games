import pygame
import time
import random
import multitasking
import signal

class snake:

    def __init__(self):
        pygame.init()

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.dis_width = 1200
        self.dis_height = 800

        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Snake Blocks')

        self.clock = pygame.time.Clock()
        self.lastInp = -1
        self.snake_speed = 10
        self.score = 0

        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.end_font = pygame.font.SysFont("comicsansms", 35)

        self.stackKeys = []
        self.len_stack = 0
        self.key = 0


        self.x1_change = 0
        self.y1_change = 0

        signal.signal(signal.SIGINT, multitasking.killall)

        self.gameLoop()

    def press(self, n):
        if(n != self.lastInp):
            print("key Pressed")
            self.stackKeys.append(int(n))
            self.len_stack += 1
            self.lastInp = n

    def keyPress(self):
        if(self.len_stack == 0):
            return False
        self.key = self.stackKeys.pop(0)
        self.len_stack -= 1
        return True

    def keysControl(self):
        if self.len_stack != 0:
            self.keyPress()
            if self.key == 2:
                self.x1_change = -20
                self.y1_change = 0
            elif self.key == 3:
                self.x1_change = 20
                self.y1_change = 0
            elif self.key == 4:
                self.y1_change = -20
                self.x1_change = 0
            elif self.key == 5:
                self.y1_change = 20
                self.x1_change = 0

    def Your_score(self):
        return self.score

    def our_snake(self, snake_list):
        x = snake_list[0]
        pygame.draw.rect(self.dis, self.white, [x[0], x[1], 20, 20])
        for x in snake_list[1:]:
            pygame.draw.rect(self.dis, self.white, [x[0]+1, x[1]+1, 18, 18])

    @multitasking.task
    def gameLoop(self):
        game_close = False

        x1 = self.dis_width / 2
        y1 = self.dis_height / 2

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, self.dis_width - 20) / 20.0) * 20.0
        foody = round(random.randrange(0, self.dis_height - 20) / 20.0) * 20.0

        while True:

            if x1 >= self.dis_width or x1 < 0 or y1 >= self.dis_height or y1 < 0:
                game_close = True
            x1 += self.x1_change
            y1 += self.y1_change

            self.dis.fill(self.black)
            pygame.draw.ellipse(self.dis, self.white, [foodx+2, foody+2, 16, 16])
            mes = self.font_style.render("Puntos: "+str(self.score), True, self.white)
            self.dis.blit(mes, [50, 25])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            self.our_snake(snake_List)
            self.score = Length_of_snake - 1

            pygame.display.update()
            self.keysControl()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, self.dis_width - 20) / 20.0) * 20.0
                foody = round(random.randrange(0, self.dis_height - 20) / 20.0) * 20.0
                Length_of_snake += 1

            self.clock.tick(self.snake_speed)

            if game_close:
                self.dis.fill(self.black)
                mes = self.end_font.render("Fin del juego", True, self.white)
                self.dis.blit(mes, [400, 150])
                mes = self.end_font.render("Puntos: "+str(self.score), True, self.white)
                self.dis.blit(mes, [400, 350])
                pygame.display.update()

                time.sleep(3)
                break


        pygame.quit()
        quit()
