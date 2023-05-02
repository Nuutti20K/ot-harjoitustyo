import os
import pygame

dirname = os.path.dirname(__file__)


class Body(pygame.sprite.Sprite):
    """Sprite luokka, joka toimii käärmeen ruumiina.

    Attributes:
        image: Kuva jota sprite käytää.
        rect: Spriten kuvasta luotu suorakulmio.
        rect.x: Suorakulmion x koordinaatti.
        rect.y: Suorakulmion y koordinaatti.
        heading: Yksittäisen ruuminosan suunta, johon osa liikkuu seuraavaksi.
    """

    def __init__(self, x_coordinate=0, y_coordinate=0, heading="right"):
        """Luokan konstruktori, joka luo uuden ruumiinosan.

        Args:
            x_coordinate: Ruuminosan x koordinaatti.
            y_coordinate: Ruuminosan y koordinaatti.
            heading: Ruumiinosan suunta alussa.
        """
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "body.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.heading = heading
