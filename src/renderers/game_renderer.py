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

    def render_player_input(self, player):
        game_over = self.font.render(f"Game Over!", True, (255, 0, 0))
        name = self.font.render(f"Name: {player}", True, (255, 0, 0))
        pygame.draw.rect(self.display, (20, 20, 20), (200, 150, 600, 450))
        self.display.blit(name, (220, 351))
        self.display.blit(game_over, (370, 255))
        pygame.display.update()
