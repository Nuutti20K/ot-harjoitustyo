import pygame
from repositories.score_repository import score_repository


class MenuLoop:
    """Luokka, joka vastaa pelin tapahtumista.

    Attributes
        menu: Valikko, joka halutaan käynnistää.
        clock: Kello, jolla määritetään tarkastusten tahti.
        renderer: Luokka, joka vastaa valikon renderoinnista.
        score_repository: Luokka, joka vastaa ennätysten tallentamisesta.
    """

    def __init__(self, menu, clock, renderer):
        """Luokan konstruktori, joka luo uuden valikon.

        Args:
            menu: Valikko, joka halutaan käynnistää.
            clock: Kello, joka määrittää tarkastusten tahdin.
            renderer: Luokka, joka vastaa valikon renderoinnista
        """
        self.menu = menu
        self.clock = clock
        self.renderer = renderer
        self.score_repository = score_repository

    def start_menu(self):
        """Valikon käynnistys, jossa tarkastuksia toistetaan kunnes peli aloitetaan tai sovellus suljetaan."""

        while True:
            if self.handle_events() is False:
                break
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        """Tarkistaa hiiren näpäimen painalluksia ja pelin sulkemista.

        Jos hiirellä klikataan start-painiketta, valikko käynnistää uuden pelin.

        Returns:
            False, jos valikko suljetaan tai jos peli suljetaan, muuten None.
        """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu.check_start_button() and self.menu.new_game():
                    return False
            if event.type == pygame.QUIT:
                return False
        return None

    def render(self):
        """Renderöi valikon ja top 5 pisteet."""
        scores = self.score_repository.get_top_five()
        self.renderer.render(scores)
