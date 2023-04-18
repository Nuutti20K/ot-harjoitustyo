import pygame


class GameLoop:
    def __init__(self, level, clock, renderer):
        self.level = level
        self.clock = clock
        self.renderer = renderer

    def start(self):
        while True:
            if self.handle_events() is False:
                break
            self.level.movement_coordinator()
            self.level.collision_check(self.level.head)
            if self.level.pellet_check():
                self.level.move_pellet()
                self.level.head.growth = True
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
        self.renderer.render()
