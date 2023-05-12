import os
import pygame

dirname = os.path.dirname(__file__)


class Pellet(pygame.sprite.Sprite):
    """Sprite luokka, jota pelissä pitää kerätä.

    Attributes:
        image: Kuva jota sprite käytää.
        rect: Spriten kuvasta luotu suorakulmio.
        rect.x: Suorakulmion x koordinaatti.
        rect.y: Suorakulmion y koordinaatti.
        score: Muuttuja laskee kuinka monta kertaa pellettiä on poimittu
    """

    def __init__(self, x_coordinate=0, y_coordinate=0, score=0):
        """Luokan konstruktori, joka luo uuden ruumiinosan.

        Args:
            x_coordinate: Pelletin x koordinaatti.
            y_coordinate: Pelletin y koordinaatti.
            score: Kerätyt pisteet.
        """
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "pellet.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.score = score

    def score_up(self):
        """Kasvattaa pisteiden määrää yhdellä.

        """
        self.score += 1

    def get_score(self):
        """Palauttaa pisteiden määrän.

        Returns:
            Kokonaisluku, joka kertoo kerättyjen pisteiden määrän.
        """
        return self.score
