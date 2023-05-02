import pygame


class TextHandler:
    def __init__(self, renderer, clock):
        self.renderer = renderer
        self.clock = clock
        self.text = ""

    def input_text(self):
        while True:
            if self.handle_events():
                return self.text
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and len(self.text) > 0:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    return True
                elif len(self.text) <= 10 and event.key != pygame.K_BACKSPACE:
                    self.text += event.unicode
            if event.type == pygame.QUIT:
                pygame.quit()
        return None

    def render(self):
        self.renderer.render_player_input(self.text)
