import os
import pygame

dirname = os.path.dirname(__file__)


class Pellet(pygame.sprite.Sprite):
    def __init__(self, x_coordinate=0, y_coordinate=0, score=0):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "pellet.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.score = score

    def score_up(self):
        self.score += 1

    def get_score(self):
        return self.score
