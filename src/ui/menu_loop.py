import pygame
from repositories.score_repository import score_repository


class MenuLoop:
    def __init__(self, menu, clock, renderer):
        self.menu = menu
        self.clock = clock
        self.renderer = renderer
        self.score_repository = score_repository

    def start_menu(self):
        while True:
            if self.handle_events() is False:
                break
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                scores = self.score_repository.get_top_five()
                for score in scores:
                    print(score)
                if self.menu.check_start_button() and self.menu.new_game():
                    return False
            if event.type == pygame.QUIT:
                return False
        return None

    def render(self):
        scores = self.score_repository.get_top_five()
        self.renderer.render(scores)
