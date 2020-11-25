import pygame


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP]:
            self.y -= self.vel
        if keys_pressed[pygame.K_DOWN]:
            self.y += self.vel
        if keys_pressed[pygame.K_LEFT]:
            self.x -= self.vel
        if keys_pressed[pygame.K_RIGHT]:
            self.x += self.vel

        self.update_char_rect()

    def update_char_rect(self):
        self.rect = (self.x, self.y, self.width, self.height)

