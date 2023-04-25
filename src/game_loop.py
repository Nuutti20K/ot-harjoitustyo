import pygame


class GameLoop:
    def __init__(self, level, clock, renderer):
        self.level = level
        self.clock = clock
        self.renderer = renderer

    def start_game(self):
        while True:
            if self.handle_events() is False:
                return True # return True if game is ended with QUIT event
            self.level.movement_coordinator()
            if self.level.collision_check(self.level.head):
                self.level.game_over()
                return False # return False if game is ended with game over
            if self.level.pellet_check():
                self.level.move_pellet()
                self.level.pellet.score_up()
                self.level.snake_growth()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
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
        self.renderer.render(self.level.pellet.get_score())
