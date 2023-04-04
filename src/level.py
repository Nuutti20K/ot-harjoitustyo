import pygame
from random import randint
from sprites.head import Head
from sprites.body import Body
from sprites.pellet import Pellet
from sprites.wall import Wall
from sprites.floor import Floor

class Level:
    def __init__(self, map):
        self.head = None
        self.bodies = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.pellet = None
        self.floors = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.map = map

        self.initialize_sprites(map)

    def initialize_sprites(self, map):
        height = len(map)
        width = len(map[0])

        for y in range(height):
            for x in range(width):

                cell = map[y][x]

                if cell == 0:
                    self.floors.add(Floor(x*50, y*50))
                if cell == 1:
                    self.walls.add(Wall(x*50, y*50))
                if cell == 2:
                    self.bodies.add(Body(x*50, y*50))
                    self.floors.add(Floor(x*50, y*50))
                if cell == 3:
                    self.head = Head(x*50, y*50)
                    self.floors.add(Floor(x*50, y*50))
                if cell == 4:
                    self.pellet = Pellet(x*50, y*50)
                    self.floors.add(Floor(x*50, y*50))

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.bodies,
            self.head,
            self.pellet
        )
    
    def head_movement(self):
        if self.head.heading == "right":
            self.head.rect.move_ip(50, 0)
        if self.head.heading == "down":
            self.head.rect.move_ip(0, 50)
        if self.head.heading == "left":
            self.head.rect.move_ip(-50, 0)
        if self.head.heading == "up":
            self.head.rect.move_ip(0, -50)

    def collision_check(self):
        collisions = pygame.sprite.spritecollide(self.head, self.walls, False)
        if collisions:
            return True
        else:
            return False

    def body_movement(self):
        for part in iter(self.bodies.sprites()):
            self.bodies.remove(part)
            self.all_sprites.remove(part)
            break
        self.bodies.add(Body(self.head.rect.x, self.head.rect.y))
        self.all_sprites.add(self.bodies)

#    def randomize_pellet(self):
#        height = len(self.map)
#        width = len(self.map[0])
#        self.pellet = Pellet(randint(0, width), randint(0, height))
#        forbidden_placements = pygame.sprite.Group()
#        forbidden_placements.add(self.walls, self.head, self.bodies)
#        collisions = pygame.sprite.spritecollide(self.pellet, forbidden_placements, False)