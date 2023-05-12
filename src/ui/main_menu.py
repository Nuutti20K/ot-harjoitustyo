import pygame
from ui.start_button import StartButton
from game_loop import GameLoop
from level import Level
from renderers.game_renderer import GameRenderer


class MainMenu:
    """Luokka, joka vastaa päävalikon toiminnoista.

    Attributes
        grid: Pelialuetta kuvaava matriisi, jota käytetään pelin alkaessa.
        display: Näyttö, johon peli renderöidään.
        clock: Kello, jolla määritetään tarkastusten tahti.
        start: Aloitus painike.
        all_buttons: Kaikista painikkeista muodostuva ryhmä.
    """

    def __init__(self, grid, display, clock):
        """Luokan konstruktori, jolla luodaan päävalikko.

        Args:
            grid: Pelialuetta kuvaava matriisi, jota käytetään pelin alkaessa.
            display: Näyttö, johon peli renderöidään.
            clock: Kello, jolla määritetään tarkastusten tahti.
        """
        self.grid = grid
        self.display = display
        self.clock = clock
        self.start = None
        self.all_buttons = pygame.sprite.Group()
        self.initialize_buttons()

    def initialize_buttons(self):
        """Alustaa valikossa tarvittavat painikkeet.
        """
        self.start = StartButton(350, 450)
        self.all_buttons.add(self.start)

    def new_game(self):
        """Luo uuden levelin ja aloittaa uuden pelin.

        Returns:
            True, jos peli lopetetaan QUIT tapahtumalla, muuten pelin loppuessa False.
        """
        level = Level(self.grid)
        game_renderer = GameRenderer(self.display, level)
        game_loop = GameLoop(level, self.clock, game_renderer)
        return game_loop.start_game()

    def check_start_button(self):
        """Tarkistaa onko start-painiketta klikattu hiirellä.

        Returns:
            True, jos painiketta on klikattu, muuten False.
        """
        mouse_pos = pygame.mouse.get_pos()
        return pygame.Rect.collidepoint(self.start.rect, mouse_pos)
