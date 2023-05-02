import os
import pygame

dirname = os.path.dirname(__file__)


class Floor(pygame.sprite.Sprite):
    """Sprite luokka, joka toimii pelialueen tyhjänä tilana.

    Attributes:
        image: Kuva jota sprite käytää.
        rect: Spriten kuvasta luotu suorakulmio.
        rect.x: Suorakulmion x koordinaatti.
        rect.y: Suorakulmion y koordinaatti.
    """
    def __init__(self, x_coordinate=0, y_coordinate=0):
        """Luokan konstruktori, joka luo uuden lattiapalan.

        Args:
            x_coordinate: Palan x koordinaatti.
            y_coordinate: Palan y koordinaatti.
        """
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "floor.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
