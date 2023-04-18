from random import randint
import pygame
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
        self.pellets = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.map = map

        self.initialize_sprites(map)

    def initialize_sprites(self, map):
        height = len(map)
        width = len(map[0])

        for y in range(height): # pylint: disable=invalid-name
            for x in range(width): # pylint: disable=invalid-name

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

        self.pellets.add(self.pellet)

        self.obstacles.add(
            self.walls,
            self.bodies
        )

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.bodies,
            self.pellet,
            self.head
        )

    def movement_coordinator(self):
        if self.head.next_move <= 0:
            self.head.next_move = self.head.speed
            self.head.heading = self.head.queued_heading
            if self.head.growth:
                self.add_body()
                self.head.growth = False
            else:
                self.body_movement()
            self.part_movement(self.head)
        else:
            self.head.next_move -= 1

    def part_movement(self, part):
        if part.heading == "right":
            part.rect.move_ip(50, 0)
        if part.heading == "down":
            part.rect.move_ip(0, 50)
        if part.heading == "left":
            part.rect.move_ip(-50, 0)
        if part.heading == "up":
            part.rect.move_ip(0, -50)
    
    def body_movement(self):
        headings = []
        for part in iter(self.bodies.sprites()):
            self.part_movement(part)
            headings.append(part.heading)
        for i in range(len(headings)-1):
            headings[i] = headings[i+1]
        headings[-1] = self.head.heading
        i = 0
        for part in iter(self.bodies.sprites()):
            part.heading = headings[i]
            i += 1

    def add_body(self):
        x = self.head.rect.x
        y = self.head.rect.y
        heading = self.head.heading
        self.bodies.add(Body(x, y, heading))
        self.all_sprites.add(self.bodies)
        self.obstacles.add(self.bodies)

    def snake_growth(self):
        self.head.growth = True

    def turn_head(self, direction):
        if direction == "right":
            if self.head.heading in ("up", "down"):
                self.head.queued_heading = "right"
        elif direction == "left":
            if self.head.heading in ("up", "down"):
                self.head.queued_heading = "left"
        elif direction == "up":
            if self.head.heading in ("left", "right"):
                self.head.queued_heading = "up"
        elif direction == "down":
            if self.head.heading in ("left", "right"):
                self.head.queued_heading = "down"

    def collision_check(self, sprite):
        collisions = pygame.sprite.spritecollide(
            sprite, self.obstacles, False)
        return bool(collisions)
    
    def pellet_check(self):
        collisions = pygame.sprite.spritecollide(
            self.head, self.pellets, False)
        return bool(collisions)

    def move_pellet(self):
        height = len(self.map)-1
        width = len(self.map[0])-1
        while self.collision_check(self.pellet) or self.pellet_check():
            x = randint(0, width)
            y = randint(0, height)
            self.pellet.rect.x = x*50
            self.pellet.rect.y = y*50
        