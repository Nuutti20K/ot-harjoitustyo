import pygame
import os

dirname = os.path.dirname(__file__)

class Head(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, heading="right", length=5, speed=1):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "head.png"))
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.heading = heading
        self.length = length
        self.speed = speed