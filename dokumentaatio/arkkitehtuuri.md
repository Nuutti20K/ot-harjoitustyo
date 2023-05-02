# Arkkitehtuurikuvaus

## Käyttöliittymä
Käyttöliittymässä on varsinaisen pelin lisäksi kaksi näkymää: päävalikko ja "game over" ruutu, johon kirjoitetaan pelaajan nimi.

Nimen kirjoittamista varten on kokonaan oma TextHandler-luokka, ja päävalikon toiminnasta vastaa MainMenu- ja MenuLoop luokat.

## Sovellusslogiikka

```mermaid
classDiagram
    class Head
    Head : coordinates
    Head : heading
    Head : queued_heading
    Head : speed
    Head : next_move
    class Body
    Body : coordinates
    Body : heading 
    class Pellet
    Pellet : coordinates
    class Wall
    Wall : coordinates
    class Level
    Level : grid
    Level : head_movement()
    Level : turn_head()
    Level : body_movement()
    Level : add_body()
    Level : movement_coordinator()
    Level : move_pellet()
    Level : collision_check()
    Level : pellet_check()
    Level "1" -- "1" Head
    Level "1" -- "*" Body
    Level "1" -- "1" Pellet
    Level "1" -- "*" Wall
```
## Tietojen pysyväistallennus
ScoreRepository-luokka vastaa ennätysten tallentamisesta SQLite-tietokantaan. 

### Tiedostot

Ennätykset tallennetaan SQLite-tiedostoon, jonka nimi voidaan määritellä .env konfiguraatiotiedostossa.

## Päätoiminnallisuudet
Kuvataan päätoiminnallisuuksia sekvenssi kaavioilla.

### Kääntyminen

Kun pelin kulkiessa painetaan jotakin nuolinäppäintä, esimerkikisi alasnuolta, niin peli toimii seuraavasti:
```mermaid
sequenceDiagram
    actor Player
    participant GameLoop
    participant Level
    participant Head
    Player->>GameLoop: press "down" key
    GameLoop->>Level: turn_head("down")
    Level-->>Head: queued_heading="down"
    GameLoop->>Level: movement_coordinator()
    Head-->>Level: queued_heading
    Level-->>Head: heading="down"
```
GameLoop tunnistaa nuolinäppäimen painalluksen ja kutsuu Level-luokan metodia, joka kääntää madon päätä. Metodi tarkistaa onko kääntyminen sallittu ja muuttaa Head-luokan suunnaksi "down". Seuraavaksi GameLoop kutsuu toista Level metodia, joka lopullisesti toteuttaa madon kääntymisen.
