import pygame

RED = (0, 0, 0)
BLUE = (0, 0, 0)


class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height, c_):

        super().__init__()

        self.image = pygame.Surface([width, height])
        if c_ == 1:
            self.image.fill(RED)
            self.image.set_colorkey(RED)
            c_ = RED
        else:
            self.image.fill(BLUE)
            self.image.set_colorkey(BLUE)
            c_ = BLUE

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels

        if self.rect.y > 400:
            self.rect.y = 400

    def moveLeft(self, pixels):
        self.rect.x -= pixels

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > 780:
            self.rect.x = 780

        if 420 < self.rect.x < 430:
            self.rect.x = 435

    def moveRight(self, pixels):
        self.rect.x += pixels

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > 780:
            self.rect.x = 780

        if 370 < self.rect.x < 380:
            self.rect.x = 365
