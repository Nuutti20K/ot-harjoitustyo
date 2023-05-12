import pygame


class TextHandler:
    """Luokka, joka vastaa tekstisyötteistä.

    Attributes
        renderer: Luokka, joka vastaa syötteen renderoinnista.
        clock: Kello, jolla määritetään tarkastusten tahti.
        text: Syötetty teksti.
    """

    def __init__(self, renderer, clock):
        """Luokan konstruktori, joka luo uuden valikon.

        Args:
            renderer: Luokka, joka vastaa syötteen renderoinnista.
            clock: Kello, joka määrittää tarkastusten tahdin.
        """
        self.renderer = renderer
        self.clock = clock
        self.text = ""

    def input_text(self):
        """Valikon käynnistys, jossa tarkastuksia toistetaan kunnes peli aloitetaan tai sovellus suljetaan.

        Returns
            Syötetty merkkijono kun pelaaja on valmis.
        """
        while True:
            if self.handle_events():
                return self.text
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        """Tarkistaa näppäimistön näppäinten painalluksia ja pelin sulkemista.

        Jos näppäin on backspace, syötteestä poistetaan viimeinen merkki.
        Jos näppäin on return, syöte on valmis.
        Jos näppäin on jokin muu, se merkki lisätään merkkijonoon

        Returns
            True, jos syöte on valmis, muuten None
        """
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
        """Renderöi pelaajan syötteen."""
        self.renderer.render_player_input(self.text)
