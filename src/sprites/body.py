import os
import pygame

dirname = os.path.dirname(__file__)


class Body(pygame.sprite.Sprite):
    def __init__(self, x_coordinate=0, y_coordinate=0, heading="right"):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "body.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.heading = heading
