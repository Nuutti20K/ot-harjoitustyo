import pygame


class MenuLoop:
    def __init__(self, menu, clock, renderer):
        self.menu = menu
        self.clock = clock
        self.renderer = renderer

    def start_menu(self):
        while True:
            if self.handle_events() is False:
                break
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu.check_start_button() and self.menu.new_game():
                    return False
            if event.type == pygame.QUIT:
                return False
        return None

    def render(self):
        self.renderer.render()
