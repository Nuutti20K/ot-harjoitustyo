import pygame


class GameRenderer:
    def __init__(self, display, level):
        self.display = display
        self.level = level
        self.font = pygame.font.SysFont("Arial", 48)

    def render(self, score):
        self.level.all_sprites.draw(self.display)
        text = self.font.render(f"Score: {score}", True, (255, 0, 0))
        self.display.blit(text, (50, 2))
        pygame.display.update()

    def wipe_screen(self):
        self.display.fill((0, 0, 0))
        pygame.display.update()
