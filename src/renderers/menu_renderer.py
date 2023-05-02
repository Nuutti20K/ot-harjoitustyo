import pygame


class MenuRenderer:
    """Luokka, joka on vastuussa renderöinnistä valikon aikana

    Attributes
        display: Näyttö, jolle kuva renderöidään.
        level: Kenttä, jota halutaan renderöidä.
        font: Fontti, jota käytetään renderöinnissä.
    """
    def __init__(self, display, menu):
        """Luokan konstruktori.

        Args:
            display: Näyttö, jolle kuva renderöidään.
            level: Kenttä, jota halutaan renderöidä.
        """
        self.display = display
        self.menu = menu
        self.font = pygame.font.SysFont("Arial", 48)

    def render(self, scores):
        """Renderöi valikon painikkeet ja viisi parasta ennätystä.

        Args:
            scores: viisi parasta ennätystä tupleina, jossa on ensin pelaajan nimi ja toisena pisteet.
        """
        self.display.fill((0, 0, 0))
        i = 1
        for score in scores:
            text = self.font.render(
                f"{i}: {score[0]} {score[1]} Points", True, (255, 0, 0))
            offset = 50 * i
            self.display.blit(text, (220, 50 + offset))
            i += 1
        self.menu.all_buttons.draw(self.display)
        pygame.display.update()
