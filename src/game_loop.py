import pygame
from ui.text_handler import TextHandler
from repositories.score_repository import score_repository


class GameLoop:
    """Luokka, joka vastaa pelin tapahtumista.

    Attributes
        level: Kenttä, jossa spritet liikkuvat.
        clock: Kello, jolla määritetään tarkastusten tahti.
        rendrer: Luokka, joka vastaa pelin renderoinnista.
        text_handler: Luokka, joka käsittelee tekstin kirjoittamisesta.
        score_repository: Luokka, joka vastaa ennätysten tallentamisesta.
    """
    def __init__(self, level, clock, renderer):
        """Luokan konstruktori, joka luo uuden pelin.

        Args:
            level: Kenttä, jossa spritet liikkuvat.
            clock: Kello, joka määrittää tarkastusten tahdin.
            renderer: Luokka, joka vastaa pelin renderoinnista
        """
        self.level = level
        self.clock = clock
        self.renderer = renderer
        self.text_handler = TextHandler(renderer, clock)
        self.score_repository = score_repository

    def start_game(self):
        """Pelin käynnistys, jossa tarkastuksia toistetaan kunnes peli on loppunut.

        Jos pää törmää esteeseen, peli loppuu ja pelaajalta kysytään nimeä pisteiden tallennukseen.

        Jos pelletti kerätään, sitä siirretään, pisteet kasvaa ja käärme kasvaa.

        Returns:
            True, jos peli lopetetaan QUIT tapahtumalla, muuten pelin loppuessa False.
        """
        while True:
            if self.handle_events() is False:
                return True
            self.level.movement_coordinator()
            if self.level.collision_check(self.level.head):
                name = self.text_handler.input_text()
                score = self.level.pellet.get_score()
                self.score_repository.add_score(name, score)
                return False
            if self.level.pellet_check():
                self.level.move_pellet()
                self.level.pellet.score_up()
                self.level.snake_growth()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        """Tarkistaa nuolinäppäimien painalluksia ja pelin sulkemista.

        Jos nuolinäppäintä painaa, käärmettä pyritään kääntämään siihen suuntaan, jos se on sallittua.
        Returns:
            False, jos peli suljetaan, muuten ei mitään.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.level.turn_head("left")
                elif event.key == pygame.K_RIGHT:
                    self.level.turn_head("right")
                elif event.key == pygame.K_UP:
                    self.level.turn_head("up")
                elif event.key == pygame.K_DOWN:
                    self.level.turn_head("down")
            if event.type == pygame.QUIT:
                return False
        return None

    def render(self):
        """Renderöi levelin ja näyttää pisteet
        """
        self.renderer.render(self.level.pellet.get_score())
