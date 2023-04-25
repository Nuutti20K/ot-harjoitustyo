import pygame
from sprites.start_button import StartButton
from game_loop import GameLoop
from level import Level
from game_renderer import GameRenderer


class MainMenu:
    def __init__(self, grid, display, clock):
        self.grid = grid
        self.display = display
        self.clock = clock
        self.start = None
        self.all_buttons = pygame.sprite.Group()
        self.initialize_buttons()

    def initialize_buttons(self):
        self.start = StartButton(350, 275)
        self.all_buttons.add(self.start)

    def new_game(self):
        level = Level(self.grid)
        game_renderer = GameRenderer(self.display, level)
        game_loop = GameLoop(level, self.clock, game_renderer)
        return game_loop.start_game()

    def check_start_button(self):
        mouse_pos = pygame.mouse.get_pos()
        return pygame.Rect.collidepoint(self.start.rect, mouse_pos)
