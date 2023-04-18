import os
import pygame

dirname = os.path.dirname(__file__)


class Body(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, heading="right"): # pylint: disable=invalid-name
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "body.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.heading = heading
