import os
import pygame

dirname = os.path.dirname(__file__)


class Head(pygame.sprite.Sprite):
    def __init__(self, x_coordinate=0, y_coordinate=0, speed=10, heading="right"):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "head.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.heading = heading
        self.queued_heading = heading
        self.speed = speed
        self.next_move = speed
        self.growth = False
