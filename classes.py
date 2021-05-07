import pygame
import math

playerImg = pygame.image.load('images/player.png')
bulletImg = pygame.image.load('images/bullet.png')
enemyImg = pygame.image.load('images/enemy.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImg
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 370, 480

    def rotate(self, mx, my):
        angle = math.degrees(math.atan2((mx-self.rect.x),(my-self.rect.y)))
        self.image = pygame.transform.rotate(playerImg, angle-180)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, px, py, mx, my):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletImg
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = px, py
        self.angle = math.atan2((mx-self.rect.x),(my-self.rect.y))
        self.image = pygame.transform.rotate(self.image, math.degrees(self.angle - math.pi))
        self.draw = True
        #print(self.angle)


    def update(self):
        speed = 15
        self.rect.x = self.rect.x + (speed*math.sin(self.angle))
        self.rect.y = self.rect.y + (speed*math.cos(self.angle))

        













