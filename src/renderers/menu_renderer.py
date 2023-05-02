import pygame


class MenuRenderer:
    def __init__(self, display, menu):
        self.display = display
        self.menu = menu
        self.font = pygame.font.SysFont("Arial", 48)

    def render(self, scores):
        self.display.fill((0, 0, 0))
        i = 1
        for score in scores:
            text = self.font.render(f"{i}: {score[0]} {score[1]} Points", True, (255, 0, 0))
            offset = 50 * i
            self.display.blit(text, (220, 50 + offset))
            i += 1
        self.menu.all_buttons.draw(self.display)
        pygame.display.update()
