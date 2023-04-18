import os
import pygame

dirname = os.path.dirname(__file__)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x_coordinate=0, y_coordinate=0):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "wall.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
