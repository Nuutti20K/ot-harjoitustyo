import pygame


class GameRenderer:
    """Luokka, joka on vastuussa renderöinnistä pelin aikana

    Attributes
        display: Näyttö, jolle kuva renderöidään.
        level: Kenttä, jota halutaan renderöidä.
        font: Fontti, jota käytetään renderöinnissä.
    """

    def __init__(self, display, level):
        """Luokan konstruktori.

        Args:
            display: Näyttö, jolle kuva renderöidään.
            level: Kenttä, jota halutaan renderöidä.
        """
        self.display = display
        self.level = level
        self.font = pygame.font.SysFont("Arial", 48)

    def render(self, score):
        """Renderöi pelin kaikki spritet ja pelaajan pisteet.

        Args:
            score: Pelaajan pisteet.
        """
        self.level.all_sprites.draw(self.display)
        text = self.font.render(f"Score: {score}", True, (255, 0, 0))
        self.display.blit(text, (50, 2))
        pygame.display.update()

    def render_player_input(self, player):
        """Renderöi 'game over' näkymän ja kentän, johon kirjoitetaan pelaajan nimi.

        Args:
            player: pelaajan nimi.
        """
        game_over = self.font.render("Game Over!", True, (255, 0, 0))
        name = self.font.render(f"Name: {player}", True, (255, 0, 0))
        pygame.draw.rect(self.display, (20, 20, 20), (200, 200, 600, 350))
        self.display.blit(name, (220, 351))
        self.display.blit(game_over, (370, 255))
        pygame.display.update()
