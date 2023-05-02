from random import randint
import pygame
from sprites.head import Head
from sprites.body import Body
from sprites.pellet import Pellet
from sprites.wall import Wall
from sprites.floor import Floor


class Level:
    """Luokka, joka vastaa spritejen sijainneista ja liikuttamisesta.

    Attributes:
        head: Levelissä oleva pää.
        bodies: Levelissä olevat ruumiinosat.
        walls: Levelissä olevat seinät.
        pellet: Levelissä oleva pelletti.
        floors: Levelissä olevat lattiat.
        obstacles: Ryhmä spritejä, joihin käärme ei saa törmätä.
        all_sprites: Ryhmä, joka koostu levelin kaikista spriteistä
        grid: Kaksiulotteinen matriisi, joka kuvaa pelialuetta.
    """
    def __init__(self, grid):
        """Luokan konstruktori, joka luo ryhmät kaikille lisättäville spriteille.
        
        Args:
            grid: Kaksiulotteinen matriisi, joka kuvaa pelialuetta.
        """
        self.head = None
        self.bodies = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.pellet = None
        self.floors = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.grid = grid
        self.initialize_sprites(grid)

    def initialize_sprites(self, grid):
        """Alustaa kaikki levelissä tarvittavat spritet pelialueen mukaisesti.

        Args:
            grid: Kaksiulotteinen matriisi, joka kuvaa pelialuetta.
        """
        height = len(grid)
        width = len(grid[0])

        for y_coordinate in range(height):
            for x_coordinate in range(width):

                cell = grid[y_coordinate][x_coordinate]

                if cell == 0:
                    self.floors.add(Floor(x_coordinate*50, y_coordinate*50))
                if cell == 1:
                    self.walls.add(Wall(x_coordinate*50, y_coordinate*50))
                if cell == 2:
                    self.bodies.add(Body(x_coordinate*50, y_coordinate*50))
                    self.floors.add(Floor(x_coordinate*50, y_coordinate*50))
                if cell == 3:
                    self.head = Head(x_coordinate*50, y_coordinate*50)
                    self.floors.add(Floor(x_coordinate*50, y_coordinate*50))
                if cell == 4:
                    self.pellet = Pellet(x_coordinate*50, y_coordinate*50)
                    self.floors.add(Floor(x_coordinate*50, y_coordinate*50))

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
        """Koordinoi käärmeen pään ja ruumiin liikkeitä ja kasvamista.

        Jos käärmeen liikkuminen tapahtuu, pään suunta lukittuu ja aika seuraavaan liikkumiseen nollaantuu.
        Muuten aika seuraavaan liikkumiseen vähenee.

        Jos käärme kasvaa liikkumisella, käärmelle lisätään osa ja sen kasvutilaksi laitetaa False.
        Muuten käärmeen osat liikkuvat pään mukana. 
        """
        if self.head.next_move <= 0:
            self.head.next_move = self.head.speed
            self.head.heading = self.head.queued_heading
            if self.head.growth:
                self.add_body()
                self.head.growth = False
            else:
                self.body_movement()
            self.head_movement()
        else:
            self.head.next_move -= 1

    def head_movement(self):
        """Liikuttaa käärmeen päätä sen heading muuttujan kertomaan suuntaan.
        """
        if self.head.heading == "right":
            self.head.rect.move_ip(50, 0)
        if self.head.heading == "down":
            self.head.rect.move_ip(0, 50)
        if self.head.heading == "left":
            self.head.rect.move_ip(-50, 0)
        if self.head.heading == "up":
            self.head.rect.move_ip(0, -50)

    def body_movement(self):
        """Käy läpi käärmeen jokaisen ruumiinosan ja liikuttaa niitä oikeisiin suuntiin.

        Lisäksi jokainen osa saa edellä olevalta osalta seuraavan suunnan.
        """
        headings = []
        for part in iter(self.bodies.sprites()):
            if part.heading == "right":
                part.rect.move_ip(50, 0)
            if part.heading == "down":
                part.rect.move_ip(0, 50)
            if part.heading == "left":
                part.rect.move_ip(-50, 0)
            if part.heading == "up":
                part.rect.move_ip(0, -50)
            headings.append(part.heading)
        for i in range(len(headings)-1):
            headings[i] = headings[i+1]
        headings[-1] = self.head.heading
        i = 0
        for part in iter(self.bodies.sprites()):
            part.heading = headings[i]
            i += 1

    def add_body(self):
        """Lisää käärmeeseen ruumiinosan, joka saa päältä sijainnin ja suunnan.
        """
        x_coordinate = self.head.rect.x
        y_coordinate = self.head.rect.y
        heading = self.head.heading
        self.bodies.add(Body(x_coordinate, y_coordinate, heading))
        self.all_sprites.add(self.bodies)
        self.obstacles.add(self.bodies)

    def snake_growth(self):
        """Muuttaa pään growth muuttujaksi True
        """
        self.head.growth = True

    def turn_head(self, direction):
        """Kääntää päätä haluttuun suuntaan.

        Estää päätä kääntymästä päinvastaiseen suuntaan.
        Args:
            direction: Suunta johon halutaan kääntyä.
        """
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
        """Tarkistaa törmääkö tarkasteltava sprite johonkin esteeksi määriteltyyn spriteen.

        Args:
            sprite: Sprite, jonka törmäystä halutaan tarkastella

        Returns:
            True, jos törmäys on tapahtunut, muuten False.
        """
        collisions = pygame.sprite.spritecollide(
            sprite, self.obstacles, False)
        return bool(collisions)

    def pellet_check(self):
        """Tarkistaa käärmeen pään törmäämisen pellettiin.

        Returns:
            True, jos törmäys on tapahtunut, muuten False.
        """
        pellet = pygame.sprite.Group(self.pellet)
        collisions = pygame.sprite.spritecollide(
            self.head, pellet, False)
        return bool(collisions)

    def move_pellet(self):
        """Siirtää pelletin satunnaiseen sijaintiin.

        Siirtoa yritetään niin pitkään kunnes se ei osu mihinkään esteeseen.
        """
        height = len(self.grid)-1
        width = len(self.grid[0])-1
        while self.collision_check(self.pellet) or self.pellet_check():
            x_coordinate = randint(0, width)
            y_coordinate = randint(0, height)
            self.pellet.rect.x = x_coordinate*50
            self.pellet.rect.y = y_coordinate*50
