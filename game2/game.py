import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QFontDatabase
import pygame, time
from block import Block
import pygame
from random import randint
import time
import datetime

a = 1


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.one = False
        self.two = False

    def initUI(self):
        self.setGeometry(282, 144, 800, 480)
        self.setWindowTitle('Старт')

        self.label2 = QLabel(self)

        self.label2.setText("для начала игры оба игрока должны подтвердить готовность")
        self.label2.move(235, 10)

        self.btn1 = QPushButton('первый игрок', self)
        self.btn1.resize(400, 450)
        self.btn1.move(0, 50)
        self.btn1.clicked.connect(self.hello1)
        self.btn1.setStyleSheet('background: rgb(200,255,200);')

        self.btn2 = QPushButton('второй игрок', self)
        self.btn2.resize(400, 450)
        self.btn2.move(400, 50)
        self.btn2.clicked.connect(self.hello2)
        self.btn2.setStyleSheet('background: rgb(200,255,200);')

        pygame.init()

    def hello1(self):
        self.one = True
        self.btn1.setStyleSheet('background: rgb(50,255,50);')

        pygame.mixer.music.load('push.mp3')
        pygame.mixer.music.play()
        if self.one == self.two == True:
            self.game()
            sys.exit(app.exec())

    def hello2(self):
        self.two = True
        self.btn2.setStyleSheet('background: rgb(50,255,50);')

        pygame.mixer.music.load('push.mp3')
        pygame.mixer.music.play()
        if self.one == self.two == True:
            self.game()
            sys.exit(app.exec())

    def game(self):

        pygame.init()

        STOP = False

        # -цвета-

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        RED = (255, 5, 5)
        BLUE = (5, 5, 255)

        # --

        size = (800, 480)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Пинг-понг")

        # -рокетки-

        Block1 = Block(RED, 10, 100, 1)
        Block2 = Block(BLUE, 10, 100, 2)
        Block1.rect.x = 20
        Block2.rect.x = 770
        Block1.rect.y = 200
        Block2.rect.y = 200

        # -шарик-

        ball = Ball(WHITE, 10, 10)
        ball.rect.x = 345
        ball.rect.y = 195

        # -спрайты-

        all_sprites_list = pygame.sprite.Group()

        all_sprites_list.add(Block1)
        all_sprites_list.add(Block2)
        all_sprites_list.add(ball)

        clock = pygame.time.Clock()

        СO = True

        while СO:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    СO = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        СO = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                Block1.moveUp(7)
            if keys[pygame.K_s]:
                Block1.moveDown(7)

            if keys[pygame.K_UP]:
                Block2.moveUp(7)
            if keys[pygame.K_DOWN]:
                Block2.moveDown(7)

            if keys[pygame.K_d]:
                Block1.moveRight(7)
            if keys[pygame.K_a]:
                Block1.moveLeft(7)
            if keys[pygame.K_RIGHT]:
                Block2.moveRight(7)
            if keys[pygame.K_LEFT]:
                Block2.moveLeft(7)

            if keys[pygame.K_q]:
                time.sleep(2)
                a = True
                while a:
                    if keys[pygame.K_q]:
                        a = not a
                    print('qwerty')

            if ball.check(Block2, Block2.y(), keys) != None:
                СO = False

            all_sprites_list.update()

            if ball.rect.x >= 795:
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x <= 0:
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y > 480:
                ball.velocity[1] = -ball.velocity[1]
            if ball.rect.y < 0:
                ball.velocity[1] = -ball.velocity[1]

            if pygame.sprite.collide_mask(ball, Block1) or pygame.sprite.collide_mask(ball, Block2):
                ball.bounce()

            bg = pygame.image.load("bg.png")

            screen.blit(bg, (0, 0))

            all_sprites_list.draw(screen)

            pygame.display.flip()

            clock.tick(60)

        sys.exit(app.exec())
        pygame.quit()


BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.image.load('pixil-frame-0.png')
        self.image = pygame.Surface([width, height])
        self.start = time.time()

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

        self.bot = False

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.image = pygame.image.load('pixil-frame-0.png')

    def rect_(self):
        return self.rect.x

    def check(self, Block2, y, keys):
        if self.rect.y <= 5 or self.rect.y >= 475:
            pygame.mixer.music.load('boarder.mp3')
            pygame.mixer.music.play()

        if keys[pygame.K_f]:
            self.bot = not self.bot

        if self.bot:
            if self.rect.y < y:
                Block2.moveUp(7)
            elif self.rect.y > y:
                Block2.moveDown(7)

        if self.rect.x <= 5:
            pygame.mixer.music.load('end.mp3')
            pygame.mixer.music.play()
            pygame.time.delay(2000)
            open('out.txt', 'a').write('blue - ' + str(datetime.datetime.now()))
            open('out.txt', 'a').write('\n')
            return 'blue'

        elif self.rect.x >= 795:
            pygame.mixer.music.load('end.mp3')
            pygame.mixer.music.play()
            pygame.time.delay(2000)
            open('out.txt', 'a').write('red - ' + str(datetime.datetime.now()))
            open('out.txt', 'a').write('\n')
            return 'red'
        else:
            return None

    def bounce(self):
        if time.time() - self.start >= 0.5:
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = randint(-8, 8)
            pygame.mixer.music.load('block_strike.mp3')
            pygame.mixer.music.play()
            self.start = time.time()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
