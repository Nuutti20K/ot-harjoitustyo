import pygame


class MenuRenderer:
    def __init__(self, display, menu):
        self.display = display
        self.menu = menu
        self.font = pygame.font.SysFont("Arial", 48)

    def render(self):
        self.display.fill((0, 0, 0))
        self.menu.all_buttons.draw(self.display)
        pygame.display.update()
