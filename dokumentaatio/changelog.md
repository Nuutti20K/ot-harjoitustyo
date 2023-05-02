# Changelog

## Viikko 3

- Lisätty Level-luokka, joka vastaa spritejen sijainneista ja törmäyksistä
- Lisätty madolle funktiot, joilla mato liikkuu suoraan, mutta ei vielä käänny
- Lisätty funktio joka tarkistaa madon törmäämisen seinään ja lopettaa pelin
- Testattu liikkumisfunktion toiminnallisuus

## Viikko 4

- Lisätty funktio jolla matoa voi kääntää
- Törmääminen ei enää sulje peliä
- Lisätty funktio, jonka avulla madon ruumis seuraa madon päätä
- Lisätty funktiot jotka siirtävät pellettiä kun mato osuu siihen
- Lisää testejä kääntymiselle ja liikkumiselle
- Lisätty GameLoop-luokka, joka tarikstaa tapahtumat
- Lisätty Renderer-luokka, joka on vastuussa ruudun päivittämisestä

## Viikko 5

- Lisätty MainMenu-luokka, joka on vastuussa päävalikon toiminnoista
- Päävalikosta voi aloittaa pelin
- MenuLoop-luokka on vastuussa tapahtumista valikossa ollessa
- MenuRenderer-luokka on vastuussa ruudun päivityksestä valikossa
- Peli laskee pelaajan pisteitä, mutta ei tallenna niitä
- Madon törmääminen palauttaa pelin päävalikkoon, josta voi aloittaa pelin uudestaan

## Viikko 6

- Lisätty funktioita, joilla SQLite-tietokanta alustetaan ja yhdistetään
- Lisätty ScoreRepository-luokka, joka on vastuussa pisteiden lisäämisestä SQLite-tietokantaan
- Päävalikossa näkyy viisi parasta ennätystä
- TextHandler-luokka, joka on vastuussa pelaajan nimen kirjaamisesta
