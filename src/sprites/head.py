import os
import pygame

dirname = os.path.dirname(__file__)


class Head(pygame.sprite.Sprite):
    """Sprite luokka, joka toimii käärmeen päänä.

    Attributes:
        image: Kuva jota sprite käytää.
        rect: Spriten kuvasta luotu suorakulmio.
        rect.x: Suorakulmion x koordinaatti.
        rect.y: Suorakulmion y koordinaatti.
        heading: Pään suunta, joka kertoo mihin suuntaa pää liikkui viimeisimpänä.
        queued_heading: Pään suunta, johon se liikkuu seuraavaksi.
        speed: Käärmeen nopeus, eli kuinka monen framen välein pää liikkuu.
        next_move: Jäljellä olevat framet pään seuraavaan liikkumiseen.
        growth: Muuttuja kertoo kasvaako käärme seuraavalla liikkumisella
    """

    def __init__(self, x_coordinate=0, y_coordinate=0, speed=10, heading="right"):
        """Luokan konstruktori, joka luo käärmeen pään.

        Args:
            x_coordinate: Pään x koordinaatti.
            y_coordinate: Pään y koordinaatti.
            speed: käärmeen nopeus.
            heading: Pään suunta alussa.
        """
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
